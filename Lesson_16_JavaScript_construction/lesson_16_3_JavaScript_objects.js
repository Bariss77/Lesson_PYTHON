var user = {
  name: 'Владимир',    // объект - Владимир
  // метод объекта:
  sayHi: function() {
    console.log(this.name);  // вызываем аргумент того объекта в контексте котором вызван метод
  }
};

user.sayHi();  // result: Владимир
----------------------------------------------------------
var boy = 'Борис';

var user = {
  name: boy,    // объект - переменная boy
  // метод объекта:
  sayHi: function() {
    console.log(this.name);  // вызываем аргумент того объекта в контексте котором вызван метод
  }
};

user.sayHi();  // result: Борис

--------------------------------------------------------------------

var MyClass = function (title) { // Создаем конструктор (в python  как __init__)
  this.title = title;            // this обращается к объекту в контексте которого вызвана функция
  var privateValue = 'secret';   //  Задаем локальнаю переменную

  this.tellTitle = function (){   // задаем неявно thiss??
    console.log(this.title);     // выводим аргумент функции function()
    console.log(this);           // выводим текущий объект
  };

  function privateFunction() {
    console.log (privateValue);    // выводим на экран secret (переменная privateValue)
    console.log ('This is:', this) // this не задан
  }

  privateFunction();

  this.runPrivate = function() {  // с помощью this мщжем вызывать внутрении функции и переменные
    privateFunction();
  };

  this.runPrivateWithCall = function () {
    privateFunction.call(this);   // метод задания правильного this ????
    privateFunction.apply(this, []); // передаем this и массив аргуменгтов ??
  };
};
// создаем объект в переменную o:
var o = new MyClass('Some title') // new - инициализация MyClass (создаем новый экземпляр)
//result: secret   - результат выполнения функции privateFunction(), строка 11
//result: This is: - результат выполнения функции privateFunction(), строка 12
