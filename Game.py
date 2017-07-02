import tkinter as tk
import time

from Towers import *
from Colors import *
from Waves import *


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

        # for i in range(len(tower_types)):
        #     tower_type = tower_types[i]
        #     b = tk.Button(button_frame, text=tower_type.name, font=("Candara", 20), width=10, height=2,
        #                   command=lambda: self.place_tower(tower_type.name))
        #     b.grid(row=i)
        self.tower_buttons = [
            tk.Button(button_frame, text=Archer.name, font=("Candara", 20), width=10, height=2,
                      command=lambda: self.place_tower(0)),
            tk.Button(button_frame, text=Mage.name, font=("Candara", 20), width=10, height=2,
                      command=lambda: self.place_tower(1)),
            tk.Button(button_frame, text=Artillery.name, font=("Candara", 20), width=10, height=2,
                      command=lambda: self.place_tower(2))
        ]
        for i in range(len(self.tower_buttons)):
            self.tower_buttons[i].grid(row=i)

        # Instantiate game variables
        self.towers = []
        self.enemies = []
        self.projectiles = []

        # Modify pygame's video output (embeds all new pg windows inside a Tk.Frame object)
        os.environ['SDL_WINDOWID'] = str(game_frame.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'

        # Instantiate pygame screen
        self.screen = pg.display.set_mode((1400, 900))
        self.update_screen()

    def mainloop(self):
        clock = pg.time.Clock()
        while self.alive:
            clock.tick(60)

            # Listen for cursor hover over Tower
            pg.event.get()
            mouse_pos = pg.mouse.get_pos()
            for t in self.towers:
                if t.rect.collidepoint(mouse_pos):
                    t.hover = True
                else:
                    t.hover = False

            self.update_screen()
            pg.display.update()
            self.root.update()

    def delete(self):
        self.alive = False
        self.root.destroy()

    def update_screen(self):
        self.screen.fill(bg_color)
        for t in self.towers:
            self.screen.blit(t.image, t.pos)
            if t.hover:
                pg.draw.circle(self.screen, red, (int(t.base_center.x), int(t.base_center.y)), t.range, 2)
        for e in self.enemies:
            self.screen.blit(e.image, e.pos)
            pg.draw.rect(self.screen, red, pg.Rect(e.pos.x + 2, e.pos.y - 15, int(48 * (float(e.health) / e.max_health)), 10), 0)
            pg.draw.rect(self.screen, black, pg.Rect(e.pos.x, e.pos.y - 15, 50, 10), 2)
        for p in self.projectiles:
            self.screen.blit(p.image, p.pos)

    def place_tower(self, tower_index):
        for b in self.tower_buttons:
            b["state"] = "disabled"
        self.tower_buttons[tower_index]["relief"] = "ridge"
        TowerType = tower_types[tower_index]
        preview = TowerType.image.copy()
        preview.fill((255, 255, 255, 180), None, pg.BLEND_RGBA_MULT)
        preview.set_alpha(10)
        pg.mouse.set_pos(self.screen.get_width() - 10, self.screen.get_height() / 2)
        clock = pg.time.Clock()
        placed = False
        while not placed:
            clock.tick(60)

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pg.mouse.get_pos()

                        self.towers.append(TowerType((pos[0] - TowerType.base_center_pos[0], pos[1] - TowerType.base_center_pos[1])))
                        self.update_screen()
                        placed = True
                    if event.button == 3:
                        placed = True

            self.update_screen()
            pos = pg.mouse.get_pos()
            self.screen.blit(preview, (pos[0] - TowerType.base_center_pos[0], pos[1] - TowerType.base_center_pos[1]))
            pg.draw.circle(self.screen, red, pos, TowerType.range, 2)

            self.root.update()
            pg.display.update()

        self.update_screen()
        pg.display.update()
        for b in self.tower_buttons:
            b["state"] = "normal"
        self.tower_buttons[tower_index]["relief"] = "raised"

    # Called when ► is pressed; Runs the next wave
    def play_wave(self):
        self.wave_button["text"] = "wave {0}\n...".format(self.wave)
        self.wave_button["state"] = "disabled"

        self.enemies = test_wave            # testing code
        self.update_screen()
        wave_active = True
        clock = pg.time.Clock()
        while wave_active:
            clock.tick(60)

            # Listen for user input
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    wave_active = False

            # Listen for cursor hover over Tower
            mouse_pos = pg.mouse.get_pos()
            for t in self.towers:
                if t.rect.collidepoint(mouse_pos):
                    t.hover = True
                else:
                    t.hover = False

            # Tower - Enemy interaction
            for t in self.towers:
                in_range = []
                for e in self.enemies:
                    distance = t.base_center.distance_to(e.get_center())
                    if distance < t.range:
                        in_range.append((e, distance))

                if len(in_range) != 0:
                    target = sorted(in_range, key=lambda x: x[1])[0][0]         # pick closest enemy
                    # print("enemy {0} in range of tower {1}".format(e.name, t.name))
                    if time.time() - t.last_attack_time > t.cooldown:
                        # print("! {0} attacks {1} !".format(t.name, target.name))
                        t.last_attack_time = time.time()
                        # Aim Projectile at Enemy
                        displacement = target.get_center() - t.base_center
                        vel = (displacement / displacement.length()) * t.projectile.speed  # scale unit vector
                        self.projectiles.append(t.projectile(t.base_center - t.projectile.center_pos, vel, t.damage))

            # Projectile - Enemy collision
            for p in self.projectiles:
                for e in self.enemies:
                    if p.get_rect().colliderect(e.get_rect()):
                        self.projectiles.remove(p)
                        e.health -= p.damage
                        if e.health <= 0:
                            self.enemies.remove(e)
                        break

            # Enemy movement
            for e in self.enemies:
                e.pos += e.vel

            # Projectile movement
            for p in self.projectiles:
                p.pos += p.vel
                if max(p.pos) > 2000 or min(p.pos) < -100:
                    self.projectiles.remove(p)

            # Check for enemy depletion
            if len(self.enemies) == 0:
                wave_active = False

            try:
                self.root.update()
            except:
                return
            self.update_screen()
            pg.display.update()

        self.enemies = []
        self.projectiles = []
        self.update_screen()
        pg.display.update()

        self.wave += 1
        self.wave_button["text"] = "wave {0}\n►".format(self.wave)
        self.wave_button["state"] = "normal"


def main():
    game = GameTop()
    game.mainloop()


if __name__ == "__main__":
    main()
