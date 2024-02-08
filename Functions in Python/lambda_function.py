operators = {
    "AND": lambda x, y: x and y,
    "OR": lambda x, y: x or y,
    "XOR": lambda x, y: x ^ y,
    "NOT": lambda x: not x,
    "NAND": lambda x, y: not (x and y),
    "NOR": lambda x, y: not (x or y),
    "XNOR": lambda x, y: not (x ^ y),
}

operator_symbols = {
    "AND": "∧",
    "OR": "∨",
    "XOR": "⊕ ",
    "NOT": "¬",
    "NAND": "⊼",
    "NOR": "⊽",
    "XNOR": "⊻",
}


try_again = True

while try_again:
    oper = input("Enter the operator: ").upper()
    # Generate the truth table
    if oper in operators:
        for i in range(2):
            if oper == "NOT":
                if operators[oper](i) == True:
                    result = "1"
                else:
                    result = "0"
                print(f"{operator_symbols[oper]} {i} = {result}")
            else:
                for j in range(2):
                    if operators[oper](i, j) == True:
                        result = "1"
                    else:
                        result = "0"
                    print(f"{i} {operator_symbols[oper]} {j} = {result}")

    do_again = input(
        "Do you want check another gate if yes type y if not type anything: "
    ).lower()

    if do_again == "y":
        try_again = True
    else:
        try_again = False
