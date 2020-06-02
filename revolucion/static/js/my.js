var date = new Date()
const monthes = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
var copyright = document.getElementById("datum");
console.log(copyright);
var datum = date.getDate().toString() + " " + monthes[date.getMonth()] + " " + date.getFullYear().toString();
console.log(datum);
copyright.innerText = datum;