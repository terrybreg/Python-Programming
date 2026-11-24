# campaign_audit.py — Campaign Audit Quiz (Session 8, final exam practice)
# Terry Bregmestre
#
# WHAT MY PROGRAM DOES
#   It reads the quarterly advertising export campaigns_A.csv, computes CTR, CPA and
#   ROAS for each campaign, asks the player five questions, checks each answer, shows
#   the final score and saves the player name, the score and the date in result.csv.
#
# WHAT IS WRONG WITH MY FILE (found by opening campaigns_A.csv and reading it)
#   - The separator is a semicolon ";", not a comma.
#   - Amounts use the European decimal comma: "11088,60" means 11088.60.
#   - There is an empty column with no name between "Conversions" and "Revenue (€)" (";;").
#   - Column names contain spaces and the € sign: "Cost (€)", "Revenue (€)".
#   - The file starts with an invisible BOM character, so the first column name can be read
#     as "﻿Campaign" instead of "Campaign". Opening with "utf-8-sig" removes it.
#   - "Monthly Newsletter" has an empty Impressions cell: excluded from every calculation.
#   - "Black Friday" and "App Install" have 0 conversions: no CPA for them, but they stay
#     in CTR, ROAS and the conversions total.
#   - The last line of the file is empty.
#
# MY CHOICES
#   - CTR is shown in percent (4838 / 283000 = 1.71 %), so question 5 expects a percent.
#   - The average CTR is the average of the CTRs of the campaigns (11 campaigns, the
#     newsletter is excluded), not total clicks / total impressions.
#   - Text answers are accepted whatever the capitals and spaces ("meta ads" = "Meta Ads").
#   - result.csv keeps every game: the header is written only the first time.


import csv
import os
from datetime import datetime

# I look for the files in the same folder as this program, so it works from any terminal
FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(FOLDER, "campaigns_A.csv")
RESULT_FILE = os.path.join(FOLDER, "result.csv")


# Turn a text amount like "11088,60" into the number 11088.60
def to_number(text):
    return float(text.strip().replace(",", "."))


