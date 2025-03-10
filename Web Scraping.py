#Import the required Libraries
import requests 
from tkinter import *
import tkinter as tk
from bs4 import BeautifulSoup

win = Tk()

#Set the geometry of tkinter frame
win.minsize(width=700,height=400)
win.maxsize(width=700,height=400)
win.config(bg="#1a374d")

#left icon of the screen
icon = PhotoImage(file='scraper.png')
win.iconphoto(True,icon)
win.title("Web scraping")

try:
    #website url which you want to scraping
    url = "https://www.businesstoday.in/technology/news"
    req = requests.get(url)

except Exception as e:
    print('errorfor Link',url)
    print(e)

#extract all data from website
soup = BeautifulSoup(req.content, 'html.parser')

#Create a list variable
finalNews=""
for data in soup.find_all("div",class_="widget-listing",limit=10):
    news=data.div.div.a["title"]
    finalNews += '\u2022 '+news+'\n'  

    #print(finalNews)
    file = open('Scrape.txt','a')
    file.writelines((finalNews,'\n'))
    file.close()

#Create a Text Box
text= Text(win, width= 50, height= 30,font= ('arial', 13, 'bold',),fg='white',bg='#1f9699')

label=Label(win, text="News headlines", font=("Courier 22 bold"),border=0,fg='#ff5454',bg='#1a374d')
label.pack()
#Insert the text at the begining
text.insert(INSERT, finalNews)
text.pack(expand= 1, fill= BOTH)

win.mainloop()