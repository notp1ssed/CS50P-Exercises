def main():
    answer = input("\nHow are you feeling right now? ")
    convert(answer)

def convert(txt):
        txt = txt.replace(":)", "🙂")
        txt = txt.replace(":(", "🙁")
        print(txt)

main()
