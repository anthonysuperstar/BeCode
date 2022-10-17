from tkinter import *
import webbrowser

def openAudio():
    webbrowser.open_new("https://soundcloud.com/anthonysprofile1/candidature/s-woUzMLJTT48?si=57e893068579427abcb253e58c92835e&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")

def dlCv():
    webbrowser.open_new("https://drive.google.com/uc?export=download&id=1luX3HAIWetAuhijCDBEXg-UxN_urFOQ2")

#Fenêtre
win = Tk()
win.title("Who is Anthony?")
win.geometry("840x180")
win.config(background = "#658B84")


frame = Frame(win, bg="#658B84")
frame.pack()

lab1 = Label(frame, text="Vous souhaitez savoir qui je suis? Cliquez sur 'GET 2 KNOW ME'", font=("Calibri",18), bg="#658B84", fg ="white")
lab1.pack()

bu1 = Button(frame, text="GET 2 KNOW ME",font=("Calibri",15), bg = "white", fg="#658B84", command=openAudio)
bu1.pack(fill=X)

lab2 = Label(frame, text = "Vous souhaitez voir mon CV? Cliquez sur 'HERE IS MY RESUME'", font=("Calibri",18), bg="#658B84", fg ="white")
lab2.pack()

bu2 = Button(frame, text="HERE IS MY RESUME", font=("Calibri",15), bg = "white", fg="#658B84", command=dlCv)
bu2.pack(fill=X)

win.mainloop()