# Step 1: read the CSV and keep only the campaigns I am allowed to use
def load_campaigns(path):
    campaigns = []
    with open(path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            # skip the empty line at the end of the file
            if not row.get("Campaign"):
                continue
            # rule 1: empty impressions -> the campaign is left out of everything
            if row["Impressions"].strip() == "":
                print("Excluded (no impressions):", row["Campaign"])
                continue
            campaigns.append({
                "name": row["Campaign"].strip(),
                "channel": row["Channel"].strip(),
                "impressions": to_number(row["Impressions"]),
                "clicks": to_number(row["Clicks"]),
                "cost": to_number(row["Cost (€)"]),
                "conversions": to_number(row["Conversions"]),
                "revenue": to_number(row["Revenue (€)"]),
            })
    return campaigns


# CTR in percent: share of people who saw the ad and clicked
def compute_ctr(campaign):
    return campaign["clicks"] / campaign["impressions"] * 100


# CPA: cost of one conversion. None when there is no conversion (rule 2, no division by 0)
def compute_cpa(campaign):
    if campaign["conversions"] == 0:
        return None
    return campaign["cost"] / campaign["conversions"]


# ROAS: how much one euro spent brings back
def compute_roas(campaign):
    if campaign["cost"] == 0:
        return None
    return campaign["revenue"] / campaign["cost"]


# Step 2: add CTR, CPA and ROAS to every campaign
def add_indicators(campaigns):
    for campaign in campaigns:
        campaign["ctr"] = compute_ctr(campaign)
        campaign["cpa"] = compute_cpa(campaign)
        campaign["roas"] = compute_roas(campaign)
    return campaigns


# Question 1: the campaign with the highest CTR
def best_ctr_campaign(campaigns):
    best = max(campaigns, key=lambda c: c["ctr"])
    return best["name"]


# Question 2: the campaign with the highest CPA, among campaigns that have a CPA
def highest_cpa_campaign(campaigns):
    with_cpa = [c for c in campaigns if c["cpa"] is not None]
    worst = max(with_cpa, key=lambda c: c["cpa"])
    return worst["name"]


# Question 3: how many campaigns have a ROAS strictly above 3
def count_roas_above(campaigns, limit):
    count = 0
    for campaign in campaigns:
        if campaign["roas"] is not None and campaign["roas"] > limit:
            count += 1
    return count


# Question 4: the channel with the most conversions, adding up all its campaigns
def top_conversion_channel(campaigns):
    totals = {}
    for campaign in campaigns:
        channel = campaign["channel"]
        totals[channel] = totals.get(channel, 0) + campaign["conversions"]
    return max(totals, key=totals.get)


# Question 5: the average CTR of all campaigns, in percent, rounded to 2 decimals
def average_ctr(campaigns):
    total = 0
    for campaign in campaigns:
        total += campaign["ctr"]
    return round(total / len(campaigns), 2)


# Build the five questions with the answers computed by the program
def build_questions(campaigns):
    return [
        ("Which campaign has the best CTR?", best_ctr_campaign(campaigns), "text"),
        ("Which campaign has the highest CPA?", highest_cpa_campaign(campaigns), "text"),
        ("How many campaigns have a ROAS above 3?", count_roas_above(campaigns, 3), "integer"),
        ("Which channel generated the most conversions in total?", top_conversion_channel(campaigns), "text"),
        ("What is the average CTR across all campaigns, in %, rounded to two decimals?", average_ctr(campaigns), "decimal"),
    ]


# Ask the player's name and refuse an empty answer
def ask_player_name():
    while True:
        name = input("Your name: ").strip()
        if name:
            return name
        print("Please type your name.")


# Ask one question and ask again until the answer has the right type
def ask_answer(question, answer_type):
    while True:
        answer = input(question + " ").strip()
        if answer_type == "text":
            if answer:
                return answer
            print("Please type an answer.")
        else:
            try:
                if answer_type == "integer":
                    return int(answer)
                return float(answer.replace(",", ".").replace("%", ""))
            except ValueError:
                print("Please type a number.")


# Step 4: compare the player's answer with the correct one
def is_correct(player_answer, correct_answer, answer_type):
    if answer_type == "text":
        return player_answer.strip().lower() == correct_answer.strip().lower()
    if answer_type == "integer":
        return player_answer == correct_answer
    # decimals: I accept the answer if it is the same once rounded to 2 decimals
    return round(player_answer, 2) == correct_answer


# Steps 3 and 4: ask the five questions and keep the score
def play_quiz(questions):
    score = 0
    for number, (question, correct_answer, answer_type) in enumerate(questions, start=1):
        player_answer = ask_answer(f"Q{number}. {question}", answer_type)
        if is_correct(player_answer, correct_answer, answer_type):
            print("Correct!")
            score += 1
        else:
            if answer_type == "decimal":
                correct_answer = f"{correct_answer:.2f}"
            print("Wrong. The answer was:", correct_answer)
    return score


# Step 6: add one line to result.csv, with the header only if the file is new
def save_result(path, player_name, score, total):
    file_is_new = not os.path.exists(path)
    with open(path, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        if file_is_new:
            writer.writerow(["player_name", "score", "date"])
        writer.writerow([player_name, f"{score}/{total}", datetime.now().strftime("%Y-%m-%d %H:%M")])


# Main function: runs the steps in order and says which step failed if something goes wrong
def main():
    step = "loading the CSV file"
    try:
        campaigns = load_campaigns(DATA_FILE)
        step = "computing the indicators"
        campaigns = add_indicators(campaigns)
        step = "building the questions"
        questions = build_questions(campaigns)

        print("\n=== Campaign Audit Quiz ===")
        step = "asking the player's name"
        player_name = ask_player_name()
        step = "playing the quiz"
        score = play_quiz(questions)

        # Step 5: final score
        print(f"\nFinal score for {player_name}: {score}/{len(questions)}")
        step = "saving result.csv"
        save_result(RESULT_FILE, player_name, score, len(questions))
        print("Result saved in result.csv")
    except FileNotFoundError:
        print("Error: campaigns_A.csv was not found. Put it in the same folder as this program.")
    except KeyError as error:
        print(f"Error while {step}: column {error} not found in the CSV file.")
    except Exception as error:
        print(f"Error while {step}: {error}")


if __name__ == "__main__":
    main()


# CHECK BY HAND (one value of each indicator, compared with the program)
#   CTR Winter Sale  = 4838 / 283000 = 0.0171 -> 1.71 %      program: 1.71 %
#   CPA Winter Sale  = 11088.60 / 290 = 38.24 €               program: 38.24
#   ROAS Winter Sale = 58416.73 / 11088.60 = 5.27             program: 5.27
#   Black Friday has 0 conversions -> no CPA, no crash.
#   Monthly Newsletter has no impressions -> excluded, so 11 campaigns are used.