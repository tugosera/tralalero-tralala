import random

class Player:
    def __init__(self, hp, energy, food):
        self.hp = hp
        self.energy = energy
        self.food = food
        self.threat_active = False  # Kas oht on aktiivne

    def rest(self):
        if self.food > 0:
            self.food -= 1
            self.energy += 3
            print("Sa puhkasid. Energia +3, toit -1.")
        else:
            print("Pole piisavalt toitu, et puhata.")

    def search_food(self):
        found = random.choice([0, 1, 2])
        self.food += found
        self.energy -= 1
        print(f"Sa otsisid toitu ja leidsid {found} ühikut. Energia -1.")

    def move(self):
        self.energy -= 2
        print("Sa liikusid edasi. Energia -2.")
        if random.random() < 0.3:
            damage = random.randint(1, 3)
            self.hp -= damage
            print(f"Sind rünnati! HP -{damage}.")

    def status(self):
        print(f"\nSeisund: HP: {self.hp}, Energia: {self.energy}, Toit: {self.food}\n")

    def threat(self):
        """Loome juhusliku ohu, mis võib mängijat kahjustada, kui ta ei liigu."""
        if random.random() < 0.3:  # 30% tõenäosus, et oht tekib
            self.threat_active = True
            print("HOIATUS: Ilmus oht! Pead liikuma või saad kahjustusi.")
    
    def handle_threat(self):
        """Kui oht on aktiivne, siis tuleb mängijal teha valik, kas liikuda või mitte."""
        if self.threat_active:
            action = input("Oht on lähedal! Kas liigid (liigu) või teed midagi muud? ").lower()
            if action == "liigu":
                if random.random() < 0.7:  # 70% tõenäosus, et õnnestub oht vältida
                    print("Õnnestus oht vältida!")
                    self.threat_active = False
                else:
                    damage = random.randint(1, 5)
                    self.hp -= damage
                    print(f"Oht ei kadunud! Sa said {damage} kahju.")
                    self.threat_active = False
            else:
                # Kui ei liigu, siis saab kohe kahju
                damage = random.randint(1, 5)
                self.hp -= damage
                print(f"Sa ei liikumist valinud, oht tabas sind! HP -{damage}.")
                self.threat_active = False

def game():
    player = Player(hp=10, energy=5, food=3)
    nights = 5

    print("Tere tulemast mängu 'Sundöö' – Sinu eesmärk on ellu jääda 5 ööd.\n")

    for night in range(1, nights + 1):
        print(f"--- ÖÖ {night} ---")
        player.status()

        # Võib tekkida oht (30% tõenäosus)
        player.threat()

        # Mängija valik tegevuseks
        action = input("Vali tegevus (puhka / otsi / liigu): ").lower()

        if action == "puhka":
            player.rest()
        elif action == "otsi":
            player.search_food()
        elif action == "liigu":
            player.move()
        else:
            print("Tundmatu tegevus, sa raiskasid aega.")

        # Kui oht on olemas, siis mängija peab tegema valiku
        player.handle_threat()

        # Kontrollime, kas mängija on elus
        if player.hp <= 0:
            print("Sa said surma. Mäng läbi.")
            break

        if player.energy <= 0:
            print("Sa kaotasid teadvuse energia puuduse tõttu. Mäng läbi.")
            break

    else:
        print("Sa jäid ellu 5 ööd! Palju õnne!")

# Käivita mäng
game()