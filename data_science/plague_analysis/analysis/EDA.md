# Exploratory Data Analysis – Historical Pandemic Dataset

    ## 1. Dataset Overview
    - 50 Pandemien
    - 21 Variablen
    - wichtigste Variabeln: Estimated_Cases, Estimated_Deaths, Economic_Impact_Billion_USD (für Pandemien und Pathogene)

    ## 2. Data Quality
    - Missing values in: laut Analyse nur in containment_method
    - cases: größtenteils unter 10 Millionen, höchste bei 2 Milliarden. -> logarithmisch darstellen?
    - deaths: größtenteils unter 4 Millionen, höchste etwa 70 Mil. -> auch Log
    - Sterberate %: Großteil unter 20%, aber auch einige mit bius zu 50%
    - Ökon. impact: größtent. unter 1e12 USD, extrem mit 1,5e13 USD

    ## 3. Key Observations
    - sehr starke Streuung bei Todesfällen
    - wenige extreme Ausreißer dominieren

    ## 4. Hypothesen
    - längere Pandemien → mehr Todesfälle?
    - länger zurückliegende Pandemien = höhere Sterberate?

    ## 5. Nächste Schritte
    - Korrelationen analysieren
    - Feature Engineering
