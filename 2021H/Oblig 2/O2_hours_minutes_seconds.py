def format(seconds):
    days = seconds // 86400
    hours = (seconds - days * 86400) // 3600
    minutes = (seconds - days * 86400 - hours * 3600) // 60
    secs = seconds - days * 86400 - hours * 3600 - minutes * 60
    result = (
        ("{:02}:".format(hours) if hours else "00:")
        + ("{:02}:".format(minutes) if minutes else "00:")
        + ("{:02}".format(secs) if secs else "00")
    )
    return result


def main():
    s = int(input("Enter total seconds: "))
    print(f"\nThe hours, minutes and seconds for total seconds {s} is {format(s)}")


if __name__ == "__main__":
    main()
