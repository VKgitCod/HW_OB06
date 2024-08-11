import random


class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: Здоровье = {self.health}, Сила удара = {self.attack_power}"


class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Начало игры!")
        print(self.player)
        print(self.computer)
        print()

        round_number = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"Раунд {round_number}")
            if random.choice([True, False]):
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)

            print(self.player)
            print(self.computer)
            print()
            round_number += 1

        if self.player.is_alive():
            print(f"{self.player.name} побеждает!")
        else:
            print(f"{self.computer.name} побеждает!")


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()