/** комментарий ..
.. многострочный **/
// комментарий однострочный

var str = "A string"; // объявление переменной
var alsoString = 'A string'; // то же

console.log(str); // вывод в консоль: A string
console.log(typeof(str)); //вывод типа переменной result: string
var nmb = 12;
console.log(typeof(nmb)); //вывод типа переменной result: number

var num1 = 1;
var num2 = 2.0;
console.log(nun1 + num2); // result: 3
console.log(nun1 * num2); // result: 2
console.log(num1 == num2); // сравнение result: false
console.log(num1 == num1); // сравнение result: true
console.log(num1 != num2); // сравнение (не равно) result: true
Number('23'); // приведение тип:строки в тип:число result: 23
String(23);  // приведение тип:число в тип:строка result: "23"

// Objects:
var o {};  // объявляем объект
typeof(o); // result: "object"
o['key'] = 12; // задаем ключ и значение объекта result:12
o; // result: {key:12}
o.key; // result: 12
o['key']; // result: 12
var x = 'key';  // задаем ключ через переменную x
o[x]; // result:12

var o = {r:54, s:12, h:'asdf'}; // объявляем объект
o; // result:{r:54, s:12, h:'asdf'}
o['key'] = 'ABC';  // добавляем ключ - значение
o; // result: {r: 54, s: 12, h: "asdf", key: "ABC"}
Object.keys(o); // достаем ключи объекта методом Object.keys  result: (4) ["r", "s", "h", "key"]

// Списки - list (в JavaScript это тоже тип "объекты")
var listEt = [1, 2, 3]; // объявляем список
listEt // result: (3) [1, 2, 3]
typeof(listEt); // result: "object"
listEt.push(4); // добавляем значение в список методом push
listEt; // result: (4) [1, 2, 3, 4]
listEt.length; // кол-во значений в списке list // result(3)
