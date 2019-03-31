import requests
from tkinter import *


def get_pm25(city_name):
    token = 'b0a041cdd8894ac66d92547eb7c645eef4f68003'
    url = 'https://api.waqi.info/feed/' + city_name + '/?token=' + token
    r = requests.get(url).json()
    pm25_value = 'PM 2.5: ' +  str(r['data']['iaqi']['pm25']['v'])
    time = 'Local time: ' + r['data']['time']['s']
    time_zone ='Time Zone: ' +  r['data']['time']['tz']
    root2 = Tk()
    message1 = Label(root2, text=pm25_value)
    message2 = Label(root2, text=time)
    message3 = Label(root2, text=time_zone)
    message1.pack()
    message2.pack()
    message3.pack()
    mainloop()









