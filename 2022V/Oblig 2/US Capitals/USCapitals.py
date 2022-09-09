import os


class StateNotFoundError(Exception):
    def __init__(self, message="State can not be found.") -> None:
        super().__init__()
        self.message = message

    def __str__(self) -> str:
        return super().__str__()


# Leser fil, returnerer liste med stater samt dictionary {stat: hovedstad, .....}
def read_file(filename):
    file_dir = os.path.dirname(__file__)
    with open(file=os.path.join(file_dir, filename), mode="r", encoding="utf-8") as file:
        datalines = [i.split(sep=", ") for i in file.readlines()]
        states = [i[0].lower() for i in datalines]
        capitols = [i[1].strip() for i in datalines]
        dictionary = dict(zip(states, capitols))

    return dictionary, states


# Søker for navn i dictionary
def search_file_in_memory(state_input, data):
    output = data.get(state_input, None)
    if output is None:
        raise StateNotFoundError
    else:
        return output


def main():
    data, states = read_file("USCapitals.txt")
    while True:
        state_input = input("Enter name of state (Q to quit): ").lower()
        if state_input.upper() == "Q":
            print("Bye!\n")
            exit()

        # Mulighet for å få opp liste over stater, skriv "List".
        elif state_input.upper() == "LIST":
            for i in states:
                print(i)

        else:
            try:
                print(f"The capital of {state_input} is: {search_file_in_memory(state_input, data)}.")
            except StateNotFoundError:
                print(f"Can not find '{state_input}', try again.")


if __name__ == "__main__":
    main()
