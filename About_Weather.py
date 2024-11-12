import tkinter #Tool Kit
from tkinter import PhotoImage
from tkinter import ttk
import requests
import json

def fun_get_weather():
    city=select_city_dd.get()
    api_key="ab4903985df14d3aa9b7e75bb44941f4"
    api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    server_data=requests.get(api_url)
    server_data_json=server_data.json()
    
    temp = server_data_json["main"]["temp"]
    temp_min = server_data_json["main"]["temp_min"]
    temp_max = server_data_json["main"]["temp_max"]
    cod = server_data_json["cod"]
    
    output_lable.config(text=f'Temperature: {temp} C \n'
                          f'Temperature_Min: {temp_min} \n'
                          f'Temperature_Max: {temp_max} \n'
                          f'COD: {cod}')
    output_frame.pack()
    


root = tkinter.Tk()
root.geometry("500x600") 
root.title("My First WebPage")

image_path=r"C:\Users\anish\Desktop\IMG_20190731_215441.png"
bg_image=PhotoImage(file=image_path)
bg_image_set = tkinter.Label(root,image=bg_image)
bg_image_set.place(relheight=1,relwidth=1)


app_header=tkinter.Label(root,text=" My First Web Page ", font=('georgia',25),bg='white',fg='black', bd=2,relief='flat', highlightbackground='blue',highlightthickness=3)
app_header.pack(pady=20)

select_city=tkinter.Label(root,text=" Select City ", font=('georgia',18),bg='white',fg='black')
select_city.pack(pady=20)

cities=['Mumbai','Bangaluru','Goa','Pune','Hyderabad','London','Kokan']
select_city_dd=ttk.Combobox(root, values=cities, font=('georgia',15))
select_city_dd.pack(pady=20)

get_button=tkinter.Button(root,text=' Get Weather ',font=('georgia',15),command=fun_get_weather)
get_button.pack(pady=20)

output_frame=tkinter.Frame(root,highlightbackground='light green',highlightthickness=5)

output_lable=tkinter.Label(output_frame,text="",font=('georgia',15))
output_lable.pack(pady=10)










root.mainloop()  # helps the app remain open