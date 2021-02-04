from tkinter import *
import os
from pygame import mixer

mixer.init()


def play_music(event):
    play_music_play.play()

def pause_music(event):
    play_music_play.pause()
    

if __name__ == "__main__":
    root = Tk()
    root.title("MS Media Player - Future of Media")
    root.wm_iconbitmap("play.ico")
    root.geometry("900x640+230+15")
    root.configure(bg="#9376C6")
    root.minsize(640,600)

    top_frame = Frame(root,bg="#5E34A7")
    top_frame.pack(side=TOP,anchor='n',fill=X,pady=20)
    top_label = Label(top_frame,text="MS Music App",bg="#5E34A7",fg="white",font=("sans-serif",20,'bold','italic'))
    top_label.pack(pady=5)

    login_name = os.getlogin()
    music_path = f"C:\\Users\\{login_name}"
    listdir = os.listdir(f"{music_path}\\Music")
    
    if len(listdir) == 0:
        Label(root,text="Defaut folder is empty or another problem with your folder may be not created or deleted",bg="#9376C6",fg="white",font=("sans-serif",15,'bold')).place(x=30,y=260)
        Label(root,text=f"Please Choose your Folder or create music folder in {music_path}",bg="#9376C6",fg="white",font=("sans-serif",15,'bold')).place(x=30,y=290)
        Button(root,text="Open Folder",bg="#5E34A7",fg="white",padx=10,pady=5,font=("sans-serif",15)).place(x=300,y=330)

    else:
        listbox = Listbox(root,bg="#9376C6",height=23,font=("sans-serif",13,'bold'),fg="white")
        listbox.bind('<<ListBox>>',play_music)
        listbox.pack(fill=BOTH,padx=10)
        for item in listdir:
            listbox.insert(END,str(item))

        listbox.bind('<<ListboxSelect>>',play_music)
        play_button = Button(root,bg="#5E34A7",fg="white",text="Play Music",font="sans-serif 13 bold",width=30,padx=10,pady=5,command=play_music).place(x=240,y=570)
        pause_button = Button(root,bg="#5E34A7",fg="white",text="Pause Music",font="sans-serif 13 bold",width=15,padx=10,pady=5,command=pause_music).place(x=450,y=570)
        song = listbox.get(ACTIVE)
        play_music_play = mixer.music.load(str(song))

    root.mainloop()