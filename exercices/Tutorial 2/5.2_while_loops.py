"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""
# 1. In:
#    User input, repeated until my stop condition is met or the attempt limit is reached.

# 2. Process:
#    The program keeps asking the user a question. Each answer is cleaned (lowercase,
#    stripped of spaces). The loop stops either when the stop condition is met or when
#    the maximum number of attempts is reached.

# 3. Out:
#    A summary describing how many attempts were made, whether the stop condition was
#    reached, and what the user answered.

# 4. My stop condition, my attempt limit, my summary:
#    Stop condition: the user must type "yes" (case-insensitive, extra spaces allowed).
#    Attempt limit: 10 attempts maximum.
#    Summary: number of attempts, the final answer, and whether the condition was met.


# Your code below

attempts = 0
max_attempts = 10   
stop_condition = "yes"  

answers = []  

while attempts < max_attempts:
    user_input = input("Type 'yes' to continue: ")
    cleaned = user_input.strip().lower()  # handles YES, yes,   yes, etc.
    answers.append(user_input)

    attempts += 1

    if cleaned == stop_condition:
        print("Stop condition met.")
        break

print("\n--- Summary ---")
print(f"Attempts made: {attempts}")
print(f"User answers: {answers}")

if cleaned == stop_condition:
    print("The user met the stop condition.")
else:
    print("The user did NOT meet the stop condition before the limit.")