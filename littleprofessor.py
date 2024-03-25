import random

def main():
    lvl = get_level()
    qns = 0
    score = 0
    while qns < 10:
        fir = generate_integer(lvl)
        sec = generate_integer(lvl)
        count = 0
        while count < 3:
            ans = fir + sec
            print(f"{fir} + {sec} = ", end = "")
            guess = input().strip()
            if guess == str(ans):
                score += 1
                break
            elif guess != str(ans):
                print("EEE")
                count += 1
        if count == 3:
            print(f"{fir} + {sec} = {ans}")
        qns += 1
    print(f"Score: {score}") #while loop broken out of when qns == 10


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n == 1 or n == 2 or n == 3:
                return n
        except ValueError:
            pass


def generate_integer(n):
    if n == 1:
        return random.randint(1, 9)

    elif n == 2:
        return random.randint(10, 99)

    elif n == 3:
        return random.randint(100, 999)




if __name__ == "__main__":
    main()