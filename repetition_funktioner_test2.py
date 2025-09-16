# return

def returnera(a):
    a = a + 1
    print(id(a))
    
    return a

mitt_värde = returnera(5)
print(mitt_värde)

def multiplicera(a,b):
    multiply = a*b
    return multiply
    

andra_värde = multiplicera(5,98)
print(andra_värde)
multiplicera(3,7)

global_lista = []

def ändrar_i_globala_listan(värde):
    global_lista.append(värde)

def ändrar_lista_baserat_på_referens(lista, värde):
    lista.append(värde)

ändrar_i_globala_listan(5)
ändrar_lista_baserat_på_referens(global_lista, 8)

stort_nummer = 234987874923923487234897234987
print(id(stort_nummer))
returnera(stort_nummer)

def reverse_order(a,b):
    return b,a,a*b

x = 10
y = 8
x,y,xy = reverse_order(x,y)
print(x, y, xy)
value = reverse_order(x,y)
x = value[0]
y = value[1]
xy = value[2]
print(x, y, xy)

print(type(reverse_order(1,2)))

ett_värde = 6
print(ett_värde)
ett_värde = multiplicera(ett_värde, 20)
print(ett_värde)

