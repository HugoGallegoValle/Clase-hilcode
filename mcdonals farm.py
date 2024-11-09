# Escribe tu código aquí :-)
variable = " "
diccionario= {
   "pig":"oing",
   "duck":"quack",
   "cow":"moo",
   "mouse":"squeak"
}
def estribillo(diccionario,variable):
    for animal,sonido in diccionario.items():
        variable = variable + f'''Old MacDonald had a farm, E-I-E-I-O
And on that farm he had a {animal}, E-I-E-I-O
With a {sonido}-{sonido} here and a {sonido}-{sonido} there
Here a {sonido}, there a {sonido}, everywhere a {sonido}-{sonido}'''
        print(variable)
        print('''

        ''')
estribillo(diccionario,variable)
