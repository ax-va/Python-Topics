"""
Lightweight scrapping by Beautiful Soup and lxml

Scrapping the table in https://en.wikipedia.org/wiki/List_of_Nobel_laureates

The DOM of the Wiki table:

<table class="wikitable sortable jquery-tablesorter">
    <thead>
        <tr>
            <th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">
                Year
            </th>
            <th width="17%" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">
                <a href="/wiki/List_of_Nobel_laureates_in_Physics" title="List of Nobel laureates in Physics">
                    Physics
                </a>
            </th>
            ...
        </tr>
    </thead>
    <tbody>
        <tr id="1901">
            <td align="center">
                1901
            </td>
            <td>
                <span data-sort-value="Röntgen, Wilhelm">
                    <span class="vcard">
                        <span class="fn">
                            <a href="/wiki/Wilhelm_R%C3%B6ntgen" title="Wilhelm Röntgen">
                                Wilhelm Röntgen
                            </a>
                        </span>
                    </span>
                </span>
            </td>
            ...
        </tr>
        ...
    ...
"""
from typing import List, Dict

import bs4
import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://en.wikipedia.org'
# Wikipedia rejects requests unless a 'User-Agent' attribute is added to the http header
HEADERS = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(
    url=BASE_URL+"/wiki/List_of_Nobel_laureates",
    headers=HEADERS,
)
response.content
# ...
# <table class="wikitable sortable">\n\n<tbody><tr>\n<th>Year\n</th>\n<th width="17%">...
# ...

# WARNING: The response content distinguishes from the HTML source

soup = BeautifulSoup(response.content, "lxml")
type(soup.find('table', {'class': 'wikitable sortable'}))
# bs4.element.Tag
str(soup.find('table', {'class': 'wikitable sortable'}))[:100]
# '<table class="wikitable sortable">\n<tbody><tr>\n<th>Year\n</th>\n<th width="17%"><a href="/wiki/List_of'

# Change the order of our CSS classes
soup.find('table', {'class': 'sortable wikitable'}) is None
#  True

# Use CSS selector
soup.select('table.sortable.wikitable')
type(soup.select('table.sortable.wikitable'))
# bs4.element.ResultSet
len(soup.select('table.sortable.wikitable'))
# 1
str(soup.select('table.sortable.wikitable')[0])[:100]
# '<table class="wikitable sortable">\n<tbody><tr>\n<th>Year\n</th>\n<th width="17%"><a href="/wiki/List_of'

# Find only the first tag that matches the selector
table = soup.select_one('table.sortable.wikitable')
type(table)
# bs4.element.Tag
len(table.select('th'))
# 14
# shorthand
len(table('th'))
# 14


def get_column_titles(table: bs4.element.Tag) -> List[Dict]:
    """
    Gets the Nobel categories from the table header
    """
    columns = []
    for th in table.select_one('tr').select('th'):
        link = th.select_one('a')
        # Store the category name and any Wikipedia link it has
        if link:
            columns.append(
                {
                    'name': link.text,
                    'href': link.attrs['href'],
                }
            )
        else:
            columns.append(
                {
                    'name': th.text,
                    'href': None,
                }
            )
    return columns


get_column_titles(table)
# [{'name': 'Year\n', 'href': None},
#  {'name': 'Physics', 'href': '/wiki/List_of_Nobel_laureates_in_Physics'},
#  {'name': 'Chemistry', 'href': '/wiki/List_of_Nobel_laureates_in_Chemistry'},
#  {'name': 'Physiologyor Medicine',
#   'href': '/wiki/List_of_Nobel_laureates_in_Physiology_or_Medicine'},
#  {'name': 'Literature', 'href': '/wiki/List_of_Nobel_laureates_in_Literature'},
#  {'name': 'Peace', 'href': '/wiki/List_of_Nobel_Peace_Prize_laureates'},
#  {'name': 'Economics', 'href': '/wiki/List_of_Nobel_laureates_in_Economics'}]


def get_nobel_winners(table: bs4.element.Tag) -> List[Dict]:
    column_titles = get_column_titles(table)
    categories = column_titles[1:]  # column titles after year
    winners = []
    for row in table.select('tr')[1:-1]:  # without the first and last rows in the response.content
        year = int(row.select_one('td').text)  # only year
        for i, td in enumerate(row.select('td')[1:]):  # without year
            for winner in td.select('a'):
                href = winner.attrs['href']
                if not href.startswith('#endnote'):
                    winners.append(
                        {
                            'year': year,
                            'category': categories[i]['name'],
                            'name': winner.text,
                            'link': winner.attrs['href'],
                        }
                    )
    return winners


winners = get_nobel_winners(table)
# the first three winners
winners[:3]
# [{'year': 1901,
#   'category': 'Physics',
#   'name': 'Wilhelm Röntgen',
#   'link': '/wiki/Wilhelm_R%C3%B6ntgen'},
#  {'year': 1901,
#   'category': 'Chemistry',
#   'name': "Jacobus Henricus van 't Hoff",
#   'link': '/wiki/Jacobus_Henricus_van_%27t_Hoff'},
#  {'year': 1901,
#   'category': 'Physiologyor Medicine',
#   'name': 'Emil von Behring',
#   'link': '/wiki/Emil_von_Behring'}]
# the last three winners
winners[-3:]
# [{'year': 2023,
#   'category': 'Literature',
#   'name': 'Jon Fosse',
#   'link': '/wiki/Jon_Fosse'},
#  {'year': 2023,
#   'category': 'Peace',
#   'name': 'Narges Mohammadi',
#   'link': '/wiki/Narges_Mohammadi'},
#  {'year': 2023,
#   'category': 'Economics',
#   'name': 'Claudia Goldin',
#   'link': '/wiki/Claudia_Goldin'}]
