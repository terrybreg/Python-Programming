"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
#    One number N typed by the user.

# 2. Process:
#    The program checks the value of N, then prints for every number from 1 to N
#    whether it is odd or even. If N is very large, it asks the user whether they
#    want all numbers or only the result for N.

# 3. Out:
#    Either a full list from 1 to N, or a single odd/even result, depending on the user's choice.

# 4. What happens on 0, on a negative number, on a very large number:
#    - If the user types 0: I display a message saying that there is nothing to list.
#    - If the user types a negative number: I display an error message.
#    - If the user types a very large number (like 5000): I ask the user whether they
#      want all numbers or just the odd/even result for N. This avoids printing thousands
#      of lines without permission.


# Your code below
N = int(input("Enter a number: "))

if N == 0:
    print("Nothing to list: 0 gives no numbers from 1 to N.")

elif N < 0:
    print("Error: negative numbers are not allowed.")

elif N > 1000:
    choice = input("This will print over 1000 lines. Do you want ALL numbers (yes/no)? ")

    if choice.lower() == "yes":
        for i in range(1, N + 1):
            if i % 2 == 0:
                print(f"{i} is even")
            else:
                print(f"{i} is odd")
    else:
        # Only show the result for N
        if N % 2 == 0:
            print(f"{N} is even")
        else:
            print(f"{N} is odd")

else:
    for i in range(1, N + 1):
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")


# CHECK (what happened):
# - With N = 6:
#     You should see: 1 odd, 2 even, 3 odd, 4 even, 5 odd, 6 even.
#
# - With N = 0:
#     The program prints the message "Nothing to list".
#
# - With a negative number:
#     The program prints the error message.
#
# - With 5000:
#     The program asks whether you want all numbers or just the result for 5000.