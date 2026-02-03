import math

class Rectangle():

    def __init__(self, user_width, user_height):
        self.width = user_width
        self.height = user_height



    def __str__(self):
        return f"A rectangle with width {self.width} and height {self.height}"
    


    def area_calculator(self):
        return self.width * self.height



    def __eq__(self, r1, r2):
        if r1 == r2:
            return True
        else:
            return False

    


def main():
    r1 = Rectangle(10, 10)
    print(r1)
    print("Area:", r1.area_calculator())


    r2 = Rectangle(10, 15)
    print(r2)
    print("Area:", r2.area_calculator())
    print(r1 == r2)
    print()


    pass

if __name__ == "__main__":
    main()