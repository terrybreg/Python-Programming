"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
#    Two user inputs: the campaign budget and the expected number of customers.
#    One of them is a number (the budget).

# 2. Process:
#    The program asks the user for both values, stores them, then builds a sentence
#    that uses the two pieces of information.

# 3. Out:
#    A sentence summarizing the campaign with the budget and the expected customers.

# 4. My two fields, and what I would do with them:
#    I chose "campaign budget" and "expected number of customers" because in marketing
#    these two values help estimate ROI (return on investment). They are realistic fields
#    I would actually use in my job.


# Your code below
budget = input("Budget in €: ")
customers = input("Expected number of customers: ")

print(f"The campaign has a budget of {budget}€ and aims to reach {customers} customers.")

# CHECK (what happened):
# - Empty line: the program accepted it and printed an empty value.
# - Space: same result, the program printed a blank space.
# - Text instead of a number: the program printed the text, but adding 1 to it would fail.

