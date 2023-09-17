#!/usr/bin/env python3

# Added a counter to track the number of steps needed to reach 1

from codetiming  import Timer


def main():
    t = Timer()
    while True:
        try:
            number = int(input("Enter a number:\n"))
            step = 0
            t.start()
            while collatz(number) != 1:
                step += 1
                print(f"step: {step} - number: {collatz(number)}")
                number = collatz(number)
            print(collatz(number))
            t.stop()
            break
        except ValueError:
            pass


def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1


if __name__ == "__main__":
    main()
