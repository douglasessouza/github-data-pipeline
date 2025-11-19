from fetch_repos import RepositoryData
import os

# Create directories if they don't exist
os.makedirs("data/amazon", exist_ok=True)
os.makedirs("data/netflix", exist_ok=True)
os.makedirs("data/spotify", exist_ok=True)

# GitHub company accounts
amazon = RepositoryData("amzn")
netflix = RepositoryData("netflix")
spotify = RepositoryData("spotify")

# Generate dataframes
df_amazon = amazon.create_language_dataframe()
df_netflix = netflix.create_language_dataframe()
df_spotify = spotify.create_language_dataframe()

# Save results as CSV
df_amazon.to_csv("data/amazon/languages_amazon.csv", index=False)
df_netflix.to_csv("data/netflix/languages_netflix.csv", index=False)
df_spotify.to_csv("data/spotify/languages_spotify.csv", index=False)

print("CSV files successfully created.")
