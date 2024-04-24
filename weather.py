from tkinter import *
from tkinter import ttk
import requests



def data_get():
 city = city_name.get()
 data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=7dcc9ed853095da081b10cb7c7264bf8").json() 
 wc_label.config(text=data["weather"][0]["main"]) 
 wd_label.config(text=data["weather"][0]["description"])
 temp_label.config(text=str(data["main"]["temp"]-275.15))
 pressure_label.config(text=data["main"]["pressure"])


window =Tk()
window.title("Apeksha WeatherApp")
window.config(bg="blue")
window.geometry("500x520")


name_label= Label(window,text="Weather App",font=("Times New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name=StringVar()


list_name= ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

combo= ttk.Combobox(window,text="Weather App",values=list_name,font=("Times New Roman",15),textvariable=city_name)
combo.place(x=25,y=120,height=50,width=450)



wc_label= Label(window,text="Weather Climate",font=("Times New Roman",17,"bold"))
wc_label.place(x=25,y=260,height=50,width=210)
wc_label= Label(window,text="",font=("Times New Roman",17,"bold"))
wc_label.place(x=260,y=260,height=50,width=210)

wd_label= Label(window,text="Weather Discription",font=("Times New Roman",17,"bold"))
wd_label.place(x=25,y=320,height=50,width=210)
wd_label= Label(window,text="",font=("Times New Roman",17,"bold"))
wd_label.place(x=260,y=320,height=50,width=210)


temp_label= Label(window,text="Temperature",font=("Times New Roman",17,"bold"))
temp_label.place(x=25,y=380,height=50,width=210)
temp_label= Label(window,text="",font=("Times New Roman",17,"bold"))
temp_label.place(x=260,y=380,height=50,width=210)


pressure_label= Label(window,text="Weather Discription",font=("Times New Roman",17,"bold"))
pressure_label.place(x=25,y=440,height=50,width=210)
pressure_label= Label(window,text="",font=("Times New Roman",17,"bold"))
pressure_label.place(x=260,y=440,height=50,width=210)

done_button=Button(window,text="Done",font=("Times New Roman",20,"bold"),command=data_get)

done_button.place(x=200,y=190,height=50,width=100)


window.mainloop()