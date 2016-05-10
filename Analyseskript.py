# -*- coding: utf-8 -*-	

#fragt, welche Datei geöffnet werden soll
eingabe = raw_input("Ausgangsdatei ")
#fragt, wohin Ergebnis geschrieben werden soll
ausgabe = raw_input("Ergebnisdatei ")

#öffnet Datei
with open(eingabe, 'r') as f:
    data = f.readlines()

#speichert alle Wörter des Texts in der Liste words und gibt sie einzeln aus
    for line in data:
        words = line.split()
        words.sort()
        sorted_words = ""
        for item in words:
        	sorted_words = sorted_words + item + "\n"
f.close()
        	
#schreibt Ergebnis in neue Datei
fh = open(ausgabe,"w")
fh.writelines(sorted_words)
fh.close()