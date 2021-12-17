class Pet:
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} is making sound {self.sound}")