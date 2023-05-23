// Function to fetch and display random recipe details
function getRandomRecipes() {
    const apiKey = '1';
    const numRecipes = 3; // Number of random recipes to display
  
    fetch(`https://www.themealdb.com/api/json/v1/${apiKey}/random.php`)
      .then(response => response.json())
      .then(data => {
        // Access the retrieved random recipe details
        const recipes = data.meals;
  
        // Display the random recipe details on the page
        const recipeContainer = document.getElementById('recipe-container');
  
        let recipeHtml = '';
        recipes.forEach(recipe => {
          recipeHtml += `
            <div class="recipe-card">
              <img src="${recipe.strMealThumb}" alt="${recipe.strMeal}" class="recipe-image">
              <h3 class="recipe-title">${recipe.strMeal}</h3>
              <p class="recipe-category">Category: ${recipe.strCategory}</p>
              <p class="recipe-instructions">${recipe.strInstructions}</p>
            </div>
          `;
        });
  
        recipeContainer.innerHTML = recipeHtml;
      })
      .catch(error => {
        // Handle any errors that occur during the API request
        console.log(error);
      });
  }
  
  // Call the function to fetch and display random recipe details
  getRandomRecipes();

  
// Add bullet points after each full stop in recipe instructions
const recipeInstructions = document.getElementsByClassName("recipe-instructions");

for (let i = 0; i < recipeInstructions.length; i++) {
  const instruction = recipeInstructions[i];
  const text = instruction.textContent;
  const newText = text.replace(/\./g, ". •");
  instruction.innerHTML = newText;
}