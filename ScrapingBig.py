import requests
# from flask import render_template
from bs4 import BeautifulSoup

# Not sure what this does
# @app.route('/', methods = ['get'])

# idk what this does it was just recommended on the tutorial I used
# Tutorial: https://towardsdatascience.com/web-scraping-with-beautiful-soup-a-use-case-fc1c60c8005d
# session = requests.Session()

URL = "https://www.allrecipes.com/recipe/19547/grandmas-corn-bread-dressing/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

container = soup.find_all(['h1'], class_=lambda x: x != 'hidden')

for lines in container:
    if lines.name == 'h1':
        province = lines.text
        print('Recipe: ', province, "\n")


# I made this function to try and connect our html file (website/frontend) and
#our backend (python file). I do not know how it works rn.
#def make_page():
#    long = render_template('BigBoyJavaScript.html', title = title, image = image)
