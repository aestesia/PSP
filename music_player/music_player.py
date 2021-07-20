from tkinter import *
import pygame
import os

root = Tk()

class MusicPlayer:
    def __init__(self,root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("1000x200+200+200")
        pygame.init()
        pygame.mixer.init()
        self.track = StringVar()
        self.status = StringVar()

        # create trackframe
        trackframe = LabelFrame(self.root, text="Song Track", font=("times new roman", 15, "bold"),
                                bg="Navyblue", fg="white", bd=5, relief=GROOVE)
        trackframe.place(x=0, y=0, width=600, height=100)

        # create song track label
        songtrack = Label(trackframe, textvariable=self.track, width=20, font=("times new roman", 24, "bold"),
                          bg="orange", fg="gold").grid(row=0, column=0, padx=10, pady=5)
        # status label
        trackstatus = Label(trackframe, textvariable=self.status, font=("times new roman", 24, "bold"),
                            bg="orange", fg="gold").grid(row=0, column=1, padx=10, pady=5)

        # create button frame
        buttonFrame = LabelFrame(self.root, text="Control Panel", font=("times new roman", 15, "bold"),
                                 bg="grey", fg="white", bd=5, relief=GROOVE)
        buttonFrame.place(x=0, y=100, width=600, height=100)
        # Inserting buttons
        playbtn = Button(buttonFrame,text="PLAY", command=self.playsong, width=10, height=1,
                         font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=0, padx=10, pady=5)
        pausebtn = Button(buttonFrame, text="PAUSE", command=self.pausesong, width=8, height=1,
                         font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=1, padx=10, pady=5)
        unpausebtn = Button(buttonFrame, text="UNPAUSE", command=self.unpausesong, width=10, height=1,
                         font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=2, padx=10, pady=5)
        stopbtn = Button(buttonFrame, text="STOP", command=self.stopsong, width=10, height=1,
                         font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=3, padx=10, pady=5)

        # create playlist frame
        songsFrame = LabelFrame(self.root, text="Song Playlist", font=("times new roman", 15, "bold"), bg="green", fg="white",
                                bd=5, relief=GROOVE)
        songsFrame.place(x=600, y=0, width=400, height=200)
        # scrollbar
        scrol_y = Scrollbar(songsFrame, orient=VERTICAL)
        # playlist listbox
        self.playlist = Listbox(songsFrame, yscrollcommand=scrol_y.set, selectbackground="gold", selectmode=SINGLE,
                                font=("times new roman", 12, "bold"), bg="silver", fg="navyblue", bd=5, relief=GROOVE)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # change directory for fetching songs
        # "PATH/OF/DIRECTORY"
        os.chdir("C:/Users/timot/Music/NieR Replicant ver.1.22474487139... Original Soundtrack mp3/Disc 3")
        # fetching songs
        songtracks = os.listdir()
        # inserting songs into playlist
        for track in songtracks:
            self.playlist.insert(END, track)

    def playsong(self):
        # display selected song
        self.track.set(self.playlist.get(ACTIVE))
        # display status
        self.status.set("-Playing")
        # load selected song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # play selected song
        pygame.mixer.music.play()

    def stopsong(self):
        self.status.set("-Stopped")
        pygame.mixer.music.stop()

    def pausesong(self):
        self.status.set("-Paused")
        pygame.mixer.music.pause()

    def unpausesong(self):
        self.status.set("-Playing")
        pygame.mixer.music.unpause()

MusicPlayer(root)
root.mainloop()
