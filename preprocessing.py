import pandas as pd

def clean_text(value):
    if value == "\\N" or value == "" or pd.isna(value):
        return ""
    return str(value).replace(",", " ").lower()

def load_and_clean_data(limit=5000):
    df = pd.read_csv("data/movies.tsv", sep="\t", low_memory=False)

    df = df[["primaryTitle", "genres", "averageRating", "numVotes", "directors", "writers"]]

    for col in ["genres", "directors", "writers"]:
        df[col] = df[col].apply(clean_text)

    df["averageRating"] = df["averageRating"].replace("\\N", "").astype(str)
    df["numVotes"] = df["numVotes"].replace("\\N", "").astype(str)

    df["text"] = (
        df["genres"] + " " +
        df["directors"] + " " +
        df["writers"] + " " +
        df["averageRating"] + " " +
        df["numVotes"]
    ).str.strip()

    df = df[df["primaryTitle"].notna()]
    df = df[df["primaryTitle"] != ""]

    df["numVotes_num"] = pd.to_numeric(df["numVotes"], errors="coerce")
    df = df.sort_values(by="numVotes_num", ascending=False)

    df = df.head(limit).reset_index(drop=True)

    return df
