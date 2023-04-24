from tkinter import *
from metar import Metar
import requests

FONT = ("Arial", 20, "normal")
FONT1 = ("Arial", 12, "normal")
window= Tk()
window.title("EK Metar Finder")
window.geometry("1200x750")
tabela = Label(text="Enter ICAO code",font=FONT)
tabela.place(x=100,y=100)
tabela.pack(padx=80, pady=80)

def metar_from_internet():
    #user_input = input("Please enter ICAO Code: ")
    user_input_str = user_input.get()
    real_user_input = user_input_str.upper()
    url = f"http://tgftp.nws.noaa.gov/data/observations/metar/stations/{real_user_input}.TXT"
    response = requests.get(url)
    metar_data = response.text.strip()
    metar_data = metar_data.split("\n")[1]
    metar_print = Metar.Metar(metar_data)
    metar_label.config(text=metar_print)
    #print (metar_print)
    
user_input=Entry(window)
user_input.pack(padx=50, pady=50)

button1=Button(window,text="Get METAR", command=metar_from_internet)
button1.pack(padx=50, pady=50)


metar_label=Label(window,text=" ",font=FONT1)
metar_label.pack()










mainloop()