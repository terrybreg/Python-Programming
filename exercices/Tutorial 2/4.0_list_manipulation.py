"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:A list of eight marketing channels that I chose myself.
# 2. Process:The program displays the whole list, selects one item, sorts the list, and computes something from it (the number of items).
# 3. Out:The full list, one chosen item, the sorted list, and the computed number.
# 4. What my list is about, and what I computed from it: My list contains different online advertising channels. I computed the total number of channels because it helps understand how many platforms I am working with.

# Your code below
list_of_items = ["Facebook Ads", "Google Ads", "LinkedIn Ads", "Twitter Ads", "Instagram Ads", "Pinterest Ads", "Snapchat Ads", "TikTok Ads"]   
print("Whole list:", list_of_items)
print("First item:", list_of_items[3])
print("Sorted list:", sorted(list_of_items))    
print("Number of items in the list:", len(list_of_items))