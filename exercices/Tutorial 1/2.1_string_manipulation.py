"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
#    One user input: a sentence typed by the user.

# 2. Process:
#    The program applies four different text transformations to the sentence.

# 3. Out:
#    Four transformed versions of the original sentence.

# 4. My four transformations, and when each is useful:
#    - strip(): useful to clean user input when they accidentally add spaces.
#    - upper(): useful to create titles or warnings in all caps.
#    - lower(): useful when normalizing text before comparing or storing it.
#    - replace(): useful to correct or standardize words automatically.


# Your code below
sentence = input("Enter a sentence: ")

t1 = sentence.strip()
t2 = sentence.upper()
t3 = sentence.lower()
t4 = sentence.replace(" ", "_")   # Example: replace spaces with underscores

print("1.", t1)
print("2.", t2)
print("3.", t3)
print("4.", t4)

# CHECK (what happened):
# - Sentence with spaces at both ends:
#     strip() removed them as expected.
#     upper(), lower(), replace() kept them unless strip() was applied first.
#
# - Sentence with a capital in the middle:
#     upper() made everything uppercase.
#     lower() made everything lowercase.
#     strip() did not change the capital.
#     replace() replaced spaces but kept the capital.
#
# - All results matched what I expected.