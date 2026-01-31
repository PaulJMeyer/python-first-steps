profile = {"name": "Paul","age": "29","profession": "molecular biologist"}

print("Pauls profile:")
for key, value in profile.items():
    print(f"{key}: {value}")

grades = {"Anna": 1.7, "Ben": 2.3, "Clara": 1.3, "Paula": 1.0}

print("Only Bens grade:")
for key, value in grades.items():
    if key == "Ben":
        print(f"{key}: {value}")
    
print("All names:")
for key, value in grades.items():
    print(f"{key}")