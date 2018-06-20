from tkinter import *
import requests

link = "https://api.privatbank.ua/p24api/exchange_rates?json&date=17.06.2017"
data = requests.get(link)
exchangeRate = data.json()["saleRateNB"]

def conv_from_uah():
    tenge = float(UAH.get())
    dollar = tenge / exchangeRate[""]
    euro = tenge / 330
    USD.set(round(dollar, 4))
    EUR.set(round(euro, 4))

def conv_from_usd():
    pass
def conv_form_eur():
    pass


wn = Tk()
wn.title("Converter")
wn.geometry("400x300")

labelKzt = Label(text="UAH: ")
labelKzt.grid(row=0, column=0)

#uah
UAH = StringVar()
enUah = Entry(textvariable=UAH)
enUah.grid(row=0, column=1)

b = Button(text="Convert", command=conv_from_uah)
b.grid(row=0, column=2)

#usd
labelUsd = Label(text="USD: ")
labelUsd.grid(row=1, column=0)

USD = StringVar()
enUsd = Entry(textvariable=USD)
enUsd.grid(row=1, column=1)

b = Button(text="Convert", command=conv_from_usd)
b.grid(row=1, column=2)

#eur
labelEur = Label(text="EUR: ")
labelEur.grid(row=2, column=0)

EUR = StringVar()
enEur = Entry(textvariable=EUR)
enEur.grid(row=2, column=1)

b = Button(text="Convert", command=conv_from_eur)
b.grid(row=2, column=2)