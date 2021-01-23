from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

github_url = "https://github.com/trending"

# Create your views here.
def home(request):
    # trending_repos = github_trending(github_url)
    context = {'repos': 'Hello World'}
    return render(request, 'gitrends/home.html', context)

def github_trending(url):
    response = requests.get(url)
    response.encoding = response.apparent_encoding

    bs = BeautifulSoup(response.text, 'html.parser')

    results = []
    repos = bs.select('h1.h3.lh-condensed')
    for i, repo in enumerate(repos):
        a_tag = repo.find('a')
        repo_name = a_tag.text
        repo_developer = a_tag.find('span').text
        results.append({'id': i, 'repo_name': repo_name, 'repo_developer': repo_developer})

    return results
