# Mathe-Abfragen

Ein kleines Python-Konsolenspiel zum Üben des Einmaleins. und + rechnen

## Starten

Python 3 muss installiert sein. Starte das Spiel im Projektordner mit:

```bash
python Main_Mal_2-9.py
```

oder

```bash
python Main_Plus_1-100.py
```

## So funktioniert es

- Das Programm stellt zufällige Multiplikationsaufgaben mit Zahlen von 2 bis 9.
- Gib dein Ergebnis ein. Du bekommst sofort eine Rückmeldung und siehst, wie lange du gebraucht hast.
- Deine beantworteten Aufgaben werden gezählt.
- Schreibe `ende`, um das Spiel zu beenden und deine Gesamtzahl zu sehen.

## Deine Ergebnisse

Für jeden Spielstart wird im Ordner `Samlung` automatisch eine neue nummerierte Datei angelegt, zum Beispiel `1.txt` oder `2.txt`. Alle Aufgaben einer Runde landen gemeinsam in dieser Datei. Gespeichert werden deine Antwort, das richtige Ergebnis, die Bewertung und die benötigte Zeit.

Ein gespeicherter Eintrag sieht zum Beispiel so aus:

```text
Aufgabe 1: 6 * 8 = ?
Deine Antwort: 48
Richtige Antwort: 48
Bewertung: Richtig

Zeit: 3.42 Sekunden
```