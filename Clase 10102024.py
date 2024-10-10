# Escribe tu código aquí :-)
# Escribe tu código aquí :-)
preguntas = True
while preguntas:
    operación = input("¿Qué operación quieres realizar(+,-,*,/)?")
    if operación == "+" or operación == "-" or operación == "*" or operación == "/":
        preguntas = False
    else:
        print("Escriba un valor correcto (+,-,* o /)")
        preguntas = True
aciertos = 0
def funcion(aciertos):
    import random
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    if operación == "+":
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        resultado = num1+num2
        print("Cuánto es",num1,"+",num2)
    if operación == "-":
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        resultado = num1-num2
        print("Cuánto es",num1,"-",num2)
    if operación == "*":
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        resultado = num1*num2
        print("Cuánto es",num1,"*",num2)
    if operación == "/":
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        resultado = num1/num2
        print("Cuánto es",num1,"/",num2)
    respuesta = int(input("Resultado:"))
    if respuesta == resultado:
        print("Correcto")
        aciertos = aciertos + 1
    else:
        print("Error vuelve a intentarlo")
    return aciertos
for pruebas in range(0,10):
    aciertos=funcion(aciertos)
print("Has acertado",aciertos,"/10")
