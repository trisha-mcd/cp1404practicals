"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print(f"{my_car.name} has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car(100, "Limo")
    # limo = Car(100)  # limo has 100 amount of fuel
    limo.add_fuel(20)  # limo now has 120 amount of fuel
    limo.drive(115)  # limo drove 115 kms
    print(f"{limo.name} has fuel: {limo.fuel}")


main()
