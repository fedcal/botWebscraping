import requests
from bs4 import BeautifulSoup
import re
import numpy as np
"""
1 messaggio tutte le partite filtrate

1 messaggio prima che la partita inizia
"""
class partita:
    league=""   #lega
    time="" #ora in cui gioca la squadra Considerare un'ora in pi da aggiungere per il fuso orario
    home="" #squadra di casa
    away="" #squadra avversaria
    handicap="" #handicap
    goalLine="" #goal line

    def __init__(self,league,time,home,away,handicap,goalLine):
        self.league=league
        self.time=time
        self.home=home
        self.away=away
        self.handicap=handicap[0:4]
        self.goalLine=goalLine[0:4]

class TableScraper:
    results = []
    datasExtract =[]
    dataFromFile=[]

    def run(self):
        response = self.fetch('https://www.totalcorner.com/match/today')
        self.parse(response.text)

    def fetch(self, url):
        return requests.get(url)

    def parse(self, html):
        content = BeautifulSoup(html, 'lxml')
        table = content.find('table')
        rows = table.findAll('tr')
        self.results.append([header.text for header in rows[0].findAll('th')])

        for row in rows:
            if len(row.findAll('td')):
                self.results.append([data.text for data in row.findAll('td')])

        del self.results[0:3]

        for one in self.results:
            self.datasExtract.append(partita(one[1].strip(),one[2].strip(),one[4].strip(),one[6].strip(),one[7].strip(),one[9].strip()))

        for i in range(len(self.datasExtract)):
            parentesi='('
            if(len(self.datasExtract[i].handicap)>0):
                if parentesi == self.datasExtract[i].handicap[0]:
                    self.datasExtract.remove(self.datasExtract[i])
                elif not (any(chr.isdigit() for chr in self.datasExtract[i].handicap)):
                    self.datasExtract.remove(self.datasExtract[i])
                elif '(' == self.datasExtract[i].goalLine[0]:
                    self.datasExtract.remove(self.datasExtract[i])
                elif not (any(chr.isdigit() for chr in self.datasExtract[i].goalLine)):
                    self.datasExtract.remove(self.datasExtract[i])
                elif not len(self.datasExtract[i].handicap) >0:
                    self.datasExtract.remove(self.datasExtract[i])
        file=open("partiteripulite.txt","w")

        for i in self.datasExtract:
            riga=i.league+";"+i.time+";"+i.home+";"+i.away+";"+i.handicap+";"+i.goalLine+"\n"
            print(riga)
            file.write(riga)
        file.close()

    """Leggere da file riga per riga, inserirli nella struttura e convertili da stringhe in float e da stringhe in data"""
    def uploadFromFile(self):
        #Lettura dati da file
        file= open("partiteripulite.txt","r").readlines()
        for i in file:
            self.dataFromFile.append(i)

        #pulizia dati con ahndicap pari a null
        j=0
        delIndex=[]
        for i in self.dataFromFile:
            verifica=len(i)-2
            if(i[verifica]==';'):
                delIndex.append(j)
            j=j+1
        arraymodified=np.delete()
        #print(len(self.dataFromFile[len(self.dataFromFile)-1]))
        #print(self.dataFromFile[len(self.dataFromFile)-1][79])


        self.datasExtract.clear()
        for x in self.dataFromFile:
            res=re.split(';',x)
            temp=partita(res[0],res[1],res[2],res[3],res[4],res[5])
            self.datasExtract.append(temp)







if __name__ == '__main__':
    #scraper.run()
    scraper = TableScraper()
    scraper.uploadFromFile()



"""Esempio time
from datetime import time
b = time(11, 34, 56)
print("b =", b)
"""

