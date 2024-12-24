import art


def add(n1, n2):
    return n1 + n2


def multipy(n1, n2):
    return n1 * n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    if n2 == 0:
        return "Can't divide by 0"
    return n1 / n2


def get_key(val):
    for key, value in choice.items():
        if val == value:
            return key

    return "key doesn't exist"


choice = {"+": add, "-": subtract, "*": multipy, "/": divide}

while True:
    print(art.logo)

    num1 = int(input("What's the first number?:"))

    operations = ["+", "-", "*", "/"]
    operation = input(f"{'\n'.join(operations)}\n Pick an operation:")
    num2 = int(input("What's the next number?:"))
    answer = choice[operation](num1, num2)

    return_answer = input(
        f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:",
    )

    if return_answer == "y":
        while True:
            operation = input(
                """ +
-
*
/
Pick an operation:""",
            )
            num2 = int(input("What's the next number?:"))
            answer = choice[operation](answer, num2)

            return_answer = input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:",
            )
            if return_answer == "n":
                print(answer)
                break
    else:
        print(answer)
        break
