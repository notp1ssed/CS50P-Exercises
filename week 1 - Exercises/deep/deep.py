question = input("\nWhat's the answer for the Great Question of Life, the Universe, and Everything? ").lower().strip()

match question:
    case "42" | "forty-two" | "forty two":
        print("\nYes")
    case _:
        print("\nNo")

