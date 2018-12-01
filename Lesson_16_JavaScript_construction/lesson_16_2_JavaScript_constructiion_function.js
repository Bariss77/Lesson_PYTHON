x = 1;
var x === 1 ? 'true' : 'false'; //  если переменная x равна 1, то 'true',  иначе 'false' // result: true
var x === 23 ? 'true' : 'false'; // result: false

// пробелы ре имеют значения
var flag = true;
if (!flag)  // если .......
{console.log('if');}  //  то .....
else if (flag && 1 < 2)  // если .......
{ // \\ - or, && - and }
console.log('elseif');}  //  то .....
else {}        // иначе .......

var ternary = 40 > 13 ? 'yes' : 'no'; // если ....,(?) то .....(:), иначе ......
console.log(ternary);  // result: yes

switch (value) {
  case '321':            // если value == '321'
    console.log('1');    // то выводим '1'
    break;
  case '123':            // если value == '123'
    console.log('2');    // то выводим '2'
    break;
  default:               // иначе
    console.log('other'); // выводим 'other'
    break;
}

for (var i = 0; i < 10; i ++) { // начальное состояние:var i = 0, конечное состояние: i < 10,
  // шаг итерации: i++  увеличивается на 1
    console.log(i);}
// result:
//0
//1
//2
//3
//4
//5
//6
//7
//8
//9

var iterable = [1, 2, 3, 'df', 'fg'] // перебираем список
for (var k in iterable) {
  console.log(iterable[k])
}
// result:
//0
//1
//2
//df
//fg
var iterable2 = ['a', 'b', 3, 4, 5]
for (var g in iterable2) {
  console.log(g, iterable2[g]);
}
// result:
//0 a
//1 b
//2 3
//3 4
//4 5

var s = 1;
do {
  console.log(s++); // выполняем s++
} while (s < 4);    //  пока не выполнится условие while
}
//result:
//1
//2
//3
//4
---------------------------------------------------
// Function
function someFunction(a, b) { //  объявляем функцию
  return a + b
}
// вызываем функцию
someFunction(1, 2);  // result:3
someFunction(1); // result: NaN (второй аргумент принимаентся, как undefind(неопреджелен))

jlk = function(s, d) { // объявляем функцию через переменную
  return s * d
}
// вызываем функцию
jlk(4, 5);
//result: 20
