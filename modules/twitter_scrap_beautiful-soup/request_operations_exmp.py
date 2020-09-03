import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.find_all('a'))
# print(soup.title)
# print(soup.select('.storylink')[0])

links = soup.select('.storylink')
subtext = soup.select('.subtext')

links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


# print(create_custom_hn(links,votes))
# create_custom_hn(links,votes)

# pprint.pprint(create_custom_hn(links, subtext))
pprint.pprint(create_custom_hn(mega_links, mega_subtext))
