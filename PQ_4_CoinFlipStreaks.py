import random


def results(n):
    # Code that creates a list of 100 'heads' or 'tails' values.
    results = []
    for i in range(n):
        coin = random.randint(0, 1)
        if coin == 1:
            results.append("H")
        else:
            results.append("T")
    # print(results)
    return results


def check(lst):
    # Code that checks if there is a streak of 6 heads or tails in a row.
    counter = 1
    numberOfStreaks = 0
    for i in range(1, len(lst)):
        if lst[i - 1] == lst[i]:
            counter += 1
        else:
            counter = 1
        if counter >= 6:
            numberOfStreaks += 1
            # print(f"{i} turn:")
            # print (f"{lst[i]} is: {counter} in a row")
            # print(f"Number of Streaks is: {numberOfStreaks}")

    return numberOfStreaks / 100


def main():
    print(f"Chance of streak: {check(results(1000000))}")


if __name__ == "__main__":
    main()
