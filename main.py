import random

def randomize(Var):
    aVar = random.randint(1,Var)
    return aVar

def main():
    WinNUM = randomize(100)
    GuessCHECK = []
    try:
        GuessNUM = input("Enter a valid number")
    except Exception:
        print("Something went wrong")
    guessCOUNTER = 0
    while(int(GuessNUM) != WinNUM):
        guessCOUNTER += 1
        GuessCHECK.append(int(GuessNUM))


        print(WinNUM)
        if guessCOUNTER >= 2:
            if GuessCHECK[guessCOUNTER-1] > GuessCHECK[guessCOUNTER-2]:
                print("Closer")
            else:
                print("Further")
        try:
            GuessNUM = input("Enter a valid number")
        except Exception:
            print("something went wrong")
    print("you win!")

if __name__ == '__main__':
    main()