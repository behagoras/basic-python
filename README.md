Python

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

| Command |      | Action                                            |
| :-----: | :--- | ------------------------------------------------- |
|   dir   |      | Muestra todos las funciones accesibles del objeto |
|  Help   |      | imprime la documentación de la función            |
|  Slice  |      |                                                   |
|         |      |                                                   |

**Docstrings**:  Para generar una documentación utilizar triples dobles comillas `"""` :

```python
def my_function():
    """ documentación de la función """ 
    pass
```

**slices**

Los slices en Python nos permiten manejar secuencias de una manera poderosa.

Slices en español significa ““rebanada””, si tenemos una secuencia de elementos y queremos una rebanada tenemos una sintaxis para definir qué pedazos queremos de esa secuencia

secuencia[comienzo:final:pasos]

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

## Strings (cadenas de caracteres)

Los **strings** o **cadenas de textos** tienen un comportamiento distinto a otros tipos como los booleanos,  enteros, floats. Las cadenas son secuencias de caracteres, todas se  pueden acceder a través de un índice.

Podemos saber la longitud de un *string*, cuántos caracteres se encuentran en esa secuencia. Lo podemos saber con la ***built-in function\*** global llamada `len`.

Algo importante a tener en cuenta cuando hablamos de *strings* es que estos son inmutables, esto significa que cada vez que modificamos uno estamos generando un nuevo objeto en memoria.

El índice de la primera letra es 0, en la programación se empieza a contar desde 0

## Funciones de cadenas de caracteres (Strings)

