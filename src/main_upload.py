from upload_files import GitHubUploader

# Initialize uploader
uploader = GitHubUploader()

# Repository where CSVs will be uploaded
repo_name = "github-language-analysis"
uploader.create_repository(repo_name)

# Upload files
uploader.upload_file(repo_name, "languages_amazon.csv", "data/amazon/languages_amazon.csv")
uploader.upload_file(repo_name, "languages_netflix.csv", "data/netflix/languages_netflix.csv")
uploader.upload_file(repo_name, "languages_spotify.csv", "data/spotify/languages_spotify.csv")

print("Upload completed.")
