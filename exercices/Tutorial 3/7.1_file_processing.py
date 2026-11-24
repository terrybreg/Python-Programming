"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""


# What is wrong with names.txt (found by reading it, not by guessing):
# - Empty lines: there are 2 blank lines (after "grace hopper" and after "GUIDO van rossum").
# - Spaces at the start of some lines: "  alan TURING" and "  linus torvalds".
# - Capital letters are inconsistent: some names are all lowercase ("grace hopper"),
#   some last names are all uppercase ("LOVELACE"), one first name is uppercase ("GUIDO").
# - One name has three words: "GUIDO van rossum". The last name is "van Rossum", not
#   just "rossum", and "van" is a particle that should stay lowercase.
# - The names are not in any order.

# 1. In: names.txt, a text file with one person per line (first name, then last name).
# 2. Process, problem by problem:
#    - Empty lines -> after removing spaces, a line with nothing left is skipped.
#    - Spaces at the start (or end) -> strip() removes them; split() also removes
#      extra spaces between words.
#    - Inconsistent capitals -> each word is rewritten with a capital first letter and
#      the rest in lowercase ("LOVELACE" -> "Lovelace", "GUIDO" -> "Guido").
#    - Three-word name -> the first word is the first name, all the other words are the
#      last name. Particles like "van" stay in lowercase ("van Rossum").
#    - No order -> the list is sorted by last name, ignoring capitals and the particle.
# 3. Out: names_clean.txt, one clean name per line ("First Last"), sorted by last name.
#    names.txt is only opened for reading ("r"), so it is never modified.
# 4. How I decide which word is the last name:
#    In this file the first name always comes first. So the first word is the first name
#    and everything after it is the last name. With two words, the last name is the
#    second word. With "Guido van Rossum", the last name is "van Rossum".
#    To sort, I ignore the particle "van" and use "Rossum", like an index in a book.
#    So Guido van Rossum is sorted under R, between Lovelace and Torvalds.


# Your code below
import os

# Look for the files in the same folder as this program, not in the folder the
# terminal happens to be in (otherwise Python says "No such file or directory")
try:
    FOLDER = os.path.dirname(os.path.abspath(__file__))
except NameError:  # Google Colab has no __file__: use the current folder
    FOLDER = os.getcwd()

INPUT_FILE = os.path.join(FOLDER, "names.txt")
OUTPUT_FILE = os.path.join(FOLDER, "names_clean.txt")
PARTICLES = ["van", "von", "de", "du", "da", "di", "le", "la"]


# Put one word in the right case: particles in lowercase, other words capitalized
def clean_word(word):
    word = word.lower()
    if word in PARTICLES:
        return word
    return word.capitalize()


# Turn a raw line into (first name, last name), or None if the line is empty
def parse_line(line):
    words = line.split()
    if not words:
        return None
    first_name = clean_word(words[0])
    last_name = " ".join(clean_word(w) for w in words[1:])
    return first_name, last_name


# Give the key used for sorting: the last name without particles, in lowercase
def sort_key(person):
    first_name, last_name = person
    main_words = [w for w in last_name.split() if w not in PARTICLES]
    return " ".join(main_words).lower(), first_name.lower()


# Read the original file (read-only) and keep only the lines that contain a name
people = []
with open(INPUT_FILE, "r", encoding="utf-8") as file:
    for line in file:
        person = parse_line(line)
        if person is not None:
            people.append(person)

# Sort the people by last name
people.sort(key=sort_key)

# Write the clean, sorted list to a new file
with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    for first_name, last_name in people:
        file.write(first_name + " " + last_name + "\n")

print(len(people), "names written to", OUTPUT_FILE)


# CHECK IT YOURSELF — result
#    names.txt has 10 lines. names_clean.txt has 8 lines.
#    The difference is 2: the two empty lines were removed. No name was lost.
#    First name of the sorted list: Margaret Hamilton (H is the first letter among
#    Hamilton, Hopper, Johnson, Liskov, Lovelace, Rossum, Torvalds, Turing).
#    Last name of the sorted list: Alan Turing (Torvalds comes before Turing because
#    "o" comes before "u"). Both checked by hand.