| Method                                                       | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [capitalize()](https://www.w3schools.com/python/ref_string_capitalize.asp) | Convierte el primer carácter en mayúsculas                   |
| [casefold()](https://www.w3schools.com/python/ref_string_casefold.asp) | Convierte una cadena en minúsculas                           |
| [center()](https://www.w3schools.com/python/ref_string_center.asp) | Devuelve una cadena centrada                                 |
| [count()](https://www.w3schools.com/python/ref_string_count.asp) | Devuelve el número de veces que un valor especificado se produce en una cadena |
| [encode()](https://www.w3schools.com/python/ref_string_encode.asp) | Devuelve una versión codificada de la cadena                 |
| [endswith()](https://www.w3schools.com/python/ref_string_endswith.asp) | Devuelve true si los extremos de cadena con el valor especificado |
| [expandtabs()](https://www.w3schools.com/python/ref_string_expandtabs.asp) | Establece el tamaño de la pestaña de la cadena               |
| [find()](https://www.w3schools.com/python/ref_string_find.asp) | Busca la cadena de un valor especificado y devuelve la posición de donde fue encontrado |
| [format()](https://www.w3schools.com/python/ref_string_format.asp) | Formatos especifican los valores de una serie                |
| [format_map()](https://www.programiz.com/python-programming/methods/string/format_map) | Formatos especifican los valores de una serie                |
| [index()](https://www.w3schools.com/python/ref_string_index.asp) | Busca la cadena de un valor especificado y devuelve la posición de donde fue encontrado |
| [isalnum()](https://www.w3schools.com/python/ref_string_isalnum.asp) | Devuelve verdadero si todos los caracteres de la cadena son alfanuméricos |
| [isalpha()](https://www.w3schools.com/python/ref_string_isalpha.asp) | Devuelve True si todos los caracteres de la cadena están en el alfabeto |
| [isdecimal()](https://www.w3schools.com/python/ref_string_isdecimal.asp) | Devuelve True si todos los caracteres de la cadena son decimales |
| [isdigit()](https://www.w3schools.com/python/ref_string_isdigit.asp) | Devuelve verdadero si todos los caracteres de la cadena son dígitos |
| [isidentifier()](https://www.w3schools.com/python/ref_string_isidentifier.asp) | Devuelve True si la cadena es un identificador               |
| [islower()](https://www.w3schools.com/python/ref_string_islower.asp) | Devuelve verdadero si todos los caracteres de la cadena son minúsculas |
| [isnumeric()](https://www.w3schools.com/python/ref_string_isnumeric.asp) | Devuelve verdadero si todos los caracteres de la cadena son numéricos |
| [isprintable()](https://www.w3schools.com/python/ref_string_isprintable.asp) | Devuelve verdadero si todos los caracteres de la cadena son imprimibles |
| [isspace()](https://www.w3schools.com/python/ref_string_isspace.asp) | Devuelve True si todos los caracteres de la cadena son espacios en blanco |
| [istitle()](https://www.w3schools.com/python/ref_string_istitle.asp) | Devuelve True si la cadena sigue las reglas de un título     |
| [isupper()](https://www.w3schools.com/python/ref_string_isupper.asp) | Devuelve True si todos los caracteres de la cadena son mayúsculas |
| [join()](https://www.w3schools.com/python/ref_string_join.asp) | Se une a los elementos de un iterable al final de la cadena  |
| [ljust()](https://www.w3schools.com/python/ref_string_ljust.asp) | Devuelve una versión justificada izquierda de la cadena      |
| [lower()](https://www.w3schools.com/python/ref_string_lower.asp) | Convierte una cadena en minúsculas                           |
| [lstrip()](https://www.w3schools.com/python/ref_string_lstrip.asp) | Devuelve una versión de ajuste izquierdo de la cuerda        |
| [maketrans()](https://www.programiz.com/python-programming/methods/string/maketrans) | Devuelve una tabla de traducción para ser utilizado en traducciones |
| [partition()](https://www.w3schools.com/python/ref_string_partition.asp) | Devuelve una tupla donde la cadena se separó en tres partes  |
| [replace()](https://www.w3schools.com/python/ref_string_replace.asp) | Devuelve una serie en un valor especificado es reemplazado con un valor especificado |
| [rfind()](https://www.w3schools.com/python/ref_string_rfind.asp) | Busca la cadena de un valor especificado y devuelve la última posición de donde fue encontrado |
| [rindex()](https://www.w3schools.com/python/ref_string_rindex.asp) | Busca la cadena de un valor especificado y devuelve la última posición de donde fue encontrado |
| [rjust()](https://www.w3schools.com/python/ref_string_rjust.asp) | Devuelve una versión justificada derecha de la cadena        |
| [rpartition()](https://www.w3schools.com/python/ref_string_rpartition.asp) | Devuelve una tupla donde la cadena se separó en tres partes  |
| [rsplit()](https://www.w3schools.com/python/ref_string_rsplit.asp) | Divide la cadena en el separador especificado y devuelve una lista |
| [rstrip()](https://www.w3schools.com/python/ref_string_rstrip.asp) | Devuelve una versión ajuste correcto de la cadena            |
| [split()](https://www.w3schools.com/python/ref_string_split.asp) | Divide la cadena en el separador especificado y devuelve una lista |
| [splitlines()](https://www.w3schools.com/python/ref_string_splitlines.asp) | Divide la cadena en los saltos de línea y devuelve una lista |
| [startswith()](https://www.w3schools.com/python/ref_string_startswith.asp) | Devuelve true si la cadena comienza con el valor especificado |
| [strip()](https://www.w3schools.com/python/ref_string_strip.asp) | Devuelve una versión recortada de la cadena                  |
| [swapcase()](https://www.w3schools.com/python/ref_string_swapcase.asp) | Permutas de los casos, se convierte en minúsculas mayúsculas y viceversa |
| [title()](https://www.w3schools.com/python/ref_string_title.asp) | Convierte el primer carácter de cada palabra en mayúsculas   |
| [translate()](https://www.tutorialspoint.com/python/string_translate.htm) | Devuelve una cadena traducida                                |
| [upper()](https://www.w3schools.com/python/ref_string_upper.asp) | Convierte una cadena en mayúsculas                           |
| [zfill()](https://www.w3schools.com/python/ref_string_zfill.asp) | Rellena la cadena con un número determinado de valores de 0 a principios |

## Lists (Arrays equivalents)

Una lista es una estructura de datos y un tipo de dato en python con características especiales. Lo especial de las listas en Python es que nos permiten almacenar cualquier tipo de valor como enteros, cadenas y hasta otras funciones; 

por ejemplo:

```python
lista = [1, 2.5, 'DevCode', [5,6] ,4]
```

Una lista es un arreglo de elementos donde podemos ingresar cualquier tipo de dato, para acceder a estos datos podemos hacer mediante un índice.

```python
print lista[0]
```

Si no quieres estar imprimir uno por uno los elementos de una lista, puedes recorrerlo utilizando un for.

```python
for element in lista:
    print element
```



| Method                                                       | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [append()](https://www.w3schools.com/python/ref_list_append.asp) | Añade un elemento al final de la lista                       |
| [clear()](https://www.w3schools.com/python/ref_list_clear.asp) | Elimina todos los elementos de la lista                      |
| [copy()](https://www.w3schools.com/python/ref_list_copy.asp) | Devuelve una copia de la lista                               |
| [count()](https://www.w3schools.com/python/ref_list_count.asp) | Devuelve el número de elementos con el valor especificado    |
| [extend()](https://www.w3schools.com/python/ref_list_extend.asp) | Añadir los elementos de una lista (o cualquier iterable), hasta el final de la lista actual |
| [index()](https://www.w3schools.com/python/ref_list_index.asp) | Devuelve el índice del primer elemento con el valor especificado |
| [insert()](https://www.w3schools.com/python/ref_list_insert.asp) | Añade un elemento en la posición especificada                |
| [pop()](https://www.w3schools.com/python/ref_list_pop.asp)   | Elimina el elemento en la posición especificada              |
| [remove()](https://www.w3schools.com/python/ref_list_remove.asp) | Elimina el primer elemento con el valor especificado         |
| [reverse()](https://www.w3schools.com/python/ref_list_reverse.asp) | Invierte el orden de la lista                                |
| [sort()](https://www.w3schools.com/python/ref_list_sort.asp) | Ordena la lista                                              |

## Operaciones con listas

Ahora que ya entiendes cómo funcionan las **listas**, podemos ver qué tipo de operaciones y métodos podemos utilizar para  modificarlas, manipularlas y realizar diferentes tipos de cómputos con  esta Estructura de Datos.

- El operador **+(suma)** concatena dos o más listas.
- El operador ***(multiplicación)** repite los elementos de la misma lista tantas veces los queramos multiplicar

Sólo podemos utilizar **+(suma)** y ***(multiplicación)**.

Las listas tienen varios métodos que podemos utilizar.

## Ejemplos de operadores

### append

Nos permite añadir elementos a listas cambiando el tamaño de la lista a `list_size +=1`. 

```python
fruits=['banana','kiwi']
fruits.append('apple')
print(fruits) # ['banana', 'kiwi', 'apple']
```

### pop

Nos permite sacar el último elemento de la lista, regresando el valor del elemento quitado, mismo que podrá ser almacenado en alguna otra variable.  

`pop` también recibe un índice y esto nos permite elegir qué elemento queremos eliminar.

```python
fruits=['banana', 'kiwi', 'apple']
some_fruit = fruits[0] 
print(some_fruit) # banana
print(fruits) # ['banana', 'kiwi', 'apple']
```

### sort

Modifica la propia lista y ordenarla de mayor a menor. 

Existe otro método llamado `sorted`, que también ordena la lista, pero genera una nueva instancia de la lista.

```python
random_numbers=[6, 7, 4, 2, 12, 10, 11, 9, 11, 10]

ordered_numbers=sorted(random_numbers) # ordena y asignar el valor ordenado a la variable
print (ordered_numbers) # [2, 4, 6, 7, 9, 10, 10, 11, 11, 12]

print(random_numbers) # [6, 7, 4, 2, 12, 10, 11, 9, 11, 10]
random_numbers.sort()  #ordena la lista y la guarda modificando las posiciones del interior

print(random_numbers) # [2, 4, 6, 7, 9, 10, 10, 11, 11, 12]
```

### del

**`del`** nos permite eliminar elementos vía indices, funciona con *slices*

```python
fruits=['banana', 'kiwi', 'apple']
print(len(fruits)) # 3
del fruits[0] #Borraras la posicion indicada en este caso 'banana'
print(fruits) # ['kiwi', 'apple']
print(len(fruits)) # 2
```

### remove

**`remove`** nos permite es pasarle un valor para que Python  compare internamente los valores y determina cuál de ellos hace match o  son iguales para eliminarlos.

```python

```



# Buenas prácticas

Dejar 2 espacios entre declaraciones de funciones o bloques de código

Dejar 1 espacio entre secciones (declaraciones, ejecuciones)