import customtkinter as CTk
import requests
import random 
from bs4 import BeautifulSoup

class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x500")
        self.protocol('WM_DELETE_WINDOW', self.ex)

        self.text = CTk.CTkTextbox(master=self, text_color='white', width=1000, height=500)
        self.text.grid(row=0, column=0)
        self.text.insert("end","Праздники")
        self.bind("<q>", self.ex)
    def ex(self,event="None"):
        self.destroy()
    def printw(self):
        self.text.insert("end",get_data())
        self.text.configure(state=CTk.DISABLED)

def get_data():
    try:
        res = requests.get('https://calend.online/holiday/')
        a=res.text.split("<h2>Праздники сегодня <small>полный список</small><")[1].split("</ul>")[0]
        a=a.split('<ul class="holidays-list">')[1]
        a=a.split("<li>\n")
        a=[i.strip(' qwertyuiop[]asdfghjkl;"zxcvbnm,./>/<=-\t\n') for i in a]
        a=[i.split("<")[0] for i in a]
        a=[i.strip(' qwertyuiop[]asdfghjkl;"zxcvbnm,./>/<=-\t\n') for i in a]
        a="\n".join(a)
    except Exception as e:
        return ("Exception (find):", e)
    return a

if __name__ == "__main__":
    app = App()
    app.printw()
    app.mainloop()
    