#Libraries
import pandas as pd                 #importerar pandas library
import matplotlib.pyplot as plt     #importerar matplotlib library
import numpy as np

#Pandas related Functions
def readTotalDeaths():
    dfDeaths = pd.read_csv("National_Daily_Deaths.csv")     #läser in csv filen till DataFramen 'dfDeaths'
    totalDeaths = dfDeaths['National_Daily_Deaths'].sum()   #summerar alla värden på colname 'National_Daily_Deaths'
    return totalDeaths      #retunerar det summerade värdet

def readTotalCases():
    dfCases = pd.read_csv("Regional_Daily_Cases.csv")       #läser in csv filen till DataFramen 'dfCases'
    totalCases = dfCases['Sweden_Total_Daily_Cases'].sum()  #summerar alla värden på colname 'Sweden_Total_Daily_Cases'
    return totalCases       #retunerar det summerade värdet

#Matplotlib related Functions
def deathratioDiagram(a,b):
    labels1 = '% of Cases that lead to Death', 'Cases that did not lead Death'    #skapar labels för pie charten
    sizes1 = [a, b]              #delar in de två tidigare summerade värden i pie charten
    explode1 = (0.1, 0)          #highlightar 'a' värdet i pie charten
    fig1, ax1 = plt.subplots()   #matplotlib funktion för en pie chart
    ax1.pie(sizes1, explode=explode1, labels=labels1, autopct='%1.1f%%', shadow=True, startangle=270)      #olika egenskaper för pie charten

    plt.title("Proportion of cases that lead to death ", bbox={'facecolor': '0.8', 'pad': 5})      #anger en titel för pie charten
    plt.show()

deathratioDiagram(readTotalDeaths(),readTotalCases())       #anropar funktionen 'deathratioDiagram' med de andra funktionernas värde som inparametrar