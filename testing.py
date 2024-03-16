# I will be using the Visual Studio Code extension called Better Comments for my code.
# If you are also using VS Code I highly recommend you get the extension as well.

# For example:
# Regular Comment
# * Highlighted Comment
# ! Error Comment
# ? Question Comment
# TODO: Comment
# //Crossed Out Comment

import re

import pandas as pd


def make_df():
    # Reading in the data
    df = pd.read_csv("Phishing_Email.csv")
    # Dropping the unecessary index row
    df = df.drop(df.columns[0], axis=1)

    # Removing Nulls
    # Check for null values in the "Email Text" column
    null_mask = df["Email Text"].isnull()

    # If there are null values, drop the corresponding rows
    if null_mask.any():
        df = df.drop(df[null_mask].index)

    # Remove 'empty' emails from the dataframe
    df_cleaned = df[df["Email Text"].str.lower() != "empty"]
    df = df_cleaned

    return df


df_phish = make_df()

df_phish["Email_Length"] = df_phish["Email Text"].str.len()

df_phish["Has_WebLink"] = df_phish["Email Text"].str.contains(
    "(https?://|www.|.com|.org|.net)"
)

df_phish["Is_Response"] = df_phish["Email Text"].str.contains("re :")

df_phish["Hypen_Count"] = df_phish["Email Text"].str.count(r"-")
df_phish["Pound_Count"] = df_phish["Email Text"].str.count(r"#")
df_phish["At_Count"] = df_phish["Email Text"].str.count(r"@")
df_phish["Exclamation_Count"] = df_phish["Email Text"].str.count(r"!")
df_phish["Question_Count"] = df_phish["Email Text"].str.count(r"\?")
df_phish["Period_Count"] = df_phish["Email Text"].str.count(r"\.")


def percent_of_all_caps(text):
    if not text or not isinstance(text, str):
        return 0
    # getting rid of special characters from check for all-caps
    alphanumeric_text = re.sub(r"[^A-Za-z0-9]", "", text)
    num_all_caps = sum(1 for c in alphanumeric_text if c.isupper())
    num_total_characters = len(alphanumeric_text)
    # prevent divide by 0
    if num_total_characters == 0:
        return 0
    percent_all_caps = (num_all_caps / num_total_characters) * 100
    return percent_all_caps


# creating a new column in dataframe for percentage of capitalization and marking emails as safe or phishing
df_phish["Capitalization_Percent"] = df_phish["Email Text"].apply(percent_of_all_caps)

print(df_phish.columns.values.tolist())
