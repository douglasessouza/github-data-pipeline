import requests
import pandas as pd
import os

class RepositoryData:

    def __init__(self, owner: str):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'

        # Load token from environment variable
        self.access_token = os.getenv("GITHUB_TOKEN")
        if not self.access_token:
            raise ValueError("Environment variable GITHUB_TOKEN is missing.")

        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def list_repositories(self):
        repos_list = []

        for page_num in range(1, 20):
            url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
            response = requests.get(url, headers=self.headers)

            if response.status_code != 200:
                break

            repos_list.append(response.json())

        return repos_list

    def extract_repo_names(self, repos_list):
        repo_names = []
        for page in repos_list:
            for repo in page:
                repo_names.append(repo.get("name"))
        return repo_names

    def extract_repo_languages(self, repos_list):
        repo_languages = []
        for page in repos_list:
            for repo in page:
                repo_languages.append(repo.get("language"))
        return repo_languages

    def create_language_dataframe(self):
        repos_list = self.list_repositories()
        names = self.extract_repo_names(repos_list)
        languages = self.extract_repo_languages(repos_list)

        df = pd.DataFrame({
            "repository_name": names,
            "language": languages
        })

        return df
