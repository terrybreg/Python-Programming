"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Une liste de valeurs (celle créée dans l’exercice 4.0).

# 2. Process: Afficher cette liste dans quatre ordres différents en utilisant des méthodes qui modifient la liste ou qui renvoient une copie.

# 3. Out:Les quatre versions réordonnées + la preuve que la liste originale n’a pas été modifiée.

# 4. My four orders, and which ones modify the original:
# - sorted(list) → returns a new list (does not modify the original)
# - list.sort() → modifies the list in place
# - reversed(list) or list[::-1] → returns a new list (does not modify the original)
# - list.reverse() → modifies the list in place

# Your code below
original = list_of_items = ["Facebook Ads", "Google Ads", "LinkedIn Ads", "Twitter Ads", "Instagram Ads", "Pinterest Ads", "Snapchat Ads", "TikTok Ads"]

print("Original list:", original)

# 1. sorted() → copie
print("Sorted (copy):", sorted(original))

# 2. sort() → modifie
temp1 = original[:]        # on fait une copie pour ne pas abîmer l’original
temp1.sort()
print("Sort() (modifies copy):", temp1)

# 3. reversed() → copie
print("Reversed (copy):", list(reversed(original)))

# 4. reverse() → modifie
temp2 = original[:]        # encore une copie
temp2.reverse()
print("Reverse() (modifies copy):", temp2)

# Preuve que l’original n’a pas bougé
print("Original list at the end:", original)
