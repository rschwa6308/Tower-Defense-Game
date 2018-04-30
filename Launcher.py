from Game import *


class Launcher:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Launcher")

        # dimensions of root
        w = 260
        h = 160

        # get dimensions of screen
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()

        # calculate x and y coordinates for the Tk root window
        x = (sw / 2) - (w / 2)
        y = (sh / 2) - (h / 2)

        # set root size and position within screen
        self.root.geometry("%dx%d%+d%+d" % (w, h, x, y))

        self.width_entry = tk.Entry(self.root)
        self.height_entry = tk.Entry(self.root)

        self.width_entry.insert(0, "1400")  # default width 1600px
        self.height_entry.insert(0, "900")  # default height 900px

        tk.Label(self.root, text="Tower Defense Game", font=("Candara", 20)).grid(row=0, column=0, columnspan=4,
                                                                                  pady=10)

        tk.Label(self.root, text="Game Width (px):").grid(row=1, column=0)
        tk.Label(self.root, text="Game Height (px):").grid(row=2, column=0)

        self.width_entry.grid(row=1, column=3)
        self.height_entry.grid(row=2, column=3)

        tk.Button(self.root, text="Start Game", command=self.start_game).grid(row=3, column=0, columnspan=4, pady=20)

    def start_game(self):
        game_width = int(self.width_entry.get())
        game_height = int(self.height_entry.get())
        self.root.destroy()
        launch(game_width, game_height)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    launcher = Launcher()
    launcher.run()
