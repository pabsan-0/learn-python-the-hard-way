## KEYWORDS cheatsheet! (not in english, this is more like notes)

# and       # Operador loxico
# del       # Quita un elemento dunha coleccion (lista ou dict)
a = [1, 2, 3]
del a[2]
print a         # a = [1, 2]

# from      # Importa funcions de modulos, de maneira que se poden chamar directamente
# not       # Operador lóxico negar
# while     # Bucle condicional
# as        # Set alias for imported modules or classes
# elif      # Else if
# global    # Importa variable global nunha funcion para modificala
            # Podo ler unha global nunha funcion sin problema
            # Non podo cambiar o valor dunha global sin importala como global
# or        # operador lóxico
# with      # simplifica manejo de excepcions porque automaticamente prepara e limpa todo o necesario
            # xeralmente usado para abrir archivos de texto
with open("foo.txt",'r') as f:
    f.read()

# assert    # Para debugear
            # Funciona como un If que, si falla, tira un AssertionError
x = "hello"
assert x == "hello"     # nothing happens
assert x == "goodbye"   # AssertionError is raised

# else      # condicional else
# if        # condicional if
# pass      # Null statement; fai absolutamente nada
# yield     # requiere entender Generadores...:
            # Iterable: unha cousa da que se poden ler mais cousas unha a unha (podese iterar)
            #           P.ex lista, string... etc
            #           Todos os valores estan nalgun sitio da memoria
            # Generator: Iterable que solo se pode iterar unha vez
            #            Generan valores sobre a marcha que non se gardan
            #            "Generan" -> definoos eu tamen
mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)                # devolverá 0; 1; 4 (o que lle pedin), pero unha sola vez
            # yield usase como un return, pero devolve un generador
# break     # salese do bucle actual
# except    # excepcion para Try statement
            # sempre hai que poñer unha, e podese especificar o tipo de error (NameError, TypeError)
# import    # ejecuta scripts de python // importa modulos (mismo concepto)
# print     # enseña output en pantalla
# class     # define unha nova clase
# exec      # comese un string e é capaz de interpretalo como codigo
# in        # test loxico si algo forma parte de contenedor(lista, tupla, string...)
# raise     # raise an exception;
            # Debe ser un nombre de excepcion nativo, non definida por min
            # OU Exception("O QUE ME DEA A MIN A GANA")
            # sigo sin entender moi ben como se identifican as excepcions co except
raise Exception("ohman jeex")

# continue  # skip to the next iteration of a loop
# finally   # usase con excepcions
            # Introduce bloque de codigo que se ejecuta sempre, sin importar as excepcions
# is        # test loxico si duas variables representan o mismo objeto ** (difuso por agora)
# return X  # X almacena resultado de chamar unha funcion
# def       # define unha funcion
# for       # For loop
# lambda    # crea funcion anonima (sin nombre) que se pode meter nunha variable
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# try       # try except finally
# nonlocal  # define variable non local dentro dunha funcion
def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x
print(myfunc1()) # vai devolver "hello"


## DATA TYPES

# True      # 1
# False     # 0
# None      # null value
# strings   # 'pepe'
# numbers   # 112; int, long...
# floats    # 112.0
# lists     # [1, 3, 4, x]
# tuple     # secuencia como unha lista na que os valores non se poden cambiar
# generator # iterable que solo se pode iterar unha vez

sample_list = [1, 2, 3, 4]              # podese comprobar o tipo con type()
generator = (i for i in sample_list)
tuple_ = (1, 2, 3, 4)


## STRING ESCAPE SEQUENCES

# \\
# \'
# \"
# \a    # ascii bel (?)
# \b    # backspace, caracteres a continuacion escribense como con insert
print "a\bc"
# \f    # ascii formfeed (salto de pagina)
# \n    # newline
# \N{name}  # caracter con nombre NAME en UNICODE database
# \r    # ascii carriage return; funciona como o backspace pero vai ao principio da linea
# \t    # tab
# \v    # vertical tab


## STRING FORMATS

# %d    # numeros
# %i    # igual que %d, d e mais vello
# %o
# %u
# %x
# %X
# %e
# %E
# %f    # floats
# %F
# %g
# %G
# %c
# %r    # raw
# %s    # string
# %%

# OPERATORS

# +
# -
# *
# **        # a^b
# /         # dividir
# //        # dividir, resultado truncado a enteiro
print 10.0/3.0
print 10.0//3.0

# %         # mod
# <
# >
# <=
# >=
# ==
# !=
# <>        # similar a is
1 == 1.0  # True
1 <> 1.0  # False
# ()
# []
# {}
# @        # nin idea
# ,
# :
# .
# =
# ;

# +=
# -=
# *=
# /=
# //=
# %=
# **=
