# ============================================================
# FREE FIRE BATTLE MANAGEMENT SYSTEM
# ============================================================

# ============================================================
# PARENT CLASS
# ============================================================

class Player:

    # ========================================================
    # CONSTRUCTOR
    # ========================================================

    def __init__(self, name, health, level):

        self.name = name
        self.health = health
        self.level = level
        self.kills = 0
        self.rank_points = 0

    # ========================================================
    # SHOW PLAYER INFO
    # ========================================================

    def show_info(self):

        print("\n==============================")
        print("PLAYER INFORMATION")
        print("==============================")

        print("Player Name:", self.name)
        print("Health:", self.health)
        print("Level:", self.level)
        print("Kills:", self.kills)
        print("Rank Points:", self.rank_points)

    # ========================================================
    # COMMON ATTACK METHOD
    # ========================================================

    def attack(self):

        print(self.name, "attacks the enemy!")

    # ========================================================
    # HEAL METHOD
    # ========================================================

    def heal(self):

        self.health += 40

        print(self.name, "used Medkit!")
        print("Health Increased to", self.health)

    # ========================================================
    # ADD KILLS
    # ========================================================

    def add_kill(self):

        self.kills += 1

        self.rank_points += 50

        print(self.name, "eliminated an enemy!")

    # ========================================================
    # SHOW RANK
    # ========================================================

    def show_rank(self):

        if self.rank_points >= 100:

            print(self.name, "Rank: Grandmaster")

        elif self.rank_points >= 70:

            print(self.name, "Rank: Heroic")

        elif self.rank_points >= 40:

            print(self.name, "Rank: Diamond")

        else:

            print(self.name, "Rank: Gold")


# ============================================================
# CHILD CLASS 1
# ============================================================

class Sniper(Player):

    """
    Sniper Player Class
    """

    def sniper_shot(self):

        print(self.name, "used AWM Headshot!")

        self.rank_points += 15


# ============================================================
# CHILD CLASS 2
# ============================================================

class Rusher(Player):

    """
    Rusher Player Class
    """

    def rush_attack(self):

        print(self.name, "is rushing with MP40!")

        self.rank_points += 12


# ============================================================
# CHILD CLASS 3
# ============================================================

class SupportPlayer(Player):

    """
    Support Player Class
    """

    def revive_teammate(self):

        print(self.name, "revived a teammate!")

        self.rank_points += 8


# ============================================================
# WEAPON PARENT CLASS
# ============================================================

class Weapon:

    def __init__(self, weapon_name, damage):

        self.weapon_name = weapon_name
        self.damage = damage

    def show_weapon(self):

        print("\nWeapon Name:", self.weapon_name)

        print("Damage:", self.damage)


# ============================================================
# WEAPON CHILD CLASS 1
# ============================================================

class SMG(Weapon):

    def spray_fire(self):

        print(self.weapon_name, "sprays bullets rapidly!")


# ============================================================
# WEAPON CHILD CLASS 2
# ============================================================

class Shotgun(Weapon):

    def close_range_fire(self):

        print(self.weapon_name, "gives heavy close range damage!")


# ============================================================
# WEAPON CHILD CLASS 3
# ============================================================

class SniperGun(Weapon):

    def long_range_fire(self):

        print(self.weapon_name, "fires long range headshots!")

# ============================================================
# OBJECT CREATION FOR PLAYERS
# ============================================================

sniper_player = Sniper("Yash", 100, 50)

rusher_player = Rusher("Chrono", 120, 60)

support_player = SupportPlayer("Kelly", 110, 45)

# ============================================================
# PLAYER OPERATIONS
# ============================================================

sniper_player.show_info()

sniper_player.attack()

sniper_player.sniper_shot()

sniper_player.heal()

sniper_player.add_kill()

sniper_player.show_rank()

# ============================================================

rusher_player.show_info()

rusher_player.attack()

rusher_player.rush_attack()

rusher_player.add_kill()

rusher_player.show_rank()

# ============================================================

support_player.show_info()

support_player.attack()

support_player.revive_teammate()

support_player.heal()

support_player.show_rank()

# ============================================================
# WEAPON OBJECTS
# ============================================================

mp40 = SMG("MP40", 75)

m1887 = Shotgun("M1887", 95)

awm = SniperGun("AWM", 120)

# ============================================================
# WEAPON OPERATIONS
# ============================================================

mp40.show_weapon()

mp40.spray_fire()

m1887.show_weapon()

m1887.close_range_fire()

awm.show_weapon()

awm.long_range_fire()