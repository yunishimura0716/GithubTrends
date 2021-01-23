from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

github_url = "https://github.com/trending"

# Create your views here.
def home(request):
    context = {'repos': trending_repos}
    return render(request, 'gitrends/home.html', context)

def detail(request, repo_id):
    repo = trending_repos[repo_id]
    context = {'repo': repo}
    return render(request, 'gitrends/detail.html', context)

def github_trending(url):
    response = requests.get(url)
    response.encoding = response.apparent_encoding

    bs = BeautifulSoup(response.text, 'html.parser')

    results = []
    repos = bs.select('article.Box-row')
    for i, repo in enumerate(repos):
        repo_name = repo.find('h1').find('a').text
        p_tag = repo.find('p')
        repo_description = ""
        if p_tag:
            repo_description = p_tag.getText()

        div_tag = repo.find('div', class_='f6 text-gray mt-2')
        span_tag = div_tag.find('span').find('span', itemprop='programmingLanguage')
        repo_lang = ""
        if span_tag:
            repo_lang = span_tag.contents[0]

        a_tags = div_tag.find_all('a')
        repo_stars = a_tags[0].text
        repo_folks = a_tags[1].text

        results.append({
            'id': i,
            'repo_name': repo_name,
            'repo_description': repo_description,
            'repo_lang': repo_lang,
            'repo_stars': repo_stars,
            'repo_folks': repo_folks
        })

    return results

trending_repos = github_trending(github_url)
