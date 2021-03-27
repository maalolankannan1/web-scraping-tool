import requests
from bs4 import BeautifulSoup as bs

git_user = input('Enter Github username: ')
url = 'https://github.com/'+git_user+'?tab=repositories'
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', {'alt' : 'Avatar'})['src']
print("Link for the Profile Image : " + profile_image)
all_repos = soup.findAll('li', {'itemprop' : 'owns'})
repo_names = []
for repo in all_repos:
    repo_names.append(repo.find('a',{'itemprop' : 'name codeRepository'}).get_text())
## repo_names contains list of all repos
print(" The Repositories of " + git_user + " :\n")
for repo in repo_names:
    print(repo)