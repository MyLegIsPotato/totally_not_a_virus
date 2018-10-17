import msvcrt

def main():
    print("Hello")
    input("Press any key to start logging.")
    while True:
        keystroke = msvcrt.getch()
        if keystroke != None:
            print('You pressed a key: ' + str(keystroke))
    input("Press Enter to exit.")

if __name__ == "__main__":
    main()