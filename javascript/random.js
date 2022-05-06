var words  = [];
var input  = document.getElementById('input');
var submitButton = document.getElementById('submit');
var output = document.getElementById('output');

submitButton.addEventListener('click', function () {
  words.push(input.value);
  input.value = '';
}, false);

submitButton.addEventListener('click', function () {
  output.innerHTML = getRandomWord();
})

function getRandomWord () {
  return words[Math.floor(Math.random()*words.length)]
}
