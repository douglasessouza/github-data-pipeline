import requests
import base64
import os

class GitHubUploader:

    def __init__(self):
        self.api_base_url = "https://api.github.com"

        # Load token
        self.token = os.getenv("GITHUB_TOKEN")
        if not self.token:
            raise ValueError("Environment variable GITHUB_TOKEN is missing.")

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "Accept": "application/vnd.github+json"
        }

        # Identify authenticated user
        response = requests.get(f"{self.api_base_url}/user", headers=self.headers)
        response.raise_for_status()
        self.username = response.json()["login"]

    def create_repository(self, repo_name: str):
        data = {
            "name": repo_name,
            "description": "Repository containing processed GitHub language data",
            "private": False
        }

        response = requests.post(
            f"{self.api_base_url}/user/repos",
            json=data,
            headers=self.headers
        )

        if response.status_code == 201:
            print("Repository created successfully.")
        elif response.status_code == 422:
            print("Repository already exists.")
        else:
            print("Error creating repository:", response.json())

    def upload_file(self, repo_name: str, file_name: str, file_path: str):

        # Read file
        with open(file_path, "rb") as f:
            encoded_content = base64.b64encode(f.read()).decode("utf-8")

        url = f"{self.api_base_url}/repos/{self.username}/{repo_name}/contents/{file_name}"

        data = {
            "message": f"Adding {file_name} via automated pipeline",
            "content": encoded_content
        }

        response = requests.put(url, json=data, headers=self.headers)
        print(f"Upload status for {file_name}: {response.status_code}")
        print(response.json())
