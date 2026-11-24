"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
#    Two numbers typed by the user.

# 2. Process:
#    Convert the inputs to numbers, then compute the four operations:
#    addition, subtraction, multiplication, and division (if possible).

# 3. Out:
#    The results of the four operations, or an error message if division is impossible.

# 4. What happens when the second number is zero, and why:
#    I chose to display a clear message instead of dividing, because dividing by zero
#    is undefined and stopping the program would be less user-friendly. Asking again
#    could also work, but I prefer informing the user directly.


# Your code below
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b == 0:
    print("Division: impossible (cannot divide by zero).")
else:
    print("Division:", a / b)

# CHECK (what happened):   
# - 7 divided by 2:
#     The program shows 3.5, but if it showed 3, it would be because I used integer
#     division (//) instead of normal division (/). Integer division removes decimals.
#
# - Second number = 0:
#     The program prints the message "impossible" instead of crashing.