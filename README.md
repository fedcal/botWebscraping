# Web scryping

Si cerca di ottenere una lista dal sito [TotalCorner](https://www.totalcorner.com/match/today)
delle partite che verranno giocate in giornata e che hanno un handicap maggiore o uguale a 1.75 (e minore di -1.75)
e come goal line maggiore o uguale di 3.25

L'ora delle partite va impostata nel fuso orario italiano, quindi +1h

Mandare un messaggio con tutte le partite a inizio giornata (orario da capire all'incirca verso le 7:00) tramite bot telegram

Nice to have messaggio notifica (bot) 1 ora prima dell'inizio della partita.

Vengono utilizzate le seguenti librerie:s
- requests
- bs4
- lxml

https://www.youtube.com/watch?v=sBdmazo4coo