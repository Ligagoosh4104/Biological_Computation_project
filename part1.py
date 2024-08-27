import itertools

# Define the combinations from the table
combinations = [
    (0, 0, 0, 0),  # Combination 1
    (0, 1, 0, 0),  # Combination 2
    (1, 1, 0, 0),  # Combination 3
    (0, 0, 0, 1),  # Combination 4
    (0, 1, 0, 1),  # Combination 5
    (1, 1, 0, 1),  # Combination 6
    (0, 0, 1, 1),  # Combination 7
    (0, 1, 1, 1),  # Combination 8
    (1, 1, 1, 1)  # Combination 9
]


def is_monotonic(func, combinations):
    num_conditions = len(combinations)

    if func[2] == 0 or func[6] == 1:
     return False

    for i in range(num_conditions):
        for j in range(num_conditions):
            # check if condition j has more activators and fewer repressors than condition i
            if (combinations[j][0] >= combinations[i][0] and  # activator
                    combinations[j][1] >= combinations[i][1] and  # activator
                    combinations[j][2] <= combinations[i][2] and  # repressor
                    combinations[j][3] <= combinations[i][3]):  # repressor

                # if func[i] is 1, func[j] must also be 1
                if func[i] > func[j]:
                    return False
    return True


def generate_monotonic_functions(combinations):
    monotonic_functions = []

    # Iterate over all possible binary functions of length 9
    for outputs in itertools.product([0, 1], repeat=len(combinations)):
        if is_monotonic(outputs, combinations):
            monotonic_functions.append(outputs)

    return monotonic_functions


def print_monotonic_functions(monotonic_functions):
    print(f"Total number of monotonic functions: {len(monotonic_functions)}")
    for i, func in enumerate(monotonic_functions):
        print(f"Function {i + 1}: {''.join(map(str, func))}")


# Generate and print monotonic functions
monotonic_functions = generate_monotonic_functions(combinations)
print_monotonic_functions(monotonic_functions)
