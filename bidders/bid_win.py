import art

print(art.logo)
total = {}
"""example = {"a": 4, "b": 3, "c": 2, "d": 1}
print(max(example, key=example.get))  # a"""
while True:
    total = {input("What is your name?: "): input("What is your bid?: $")}
    answer = input("Are there any other bidders? Type 'yes or 'no'.")
    if answer.lower() == "no":
        max = 0
        for key, value in total.items():
            if int(total[key]) > max:
                max = int(total[key])
        print(f"The winner is {key} with a bid of ${max}")
        exit()

    else:
        print("\n" * 20)
