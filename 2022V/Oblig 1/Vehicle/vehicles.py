class Vehicle:
    def __init__(self, make="not set", model=0, milage=0, price=0):
        make = make.replace("_", " ")
        self.make = make
        self.model = model
        self.milage = milage
        self.price = price

    # "Setters"
    def set_make(self, value):
        value = value.replace("_", " ")
        self.make = value

    def set_milage(self, value):
        self.milage = value

    def set_model(self, value):
        self.model = value

    def set_price(self, value):
        self.price = value

    # "Getters"
    def get_make(self):
        return self.make

    def get_milage(self):
        return self.milage

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price

    def __str__(self):
        return f"{self.make:<15} Model: {self.model:<6} Milage: {self.milage:<10} Price: {self.price:<10}"


class Car(Vehicle):
    def __init__(self, make="not set", model=0, milage=0, price=0, doors=0):
        super().__init__(make, model, milage, price)
        self.doors = doors

    def set_doors(self, value):
        self.doors = value

    def get_doors(self):
        return self.doors

    def __str__(self):
        return f"{self.make:<15} Model: {self.model:<6} Milage: {self.milage:<10} Price: {self.price:<10} Doors: {self.doors:<3}"


class Truck(Vehicle):
    def __init__(self, make="not set", model=0, milage=0, price=0, drive_type="N/S"):
        super().__init__(make, model, milage, price)
        self.drive_type = drive_type
        self.type = type

    def set_drive_type(self, value):
        self.drive_type = value

    def get_drive_type(self):
        return self.drive_type

    def __str__(self):
        return f"{self.make:<15} Model: {self.model:<6} Milage: {self.milage:<10} Price: {self.price:<10} Drive type: {self.drive_type}"


class SUV(Vehicle):
    def __init__(self, make="not set", model=0, milage=0, price=0, pass_cap=0):
        super().__init__(make, model, milage, price)
        self.pass_cap = pass_cap
        self.type = type

    def set_pass_cap(self, value):
        self.pass_cap = value

    def get_pass_cap(self):
        return self.pass_cap

    def __str__(self):
        return f"{self.make:<15} Model: {self.model:<6} Milage: {self.milage:<10} Price: {self.price:<10} Pass Cap: {self.pass_cap}"


if __name__ == "__main__":
    pass
