"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""
# 1. In: a list of advertising channels (the list I built in exercise 4.0).
# 2. Process: the function counts how many channels in the list belong to Meta
#    (Facebook Ads and Instagram Ads), then divides by the total number of channels.
# 3. Out: a number, the share of Meta channels in the list, as a percentage (e.g. 25.0).
# 4. My function name, and why return rather than print:
#    My function is called share_of_meta_channels. The name says what it gives back
#    (a share) and what it measures (Meta channels), so you don't need to read the code.
#    It is useful because if a big part of a media plan depends on one company, a change
#    in Meta's prices or algorithm hits the whole plan. This number shows that risk.
#
#    Why return rather than print: print() only shows the result on the screen, and the
#    function then gives back None. return gives the value back to the program, so I can
#    store it in a variable, compare it, use it in another calculation
#    (e.g. "if share >= 50: warning") or display it however I want.
#    A printed result is lost for the rest of the program.
#
# Empty list check:
#    Without the "if not channels" check, an empty list makes the function divide by 0
#    and the program crashes with ZeroDivisionError. I decided to return 0.0 instead:
#    an empty media plan has no Meta channel, and the program keeps running.
#    Limit: 0.0 could also mean "channels but none from Meta", so the two cases look the same.

# Your code below
META_CHANNELS = ["Facebook Ads", "Instagram Ads"]

def share_of_meta_channels(channels):
    if not channels:
        return 0.0
    meta_count = 0
    for channel in channels:
        if channel in META_CHANNELS:
            meta_count += 1
    return meta_count / len(channels) * 100


# The list from exercise 4.0
all_channels = ["Facebook Ads", "Google Ads", "LinkedIn Ads", "Twitter Ads",
                "Instagram Ads", "Pinterest Ads", "Snapchat Ads", "TikTok Ads"]

# Three different inputs
b2c_plan = ["Facebook Ads", "Instagram Ads", "Google Ads", "TikTok Ads"]
b2b_plan = ["LinkedIn Ads", "Google Ads"]

result_all = share_of_meta_channels(all_channels)   # 2 / 8 = 25 %
result_b2c = share_of_meta_channels(b2c_plan)       # 2 / 4 = 50 %
result_b2b = share_of_meta_channels(b2b_plan)       # 0 / 2 = 0 %

print("All channels:", result_all, "% Meta")
print("B2C plan:", result_b2c, "% Meta")
print("B2B plan:", result_b2b, "% Meta")

# Because the function returns a value, I can reuse it:
if result_b2c >= 50:
    print("Warning: the B2C plan depends heavily on Meta.")

# Empty list test
print("Empty list:", share_of_meta_channels([]), "% Meta")