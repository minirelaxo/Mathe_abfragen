from pathlib import Path
import os
import random
import time


def neue_sitzungsdatei() -> Path:
	sammlung = Path(__file__).parent / "Samlung"
	sammlung.mkdir(parents=True, exist_ok=True)

	nummer = 1
	while True:
		datei = sammlung / f"{nummer}.txt"
		try:
			datei.touch(exist_ok=False)
			return datei
		except FileExistsError:
			nummer += 1


def main() -> None:
	print("Löse die Multiplikationsaufgaben. Gib 'ende' ein, um aufzuhören.")
	datei = neue_sitzungsdatei()
	print(f"Alle Antworten dieser Runde werden in {datei.name} gespeichert.")
	aufgaben_seit_clear = 0

	with datei.open("a", encoding="utf-8") as datei_inhalt:
		while True:
			zahl_1 = random.randint(1, 10)
			zahl_2 = random.randint(1, 10)
			richtiges_ergebnis = zahl_1 * zahl_2
			aufgaben_start = time.perf_counter()

			while True:
				antwort = input(f"{zahl_1} * {zahl_2} = ").strip()
				if antwort.casefold() == "ende":
					return

				try:
					ergebnis = int(antwort)
				except ValueError:
					print("Bitte gib eine ganze Zahl oder 'ende' ein.")
					continue

				break

			dauer = time.perf_counter() - aufgaben_start
			ist_richtig = ergebnis == richtiges_ergebnis
			bewertung = "Richtig" if ist_richtig else "Falsch"
			inhalt = (
				f"Aufgabe: {zahl_1} * {zahl_2} = ?\n"
				f"Deine Antwort: {ergebnis}\n"
				f"Richtige Antwort: {richtiges_ergebnis}\n"
				f"Bewertung: {bewertung}\n\n"
				f"Zeit: {dauer:.2f} Sekunden\n\n"
			)
			datei_inhalt.write(inhalt)
			datei_inhalt.flush()
			aufgaben_seit_clear += 1

			if aufgaben_seit_clear == 1:
				os.system("cls" if os.name == "nt" else "clear")
				aufgaben_seit_clear = 0

			if ist_richtig:
				print("Richtig!")
			else:
				print(f"Leider falsch. Richtig wäre {richtiges_ergebnis}.")
			print(f"Zeit: {dauer:.2f} Sekunden")


if __name__ == "__main__":
	main()

