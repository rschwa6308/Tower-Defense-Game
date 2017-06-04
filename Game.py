import pygame as pg
import tkinter as tk
import os

from Towers import *





def main():
    root = tk.Tk()
    root.geometry("%dx%d%+d%+d" % (1600, 900, 100, 50))

    game_frame = tk.Frame(root, width=1400, height=900)  # creates embed frame for pg window
    game_frame.grid(column=0)

    menu_frame = tk.Frame(root, width=200, height=900)
    menu_frame.grid(column=1)

    os.environ['SDL_WINDOWID'] = str(game_frame.winfo_id())
    os.environ['SDL_VIDEODRIVER'] = 'windib'

    screen = pg.display.set_mode((1400, 900))

    while True:
        root.update()
        pg.display.update()




if __name__ == "__main__":
    main()