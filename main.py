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
        self.StatusLabel = Label(self, text='NONE', font='Arial 12', bg=self.background, fg='white')

    def __register(self):
        headers = {'User-Agent': 'Mozilla/5.0'}
        payload = {'auth': '2', 'login': randstring(10), 'password': randstring(15)}
        data = requests.post('https://hugerain.net/app/includes/controller.php', headers=headers, data=payload).json()

        if data['status']:
            self.StatusLabel.config(text="Generated", fg='green')

            with open('accounts.txt', 'a') as f:
                f.write(f"{payload['login']}:{payload['password']}\n")
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
        Label(self, text='HAG', font='Arial 20', bg=self.background, fg='white').pack()
        Label(self, text='Hugerain Account Generator', font='System 12', bg=self.background, fg='white').pack()
        Label(self, text='(С) Little Software Studio', font='System 8', bg=self.background, fg='white').place(x=115, y=212)

        Button(self, text='Generate!',
               bd=0, font='System', bg='#424242',
               activebackground='#545454',
               activeforeground='white',
               command=self.__register).place(x=75, y=80, width=105)

        Button(self, text='Github',
               bd=0, font='System', bg='#424242',
               activebackground='#545454',
               activeforeground='white',
               command=self.__github).place(x=75, y=118, width=105)

        Button(self, text='FAQ',
               bd=0, font='System', bg='#424242',
               activebackground='#545454',
               activeforeground='white',
               command=self.__github_faq).place(x=75, y=156, width=105)

        self.StatusLabel.pack()
        self.mainloop()


if __name__ == '__main__':
    MainWindow('HAG', '256x230', '#303030').run()
