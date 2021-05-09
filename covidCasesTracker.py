from bs4 import BeautifulSoup
import requests
from tkinter import * 

url = 'https://www.worldometers.info/coronavirus/country/india/'
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
i,main=0,[]
for data in soup.find_all('div',class_='maincounter-number') :
    main.append(data.text.strip())
    i+=1

top = Tk()
top.title('COVID-19 INDIA')
top.geometry('400x370')
txt0,txt1,txt2 = StringVar(),StringVar(),StringVar()

l0 = Label(top, text = 'Cases', font=('Arial', 20)).place(x=200,y=60,a='center')
e0 = Entry(top, textvariable = txt0, justify="center", font=('Arial',15)).place(x=200,y=90,a='center')
txt0.set(main[0])

l1 = Label(top, text = 'Deaths', font=('Arial', 19)).place(x=200,y=150,a='center')
e1 = Entry(top, textvariable = txt1, justify="center", font=('Arial',15)).place(x=200,y=180,a='center')
txt1.set(main[1])

l2 = Label(top, text = 'Recovered', font=('Arial', 19)).place(x=200,y=240,a='center')
e1 = Entry(top, textvariable = txt2, justify="center", font=('Arial',15)).place(x=200,y=270,a='center')
txt2.set(main[2])

top.mainloop()
