import requests
# from flask import render_template
from bs4 import BeautifulSoup

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('BigManHTML.html')
if __name__ == '__main__':
    app.run()

# Not sure what this does
# @app.route('/', methods = ['get'])

# idk what this does it was just recommended on the tutorial I used
# Tutorial: https://towardsdatascience.com/web-scraping-with-beautiful-soup-a-use-case-fc1c60c8005d
# session = requests.Session()

URL = "https://www.allrecipes.com/recipe/239960/fresh-cranberry-sauce/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

header_container = soup.find_all(['h1'], class_=lambda x: x != 'hidden')

ingredient_container = soup.find_all("div", {'class':"comp mntl-structured-ingredients"})

for lines in header_container:
    if lines.name == 'h1':
        province = lines.text
        print('Recipe: ', province, "\n")

for lines in ingredient_container:
    if lines.name == 'div':
        ingredients = lines.text
        print(ingredients, "\n")

"""
for lines in ingredient_container:
    if lines.name == 'div':
        print('')
"""
# I made this function to try and connect our html file (website/frontend) and
#our backend (python file). I do not know how it works rn.
#def make_page():
#    long = render_template('BigBoyJavaScript.html', title = title, image = image)
