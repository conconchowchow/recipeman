const fs = require("fs");

// if using ES6 Imports uncomment line below
// import {readFileSync, promises as fsPromises} from 'fs';
const {readFileSync, promises: fsPromises} = require('fs');

// read file SYNCHRONOUSLY
function syncReadFile(filename) {
  const contents = readFileSync(filename, 'utf-8');

  const arr = contents.split(/\r?\n/);

  console.log(arr); // -> ['One', 'Two', 'Three', 'Four']

  return arr;
}

// syncReadFile('./example.txt');

// --------------------------------------------------------------

// read file ASYNCHRONOUSLY
async function asyncReadFile(filename) {
  try {
    const contents = await fsPromises.readFile(filename, 'utf-8');

    const arr = contents.split(/\r?\n/);

    console.log(arr); // -> ['One', 'Two', 'Three', 'Four']

    return arr;
  } catch (err) {
    console.log(err);
  }
}

// const recipe_list = asyncReadFile('recipes.txt');
const recipe_list = asyncReadFile('./recipes.txt');

function update() {
    // update the scene
    var text = document.getElementById("ingredients-box").value;
    var ingredients = text.split(",");
    var ingredientsList = document.getElementById("ingredients-list");
    // ingredientsList.innerHTML = "";
    // for (var i = 0; i < ingredients.length; i++) {
    //     var ingredient = ingredients[i];
    //     var li = document.createElement("li");
    //     li.innerHTML = ingredient;
    //     ingredientsList.appendChild(li);
    // }
    
    // fs.readFile("recipes.txt", (err, data) => {
    //     if (err) throw err;
      
    //     console.log(data.toString());
    //   });

    alert(ingredients + "\n\n" + ingredientsList);

    

}