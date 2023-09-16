import random

numberOfStreaks = 0

# for experimentNumber in range(10000):

def results():
    # Code that creates a list of 100 'heads' or 'tails' values.
    results = []
    for i in range(100):
        coin = random.randint(0, 1)
        if coin == 1:
            results.append("heads")
        else:
            results.append("tails")
    return results

    # Code that checks if there is a streak of 6 heads or tails in a row.

print(results())
# print('Chance of streak: %s%%' % (numberOfStreaks / 100))