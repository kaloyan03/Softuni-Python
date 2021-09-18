  function calculatesFruitPrice(typeOfFruit, weightInGrams, pricePerKilogram) {
    let weightInKilograms = weightInGrams / 1000;
    let fruitPrice = weightInKilograms * pricePerKilogram;

    console.log(`I need $${fruitPrice.toFixed(2)} to buy ${weightInKilograms.toFixed(2)} kilograms ${typeOfFruit}.`);

}
