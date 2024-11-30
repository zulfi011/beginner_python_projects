import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import pygame
from mutagen.mp3 import MP3


class MusicPlayer:
    def __init__(self,root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry('700x400')
        self.song_name_box()
        self.progress_bar()
        self.buttons()
        self.modifiy()
        
    # =====================  song name portion  ==========================
    def song_name_box(self):
        song_label = Label(self.root,text="song name",bg="black",fg='violet',justify=CENTER,font=("Arial", 16, "italic"),wraplength=300,height=10,width=58)
        song_label.grid(row=0,column=0,columnspan=3,sticky='n')
        return song_label
    
    def progress_bar(self):
        progress = ttk.Progressbar(self.root, orient="horizontal", length=700, mode="determinate")
        progress.grid(row=1,column=0,columnspan=3,sticky='w')
        return progress

    # ===================  buttons  =================================
    def buttons(self):
        # backward btn
        back_img = ImageTk.PhotoImage(Image.open('icons/backward-button.png').resize((50,50)))
        back_btn = Button(self.root,image=back_img,width=50,height=50,border=0)
        back_btn.image = back_img
        back_btn.grid(row=2,column=0,padx=10)
        # toogle btn
        toogle_img1 = ImageTk.PhotoImage(Image.open('icons/pause.png').resize((50,50)))
        toogle_img2 = ImageTk.PhotoImage(Image.open('icons/play-button.png').resize((50,50)))
        toogle_btn = Button(self.root,image=toogle_img1,width=50,height=50,border=0)
        toogle_btn.image = toogle_img1
        toogle_btn.grid(row=2,column=1,pady=40)
        # forward btn
        forward_img = ImageTk.PhotoImage(Image.open('icons/forward-button.png').resize((50,50)))
        forward_btn = Button(self.root,image=forward_img,width=50,height=50,border=0)
        forward_btn.image = forward_img
        forward_btn.grid(row=2,column=2,padx=10)

        return back_btn,forward_btn,toogle_btn,toogle_img1,toogle_img2

    
    # modification funcion
    def modifiy(self):
        player = player_cdllist(self,self.root)



class MusicNode:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class player_cdllist(MusicPlayer):
    def __init__(self,parent_root,main_root):
        self.main_root = main_root
        self.head = None
        self.tail = None
        self.parent_root = parent_root
        # getting songs
        self.songs = []
        for root,dirs,files in os.walk('songs/'):
            for i in files:
                self.songs.append(f"{root}{i}")
        for i in self.songs:
            self.insertion(i)

        self.cur_node = self.head
        self.back_btn,self.forwar_btn,self.toogle_btn,self.pause,self.play = self.parent_root.buttons()
        self.progress = self.parent_root.progress_bar()
        self.progress_value = 0
        self.progres_max = 100
        self.pausing_interval = 0
        self.running = False

        self.update_app()
        self.playing_song()

    # ================== song insertion in linked list =============
    def insertion(self, nodeValue):
        if self.head == None:
            newNode = MusicNode(nodeValue)
            self.head = newNode
            self.tail = newNode
            newNode.prev = newNode
            newNode.next = newNode
        if self.head:
            newNode = MusicNode(nodeValue)
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.tail.next = newNode
            self.tail = newNode
    
    # ===================== updating app =========================
    def update_app(self):
        self.song_title()
        self.back_btn.config(command=self.previous_song)
        self.forwar_btn.config(command=self.next_song)
        self.toogle_btn.config(command=self.toogle_buttons)
    def previous_song(self):
        self.cur_node = self.cur_node.prev
        self.pausing_interval = 0
        self.song_title()
        self.progress_value = 0
        self.playing_song()
    def next_song(self):
        self.cur_node = self.cur_node.next
        self.pausing_interval = 0
        self.song_title()
        self.progress_value = 0
        self.playing_song()
    def song_title(self):
        self.parent_root.song_name_box().config(text=f"{self.cur_node.value.replace('songs/','')}")
        self.toogle_btn.config(image=self.pause)
        self.toogle_btn.image = self.pause

    def toogle_buttons(self):
        if self.toogle_btn.image is self.pause:
            self.toogle_btn.config(image=self.play)
            self.toogle_btn.image = self.play
        else:
            self.toogle_btn.config(image=self.pause)
            self.toogle_btn.image = self.pause
        self.playing_song()

    def playing_song(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.cur_node.value)
        if self.toogle_btn.image is self.pause:
            pygame.mixer.music.play(start=self.pausing_interval)
            if not self.running:  # Start or resume if not already running
                self.running = True
                self.update_progress_bar()
        else:
            self.pausing_interval += pygame.mixer.music.get_pos()/1000
            pygame.mixer.music.pause()
            self.running = False
    
    def update_progress_bar(self):
        progress_per_sec = int((self.get_file_len()/100)*1000)
        if self.running and self.progress_value < self.progres_max:
            self.progress_value += 1
            self.progress["value"] = self.progress_value
            if self.progress_value >= self.progres_max and self.running:
                self.cur_node = self.cur_node.next
                self.pausing_interval = 0
                self.song_title()
                self.progress_value = 0
                self.playing_song()
            self.main_root.after(progress_per_sec, self.update_progress_bar)  # Schedule next update
        elif self.progress_value >= self.progres_max:
            self.running = False   
   
    def get_file_len(self):
        audio = MP3(self.cur_node.value)
        length = audio.info.length
        return length
    

        
root = tk.Tk()
app = MusicPlayer(root)
root.mainloop()