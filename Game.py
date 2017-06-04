import pygame as pg
import tkinter as tk
import os

from Towers import *





def main():
    root = tk.Tk()
    root.geometry("%dx%d%+d%+d" % (1600, 900, 100, 50))

    game_frame = tk.Frame(root, width=1400, height=900)  # creates embed frame for pg window
    game_frame.pack(side=tk.LEFT)

    menu_frame = tk.Frame(root, width=200, height=900)
    menu_frame.pack(side=tk.RIGHT)

    info_frame = tk.LabelFrame(menu_frame)
    info_frame.place(anchor="n", relx=0.5, rely=0)

    tk.Label(info_frame, text="$: 12345", font=("Candara", 20)).grid(row=0)
    tk.Label(info_frame, text="♡: 100", font=("Candara", 20)).grid(row=1)

    button_frame = tk.Frame(menu_frame)
    button_frame.place(anchor="n", relx=0.5, rely=0.1)

    for i in range(len(tower_types)):
        type = tower_types[i]
        b = tk.Button(button_frame, text=type.name, font=("Candara", 20), width=10, height=2)
        # b.place(relx=0.5, rely=0.2 + 0.1 * i, anchor="n")
        b.grid(row=i)

    os.environ['SDL_WINDOWID'] = str(game_frame.winfo_id())
    os.environ['SDL_VIDEODRIVER'] = 'windib'

    screen = pg.display.set_mode((1400, 900))

    screen.fill(pg.Color(0, 0, 150))

    clock = pg.time.Clock()
    while True:
        clock.tick(60)

        for event in pg.event.get():
            pass

        root.update()
        pg.display.update()




if __name__ == "__main__":
    main()