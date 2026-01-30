Projektüberblick
Zweck: Ein einfacher GUI‑Zeitrechner (Tkinter), mit dem man
die aktuelle Uhrzeit für einen festen Standort (Salzburg) und einen beliebig eingegebenen Ort anzeigen kann,
die Zeitdifferenz in Stunden zwischen zwei eingegebenen Orten berechnen kann.
Oberfläche: Drei Tabs (Uhrzeit, Zeitdifferenzrechner, Gründer/Info).
Daten: Viele Listen (utc_minus_10, utc_plus_01, …) mit Städtenamen, die Zuordnungen zu UTC‑Offsets repräsentieren.
Aufbau der Datei / Hauptbestandteile
Datenbank (oben): Viele Python‑Listen, jeweils für eine UTC‑Zone (z. B. utc_plus_01). Diese Listen enthalten Städtenamen als Strings.
GUI‑Initialisierung: Tk(), ttk.Notebook, Tabs (tab1, tab2, about), Widgets (Label, Entry, Button).
Widgets (wichtig):
tab1: Anzeige "Standort: Salzburg" + Eingabefeld für einen anderen Ort (Entry gefragt) + Labels zur Anzeige der Uhrzeiten.
tab2: Zwei Entry‑Felder für "Ort 1" und "Ort 2" und ein Button zur Berechnung der Zeitdifferenz.
Hauptschleife: window.mainloop()
Wichtige Funktionen — was sie tun
check_time_dif()
Liest die Inhalte aus ort_1_e und ort_2_e (Entry‑Felder).
Prüft (mit einer Kette von if/elif), in welcher UTC‑Liste der jeweilige Ort vorkommt und setzt time_1 bzw. time_2 als Ganzzahl (z. B. -5, 1, 3).
Berechnet die absolute Differenz x = |time_1 - time_2| und zeigt diese in result_d an.
Hinweise: Die Funktion verwendet viele manuelle Vergleiche; wenn ein Ort nicht gefunden wird, kann time_1/time_2 nicht gesetzt werden (siehe Abschnitt Probleme).
submit_s_time()
Setzt ein Label standort_uhr (steht auf "Salzburg"). Diese Funktion ist minimal und wird aktuell kaum genutzt (Salzburg ist hardcodiert).
submit_g_time()
Ruft update_z() auf und aktualisiert das Label gefragt_uhr auf den eingegebenen Ort.
update_s()
Aktualisiert standort_zeit: nutzt time.strftime("%H:%M:%S") und Datum, ruft sich alle 500 ms erneut per .after() auf.
update_z()
Ziel: berechnet die Uhrzeit für den in Entry 'gefragt' eingegebenen Ort, relativ zur lokalen Uhrzeit.
Vorgehen: Prüft, in welcher UTC‑Liste der Ort vorkommt, erstellt einen String wie "utc_03" bzw. "utc_10" und extrahiert zuletzt die Ziffern, um einen Versatz z zu berechnen. (Hier sind einige unübliche Formeln/Hacks, z. B. ein -1 für Leogang).
Addiert z zur Stunde der lokalen Zeit (strftime("%H")), passt das Datum an, baut time_string/date_string zusammen und aktualisiert gefragt_zeit; ruft sich alle 500 ms erneut auf.
Benutzung (kurz)
Tab "Uhrzeit": öffne das Fenster — die lokale Zeit (Salzburg) erscheint automatisch. Trage in "Wie spät ist es in:" eine Stadt (die in den Listen vorhanden sein muss) und klicke "enter", um die Uhrzeit für diesen Ort zu sehen.
Tab "Zeitdifferenzrechner": trage zwei Ortenamen ein, klicke "Differenz berechnen" — Ergebnis in Stunden erscheint.     https://zeitverschiebungsrechner-py-1.onrender.com
