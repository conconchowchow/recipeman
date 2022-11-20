import requests
# from flask import render_template
from bs4 import BeautifulSoup

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('BigManHTML.html')
if __name__ == '__main__':
    app.run(debug=True)

# idk what this does it was just recommended on the tutorial I used
# Tutorial: https://towardsdatascience.com/web-scraping-with-beautiful-soup-a-use-case-fc1c60c8005d
# session = requests.Session()
list_of_webPages = ["https://www.allrecipes.com/recipe/8318099/holiday-roast-turkey-cordon-bleu/", 'https://www.allrecipes.com/recipe/8318099/holiday-roast-turkey-cordon-bleu/',
                    "https://www.allrecipes.com/recipe/27072/mexican-rice-ii/", "https://www.allrecipes.com/recipe/203800/pico-de-gallo/",
                    "https://www.allrecipes.com/recipe/10402/the-best-rolled-sugar-cookies/", "https://www.allrecipes.com/recipe/17345/buche-de-noel/",
                    "https://www.allrecipes.com/recipe/158140/spaghetti-sauce-with-ground-beef/", "https://www.allrecipes.com/recipe/279015/air-fryer-chicken-taquitos/",
                    "https://www.allrecipes.com/recipe/8490854/roasted-carrots-with-garlic-bread-crumbs/", "https://www.allrecipes.com/recipe/212721/indian-chicken-curry-murgh-kari/"]

for i in range(len(list_of_webPages)):
    URL = list_of_webPages[i]
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    header_container = soup.find_all(['h1'], class_=lambda x: x != 'hidden')

    ingredient_container = soup.find_all("div", {'class':"comp mntl-structured-ingredients"})
    ul = soup.find('ul', class_="mntl-structured-ingredients__list")
    Others = ul.find_all("span")

    for lines in header_container:
        if lines.name == 'h1':
            province = lines.text
            print('Recipe: ', province, "\n")
    """
    for lines in ingredient_container:
        if lines.name == 'div':
            ingredients = lines.text
            print(ingredients, "\n")
    """
    """
    new_ingredient = soup.find_all('div', {'class':"mntl-structured-ingredients"})
    for lines in new_ingredient:
        if lines.name == 'div':
            stuff = lines.text
            print(lines)
    """

    for lines in Others:
        print(lines.text)





    #    print(soup.select_one('ul.mntl-structured-ingredients__list span: last - child'))
    #    data = Others.find_all('span', data-ingredient-name="true")
    #    print(date_published)
    #    print(soup.select_one('ul.mntl-structured-ingredients__list span:last-of-type').text)

    # I made this function to try and connect our html file (website/frontend) and
    #our backend (python file). I do not know how it works rn.
    #def make_page():
    #    long = render_template('BigBoyJavaScript.html', title = title, image = image)
