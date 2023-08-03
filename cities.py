import tkinter
import requests
import json
from PIL import Image, ImageTk
from webbrowser import *
from itertools import count
from playsound import playsound
import time
from threading import *
from ctypes import windll


lastClickX = 0
lastClickY = 0
threading_on = False

isReady = False

GWL_EXSTYLE = -20
WS_EX_APPWINDOW = 0x00040000
WS_EX_TOOLWINDOW = 0x00000080


class ImageLabel(tkinter.Label):
    """a label that displays images, and plays them if they are gifs"""

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


root = tkinter.Tk()
root.geometry("498x281")
# root.geometry("700x500")


def submitamount(event):
    isReady = True
    quote = "Es"
    amounttext = amount.get()
    URL = f"https://api.api-ninjas.com/v1/worldtime?city={amounttext}"

    headers = {"X-Api-Key": "xIkGWkTLdtOY/7Ty6Zzlmw==Dkw5ourkibKSA2sr"}

    response = requests.request("GET", URL, headers=headers)

    result = response.json()

    URL_2 = f"https://api.api-ninjas.com/v1/worldtime?city=Moscow"

    headers_2 = {"X-Api-Key": "xIkGWkTLdtOY/7Ty6Zzlmw==Dkw5ourkibKSA2sr"}

    response_2 = requests.request("GET", URL_2, headers=headers_2)

    result_2 = response_2.json()

    print(result)
    print(result_2)
    if result_2['hour'] > result['hour'] and result_2['day'] == result['day']:
        quote = f"You are {int(result_2['hour']) - int(result['hour'])} hours ahead Dashibun!"
        text_box.config(text=quote)
        text_box.place(x=140, y=240)
        print(
            f"You are {int(result_2['hour']) - int(result['hour'])} hours ahead Dashibun!1")
    elif result_2['hour'] == result['hour']:
        quote = "You are sharing same hour with this city Dashibun!"
        text_box.config(text=quote)
        text_box.place(x=87, y=240)
        print("You are sharing same hour with this city Dashibun!2")
    elif result_2['hour'] < result['hour'] and result_2['day'] == result['day']:
        quote = f"You are {int(result['hour']) - int(result_2['hour'])} hours behind Dashibun!"
        text_box.config(text=quote)
        text_box.place(x=140, y=240)
        print(
            f"You are {int(result['hour']) - int(result_2['hour'])} hours behind Dashibun!3")
    elif result['day'] < result_2['day']:
        quote = f"You are {int(result_2['hour']) - int(result['hour']) + 24} hours ahead Dashibun!"
        text_box.config(text=quote)
        text_box.place(x=140, y=240)
        print(
            f"You are {int(result_2['hour']) - int(result['hour']) + 24} hours ahead Dashibun!4")
    elif result['day'] > result_2['day']:
        quote = f"You are {-int(result_2['hour']) + int(result['hour']) + 24} hours behind Dashibun!"
        text_box.config(text=quote)
        text_box.place(x=140, y=240)
        print(
            f"You are {int(result_2['hour']) - int(result['hour']) + 24} hours behind Dashibun!5")
    elif (result['minute'] >= 59 and result['second']) >= 55 or (result_2['minute'] >= 59 and result_2['second'] >= 55):
        quote = "Try again dashibun, I think the clock is like this format xx:00 so it would give a bug!6"
        text_box.config(text=quote)
        text_box.place(x=87, y=240)
    # deletes all the text that is currently
    # in the TextBox
    # text_box.delete('1.0', tkinter.END)


    # # inserts new data into the TextBox
    # text_box.insert(tkinter.END, quote)
    # Do stuff here / call another function to do stuff
    #
    # If you want to make some variables accessible to other parts of
    # the code, simply define them before this function is declared;
    # Ex.
    #
    # Instead of:
    #   root = tkinter.Tk()
    #   ...
    #   def submitamount():
    #        ...
    #
    # Do:
    #   root = tkinter.Tk()
    #   ...
    #   response = None
    #   status_code = None
    #   result = None
    #
    #   def submitamount():
    #        ...
    #
file = "moon.gif"

lbl = ImageLabel(root)
lbl.pack()
lbl.load('moon.gif')


def play():
    playsound('surprise.mp3')


def playa():
    playsound('song.mp3')


def threading():
    # Call work function
    # t1 = Thread(target=play("song"))
    # t1.start()
    t1 = Thread(target=play)
    t1.start()


def threadinga():
    # Call work function
    # t1 = Thread(target=play("song"))
    # t1.start()
    t1 = Thread(target=playa)
    t1.start()


def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - \
        lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x, y))


root.overrideredirect(True)
gif_label = tkinter.Label(image="")
gif_label.pack()
root.lift()
root.bind('<Button-1>', SaveLastClickPos)
root.bind('<B1-Motion>', Dragging)

amount = tkinter.Entry(root)
amount.focus_set()
amount.place(x=200, y=50)

my_font = ('times', 12, 'bold')
text_box = tkinter.Label(root, font=my_font, bg="#252734", fg="white")
# text_box.place(relx=0.5, rely=0.5, x=0, y=95)
text = tkinter.Text(root)

song_button = tkinter.Button(
    root, text="♫", command=threadinga, relief='groove')
song_button.place(x=20, y=240)

song_button_2 = tkinter.Button(
    root, text="?", command=threading, )
song_button_2.place(x=50, y=240)


def set_appwindow(root):
    hwnd = windll.user32.GetParent(root.winfo_id())
    style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    style = style & ~WS_EX_TOOLWINDOW
    style = style | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
    # re-assert the new window style
    root.wm_withdraw()
    root.after(10, lambda: root.wm_deiconify())


root.wm_title("Difference of hours on cities from Russia")
root.iconbitmap("dashibun.ico")
root.bind('<Return>', submitamount)
root.after(10, lambda: set_appwindow(root))
root.mainloop()
