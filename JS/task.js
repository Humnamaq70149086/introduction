function updateFruits(fruitArray) {

    fruitArray.push('Mango', 'Kiwi', 'Strawberry');
  
    fruitArray.pop();

    return fruitArray;
  }
  
  const myFruits = ['Apple', 'Dragon fruit', 'Orange'];
  const updatedFruits = updateFruits(myFruits);
  console.log(updatedFruits); 
  