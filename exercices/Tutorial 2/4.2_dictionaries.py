"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
#    A dictionary describing one real object from my field, with at least five meaningful fields.

# 2. Process:
#    The program reads one field, modifies another, removes one field, and safely handles
#    the case where a requested field does not exist.

# 3. Out:
#    The updated dictionary displayed field by field, plus a demonstration that the program
#    survives a missing-field lookup.

# 4. My object, my five fields, and why those:
#    I chose APIs, because it is one thing I am particularly interested in, and linked to Python.
#    My five fields:
#      - "client": identifies which client or service the API belongs to
#      - "server": the base URL used to send requests
#      - "dashboard": used to monitor API usage and performance
#      - "auth_required": important to know whether authentication is needed
#      - "rate_limit": a real constraint when working with APIs
#    All of these are fields I would actually use in my job.


# Your code below
api = {
    "client": "YouTube",
    "server": "https://www.googleapis.com/youtube/v3",
    "dashboard": "Brandwatch",
    "auth_required": True,
    "rate_limit": "10,000 requests/day"
}

print("Original dictionary:")
print(api)

# Read one field
print("\nReading field 'server':", api["server"])

# Modify one field
api["rate_limit"] = "20,000 requests/day"
print("\nAfter modifying 'rate_limit':", api)

# Remove one field
removed = api.pop("dashboard")
print("\nRemoved field 'dashboard' (value was:", removed, ")")
print("Dictionary now:", api)

# Ask for a field that does not exist
print("\nTrying to access a missing field 'timeout':")

# Safe version (survives the missing key)
value = api.get("timeout", "Field does not exist — handled safely.")
print(value)

# Display every field with its value
print("\nFinal dictionary fields:")
for key, value in api.items():
    print(f"{key}: {value}")