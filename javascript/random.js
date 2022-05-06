var words  = [];
var input  = document.getElementById('input');
var submitButton = document.getElementById('submit');
var output = document.getElementById('output');
var randomButton = document.getElementById('random')

submitButton.addEventListener('click', function () {
  words.push(input.value);
  input.value = '';
}, false);


randomButton.addEventListener('click', function () {
  output.innerHTML = getRandomWord();
})

function getRandomWord () {
  return words[Math.floor(Math.random()*words.length)]
}