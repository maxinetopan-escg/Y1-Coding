class Animal():
 def __init__(self):
  self.__diets = ["carnivore", "herbivore", "omnivore", "piscivore"]

 def setFeeding(self,feeding):
  if feeding.lower() in self.__diets:
    self.__feeding=feeding
  else:
    print(f"ERROR: Invalid feeding argument: {feeding}")

 def getFeeding(self):
  return self.__feeding

class Bird(Animal):
 def __init__(self,species):
  super().__init__()
  self.species=species


eagle=Bird("Golden Eagle")
eagle.setFeeding("Carnivore")
# eagle.__feeding="carnivore"
print(eagle.getFeeding())