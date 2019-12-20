# Python

Este proyecto es un primer acercamiento al lenguaje de programación `Python`

Python es un lenguaje diseñado para ser fácil de utilizar

## Operadores

Existen 4 tipos de operadores, siendo los operadores aritméticos los vistos en esta clase:

- Operadores lógicos
- Operadores relacionales
- Operadores de asignaciones
- Operadores aritméticos

## Operadores matemáticos

En **programación** estos operadores son muy similares a nuestras clases básicas de matemáticas.

- `+` Suma, Concatena
- `-`
- `*`
- `/`
- `//`: Es división de entero, básicamente tiramos la parte decimal
- `%`: Módulo Es el residuo de la división, lo que te sobra.
- `**`: Exponente

```python
print(22//4)#division mostrando numero entero
print(10%4)#modulo, residuo de la division
print(10**4)#numero elevado a la potencia
print(type(5))  #muestra el tipo de valor, en este caso entero
print(type(5.5))  #muestra el tipo de valor, en este caso decimal
print(type("a"))  #muestra el tipo de valor, en este caso string
print("a"+"b")#se puede hacer una concatenacion con dos strings
print("a"*3)#se asigna que se repita el string 
print(5 == 3)#se comprueba si dos valores son iguales o no. Bota true or false
print(5 != 3)#se comprueba si dos valores son iguales o no. Bota true or false
print(8>5>3)#se compara si son mayor o menor. Bota true or false
```

Los operadores son **contextuales**, dependen del tipo de valor. Un valor es la representación de una entidad que puede ser manipulada por un programa.

Podemos conocer el tipo del valor con type() y nos devolverá algo similar a `, , `. Dependiendo del tipo los operadores van a funcionar de manera diferente.

