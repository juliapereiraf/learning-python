
class Pokémon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry 
    self.name = name
    self.types = types 
    self.description = description 
    self.is_caught = is_caught

  def speak(self):
    print(self.name + '!' + self.name + '!')

  def display_details(self):
        if self.is_caught:
            print(f"Entry Number: {self.entry}\n"
                  f"Name: {self.name}\n"
                  f"Type: {self.types}\n"
                  f"Description: {self.description}\n"
                  f"{self.name} has already been caught!")
        else:
            print(f"Entry Number: {self.entry}\n"
                  f"Name: {self.name}\n"
                  f"Type: {self.types}\n"
                  f"Description: {self.description}\n"
                  f"{self.name} has not been caught yet!")


pikachu = Pokémon(25, 'Pikachu', "Electric", 'It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.', True)

pikachu.speak()
pikachu.display_details()

charmander = Pokémon(3, "Charmander", "Fire", "The flame on its tail shows the strength of its life-force. If Charmander is weak, the flame also burns weakly.", False)

charmander.speak()
charmander.display_details()

ivysaur = Pokémon(2, "Ivysaur", "Plant and poison", 'The more sunlight Ivysaur bathes in, the more strength wells up within it, allowing the bud on its back to grow larger.', True)

ivysaur.speak()
ivysaur.display_details()
