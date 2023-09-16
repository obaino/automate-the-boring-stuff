spam = ["apples", "bananas", "tofu", "cats"]
eggs = []
abc = ["a", "b", "c", "d"]
philosophers = ["Plato", "Aristotle", "Marx", "Hegel", "Kant", "Sartre", "Habermas"]
numbers = [1, 2, 3, 4, 5, 6]


def main():
    lists = [spam, eggs, abc, philosophers, numbers]
    for i in lists:
        print(list_to_string(i))


def list_to_string(lst):
    string = ""
    for i in range(len(lst)):
        if i < len(lst) - 1:
            string += str(lst[i]) + ", "
        else:
            string += "and " + str(lst[i])
    return string


if __name__ == "__main__":
    main()
