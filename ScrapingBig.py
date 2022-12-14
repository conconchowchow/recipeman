import requests
# from flask import render_template
from bs4 import BeautifulSoup
from flask import Flask, request, render_template

######################
### RECIPE SCRAPER ###
######################

recipe_list = []

# idk what this does it was just recommended on the tutorial I used
# Tutorial: https://towardsdatascience.com/web-scraping-with-beautiful-soup-a-use-case-fc1c60c8005d
# session = requests.Session()
list_of_webPages = [ 'https://www.allrecipes.com/recipe/8318099/holiday-roast-turkey-cordon-bleu/',
                    "https://www.allrecipes.com/recipe/27072/mexican-rice-ii/", "https://www.allrecipes.com/recipe/203800/pico-de-gallo/",
                    "https://www.allrecipes.com/recipe/10402/the-best-rolled-sugar-cookies/", "https://www.allrecipes.com/recipe/17345/buche-de-noel/",
                    "https://www.allrecipes.com/recipe/158140/spaghetti-sauce-with-ground-beef/", "https://www.allrecipes.com/recipe/279015/air-fryer-chicken-taquitos/",
                    "https://www.allrecipes.com/recipe/8490854/roasted-carrots-with-garlic-bread-crumbs/", "https://www.allrecipes.com/recipe/212721/indian-chicken-curry-murgh-kari/"]

webPages_names = [ 'Holiday Roast Turkey Cordon Bleu', 'Mexican Rice', 'Pico de Gallo', 'The Best Rolled Sugar Cookies',
                  'Buche de Noel', 'Spaghetti Sauce with Ground Beef', 'Air Fryer Chicken Taquitos', 'Roasted Carrots with Garlic Bread Crumbs', 'Indian Chicken Curry Murgh Kari']


print("Scraping website...",end="")

for i in range(len(list_of_webPages)):
    URL = list_of_webPages[i]
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    header_container = soup.find_all(['h1'], class_=lambda x: x != 'hidden')

    image = soup.find_all({'class': 'primary-image__image mntl-primary-image--blurry loaded'})

    ingredient_container = soup.find_all("div", {'class':"comp mntl-structured-ingredients"})
    ul = soup.find('ul', class_="mntl-structured-ingredients__list")
    Others = ul.find_all("span")

    recipe_item = [list_of_webPages[i]]

    for lines in header_container:
        if lines.name == 'h1':
            province = lines.text
            recipe_item.append(province[1:])
            # print('Recipe: ', province, "\n")

    for lines in range(2,len(Others), 3):
        recipe_item.append(Others[lines].text)
        # print(lines.text)

    # print(recipe_item) ### prints each item going into recipe_item
    recipe_list.append(recipe_item)

print("Done!")

######################
### RECIPE  WRITER ###
######################

print("Writing to file...",end="")

with open("recipes.txt", "w") as txt_file:
    for line in recipe_list:
        txt_file.write(";".join(line) + "\n")

print("Done!")

# print(ingredientDict)
    #    long = render_template('BigBoyJavaScript.html', title = title, image = image)

print("Opening file...", end="")

file1 = open('recipes.txt', 'r')
Lines = file1.readlines()
ingredientDict = {}
for i in range(len(Lines)):
    ingredients = Lines[i].strip('\n').split(';')[2:]
    #print(webPages_names[i])
    ingredientDict[webPages_names[i]] = ingredients

print("Done!")

######################
### RECIPE WEBSITE ###
######################

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('BigManHTML.html', url_list = list_of_webPages, name_list = webPages_names, ingredient_list = ingredientDict, recipe_1 = 0, recipe_1_num = 1, recipe_2 = 1, recipe_2_num = 0)


def my_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    recipe_ingredient_count = []
    inputs = request.form['variable'].split(', ')
    print(inputs)
    for recipe_count in range(len(ingredientDict)):
        count = 0

        for item in range(len(inputs)):
            if inputs[item] in ingredientDict[webPages_names[recipe_count]]:
                count+=1

        recipe_ingredient_count.append(count)
    print(recipe_ingredient_count)

    max_value = max(recipe_ingredient_count)


    for i in range(len(recipe_ingredient_count)):
        if recipe_ingredient_count[i] == max_value:
            # return webPages_names[i]
            return render_template('BigManHTML.html', url_list = list_of_webPages, name_list = webPages_names, ingredient_list = ingredientDict, recipe_1 = i, recipe_1_num = max_value, recipe_2 = 1, recipe_2_num = 0)
    return render_template('BigManHTML.html', url_list = list_of_webPages, name_list = webPages_names, ingredient_list = ingredientDict, recipe_1 = 0, recipe_2 = 1, recipe_2_num = 0)


if __name__ == '__main__':
    app.run(debug=True)
