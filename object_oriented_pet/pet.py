import threading

import time
class pet:
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
                if self.hunger>100:
                    self.hunger = 100
                if self.happiness<0:
                    self.happiness = 0
        
        thread = threading.Thread(target=increase_hunger,daemon=True)
        thread.start()
    
    def feed(self):
        self.hunger -= 1
        self.happiness += 1
        if self.happiness>100:
            self.happiness = 100
        if self.hunger<0:
            self.hunger = 0
            
    
    def get_name(self):
        return self.name
    
    def get_happiness(self):
        return self.happiness
    
    def get_hunger(self):
        return self.hunger    



print("What is you pets name?")
name = input()
vrit_pet = pet(name)
while True:
    print(f"Say Hi to your virtual pet {name}")
    print(f"{name} is {vrit_pet.get_happiness()} % happy")
    print(f"{name} is {vrit_pet.get_hunger()}% hungry")
    if (vrit_pet.get_hunger()>50):
        print(f"{name} is very hungry")
    print(f"Would you like to feed {name}?(y/n)")
    choice = input()
    if (choice.lower() == "y"):
        vrit_pet.feed()
    # time.sleep(2)
    