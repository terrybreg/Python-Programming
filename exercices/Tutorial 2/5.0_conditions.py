"""Exercise 5.0 — Making the program decide

WHAT THE PROGRAM MUST DO
    Ask the user for a number, then display a different message depending on which
    range that number falls into. At least four ranges.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your four ranges, what are their exact boundaries, and what does each
       message say? Write the boundaries down before you code them.

WHAT THE AI CANNOT KNOW
    Your ranges and your boundaries. It can be an age, a budget, a satisfaction score,
    a delivery time. Choose something with a real meaning and defend the cut-off points.

    Boundaries are where programs go wrong. Decide explicitly whether a value exactly
    on the boundary belongs to the range above or the one below.

CHECK IT YOURSELF
    Test each of your boundary values exactly: if one range ends at 25, run it with 25.
    Then with 24 and 26. Write in a comment whether each landed where you intended.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
#    One number entered by the user.

# 2. Process:
#    The program checks which range the number falls into and displays the
#    corresponding message. Boundaries are explicitly defined.

# 3. Out:
#    A message describing the range of the number.

# 4. My ranges, my boundaries, my messages:
#    I chose to classify a delivery time (in days), because it is meaningful in my field.
#    My four ranges:
#      - 0 to 2 days: "Ultra fast delivery"
#      - 3 to 5 days: "Standard delivery"
#      - 6 to 10 days: "Slow delivery"
#      - 11 days and above: "Very late delivery"
#
#    Boundary decisions:
#      - 2 belongs to the first range (0–2)
#      - 3 belongs to the second range (3–5)
#      - 5 belongs to the second range (3–5)
#      - 6 belongs to the third range (6–10)
#
#    Boundary tests:
#      - Input 2 → correct range
#      - Input 3 → correct range
#      - Input 5 → correct range
#      - Input 6 → correct range

# Your code below

days = int(input("Enter delivery time in days: "))

if 0 <= days <= 2:
    print("Ultra fast delivery")
elif 3 <= days <= 5:
    print("Standard delivery")
elif 6 <= days <= 10:
    print("Slow delivery")
elif days >= 11:
    print("Very late delivery")
else:
    print("Invalid value")

    # Everything went well. The program behaved exactly as intended.
# All boundary values landed in the correct ranges:
# - 0 and 2 were classified as "Ultra fast delivery"
# - 3 and 5 were classified as "Standard delivery"
# - 6 and 10 were classified as "Slow delivery"
# - 11 was classified as "Very late delivery"
# - Any invalid negative value was correctly flagged as "Invalid value"
#
# The logic is correct, the boundaries are respected, and the program displays the right message for each delivery-time range.