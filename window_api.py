import requests
import json
from tkinter import *
import serial
from time import sleep

# UART 정의
SERVO = 0x63
FAN_N_UV = 0x64
OFF =  0x66
ON = 0x65
SUN_SPEED = 0x65
CLOUD_SPEED = 0x66
RAIN_SPEED = 0x67
SNOW_SPEED = 0x68

uart_header = [0x61,0x62]
ser = serial.Serial ("/dev/ttyS0",115200) 


# 날씨 api 받아오기
apikey = "key num"

city_list = ["Seongnam-si"]
weather_list = ["clear sky", "few clouds", "scattered clouds", "broken clouds", "mist", "shower rain", "rain", "thunderstorm", "snow"]

api = "http://api.openweathermap.org/data/2.5/weather?q=SeongNam&APPID=f7524e34fb3177e614067cdb61dd9442"

k2C = lambda k: k - 273.15

for name in city_list:
    url = api.format(city=name, key=apikey)

    res = requests.get(url)

    data = json.loads(res.text)

    cl = round(k2C(data["main"]["temp"]), 2)

    wtr = data["weather"][0]["description"]

    print("City = ", data["name"])
    print("Weather = ", wtr)
    print("Temperatures= ", cl)
    print("Humidity = ", data["main"]["humidity"])

# close버튼 누르면 호출되는 함수
def close():
    send_data = [0x61, 0x62, SERVO, OFF]
    if (wtr == weather_list[0])|(wtr == weather_list[1]):
        ser.write([0x61, 0x62, FAN_N_UV, SUN_SPEED])
    elif (wtr == weather_list[2])|(wtr == weather_list[3])|(wtr == weather_list[4]):
        ser.write([0x61, 0x62, FAN_N_UV, CLOUD_SPEED])
    elif (wtr == weather_list[5])|(wtr == weather_list[6])|(wtr == weather_list[7]):
        ser.write([0x61, 0x62, FAN_N_UV, RAIN_SPEED])
    elif wtr == weather_list[8]:
        ser.write([0x61, 0x62, FAN_N_UV, SNOW_SPEED])
    ser.write(send_data)


# 날씨에 따른 라벨 변경 함수
def weather(wtr):
    # "clear sky", "few clouds" => sunny
    if (wtr == weather_list[0])|(wtr == weather_list[1]):
        lab.config(text="sunny")  # 라벨 내용
        lab_img.config(image=img_1)
        lab_img.place(relx=0.1, rely=0.4)
        lab.place(relx=0.3, rely=0.3)
        speed = 0x01

    # "scattered clouds", "broken clouds", "mist" => cloudy
    elif (wtr == weather_list[2])|(wtr == weather_list[3])|(wtr == weather_list[4]):
        lab.config(text="cloudy")  # 라벨 내용
        lab_img.config(image=img_2)
        lab_img.place(relx=0.1, rely=0.4)
        lab.place(relx=0.3, rely=0.3)
        speed = 0x02

    # "shower rain", "rain", "thunderstorm" => rainy
    elif (wtr == weather_list[5])|(wtr == weather_list[6])|(wtr == weather_list[7]):
        lab.config(text="rainy")  # 라벨 내용
        lab_img.config(image=img_3)
        lab_img.place(relx=0.1, rely=0.4)
        lab.place(relx=0.3, rely=0.3)
        speed = 0x03

    # "snow" => snowy
    elif wtr == weather_list[8]:
        lab.config(text="snowy")  # 라벨 내용
        lab_img.config(image=img_4)
        lab_img.place(relx=0.1, rely=0.4)
        lab.place(relx=0.3, rely=0.3)
        speed = 0x04


# 창
win = Tk()  # 창 생성
win.geometry("500x500")  # 창 크기
win.title("Hello")  # 창 이름 설정

# 이미지 설정
img_1 = PhotoImage(file = "/home/pi/GUI/sun.png", master = win)
img_2 = PhotoImage(file = "/home/pi/GUI/cloud.png", master = win)
img_3 = PhotoImage(file = "/home/pi/GUI/rain.png", master = win)
img_4 = PhotoImage(file = "/home/pi/GUI/snow.png", master = win)

# close 버튼
btn = Button(win, text="Close")  # 버튼 생성
btn.config(width=20, height=2)  # 버튼 크기
btn.pack(side=RIGHT)  # 버튼 배치

# 텍스트/ 이미지 라벨
lab = Label(win)  # 라벨 생성
lab_img = Label(win)

# weather 값에 따라 라벨 변경
weather(wtr)

# 버튼 누를 때 함수 호출
btn.config(command=close)  # btn을 클릭할 때 close 함수 실행

# 종료될때까지 원도우창 실행
win.mainloop()  # 창 실행

