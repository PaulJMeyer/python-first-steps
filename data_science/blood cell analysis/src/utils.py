"""
Hilfsfunktionen für das Blood Cell Anomaly Detection Projekt.
Importierbar in allen Notebooks: from src.utils import show_sample_images
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image


# ── Pfade ──────────────────────────────────────────────────────────────────

DATA_DIR = Path(__file__).parent.parent / "data" / "raw"


def get_class_dirs(split: str = "train") -> dict:
    """
    Gibt ein Dict {klassenname: pfad} für einen Split zurück.
    split: 'train' oder 'test'
    """
    split_dir = DATA_DIR / split
    if not split_dir.exists():
        raise FileNotFoundError(
            f"Ordner '{split_dir}' nicht gefunden.\n"
            "Bitte zuerst das Dataset in data/raw/ entpacken (siehe README)."
        )
    return {d.name: d for d in sorted(split_dir.iterdir()) if d.is_dir()}


def count_images_per_class(split: str = "train") -> dict:
    """Gibt {klassenname: anzahl_bilder} zurück."""
    class_dirs = get_class_dirs(split)
    return {
        name: len(list(path.glob("*.jpg")) + list(path.glob("*.png")))
        for name, path in class_dirs.items()
    }


# ── Visualisierung ─────────────────────────────────────────────────────────

def show_sample_images(split: str = "train", n_per_class: int = 3, figsize_per_img: float = 2.5):
    """
    Zeigt n Beispielbilder pro Klasse in einem Grid an.
    Gutes Beispiel für fig, ax Matplotlib-Muster.
    """
    class_dirs = get_class_dirs(split)
    classes = list(class_dirs.keys())
    n_classes = len(classes)

    fig, axes = plt.subplots(
        n_classes, n_per_class,
        figsize=(n_per_class * figsize_per_img, n_classes * figsize_per_img)
    )

    # axes ist 2D-Array – sicherstellen auch bei n_classes=1
    if n_classes == 1:
        axes = [axes]

    for row, class_name in enumerate(classes):
        images = sorted(class_dirs[class_name].glob("*.jpg"))[:n_per_class]
        images += sorted(class_dirs[class_name].glob("*.png"))[:max(0, n_per_class - len(images))]

        for col in range(n_per_class):
            ax = axes[row][col]
            if col < len(images):
                img = Image.open(images[col])
                ax.imshow(img)
                ax.set_title(class_name if col == 0 else "", fontsize=9, loc="left")
            ax.axis("off")

    fig.suptitle(f"Beispielbilder – Split: {split}", fontsize=12, y=1.01)
    plt.tight_layout()
    plt.show()


def plot_class_distribution(split: str = "train"):
    """Balkendiagramm der Klassenverteilung (erkennt Imbalance)."""
    counts = count_images_per_class(split)
    classes = list(counts.keys())
    values = list(counts.values())

    fig, ax = plt.subplots(figsize=(max(6, len(classes) * 1.2), 4))
    bars = ax.bar(classes, values, color="steelblue", edgecolor="white", linewidth=0.5)

    # Werte über den Balken anzeigen
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
                str(val), ha="center", va="bottom", fontsize=9)

    ax.set_xlabel("Klasse")
    ax.set_ylabel("Anzahl Bilder")
    ax.set_title(f"Klassenverteilung – Split: {split}")
    ax.tick_params(axis="x", rotation=30)
    plt.tight_layout()
    plt.show()

    total = sum(values)
    print(f"\nGesamt: {total} Bilder")
    for cls, cnt in counts.items():
        print(f"  {cls}: {cnt} ({cnt/total*100:.1f}%)")


# ── Bildanalyse ────────────────────────────────────────────────────────────

def load_images_as_array(class_dir: Path, size: tuple = (64, 64), max_images: int = 200) -> np.ndarray:
    """
    Lädt Bilder aus einem Ordner als numpy-Array (N, H, W, 3), normalisiert auf [0, 1].
    max_images begrenzt die Anzahl für schnellere Entwicklung.
    """
    images = []
    paths = list(class_dir.glob("*.jpg")) + list(class_dir.glob("*.png"))
    paths = paths[:max_images]

    for p in paths:
        img = Image.open(p).convert("RGB").resize(size)
        images.append(np.array(img) / 255.0)

    return np.array(images)


def get_pixel_stats(arr: np.ndarray) -> dict:
    """
    Berechnet Pixelstatistiken für ein Bild-Array.
    arr: numpy-Array der Form (N, H, W, 3)
    """
    return {
        "mean_r": float(arr[:, :, :, 0].mean()),
        "mean_g": float(arr[:, :, :, 1].mean()),
        "mean_b": float(arr[:, :, :, 2].mean()),
        "std_r":  float(arr[:, :, :, 0].std()),
        "std_g":  float(arr[:, :, :, 1].std()),
        "std_b":  float(arr[:, :, :, 2].std()),
        "mean_brightness": float(arr.mean()),
    }
