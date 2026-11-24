"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
#    The list I created in exercise 4.0.

# 2. Process:
#    For each item, the program displays a line combining:
#    - the item itself
#    - its position in the list
#    - something computed about it (here: the length of the item name)

# 3. Out:
#    One line per item, each containing the item, its index, and the computed value.

# 4. What I compute for each item, and why it is worth showing:
#    I compute the length of each item name. This is useful because it shows how long each advertising channel name is, which can matter for formatting, reporting, or UI constraints.


# Your code below

list_of_items = [
    "Facebook Ads", "Google Ads", "LinkedIn Ads", "Twitter Ads","Instagram Ads", "Pinterest Ads", "Snapchat Ads", "TikTok Ads"]

for index, item in enumerate(list_of_items):
    length = len(item)
    print(f"Position {index}: {item} — Length: {length}")

# Check: number of printed lines must match number of items
# There are 8 items → the program prints exactly 8 lines.