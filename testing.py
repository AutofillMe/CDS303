# I will be using the Visual Studio Code extension called Better Comments for my code.
# If you are also using VS Code I highly recommend you get the extension as well.

# For example:
# Regular Comment
# * Highlighted Comment
# ! Error Comment
# ? Question Comment
# TODO: Comment
# //Grossed Out Comment

import re

import pandas as pd

# Reading in the data
df_phish = pd.read_csv("Phishing_Email.csv")
# Dropping the unecessary index row
df_phish = df_phish.drop(df_phish.columns[0], axis=1)
# checking that it read in correctly
df_phish[0:10]

NullCount = df_phish["Email Text"].isnull().sum()
print("Nulls:", NullCount)
# Check for null values in the "Email Text" column
null_mask = df_phish["Email Text"].isnull()

# If there are null values, drop the corresponding rows
if null_mask.any():
    df_phish = df_phish.drop(df_phish[null_mask].index)
# Checking if null values were dropped
NullCount = df_phish["Email Text"].isnull().sum()
print("Nulls:", NullCount)

# Visual Inspection
print(df_phish.head(10))
print(df_phish.tail(20))

temp = input()

# Check if each "Email Text" is type string
print(df_phish.shape)
# Check if each "Email Text" is type string
is_string = df_phish["Email Text"].apply(lambda x: isinstance(x, str))
print("Number of non-string values in 'Email Text':", (~is_string).sum())
print(df_phish.shape)

temp = input()

# Get count of 'empty' emails
empty_email_count = df_phish["Email Text"].str.lower().eq("empty").sum()
print(f"Number of 'empty' emails: {empty_email_count}")
# Remove those 'empty' emails from the dataframe
df_phish_cleaned = df_phish[df_phish["Email Text"].str.lower() != "empty"]
df_phish_cleaned.shape
empty_email_count = df_phish_cleaned["Email Text"].str.lower().eq("empty").sum()
print(f"Number of 'empty' emails: {empty_email_count}")
df_phish = df_phish_cleaned

temp = input()

print(df_phish.tail(5))
countNAN = df_phish["Email Text"] == "NaN"
print(countNAN.sum())

temp = input()

# print(df_phish.tail(20))
# # Adding "Is_Response" feature
# df_phish["Is_Response"] = None
# # Looping over the DataFrame to determine "Is_Response"
# for i in range(df_phish.shape[0]):
#     has_re = re.search("re :", df_phish.iloc[i]["Email Text"])
#     df_phish.at[i, "Is_Response"] = bool(has_re)
# print(df_phish.tail(20))

# df_phish["Is_Response"].value_counts(normalize=True)

print(df_phish.tail(5))

df_phish["Email_Length"] = df_phish["Email Text"].str.len()

print(df_phish.tail(5))

temp = input()

df_phish["Has_WebLink"] = df_phish["Email Text"].str.contains("(https?://|www\.)")

print(df_phish.tail(5))

temp = input()

df_phish["Is_Response"] = df_phish["Email Text"].str.contains("re :")

print(df_phish.tail(5))
