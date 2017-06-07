import pygame as pg
import tkinter as tk
import os

from Towers import *
from Colors import *



class GameTop():
    def __init__(self):
        self.alive = True

        # Instantiate tk window and set up frames
        self.root = tk.Tk()
        self.root.geometry("%dx%d%+d%+d" % (1600, 900, 100, 50))
        self.root.protocol('WM_DELETE_WINDOW', self.delete)

        game_frame = tk.Frame(self.root, width=1400, height=900)  # creates embed frame for pg window
        game_frame.pack(side=tk.LEFT)

        menu_frame = tk.Frame(self.root, width=200, height=900)
        menu_frame.pack(side=tk.RIGHT)

        info_frame = tk.Frame(menu_frame)
        info_frame.place(anchor="n", relx=0.5, rely=0)

        # Money and Health labels
        tk.Label(info_frame, text="$: 12345", font=("Candara", 20)).grid(row=0)
        tk.Label(info_frame, text="♡: 100", font=("Candara", 20)).grid(row=1)

        # Wave count and play button
        self.wave = 1
        self.wave_button = tk.Button(info_frame, text="wave 1\n►", font=("Candara", 15), width=6, height=2,
                      command=self.play_wave)
        self.wave_button.grid(row=2, column=0)

        # Set up tower-buttons
        button_frame = tk.Frame(menu_frame)
        button_frame.place(anchor="n", relx=0.5, rely=0.2)

        for i in range(len(tower_types)):
            type = tower_types[i]
            b = tk.Button(button_frame, text=type.name, font=("Candara", 20), width=10, height=2)
            # b.place(relx=0.5, rely=0.2 + 0.1 * i, anchor="n")
            b.grid(row=i)

        # Instantiate game variables
        self.towers = [Archer((100, 300))]

        # Modify pygame's video output (embeds all new pg windows inside a Tk.Frame object)
        os.environ['SDL_WINDOWID'] = str(game_frame.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'

        # Instantiate pygame screen
        self.screen = pg.display.set_mode((1400, 900))
        self.update_screen()




    def mainloop(self):
        while self.alive:
            self.root.update()

    def delete(self):
        self.alive = False
        self.root.destroy()

    def update_screen(self):
        self.screen.fill(bg_color)
        for t in self.towers:
            self.screen.blit(t.image, t.pos)

        pg.display.update()

    # Called when ► is pressed; Runs the next wave
    def play_wave(self):
        self.wave_button["text"] = "wave {0}\n...".format(self.wave)
        self.wave_button["state"] = "disabled"
        wave_active = True
        clock = pg.time.Clock()
        while wave_active:
            clock.tick(60)

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    wave_active = False

            self.root.update()
            pg.display.update()

        self.wave += 1
        self.wave_button["text"] = "wave {0}\n►".format(self.wave)
        self.wave_button["state"] = "normal"




def main():

    game = GameTop()
    game.mainloop()





if __name__ == "__main__":
    main()