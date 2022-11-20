import requests
# from flask import render_template
from bs4 import BeautifulSoup
from flask import Flask, render_template

######################
### RECIPE SCRAPER ###
######################

recipe_list = []
f = open("recipes.txt", "w")

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

ingedients_for_recipes = ['vegetable oil;boneless, skin-on turkey breast;kosher salt, divided;freshly ground black pepper, divided;ground cayenne pepper;Dijon mustard;prepared pesto sauce;dried cranberries, or to taste;ham, thinly sliced;provolone cheese',
'vegetable oil;uncooked long-grain rice;garlic salt;ground cumin;chopped onion;chicken broth;tomato sauce',
'roma (plum) tomatoes, diced;red onion, minced;chopped fresh cilantro;jalapeño pepper, seeded and minced;lime, juiced;garlic, minced;garlic powder;ground cumin, or to taste;salt and ground black pepper to taste',
'butter, softened;white sugar;eggs;vanilla extract;all-purpose flour;baking powder;salt',
'confectioners\' sugar;unsweetened cocoa powder;vanilla extract;egg yolks;white sugar;unsweetened cocoa powder;vanilla extract;salt;egg whites;white sugar;confectioners\' sugar for dusting',
'ground beef;onion, chopped;garlic, minced;green bell pepper, diced;diced tomatoes;tomato sauce;tomato paste;dried oregano;dried basil;salt;ground black pepper',
'vegetable oil;diced onion;garlic, minced;chopped green chiles (such as Ortega®);Mexican-style hot tomato sauce (such as El Pato®);shredded rotisserie chicken;shredded Mexican cheese blend;Neufchâtel cheese;salt and ground black pepper to taste;corn tortillas;avocado oil cooking spray',
'carrots, peeled;orange juice;water;ground coriander;salt;freshly ground black pepper;butter, melted, divided;panko bread crumbs;orange zest;garlic, minced;chopped fresh parsley for garnish',
'skinless, boneless chicken breast halves;salt;cooking oil;chopped onion;minced garlic;minced fresh ginger root;curry powder;ground cumin;ground turmeric;ground coriander;cayenne pepper;water;crushed tomatoes;plain yogurt;chopped fresh cilantro;salt;water;garam masala;chopped fresh cilantro;fresh lemon juice']


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


    #    long = render_template('BigBoyJavaScript.html', title = title, image = image)

######################
### RECIPE WEBSITE ###
######################

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('BigManHTML.html', url_list = list_of_webPages, name_list = webPages_names, ingredient_list = ingedients_for_recipes)

if __name__ == '__main__':
    app.run(debug=True)