import requests

def get_github_data(username):
    # Replace 'YOUR_GITHUB_TOKEN' with your actual GitHub Personal Access Token
    # You can generate a token in your GitHub account settings: https://github.com/settings/tokens
    headers = {'Authorization': 'Bearer YOUR_GITHUB_TOKEN'}
    
    # Fetch user data
    user_url = f'https://api.github.com/users/{username}'
    user_response = requests.get(user_url, headers=headers)

    # Check if the request was successful (status code 200)
    if user_response.status_code == 200:
        user_data = user_response.json()
    else:
        print(f"Error fetching user data. Status code: {user_response.status_code}")
        return None, None

    # Fetch repository data
    repos_url = f'https://api.github.com/users/{username}/repos'
    repos_response = requests.get(repos_url, headers=headers)

    # Check if the request was successful (status code 200)
    if repos_response.status_code == 200:
        repos_data = repos_response.json()
    else:
        print(f"Error fetching repository data. Status code: {repos_response.status_code}")
        return None, None

    return user_data, repos_data

def analyze_github_profile(username):
    user_data, repos_data = get_github_data(username)

    # Check if user_data is None (indicating an error in fetching data)
    if user_data is None:
        return

    # Print user details
    print(f'GitHub Profile Analysis for {username}:')
    print(f'Name: {user_data.get("name", "N/A")}')
    print(f'Followers: {user_data["followers"]}')
    print(f'Following: {user_data["following"]}')
    print(f'Repositories: {user_data["public_repos"]}')
    print('---')

    # Analyze programming languages
    languages = {}
    for repo in repos_data:
        language = repo.get('language', 'Unknown')
        languages[language] = languages.get(language, 0) + 1

    print('Most Used Programming Languages:')
    for language, count in sorted(languages.items(), key=lambda x: x[1], reverse=True):
        print(f'{language}: {count}')

if __name__ == '__main__':
    username = input('Enter GitHub username: ')
    analyze_github_profile(username)
