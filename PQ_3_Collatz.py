def main():
    number = int(input("Enter a number: "))
    print(collatz(number))


def collatz(num):
    if num % 2 == 0:
        print(num // 2)
        return num // 2
    else:
        print(3 * num + 1)
        return 3 * num + 1


if __name__ == "__main__":
    main()