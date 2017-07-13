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

        self.game_frame = tk.Frame(self.root, width=1400, height=900)  # creates embed frame for pg window
        self.game_frame.pack(side=tk.LEFT)

        self.menu_frame = tk.Frame(self.root, width=200, height=900)
        self.menu_frame.pack(side=tk.RIGHT)

        info_frame = tk.Frame(self.menu_frame)
        info_frame.place(anchor="n", relx=0.5, rely=0)

        # For later reference
        self.upgrade_frame = tk.LabelFrame(self.menu_frame, text="", font=("Candara", 15))
        self.upgrade_labels = [
            tk.Label(self.upgrade_frame, text="Health:", font=("Candara", 13)),
            tk.Label(self.upgrade_frame, text="Damage:", font=("Candara", 13)),
            tk.Label(self.upgrade_frame, text="Speed:", font=("Candara", 13)),
            tk.Label(self.upgrade_frame, text="Range:", font=("Candara", 13))
        ]
        self.upgrade_amounts = [
            tk.Label(self.upgrade_frame, text="", font=("Candara", 13)),
            tk.Label(self.upgrade_frame, text="", font=("Candara", 13)),
            tk.Label(self.upgrade_frame, text="", font=("Candara", 13)),
            tk.Label(self.upgrade_frame, text="", font=("Candara", 13))
        ]
        self.upgrade_buttons = [
            tk.Button(self.upgrade_frame, text="$10", font=("Candara", 13), command=lambda: self.upgrade_selected("health")),
            tk.Button(self.upgrade_frame, text="$10", font=("Candara", 13), command=lambda: self.upgrade_selected("damage")),
            tk.Button(self.upgrade_frame, text="$10", font=("Candara", 13), command=lambda: self.upgrade_selected("speed")),
            tk.Button(self.upgrade_frame, text="$10", font=("Candara", 13), command=lambda: self.upgrade_selected("range"))
        ]
        modes = ["closest", "fastest", "strongest", "weakest"]
        self.aim_mode = tk.StringVar()
        self.aim_mode_buttons = [tk.Radiobutton(self.upgrade_frame, text=mode, variable=self.aim_mode, value=mode,
                                 command=self.update_mode_selected, font=("Candara", 10)) for mode in modes]
        self.kills_label = tk.Label(self.upgrade_frame, text="", font=("Candara", 10))

        # Money and Health variables
        self.money = 300
        self.health = 100

        # Money and Health labels
        self.money_label = tk.Label(info_frame, text="$: " + str(self.money), font=("Candara", 20))
        self.health_label = tk.Label(info_frame, text="<3: " + str(self.health), font=("Candara", 20))
        self.money_label.grid(row=0)
        self.health_label.grid(row=1)

        # Wave count and play button
        self.wave = 1
        self.wave_button = tk.Button(info_frame, text="wave 1\nstart", font=("Candara", 15), width=6, height=2,
                                     command=self.play_wave)
        self.wave_button.grid(row=2, column=0)

        # Set up tower-buttons
        button_frame = tk.Frame(self.menu_frame)
        button_frame.place(anchor="n", relx=0.5, rely=0.2)

        # for i in range(len(tower_types)):
        #     tower_type = tower_types[i]
        #     b = tk.Button(button_frame, text=tower_type.name, font=("Candara", 20), width=10, height=2,
        #                   command=lambda: self.place_tower(tower_type.name))
        #     b.grid(row=i)
        self.tower_buttons = [
            tk.Button(button_frame, text=Archer.name + "\n$" + str(Archer.cost), font=("Candara", 20), width=10, height=2,
                      command=lambda: self.place_tower(0)),
            tk.Button(button_frame, text=Mage.name + "\n$" + str(Mage.cost), font=("Candara", 20), width=10, height=2,
                      command=lambda: self.place_tower(1)),
            tk.Button(button_frame, text=Artillery.name + "\n$" + str(Artillery.cost), font=("Candara", 20), width=10, height=2,
                      command=lambda: self.place_tower(2)),
            tk.Button(button_frame, text=Sniper.name + "\n$" + str(Sniper.cost), font=("Candara", 20), width=10,height=2,
                      command=lambda: self.place_tower(3))
        ]
        for i in range(len(self.tower_buttons)):
            self.tower_buttons[i].grid(row=i)

        # Instantiate game variables
        self.towers = []
        self.enemies = []
        self.projectiles = []

        # Modify pygame's video output (embeds all new pg windows inside a Tk.Frame object)
        os.environ['SDL_WINDOWID'] = str(self.game_frame.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'

        # Instantiate pygame screen
        self.screen = pg.display.set_mode((1400, 900))
        self.update_screen()

    def mainloop(self):
        clock = pg.time.Clock()
        while self.alive:
            clock.tick(60)

            # Listen for cursor hover over Tower
            mouse_pos = pg.mouse.get_pos()
            for t in self.towers:
                if t.rect.collidepoint(mouse_pos):
                    t.hover = True
                else:
                    t.hover = False

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for t in self.towers:
                            if t.hover:
                                for t_ in self.towers:
                                    t_.selected = False
                                t.selected = True
                                self.select_tower(t)
                                break
                            else:
                                t.selected = False
                                self.upgrade_frame.place_forget()
                                self.root.update()

            self.update_screen()
            pg.display.update()
            self.root.update()

    def delete(self):
        self.alive = False
        self.root.destroy()

    def get_selected(self):
        for t in self.towers:
            if t.selected:
                return t
        return None

    def update_labels(self):
        self.money_label["text"] = "$: " + str(self.money)
        self.health_label["text"] = "<3: " + str(self.health)

        for i in range(len(tower_types)):
            if self.money < tower_types[i].cost:
                self.tower_buttons[i]["state"] = "disabled"
            else:
                self.tower_buttons[i]["state"] = "normal"

        tower = self.get_selected()

        if tower is not None:
            self.upgrade_frame["text"] = tower.name + " Upgrades"
            self.upgrade_amounts[0]["text"] = str(tower.health_level)
            self.upgrade_amounts[1]["text"] = str(tower.damage_level)
            self.upgrade_amounts[2]["text"] = str(tower.speed_level)
            self.upgrade_amounts[3]["text"] = str(tower.range_level)

            self.upgrade_buttons[0]["text"] = "$" + str(tower.get_upgrade_cost("health"))
            self.upgrade_buttons[1]["text"] = "$" + str(tower.get_upgrade_cost("damage"))
            self.upgrade_buttons[2]["text"] = "$" + str(tower.get_upgrade_cost("speed"))
            self.upgrade_buttons[3]["text"] = "$" + str(tower.get_upgrade_cost("range"))

            for i in range(len(self.upgrade_buttons)):
                if self.money < tower.get_upgrade_cost(["health", "damage", "speed", "range"][i]):
                    self.upgrade_buttons[i]["state"] = "disabled"
                else:
                    self.upgrade_buttons[i]["state"] = "normal"

            for button in self.aim_mode_buttons:
                if button["text"] == tower.aim_mode:
                    button.select()
                else:
                    button.deselect()

            self.kills_label["text"] = "kills: " + str(tower.kills)

        self.root.update()

    def update_screen(self):
        # self.screen.fill(bg_color)
        self.screen.blit(background_image, (0, 0))

        for t in self.towers:
            self.screen.blit(t.image, t.pos)
            pg.draw.rect(self.screen, red, pg.Rect(t.pos.x + 4, t.pos.y - 15, int((t.dims[0] - 6) * (float(t.health) / t.max_health)), 10), 0)
            pg.draw.rect(self.screen, black, pg.Rect(t.pos.x + 2, t.pos.y - 15, t.dims[0] - 4, 10), 2)
            if t.hover or t.selected:
                pg.draw.circle(self.screen, range_color, (int(t.base_center.x), int(t.base_center.y)), t.range, 2)

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
        try:
            preview = TowerType.image.copy()
        except:
            print("no image available")
            self.update_labels()
            self.tower_buttons[tower_index]["relief"] = "raised"
            return
        preview.fill((255, 255, 255, 180), None, pg.BLEND_RGBA_MULT)

        pg.mouse.set_pos(self.screen.get_width() - 10, self.screen.get_height() / 2)        # Initialize mouse at edge
        clock = pg.time.Clock()
        placed = False
        valid_location = True
        while not placed:
            clock.tick(60)

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if valid_location:
                            old = self.get_selected()
                            if old is not None:
                                old.selected = False
                            pos = pg.mouse.get_pos()
                            new = TowerType((pos[0] - TowerType.base_center_pos[0], pos[1] - TowerType.base_center_pos[1]))
                            self.towers.append(new)
                            self.towers.sort(key=lambda t: t.pos.y)    # Sort towers based on y position (for rendering)
                            new.selected = True
                            self.select_tower(new)

                            self.update_screen()
                            placed = True
                            self.money -= TowerType.cost        # Pay for tower

                    if event.button == 3:
                        placed = True

            self.update_screen()
            pos = pg.mouse.get_pos()

            # Determine if potential tower location is colliding with existing towers or with walls
            valid_location = True
            test_rec = pg.Rect(pos[0] - TowerType.base_center_pos[0],
                               pos[1] - TowerType.base_center_pos[1],
                               TowerType.dims[0], TowerType.dims[1])
            for t in self.towers:
                if test_rec.colliderect(t.rect):
                    valid_location = False
            if min(test_rec.topleft) < 0 or test_rec.y + test_rec.height > 900 or test_rec.x + test_rec.width > 1400:
                valid_location = False

            self.screen.blit(preview, (pos[0] - TowerType.base_center_pos[0], pos[1] - TowerType.base_center_pos[1]))
            if valid_location:
                pg.draw.circle(self.screen, green, pos, TowerType.range, 2)
            else:
                pg.draw.circle(self.screen, red, pos, TowerType.range, 2)

            self.root.update()
            pg.display.update()

        self.update_screen()
        pg.display.update()
        self.update_labels()
        self.tower_buttons[tower_index]["relief"] = "raised"

    def upgrade_selected(self, attribute):
        tower = self.get_selected()

        if tower is not None:
            self.money -= tower.get_upgrade_cost(attribute)
            tower.upgrade(attribute)
            self.update_labels()

    def update_mode_selected(self):
        tower = self.get_selected()
        if tower is not None:
            tower.aim_mode = self.aim_mode.get()

    def select_tower(self, tower):
        self.upgrade_frame.place(anchor="n", relx=0.5, rely=0.7)
        self.update_labels()
        for y in range(len(self.upgrade_labels)):
            self.upgrade_labels[y].grid(row=y, column=0)

        for y in range(len(self.upgrade_amounts)):
            self.upgrade_amounts[y].grid(row=y, column=1)

        for y in range(len(self.upgrade_buttons)):
            self.upgrade_buttons[y].grid(row=y, column=2)
        self.root.update()

        for i in range(len(self.aim_mode_buttons)):
            self.aim_mode_buttons[i].grid(row=int(4+i/2), column=2*int(i%2))

        self.kills_label.grid(row=6, column=1)

    # Called when 'play' is pressed; Runs the next wave
    def play_wave(self):
        self.wave_button["text"] = "wave {0}\n...".format(self.wave)
        self.wave_button["state"] = "disabled"

        if len(waves) >= self.wave:                 # Generate waves automatically after predefined waves are exhausted
            self.enemies = waves[self.wave - 1]
        else:
            self.enemies = [Orc((randint(0, 1400), 0)) for _ in range(10 * self.wave)]
        self.update_screen()
        wave_active = True
        clock = pg.time.Clock()
        while wave_active:
            clock.tick(60)

            # Listen for user input
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    wave_active = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for t in self.towers:
                            if t.hover:
                                for t_ in self.towers:
                                    t_.selected = False
                                t.selected = True
                                self.select_tower(t)
                                break
                            else:
                                t.selected = False
                                self.upgrade_frame.place_forget()
                                self.root.update()

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
                    if t.aim_mode == "closest":
                        target = sorted(in_range, key=lambda x: x[1])[0][0]         # pick closest enemy
                    elif t.aim_mode == "fastest":
                        target = sorted(in_range, key=lambda x: x[0].speed)[0][0]
                    elif t.aim_mode == "strongest":
                        target = sorted(in_range, key=lambda x: x[0].health)[-1][0]
                    elif t.aim_mode == "weakest":
                        target = sorted(in_range, key=lambda x: x[0].health)[0][0]

                    if time.time() - t.last_attack_time > t.cooldown:
                        t.last_attack_time = time.time()
                        # Aim Projectile at Enemy
                        displacement = target.get_center() - t.base_center
                        vel = (displacement / displacement.length()) * t.projectile.speed           # scale unit vector
                        proj = t.projectile(t.base_center - t.projectile.center_pos, vel, t.damage)
                        proj.associate(t)
                        self.projectiles.append(proj)

            # Projectile - Enemy collision
            for p in self.projectiles:
                for e in self.enemies:
                    if p.get_rect().colliderect(e.get_rect()):
                        self.projectiles.remove(p)
                        e.health -= p.damage
                        if e.health <= 0:
                            self.enemies.remove(e)
                            self.money += e.value       # Collect value of enemy
                            p.tower.kills += 1          # Iterate tower kill counter
                            self.update_labels()
                        break

            # Enemy movement
            for e in self.enemies:
                e.pos += e.vel
                if e.pos.x < 0 or e.pos.x > 1400 - e.get_rect().width: e.vel.x *= -1        # TEMPORARY wall collision
                if e.pos.y < 0 or e.pos.y > 900 - e.get_rect().height: e.vel.y *= -1        # TEMPORARY wall collision

            # Projectile movement
            for p in self.projectiles:
                p.pos += p.vel
                # if p.pos.x < 0 or p.pos.x > 1400 - p.get_rect().width: p.vel.x *= -1        # TEMPORARY wall collision
                # if p.pos.y < 0 or p.pos.y > 900 - p.get_rect().height: p.vel.y *= -1        # TEMPORARY wall collision
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
        self.wave_button["text"] = "wave {0}\nstart".format(self.wave)
        self.wave_button["state"] = "normal"


def main():
    game = GameTop()
    game.mainloop()


if __name__ == "__main__":
    main()
