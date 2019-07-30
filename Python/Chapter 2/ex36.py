import platform  # For getting the operating system name
import subprocess  # For executing a shell command
import random


def clear_screen():
    """
    Clears the terminal screen.
    """

    # Clear command as function of OS
    command = "cls" if platform.system().lower() == "windows" else "clear"

    # Action
    return subprocess.call(command) == 0


class Pool:
    def __init__(self, size):
        # self._locations = [None] * (size * size)
        self._registers = [None] * (size * size)
        self._size = size
        self._animals = []
        self._fishes = 0
        self._bears = 0

    def draw_board(self):
        clear_screen()
        for i in range(0, self._size * self._size):
            object = self._registers[i]
            if object is None:
                print("-", end=" ")
            elif isinstance(object, Animal):
                print(object.get_appearance(), end=" ")
            else:
                raise ValueError("Pool is ded")
            if (i + 1) % self._size == 0:
                print()
        print("Current Fishes: %d" % self._fishes)
        print("Current Bears: %d" % self._bears)
        currentAnims = 0
        for i in self._registers:
            if i != None:
                currentAnims += 1
        print("Current Animals: %d" % currentAnims)
        if currentAnims != self._bears + self._fishes:
            raise ValueError

    def register(self, animal, location):
        if len(self._animals) >= len(self._registers):
            return
        if not isinstance(animal, Animal):
            raise TypeError(
                "This ecosystem doesnt allow other creature other than Animal"
            )
        # Get this animal's info
        animalType = animal.get_appearance()

        # Get the infomation of the animal occupying this slot
        currentSlotAnimal = self._registers[location]
        animalTypeOfCurrentLocation = None

        if currentSlotAnimal == None:
            # If no animal wants to go here
            # Un-occupy the slot that this animal is currently on
            animalCurrentLocation = animal.get_location()
            self._registers[animalCurrentLocation] = None
            self._registers[location] = animal

        else:
            # Update because is not None
            animalTypeOfCurrentLocation = currentSlotAnimal.get_appearance()

            if animalType == animalTypeOfCurrentLocation:
                oldLocationOfCurrentSlotAnimal = currentSlotAnimal.get_location()
                # print(oldLocationOfCurrentSlotAnimal)
                if oldLocationOfCurrentSlotAnimal != location:
                    if self._registers[oldLocationOfCurrentSlotAnimal] == None:
                        self._registers[
                            oldLocationOfCurrentSlotAnimal
                        ] = currentSlotAnimal
                        self._registers[location] = None

                # Born a new Fish
                if animal._gender != currentSlotAnimal._gender:
                    newLocation = -1
                    index = -1
                    while newLocation != None:
                        index = random.randint(0, len(self._registers) - 1)
                        newLocation = self._registers[index]
                    if animalType == "B":
                        animal = Bear(index, self, random.randint(0, 1))
                        self._bears += 1
                    else:
                        animal = Fish(index, self, random.randint(0, 1))
                        self._fishes += 1

                    self._registers[index] = animal
                    self._animals.append(animal)

            else:
                # If these guys will kill each other
                fish = None
                bear = None

                # Get which one is which type
                if animalType == "B" and animalTypeOfCurrentLocation == "F":
                    fish = currentSlotAnimal
                    bear = animal
                else:
                    fish = animal
                    bear = currentSlotAnimal

                # The Fish will disappear
                self._registers[fish.get_location()] = None
                self._animals.remove(fish)
                self._fishes -= 1
                # The Bear will get the slot
                self._registers[bear.get_location()] = None
                self._registers[location] = bear

    def get_possible_moves(self, location):
        res = [location]
        fullSize = self._size * self._size
        up = down = left = right = True
        if location % self._size == 0:
            left = False
        elif (location + 1) % self._size == 0:
            right = False
        if 0 <= location <= self._size - 1:
            up = False
        elif fullSize - self._size <= location <= fullSize - 1:
            down = False
        if up:
            res.append(location - self._size)
        if down:
            res.append(location + self._size)
        if left:
            res.append(location - 1)
        if right:
            res.append(location + 1)
        return res

    def next_tick(self):
        for i in range(len(self._registers)):
            animal = self._registers[i]
            if animal != None:
                animal.move(i)
        # self._locations = self._registers
        self.draw_board()
        for animal in self._animals:
            animal.register_move()

    def add_animal(self, animal):
        if isinstance(animal, Bear):
            self._bears += 1
        elif isinstance(animal, Fish):
            self._fishes += 1
        else:
            raise TypeError(
                "This ecosystem doesnt allow other creature other than Animal"
            )
        self._animals.append(animal)
        self.register(animal, animal.get_location())


class Animal:
    def __init__(self, location, pool, appearance, gender):
        self._location = location
        self._pool = pool
        self._appearance = appearance
        self._gender = gender

    def register_move(self):
        possibleLocations = self._pool.get_possible_moves(self._location)
        index = random.randint(0, len(possibleLocations) - 1)
        if possibleLocations[index] != self._location:
            self.register_move_with_location(possibleLocations[index])

    def register_move_with_location(self, location):
        self._pool.register(self, location)

    def move(self, location):
        self._location = location

    def get_appearance(self):
        return self._appearance

    def get_location(self):
        return self._location

    def __str__(self):
        return "Bear, location: %d" % self._location


class Bear(Animal):
    def __init__(self, location, pool, gender):
        super().__init__(location, pool, "B", gender)


class Fish(Animal):
    def __init__(self, location, pool, gender):
        super().__init__(location, pool, "F", gender)


if __name__ == "__main__":
    import time

    pool = Pool(25)
    # print(pool.get_possible_moves(7))
    # for i in [1, 4, 7, 8, 9, 2, 3]:
    #     bare = Bear(i, pool)
    #     pool.add_animal(bare)
    bare = None
    mama = None
    for i in range(0, 5):
        bear = Bear(i, pool, random.randint(0, 1))
        pool.add_animal(bear)

    for i in range(8, 13):
        bear2 = Fish(i, pool, random.randint(0, 1))
        pool.add_animal(bear2)

    while True:
        pool.next_tick()
        time.sleep(1)
    # pool.next_tick()
    # bear.register_move_with_location(8)
    # bear2.register_move_with_location(8)
    # other.register_move_with_location(23 - 8)
    # bare.register_move_with_location(15 + 8)
    # other.register_move_with_location(23)
    # pool.next_tick()

