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