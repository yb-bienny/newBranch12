from pet import Pet

def main():
    # Create a pet object
    my_pet = Pet(name="Bingo")

    # Test methods
    my_pet.get_status()
    my_pet.eat()
    my_pet.sleep()
    my_pet.play()
    my_pet.get_status()

    # Bonus: Train and show tricks
    my_pet.train("roll over")
    my_pet.train("sit")
    my_pet.show_tricks()

if __name__ == "__main__":
    main()
    