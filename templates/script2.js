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

    alert(ingredients + "\n\n" + ingredientsList);


}