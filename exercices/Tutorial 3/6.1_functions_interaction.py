"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of advertising channels (my list from exercise 4.0) and a maximum
#    share I accept for Meta, in percent (for example 40).
# 2. Process, function by function:
#    a) count_meta_channels counts how many channels in the list belong to Meta.
#    b) percentage turns a part and a total into a percentage.
#    c) is_above_limit says whether a value is higher than a limit.
#    d) is_plan_too_dependent_on_meta uses a), then b), then c) to answer the question.
# 3. Out: True if the media plan depends too much on Meta, False if it does not.
# 4. The question my fourth function answers:
#    "Does this media plan depend too much on Meta?" This matters because if Meta
#    changes its prices or its algorithm, a plan built mostly on Facebook and
#    Instagram is hit everywhere at once.
#    Splitting it into three makes it easier to check: each small function can be
#    tested alone with numbers I can work out in my head. If the final answer is
#    wrong, I test the three parts one by one and I find which step is wrong,
#    instead of searching through one big function.
#
# Test cases (input -> expected output), checked by hand:
#    count_meta_channels(["Facebook Ads", "Google Ads", "Instagram Ads"]) -> 2
#    percentage(2, 8) -> 25.0
#    is_above_limit(50, 40) -> True
#
# Empty list: count_meta_channels([]) returns 0, then percentage(0, 0) would divide
#    by zero, so percentage returns 0.0 when the total is 0. An empty plan does not
#    depend on Meta, so the final answer False is acceptable.


# Your code below
META_CHANNELS = ["Facebook Ads", "Instagram Ads"]


def count_meta_channels(channels):
    count = 0
    for channel in channels:
        if channel in META_CHANNELS:
            count += 1
    return count


def percentage(part, total):
    if total == 0:
        return 0.0
    return part / total * 100


def is_above_limit(value, limit):
    return value > limit


def is_plan_too_dependent_on_meta(channels, max_share):
    meta_count = count_meta_channels(channels)
    meta_share = percentage(meta_count, len(channels))
    return is_above_limit(meta_share, max_share)


# Test each small function on its own
print("Test count_meta_channels:", count_meta_channels(["Facebook Ads", "Google Ads", "Instagram Ads"]), "(expected 2)")
print("Test percentage:", percentage(2, 8), "(expected 25.0)")
print("Test is_above_limit:", is_above_limit(50, 40), "(expected True)")

# Use the fourth function on real plans
all_channels = ["Facebook Ads", "Google Ads", "LinkedIn Ads", "Twitter Ads",
                "Instagram Ads", "Pinterest Ads", "Snapchat Ads", "TikTok Ads"]
b2c_plan = ["Facebook Ads", "Instagram Ads", "Google Ads", "TikTok Ads"]

print("All channels too dependent on Meta?", is_plan_too_dependent_on_meta(all_channels, 40))  # 25 % -> False
print("B2C plan too dependent on Meta?", is_plan_too_dependent_on_meta(b2c_plan, 40))          # 50 % -> True
print("Empty plan too dependent on Meta?", is_plan_too_dependent_on_meta([], 40))              # 0 % -> False