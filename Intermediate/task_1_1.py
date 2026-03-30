# Task 1.1 — Class & Constructor
#
# Create a Car class with make, model, and year attributes.
# Set them in __init__ and print them.
#
# Syntax:
#   class ClassName:
#       def __init__(self, param: type) -> None:
#           self.param = param
#
# Example output:
#   Make:  Toyota
#   Model: Corolla
#   Year:  2022


# TODO: define the Car class
# TODO: implement __init__ with make, model, year — all str except year (int)
# TODO: create an instance and print each attribute on its own line


class Car:
        def __init__(self, make: str, model: str, year: int) -> None:
                self.make = make
                self.model = model
                self.year = year


def main() -> None:
        first_car = Car("Toyota", "Corolla", 2022)
        print(f"Make: {first_car.make}")
        print(f"Model: {first_car.model}")
        print(f"Year: {first_car.year}")


if __name__ == "__main__":
        main()