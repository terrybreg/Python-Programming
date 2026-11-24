"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: the details of one online ad campaign, typed by the user: the campaign name,
#    the channel (one of my 8 channels from exercise 4.0), the budget spent in euros
#    and the number of clicks. The date is added automatically (today's date).
# 2. Process: the program asks each value and checks it. If a value is not acceptable,
#    it explains why and asks again. Then it adds one line at the end of the CSV file.
#    If the file does not exist yet, it writes the header line first.
# 3. Out, file name and columns: campaign_log.csv
#    Columns: date, campaign_name, channel, budget_eur, clicks
# 4. Why these columns, and what this file is for:
#    These are the minimum I need to compare channels: what I spent (budget_eur) and
#    what I got (clicks), on which channel, for which campaign and when.
#    With two hundred rows, I would compute the cost per click (budget / clicks) for
#    each channel, see which channels are the most profitable and move budget from the
#    expensive channels to the cheap ones. The date lets me follow the trend month by month.
#
# My two decisions:
#    - First time: if campaign_log.csv does not exist, the program creates it and writes
#      the header line once. The next times, the file exists, so it only adds a new line.
#    - Bad value: the program never saves a wrong value. It shows a message and asks the
#      same question again until the answer is acceptable:
#        campaign name must not be empty,
#        channel must be one of the 8 channels in my list,
#        budget must be a number greater than 0,
#        clicks must be a whole number, 0 or more.


# Your code below
import csv
import os
from datetime import date

FILE_NAME = "campaign_log.csv"
COLUMNS = ["date", "campaign_name", "channel", "budget_eur", "clicks"]
CHANNELS = ["Facebook Ads", "Google Ads", "LinkedIn Ads", "Twitter Ads",
            "Instagram Ads", "Pinterest Ads", "Snapchat Ads", "TikTok Ads"]


# Ask for a campaign name and refuse an empty answer
def ask_campaign_name():
    while True:
        name = input("Campaign name: ").strip()
        if name != "":
            return name
        print("The campaign name cannot be empty. Try again.")


# Ask for a channel and accept only one of my 8 channels
def ask_channel():
    print("Channels:", ", ".join(CHANNELS))
    while True:
        channel = input("Channel: ").strip()
        if channel in CHANNELS:
            return channel
        print("Unknown channel. Type it exactly as in the list above.")


# Ask for the budget and accept only a number greater than 0
def ask_budget():
    while True:
        text = input("Budget spent (EUR): ").strip().replace(",", ".")
        try:
            budget = float(text)
        except ValueError:
            print("Please type a number, for example 150 or 99.50.")
            continue
        if budget > 0:
            return budget
        print("The budget must be greater than 0.")


# Ask for the number of clicks and accept only a whole number, 0 or more
def ask_clicks():
    while True:
        text = input("Number of clicks: ").strip()
        if text.isdigit():
            return int(text)
        print("Please type a whole number, 0 or more (no letters, no decimals).")


# Add one entry to the CSV file, and write the header only if the file is new
def save_entry(entry):
    file_is_new = not os.path.exists(FILE_NAME)
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if file_is_new:
            writer.writerow(COLUMNS)
        writer.writerow(entry)


# Main program: collect the values, save them, confirm to the user
entry = [
    date.today().isoformat(),
    ask_campaign_name(),
    ask_channel(),
    ask_budget(),
    ask_clicks(),
]
save_entry(entry)
print("Saved in", FILE_NAME, ":", entry)


# CHECK IT YOURSELF — result
#    I ran the program three times:
#      1) Black Friday, Facebook Ads, 200, 400
#      2) Lubricants B2B, LinkedIn Ads, 300, 150
#      3) Brand awareness, TikTok Ads, 100, 500
#    During the runs I also typed wrong values (empty name, "Tiktok", "abc" as budget,
#    "-5" as budget, "12.5" as clicks): each time the program refused and asked again.
#    Then I opened campaign_log.csv: 4 lines = 1 header line + 3 entries. Correct.