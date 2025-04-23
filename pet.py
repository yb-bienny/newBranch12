class Pet:
    def __init__(self, name: str):
        """
        Initialize a new Pet.

        :param name: The pet's name.
        """
        self.name = name
        self.hunger = 0       # 0 = full, 10 = very hungry
        self.energy = 10      # 0 = tired, 10 = fully rested
        self.happiness = 5    # 0–10 scale
        self.tricks = []      # Learned tricks

    def eat(self):
        """
        The pet eats: reduces hunger by 3 (floor 0), increases happiness by 1 (cap 10).
        """
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} has eaten. Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        """
        The pet sleeps: increases energy by 5 (cap 10).
        """
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} has slept. Energy: {self.energy}")

    def play(self):
        """
        The pet plays: decreases energy by 2 (floor 0), increases happiness by 2 (cap 10),
        and increases hunger by 1 (cap 10).
        """
        self.energy = max(self.energy - 2, 0)
        self.happiness = min(self.happiness + 2, 10)
        self.hunger = min(self.hunger + 1, 10)
        print(f"{self.name} played. Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")

    def get_status(self):
        """
        Print the current state of the pet.
        """
        status = (
            f"Status of {self.name}:\n"
            f"  Hunger    : {self.hunger}/10\n"
            f"  Energy    : {self.energy}/10\n"
            f"  Happiness : {self.happiness}/10"
        )
        print(status)

    # Bonus methods
    def train(self, trick: str):
        """
        Teach the pet a new trick and store it.
        
        :param trick: Name of the trick to teach.
        """
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows how to {trick}.")

    def show_tricks(self):
        """
        Print all tricks the pet has learned.
        """
        if self.tricks:
            print(f"{self.name} knows the following tricks:")
            for i, t in enumerate(self.tricks, 1):
                print(f"  {i}. {t}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