![pemdas.PNG](https://static.platzi.com/media/user_upload/pemdas-eb6b0f3f-24fc-4b2f-a80a-3383331a9abd.jpg)

**Operadores lógicos:** Sirven para realizar comparaciones, devuelven un valor verdadero o falso.

| Operador | Descripción       | Ejemplo        | Resultado  |
| -------- | ----------------- | -------------- | ---------- |
| and      | ¿se cumple a y b? | r=TrueandFalse | r es False |
| or       | ¿se cumple a o b? | r=True o False | r es True  |
| not      | No a              | r=notTrue      | r es False |

**Operadores relacionales:** comparan dos expresiones y devuelven un valor verdadero o falso.

| Operador | Descripción                | Ejemplo | Resultado  |
| -------- | -------------------------- | ------- | ---------- |
| ==       | ¿Son iguales a y b?        | r=5==3  | r es False |
| !=       | ¿Son distintos a y b?      | r=5!=3  | r es True  |
| <        | ¿Es a menor que b?         | r=5<3   | r es False |
| >        | ¿Es a mayor que b?         | r=5>3 3 | r es True  |
| <=       | ¿Es a menor o igual que b? | r=5<=5  | r es True  |
| >=       | ¿Es a mayor o igual que b? | r=5>=3  | r es True  |

```python
print("Na"*8+" ")*2+"Batman Batman" # NaNaNaNaNaNaNaNa NaNaNaNaNaNaNaNa Batman Batman
```



## Operadores lógicos



## Variables y expresiones

Una **variable** es simplemente el contenedor de un valor. Es una forma de decirle a la  computadora de que nos guarde un valor para luego usarlo.

Python es un lenguaje **dinámico**, este concepto de privado y público se genera por convenciones del lenguaje. En programación el signo `=` significa asignación.

Si una variable esta en mayúscula, usualmente se refiere a una constante, no debería reasignarse. Es una convención.

**Reglas de Variables**:

- Pueden contener números y letras
- No deben comenzar con número
- Múltiples palabras se unen con _
- No se pueden utilizar palabras reservadas

Expresiones son instrucciones para el interprete para evaluar la  expresión. Los enunciados tienen efectos dentro del programa, como `print` que genera un **output**.

**PEMDAS** = Paréntesis, Exponente, Multiplicación, Adicción, Substracción

## Palabras reservadas

| and   | del     | for      | is    | raise  | assert |
| ----- | ------- | -------- | ----- | ------ | ------ |
| if    | else    | elif     | from  | lambda | return |
| break | global  | not      | try   | class  | except |
| or    | while   | continue | exec  | import | yield  |
| def   | finally | in       | print |        |        |

## Sobre las variables en python

- Pueden reasignarse cuantas veces se necesite
- No pueden comenzar con numeros
- No se pueden utilizar las palabras reservadas de Python como variable.
- Se utiliza snake_case (guión bajo) para dividir las palabras de las variables multipalabra

**Palabras reservadas del lenguaje:**

| and   | del        | for           | is       | raise      | assert |
| if        | else      | elif           | from  | lambda | return |
| break | global  | not          | try     | class      | except |
| or       | while   | continue | exec  | import   | yield  |
| def    | finally   | in             | print |             

## Convenciones en el nombre de las variables

No existen las variables privadas, y la reasignación es muy común en python, por lo que algo que nos puede proteger de no cometer errores graves en el uso de las variables es entender las convenciones de nombrado de variables que utilizan los programadores (ya que se puede nombrar una variable de diversas formas, pero eso no significa que se deba).

- **variables_regulares**: `snake_case`
- **CONSTANTES**: Una variable toda en mayuscula no debería de modificarse 
- **_privada**: `Single Leading Underscore: ` **`_var`** : una variable que empieza con guion bajo ( “_” ) se deberá tratar como _privada y no se deberá de acceder fuera de la clase
- **__importante**: `Double Leading Underscore:` **`__`** variables que empiezan con doble guion bajo ( “__”) son`Variables importantes`, si se llegara a modificar es provable que se pierda estabilidad del programa, así que mejor no tocarla mucho
- **var_**: `Single Trailing Underscore:` **`var_`**: A veces, el nombre más apropiado para una variable lo toma una palabra clave. Por lo tanto, los nombres como class o def no se pueden usar como nombres de variables en Python. En este caso, puede agregar un solo guión bajo ("_") para romper el conflicto de nombres:
- **\_\_main\_\_**: `Double Leading and Trailing Underscore: __var__`:  Las variables rodeadas por un prefijo de subrayado doble y un postfix quedan reservadas por el intérprete de Python.

![pemdas.PNG](https://static.platzi.com/media/user_upload/pemdas-eb6b0f3f-24fc-4b2f-a80a-3383331a9abd.jpg)

## Funciones

En el contexto de la programación las funciones son una agrupación de enunciados que tienen un nombre.

*  **`!important`**: Una de las cosas más importantes que hace un programador es poner nombres porque se pasa más tiempo leyendo código que escribiendo.
* El nombre de la función deberá ser  descriptivo
* Puede tener parámetros

* Puede regresar un valor después  que se generó el cómputo (Lo que devuelve, después de realizar el computo de nuestra función)
* Se puede usar funciones con parámetros opcionales, que son  inicializados con datos por defecto

Python tiene una librería de funciones estándar muy completa (**built in functions**), la cuál se puede encontras a continuación:

Python tiene **Battery included**, lo que significa que tiene una librería  estándar con **muchas funciones** que podemos utilizar sin tener que instalar nada más conocidas como built-in functions.

A continuación la lista actualizada hasta hoy (pueden acceder a la documentación al hacer click):

| Built-in Functions                                           |                                                              |                                                              |                                                              |                                                              |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |                                                              |                                                              |                                                              |
| [`abs()`](https://docs.python.org/3/library/functions.html#abs) | [`delattr()`](https://docs.python.org/3/library/functions.html#delattr) | [`hash()`](https://docs.python.org/3/library/functions.html#hash) | [`memoryview()`](https://docs.python.org/3/library/functions.html#func-memoryview) | [`set()`](https://docs.python.org/3/library/functions.html#func-set) |
| [`all()`](https://docs.python.org/3/library/functions.html#all) | [`dict()`](https://docs.python.org/3/library/functions.html#func-dict) | [`help()`](https://docs.python.org/3/library/functions.html#help) | [`min()`](https://docs.python.org/3/library/functions.html#min) | [`setattr()`](https://docs.python.org/3/library/functions.html#setattr) |
| [`any()`](https://docs.python.org/3/library/functions.html#any) | [`dir()`](https://docs.python.org/3/library/functions.html#dir) | [`hex()`](https://docs.python.org/3/library/functions.html#hex) | [`next()`](https://docs.python.org/3/library/functions.html#next) | [`slice()`](https://docs.python.org/3/library/functions.html#slice) |
| [`ascii()`](https://docs.python.org/3/library/functions.html#ascii) | [`divmod()`](https://docs.python.org/3/library/functions.html#divmod) | [`id()`](https://docs.python.org/3/library/functions.html#id) | [`object()`](https://docs.python.org/3/library/functions.html#object) | [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) |
| [`bin()`](https://docs.python.org/3/library/functions.html#bin) | [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate) | [`input()`](https://docs.python.org/3/library/functions.html#input) | [`oct()`](https://docs.python.org/3/library/functions.html#oct) | [`staticmethod()`](https://docs.python.org/3/library/functions.html#staticmethod) |
| [`bool()`](https://docs.python.org/3/library/functions.html#bool) | [`eval()`](https://docs.python.org/3/library/functions.html#eval) | [`int()`](https://docs.python.org/3/library/functions.html#int) | [`open()`](https://docs.python.org/3/library/functions.html#open) | [`str()`](https://docs.python.org/3/library/functions.html#func-str) |
| [`breakpoint()`](https://docs.python.org/3/library/functions.html#breakpoint) | [`exec()`](https://docs.python.org/3/library/functions.html#exec) | [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance) | [`ord()`](https://docs.python.org/3/library/functions.html#ord) | [`sum()`](https://docs.python.org/3/library/functions.html#sum) |
| [`bytearray()`](https://docs.python.org/3/library/functions.html#func-bytearray) | [`filter()`](https://docs.python.org/3/library/functions.html#filter) | [`issubclass()`](https://docs.python.org/3/library/functions.html#issubclass) | [`pow()`](https://docs.python.org/3/library/functions.html#pow) | [`super()`](https://docs.python.org/3/library/functions.html#super) |
| [`bytes()`](https://docs.python.org/3/library/functions.html#func-bytes) | [`float()`](https://docs.python.org/3/library/functions.html#float) | [`iter()`](https://docs.python.org/3/library/functions.html#iter) | [`print()`](https://docs.python.org/3/library/functions.html#print) | [`tuple()`](https://docs.python.org/3/library/functions.html#func-tuple) |
| [`callable()`](https://docs.python.org/3/library/functions.html#callable) | [`format()`](https://docs.python.org/3/library/functions.html#format) | [`len()`](https://docs.python.org/3/library/functions.html#len) | [`property()`](https://docs.python.org/3/library/functions.html#property) | [`type()`](https://docs.python.org/3/library/functions.html#type) |
| [`chr()`](https://docs.python.org/3/library/functions.html#chr) | [`frozenset()`](https://docs.python.org/3/library/functions.html#func-frozenset) | [`list()`](https://docs.python.org/3/library/functions.html#func-list) | [`range()`](https://docs.python.org/3/library/functions.html#func-range) | [`vars()`](https://docs.python.org/3/library/functions.html#vars) |
| [`classmethod()`](https://docs.python.org/3/library/functions.html#classmethod) | [`getattr()`](https://docs.python.org/3/library/functions.html#getattr) | [`locals()`](https://docs.python.org/3/library/functions.html#locals) | [`repr()`](https://docs.python.org/3/library/functions.html#repr) | [`zip()`](https://docs.python.org/3/library/functions.html#zip) |
| [`compile()`](https://docs.python.org/3/library/functions.html#compile) | [`globals()`](https://docs.python.org/3/library/functions.html#globals) | [`map()`](https://docs.python.org/3/library/functions.html#map) | [`reversed()`](https://docs.python.org/3/library/functions.html#reversed) | [`__import__()`](https://docs.python.org/3/library/functions.html#__import__) |
| [`complex()`](https://docs.python.org/3/library/functions.html#complex) | [`hasattr()`](https://docs.python.org/3/library/functions.html#hasattr) | [`max()`](https://docs.python.org/3/library/functions.html#max) | [`round()`](https://docs.python.org/3/library/functions.html#round) |                                                              |

## Declaración de funciones

Para declarar una función se sigue la siguiente estructura:

```python
def nombre_de_funcion(argumento1, argumento2):
  return argumento1+argumento2
```

![img](http://swcarpentry.github.io/python-novice-inflammation/fig/python-function.svg)

Donde:

* La palabra reservada **`def`** se utiliza para declarar que se va a **definir** una **función** y se termina con un espacio `" "`
* El **`nombre_de_funcion`** será con el que nos referamos a la **función** a la hora de llamarla
* Los **`argumentos`** son variables que podemos utilizar solamente dentro de la función
* Los **`:`** (dos puntos): se refieren al final del encabezado
* En el cuerpo de la función es importante utilizar un tabulador por línea **`"  "`**
* El **`return`** regresará el valor de la función, mismo que podremos utilizar como argumento de otras funciones.

# Truthy and falsy values

Los valores verdadero y falso (**`true`**, **`false`**) funcionan muy similar que en javascript, se puede probar cualquier valor de cualquier tipo de objeto e interpretar como **booleano** (true o false), para usarlo en una condición **if o while** o como operador de operaciones booleanas.

Los siguientes valores se consideran falsos (**`false`**)):

+ None = **`false`**

+ False = **`false`**

+ Cero o números equivalentes a cero, por ejemplo: (0, 0L, 0.0, 0j) = **`false`**

+ cualquier secuencia vacía, por ejemplo: '', (), [] = **`false`**

+ cualquier mapeo vacío, por ejemplo: {} = **`false`**

+ instancias de clases definidas por el usuario, si la clase define un método __nonzero __ () o __len __ (), cuando ese método devuelve el entero cero o valor bool o False = **`false`**

Todos los demás valores se consideran verdaderos, por lo que los objetos de muchos tipos siempre son verdaderos. = **`true`**

# Buenas prácticas

Dejar 2 espacios entre declaraciones de funciones o bloques de código

Dejar 1 espacio entre secciones (declaraciones, ejecuciones)