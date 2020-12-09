import requests
import random
from tkinter import *
import webbrowser


def randstring(length: int):
    stub = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    outstr = ''

    for _ in range(length):
        outstr += random.choice(stub)
    return outstr


class MainWindow(Tk):

    def __init__(self, title: str, geometry: str, background: str):
        super().__init__()
        self.background = background
        self.title(title)
        self.geometry(geometry)
        self["bg"] = background
        self.resizable(0, 0)
        self.StatusLabel = Label(self, text='NONE', font='Arial 12', bg='#36516b', fg='white')

    def __register(self):
        headers = {'User-Agent': 'Mozilla/5.0'}
        payload = {'auth': '2', 'login': randstring(10), 'password': randstring(15)}
        data = requests.post('https://hugerain.net/app/includes/controller.php', headers=headers, data=payload).json()

        if data['status']:
            self.StatusLabel.config(text="Generated", fg='green')

            with open('accounts.txt', 'a') as f:
                f.write(f"{payload['login']}:{payload['password']}\n")
                self.clipboard_clear()
                self.clipboard_append(f"{payload['login']}:{payload['password']}")

        else:
            self.StatusLabel.config(text="GENERATION ERROR!", fg='red')

    @staticmethod
    def __github():
        webbrowser.open('https://github.com/VladislavAlpatov/hag')

    @staticmethod
    def __github_faq():
        webbrowser.open('https://github.com/VladislavAlpatov/hag/wiki/FAQ')

    def run(self):
        Label(self, text='Hugerain Account Generator', font='Roboto 12', bg='#0f9696', fg='white').pack()
        Label(self, text='(С) Little Software Studio', font='Roboto 8', bg='#36516b', fg='white').place(x=125, y=222)
        self.StatusLabel.pack()

        Button(self, text='Generate!',
               bd=2, font='Roboto',
               bg=self.background,
               fg='white',
               activebackground='#0f9696',
               activeforeground='white',
               command=self.__register,
               highlightthickness=1,
               highlightbackground="#0f9696",
               relief='flat').place(x=75, y=85, width=105)

        Button(self, text='Github',
               bd=2, font='Roboto',
               bg=self.background,
               fg='white',
               activebackground='#0f9696',
               activeforeground='white',
               command=self.__github,
               highlightthickness=1,
               highlightbackground="#0f9696",
               relief='flat').place(x=75, y=128, width=105)

        Button(self, text='FAQ',
               bd=2, font='Roboto',
               bg=self.background,
               fg='white',
               activebackground='#0f9696',
               command=self.__github_faq,
               activeforeground='white',
               highlightthickness=1,
               highlightbackground="#0f9696",
               relief='flat').place(x=75, y=172, width=105)

        self.mainloop()


if __name__ == '__main__':
    MainWindow('HAG', '256x240', '#22313f').run()
