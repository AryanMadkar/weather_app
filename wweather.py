import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image,ImageTk
import ttkbootstrap
import ttkbootstrap

def get_weather(city):
    API_key = "175ceee39699ab62aeb8be05e73337e0"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)
    
    if res.status_code == 404:
        messagebox.showerror("Error", "City not found!")
        return None
    
    weather = res.json()
    icon_id = weather["weather"][0]['icon']
    temperature = weather["main"]["temp"]-273.15
    description = weather["weather"][0]["description"]
    city = weather['name']
    country = weather['sys']['country']
    
    icon_url = f" https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return(icon_url,temperature,description,city,country)



def search():
    city = city_enter.get()
    result = get_weather(city)
    if result is None:
        result
    
    icon_url,temperature,description,city,country = result   
    location_label.config(text=f"{city},{country}")
    image = Image.open(requests.get(icon_url,stream=True).raw)
    icon=ImageTk.PhotoImage(image)
    icon_label.config(image=icon)
    icon_label.image = icon
    
    temperature_label.config(text=f"Temperature: {temperature: .2f}°C")
    description_label.config(text=f"Description: {description}")

root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("400x400")


#Enter widget -> to enter the city name

city_enter = ttkbootstrap.Entry(root,font="Helvetica")
city_enter.pack(pady=10)

#button widget 

search_button = ttkbootstrap.Button(root,text="Search",bootstyle="warning",command=search)
search_button.pack(pady=10)

#label widget 
location_label = tk.Label(root,font="Helvetica")
location_label.pack(pady=20)

icon_label = tk.Label(root)
icon_label.pack()


temperature_label=tk.Label(root,font="Helvetica")
temperature_label.pack()

description_label = tk.Label(root,font="Helvetica")
description_label.pack()

root.mainloop()

