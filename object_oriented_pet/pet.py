import threading

import time

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.happiness = 100
        self.running = True
        self._start_hunger_timer()
    
    def _start_hunger_timer(self):
        def increase_hunger():
            while self.running:
                time.sleep(3)
                self.hunger += 1
                self.happiness -= 2
                if self.hunger > 100:
                    self.hunger = 100
                if self.happiness < 0:
                    self.happiness = 0
        
        thread = threading.Thread(target=increase_hunger, daemon=True)
        thread.start()
    
    def feed(self):
        self.hunger -= 1
        self.happiness += 1
        if self.happiness > 100:
            self.happiness = 100
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        self.happiness += 5
        if self.happiness > 100:
            self.happiness = 100

    def get_name(self):
        return self.name
    
    def get_happiness(self):
        return self.happiness
    
    def get_hunger(self):
        return self.hunger
    
    def get_status(self):
        print(f"Say Hi to your virtual pet {self.name}")
        print(f"{self.name} is {self.get_happiness()}% happy")
        print(f"{self.name} is {self.get_hunger()}% hungry")


print("What is your pet's name?")
name = input()
pet = Pet(name)
while True:
    pet.get_status()
    if pet.get_hunger() > 50:
        print(f"{name} is very hungry")
    print(f"Would you like to feed or play with {name}? (f/p)")
    choice = input()
    if choice.lower() == "f":
        pet.feed()
    elif choice.lower() == "p":
        pet.play()
