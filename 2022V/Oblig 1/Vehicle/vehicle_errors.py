class BaseError(Exception):
    def __init__(self, message="An error has occurred!"):
        super().__init__()
        self.message = message
        print(message)

    def __str__(self):
        return self.message


class LengthError(BaseError):
    def __init__(self, message="Error: Make is too long, max 12 char."):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message


class ModelError(BaseError):
    def __init__(self, message="Error: Invalid model year (1900-2022)."):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message


class MilageError(BaseError):
    def __init__(self, message="Error: Milage can not be negative numbers....duh!"):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message


class DoorError(BaseError):
    def __init__(self, message="Error: Vehicle can only have 2 or 4 doors. Unless it's a bus...and then you're using the wrong app dude!"):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message


class DriveTypeError(BaseError):
    def __init__(self, message="Error: Enter only 2WD or 4WD. Nothing Fancy!"):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message


class PassCapError(BaseError):
    def __init__(self, message="Error: Negative passengers also counts as passengers..."):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message


if __name__ == "__main__":
    pass
