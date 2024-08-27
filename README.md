# Biological Computation project- part 1
This program aims to find all monotonic Boolean functions that meet the set of given combinations (gens) where the first two bits are activators and the last two bits are repressors. In other words, it simply goes through all possible Boolean functions-there are 512 (2^9) of them-and verifies if they satisfy this principle of monotonicity.

### Monotonicity Rule:

If a Boolean function is 1 (on) for a given combination (gen), it must also be 1 for all combinations that have more activators or fewer repressors. Conversely, if it is 0 (off) for a combination, it can remain off or turn on as activators increase or repressors decrease but cannot turn off if it was on.

### Steps the Program Takes:

- Combination Setup: The combinations are predefined as a list of tuples where each tuple represents a specific combination of activators and repressors.
- Monotonicity Check: For each possible Boolean function, the program checks whether it is monotonic by comparing the output for all pairs of conditions.
- Function Generation: The program generates all possible 9-bit Boolean functions (512 total) and filters them based on the monotonicity check.
- Output: The program prints all valid monotonic functions that satisfy the combinations.

### How to Run the Program:
Prerequisites:
Python 3.x should be installed on your system.
##### Steps to Run:
- Save the provided Python code in a file named part1.py or other name.
- Run regularly over pycharm or open a terminal (\command prompt) and navigate to the directory where the file is saved.
- Run the program using the following command:
````
python part1.py
````
The program will print the total number of monotonic functions identified, followed by the list of those functions.

### Expected Output:
Upon running the program, the expected output should be:
````
Total number of monotonic functions: 18
Function 1: 001000000
Function 2: 001001000
Function 3: 001001001
Function 4: 011000000
Function 5: 011001000
Function 6: 011001001
Function 7: 011011000
Function 8: 011011001
Function 9: 011011011
Function 10: 111000000
Function 11: 111001000
Function 12: 111001001
Function 13: 111011000
Function 14: 111011001
Function 15: 111011011
Function 16: 111111000
Function 17: 111111001
Function 18: 111111011
````
