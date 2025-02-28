import requests

GITHUB_TOKEN = "Github TOKEN"
USERNAME = "Github USERNAME"

BASE_URL = "https://api.github.com"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

response = requests.get(f"{BASE_URL}/user/repos", headers=headers)
repos = response.json()

for repo in repos:
    repo_name = repo["name"]
    delete_url = f"{BASE_URL}/repos/{USERNAME}/{repo_name}"
    delete_response = requests.delete(delete_url, headers=headers)

    if delete_response.status_code == 204:
        print(f"{repo_name} o'chirildi.")
    else:
        print(f"{repo_name} o'chirilmadi.")
