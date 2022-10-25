# RYL Matching algorithm

## getting started
`usage: main.py [-h] [-m] mentor_file mentee_file`

for example:
```
python main.py ~/Downloads/mentors.csv ~/Downloads/mentees.csv
```

## Requirements 
- geopy
- numpy
- scipy
- python >= 3.7
## Similarity berechnung

1. Distanz - Gewichtung 1 
    1. <2km - Parameter: 1
    2. 2-4km - Parameter: 0,75
    3. 4-6km - Parameter: 0,5
    4. 6-8km - Parameter: 0,25
    5. 8-10km - Parameter: 0,1
    6. \>10km - Parameter: 0
2. Sprache - Gewichtung 1
    1. Muttersprache == Muttersprache —> Parameter 1
    2. Fremdsprache == Muttersprache —> Parameter 0,75
    3. Fremdsprache == Fremdsprache —> Parameter 0,5 (Fremdsprache Üben als gemeinsamer Nenner)
3. Distanzfunktion Schule - Gewichtung 0,5 
    1. <2km - Parameter: 1
    2. 2-4km - Parameter: 0,75
    3. 4-6km - Parameter: 0,5
    4. 6-8km - Parameter: 0,25
    5. 8-10km - Parameter: 0,1
    6. \>10km - Parameter: 0
4. Traumberuf & Studiumfachrichtung (manuell) - Gewichtung 0,25
    1. Match —> Parameter 1 
    2. Non-Match —> Parameter 0
5. Erzielter Weg nach der Mittelschule & Gegangener Weg der Mentor*innen - Gewichtung 0,75
    1. Ausbildung == Ausbildung —> 1
    2. Schule == Zweiter Bildungsweg —> 1 
    3. Ausbildung == Zweiter Bildungsweg —> 0
    4. Schule == Ausbildung —> 0
    5. Weiß ich nicht == Ausbildung —> 0,5 (Perspektive aufzeigen)
    6. Weiß ich nicht == Zweiter Bildungsweg —> 0,5 (Perspektive aufzeigen)
6. Lieblingsfächer & Studiumfachrichtung (manuell) - Gewichtung 0,5
    - Details
        
        Wir gehen von Change auf 3 Auswahloptionen (3 Lieblingsfächer) aus 
        
    1. ≥1 Match —> 1
    2. 0 Matches —> 0
7. Filme und Serien - Gewichtung 0,25
    1. 1 Punkt für jede Gemeinsamkeit; addieren; durch 3 (mögliche Gesamtanzahl) teilen 
8. Musik - Gewichtung 0,25
    1. 1 Punkt für jede Gemeinsamkeit; addieren; durch 3 (mögliche Gesamtanzahl) teilen 
9. Sport - Gewichtung 0,5
    1. 1 Punkt für jede Gemeinsamkeit; addieren; durch 3 (mögliche Gesamtanzahl) teilen
10. Hobbies - Gewichtung 0,5
    1. 1 Punkt für jede Gemeinsamkeit; addieren; durch 3 (mögliche Gesamtanzahl) teilen