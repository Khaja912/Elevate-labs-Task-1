import pandas as pd

# 1. Load dataset
df = pd.read_csv("netflix_titles.csv")

# 2. Handle missing values with placeholders
df = pd.DataFrame(df)
print(df.isnull())
print(df.isnull().sum())
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Not Available")
df['country'] = df['country'].fillna("Unknown")
df['date_added'] = df['date_added'].fillna("01-Jan-1900")
df['rating'] = df['rating'].fillna("Unknown")
df['duration'] = df['duration'].fillna("Unknown")

# 3. Remove duplicates
df = df.drop_duplicates()

# 4. Standardize text values
df['country'] = df['country'].astype(str).str.strip().str.title()
df['rating'] = df['rating'].astype(str).str.upper().str.replace(" ", "")

# 5. Convert date formats (dd-mm-yyyy)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['date_added'] = df['date_added'].dt.strftime("%d-%m-%Y")

# 6. Rename column headers (lowercase, no spaces)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 7. Fix data types
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce').astype('Int64')
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce', format="%d-%m-%Y")

# 8. Save cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False)

print("Netflix dataset cleaned and saved as netflix_cleaned.csv")

