# Task 1.2 — Instance Methods
#
# Add a description() method to the Car class from task 1.1.
# It should return a formatted string like "2022 Toyota Corolla".
#
# Syntax:
#   class ClassName:
#       def method(self) -> return_type:
#           ...
#
# Example output:
#   2022 Toyota Corolla


# TODO: define the Car class with make, model, year (reuse from 1.1)
# TODO: add a description() method that returns "{year} {make} {model}"
# TODO: create an instance and print the result of description()


class Car:
        def __init__(self, make: str, model: str, year: int):
                self.make = make
                self.model = model
                self.year = year


        def description(self) -> str:
                return f"{self.year} {self.make} {self.model}"


def main() -> None:
        the_car = Car("Toyota", "Corolla", 2022)
        print(the_car.description())

if __name__ == "__main__":
        main()