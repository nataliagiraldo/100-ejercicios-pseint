
def ej1():
    numero = int(input("Ingrese numero: "))

    for i in range(12):
        print(f"{numero} x {i} = {numero * i}")

def ej2():
    numeroI = 0
    numeroP = 0

    for i in range(10):
        numero = int(input("Ingrese numero: "))
        if numero % 2 == 0:
            numeroP += 1
        else:
            numeroI += 1
    print(f"Numeros pares: {numeroP}\nNumeros impares: {numeroI}")

def ej3():
    total = 0
    desc = 0
    for cont in range(10):
        print("CONSUMO", cont, ": $")
        consumo = float(input())
        total += consumo

    if total > 50:
        desc = total * 0.07

    print("CONSUMO TOTAL: $", total)
    print("DESCUENTO: $", desc)
    print("PAGO TOTAL: $", total - desc)

def ej4():
    xpromedio = 0
    xnombre = 0
    for i in range (5):
        nombre = input("Ingrese el nombre del alumno: ")
        promedio = int(input(f"Ingrese el promedio del alumno {nombre}: "))
        if xpromedio < promedio:
            xpromedio = promedio
            xnombre = nombre
    print(f"El promedio mas alto fue el de {xnombre} siendo {xpromedio}")

def ej5():
    a = 0
    b = 1
    c = 0
    for i in range (10):
        print(c)
        a = b
        b = c
        c = a + b

def ej6():
    a = 1
    b = 1
    c = 5
    for i in range (5):
        print(a)
        print((i + 1) * 5)
        a += 6

def ej7():
    F = 0
    C = 0
    S = 0
    serie = 0

    for F in range(10):
        S = 0
        serie = 0

        for C in range(1, 10 - F + 1, 1):
            S = (10 - F)
            serie = (serie * 10) + S

        print(serie)    

def ej8():
    F = 0
    C = 0
    serie = 0

    for F in range(1, 10, 1):
        serie = 0

        for C in range(1, 10 - F + 1, 1):
            serie = (serie * 10) + C

        print(serie)
def ej9():
    C = 0
    F = 0
    XN = 0
    serie = ""
    XN = 7

    for F in range(1, 8, 1):
        serie = ""
        
        if F >= 5:
            XN = XN + 2

        for C in range(1, XN - F + 1, 1):
            serie = serie + "* "

        print(serie)
def ej10():
    for i in range(10):
        palabra = input(f"palabra {i+1}:")

def ej11():
    producto = 1
    n = int(input("Ingrese un numero "))

    for i in range(1, n+1):
        producto = producto * i 

    print(f"El producto de {n} es {producto}")

def ej12():
    a = int(input("Ingrese un numero "))
    b = int(input("Ingrese un numero "))

    for i in range(a, b-1):
        print(i+1)

def ej13():
    import random
    for i in range(10):
        numAleatorio = random.randint(10,99)
        print(numAleatorio)

def ej14():
    for i in range(51):
        print (i)

def ej15():
    for i in range (19, -1, -1):
        print(i + 1)

def ej16():
    for i in range (20):
        print(" NO DECIR MALAS PALABRAS")

def ej17():
    for i in range (20):
        print (i + 1)

def ej18():
    num = int(input("Ingrese un numero: "))
    strNum = str(num)
    if strNum == strNum[::-1]:
        print(f"El numero {num} es capicua ")
    else:
        print(f"El numero {num} no es capicua ")

def ej19():
    numero = int(input("Ingrese numero: "))

    for i in range(12):
        print(f"{numero} x {i} = {numero * i}")

def ej20():
    import random
    numAleatorio = random.randint(1, 20)
    for i in range(3):
        intento = int(input("Encuentre el número [1-20]: "))

        if intento < numAleatorio:
            print("Intenta con un número mayor.")
        elif intento > numAleatorio:
            print("Intenta con un número menor.")
        elif intento == numAleatorio:
            print("¡Has acertado!")
            break 

    if intento == numAleatorio:
        print(f"El número a encontrar era {numAleatorio}")
    else:
        print(f"Lo siento, no has adivinado. El número correcto era {numAleatorio}")

def ej21():
    for i in range(2, 21, 2):
        print(i)   

def ej22():
    for i in range(1, 21, 2):
        print(i)

def ej23():
    sum = 0
    cantNotas = int(input("Ingrese la cantidad de notas que desea registrar: "))
    for i in range (cantNotas):
        nota = int(input(f"NOTA {i+1}: "))
        sum += nota
    promedio = sum/cantNotas
    print(f"PROMEDIO: {promedio}")

def ej24():
    num = int(input("FACTORIAL A CALCULAR: "))
    fact = 1
    print(f"SERIE DEL FACTORIAL: ", end="")
    for x in range(1, num + 1):
        print(f"{num + 1 - x} ", end="")
        fact *= x
    print("\nEL FACTORIAL ES: ", fact)

def ej25():
    suma = 0.0
    n = int(input("VALOR DE N: "))
    i = 0
    d = 3
    if n > 1:
        print(suma, " +", end="")
        for i in range(2, n + 1):
            if i == n:
                print(i, "/", d, end="")
            else:
                print(i, "/", d, " +", end="")
            
            suma += i / d
            d += 2

    print("\nLa suma es:", suma)

def ej26():
    for i in range(100, 1000):
        a = i % 10
        b = i % 100 - a
        c = (i - (i % 100))/ 100
        if i == a * 100 + b + c:
            print(i)

def ej27():
    N = int(input("Ingrese un número N: "))

    primos = [num for num in range(2, N + 1) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]

    print(f"Números primos hasta {N}: {primos}")


def ej28():
    numero_ingresado = int(input("Ingrese un número: "))

    if numero_ingresado < 2:
        es_primo = False
    else:
        es_primo = all(numero_ingresado % i != 0 for i in range(2, int(numero_ingresado**0.5) + 1))

    if es_primo:
        print(f"{numero_ingresado} es un número primo.")
    else:
        print(f"{numero_ingresado} no es un número primo.")

def ej29():
    numeroI = 0
    numeroP = 0
    numero = int(input("Ingrese numero: "))

    for i in range(numero):
        if i % 2 == 0:
            numeroP += i
        else:
            numeroI += i
    print(f"Suma pares: {numeroP}\nSuma impares: {numeroI}")

def ej30():
    tv_h = 0
    tv_m = 0
    muj = 0

    empleados = int(input("CANTIDAD DE EMPLEADOS: "))

    for cont in range(1, empleados + 1):
        print(f"EMPLEADO Nro {cont}/{empleados}")
        nom = input("NOMBRE: ")
        genero = input("GÉNERO (H/M): ")

        if genero.upper() == "H":
            ventas = float(input(f"VENTAS DE {nom}: "))
            tv_h += ventas
        elif genero.upper() == "M":
            ventas = float(input(f"VENTAS DE {nom}: "))
            tv_m += ventas
            muj += 1

    print(f"\nTotal de ventas hombres: {tv_h}")
    print(f"Total de ventas mujeres: {tv_m}")
    print(f"Número de mujeres: {muj}")

def ej31():
    refran = input("Ingresa un refrán: ")
    contador_c = contador_s = contador_d = contador_l = contador_r = contador_m = 0

    for letra in refran:
        letra_mayuscula = letra.upper()

        if letra_mayuscula == 'C':
            contador_c += 1
        elif letra_mayuscula == 'S':
            contador_s += 1
        elif letra_mayuscula == 'D':
            contador_d += 1
        elif letra_mayuscula == 'L':
            contador_l += 1
        elif letra_mayuscula == 'R':
            contador_r += 1
        elif letra_mayuscula == 'M':
            contador_m += 1

    print(f"Número de letras C: {contador_c}")
    print(f"Número de letras S: {contador_s}")
    print(f"Número de letras D: {contador_d}")
    print(f"Número de letras L: {contador_l}")
    print(f"Número de letras R: {contador_r}")
    print(f"Número de letras M: {contador_m}")

def ej32():
    for _ in range(10):
        print("DNI: ", end="")
        onia = input()
        
        print("DIA DE NACIMIENTO : ", end="")
        dia = int(input())
        
        print("MES DE NACIMIENTO : ", end="")
        mes = int(input())
        
        print("AÑO DE NACIMIENTO : ", end="")
        anio = int(input())
        
        print("GÉNERO (H/M): ", end="")
        genero = input()
        
        print("FECHA ACTUAL: {}/{}/{}".format(dia, mes, anio))
        
        edad = 2023 - anio
        
        if mes > 12 or dia > 31:
            print("Fecha de nacimiento no válida.")
        else:
            if mes > 1 or (mes == 1 and dia > 1):
                edad -= 1

        print("EDAD: {} años".format(edad))

        if edad >= 8:
            print("RECIBE TABLET")
        elif edad == 6:
            if genero == "H":
                print("RECIBE CARRITO")

def ej33():
    frase = input("Ingrese una frase: ")
    contador_vocales = 0

    for caracter in frase:
        if caracter.lower() in "aeiou":
            contador_vocales += 1

    print(f"La frase tiene {contador_vocales} vocal(es).")

def ej34():
    tarifas = {'moto': 13, 'auto': 10, 'camion': 8}

    total_recaudado_mañana = 0
    total_recaudado_noche = 0
    total_recaudado_por_tipo = {'moto': 0, 'auto': 0, 'camion': 0}

    cantidad_vehiculos = int(input("Ingrese la cantidad de vehículos: "))

    for _ in range(cantidad_vehiculos):
        tipo_vehiculo = input("Ingrese el tipo de vehículo (moto/auto/camion): ")
        turno = input("Ingrese el turno (Mañana/Noche): ")

        if tipo_vehiculo in tarifas:
            tarifa = tarifas[tipo_vehiculo]

            total_recaudado_por_tipo[tipo_vehiculo] += tarifa

            if turno.lower() == 'mañana':
                total_recaudado_mañana += tarifa
            elif turno.lower() == 'noche':
                total_recaudado_noche += tarifa
            else:
                print("Turno no válido. Se omitirá este vehículo.")

        else:
            print("Tipo de vehículo no válido. Se omitirá este vehículo.")

    print("\nTotal recaudado en la mañana:", total_recaudado_mañana, "soles")
    print("Total recaudado en la noche:", total_recaudado_noche, "soles")

    for tipo, total_por_tipo in total_recaudado_por_tipo.items():
        print(f"Total recaudado por {tipo}: {total_por_tipo} soles")

def ej35():
    try:
        filas = int(input("Ingrese un número entero mayor a 3 para la cantidad de filas: "))
        if filas < 3:
            print("Ingrese un número de filas mayor o igual a 3.")
        else:
            for i in range(filas):
                numeros = ''
                for j in range(1, i * 2 + 2):
                    numeros += str((j - 1) % 10)
                espacios = ' ' * (filas - i - 1)
                print(espacios + numeros)
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

def ej36():
    v = 4
    x = 2
    ope = "-"
    sumatoria = 0

    print("MUESTRA SERIE DE NUMEROS : ")
    print("VALOR DE N: ", end="")
    n = int(input())

    for i in range(1, n + 1):
        print(f"{v}/{x} {ope} ", end="")
        
        if i % 2 == 1:
            ope = "+"
            sumatoria += v / x
        else:
            ope = "-"
            sumatoria -= v / x
        
        v += 1 
        x1 = x * 0.5
        x *= x1


    print("\nSUMATORIA : ", sumatoria)

def ej37():
    try:
        n = int(input("Ingrese un número entero para generar el Triángulo de Pascal: "))
        coeficientes = []

        for i in range(n):
            fila = [1] * (i + 1)

            if i > 1:
                for j in range(1, i):
                    fila[j] = coeficientes[i - 1][j - 1] + coeficientes[i - 1][j]

            coeficientes.append(fila)

        max_digitos = len(str(max(map(max, coeficientes))))

        for fila in coeficientes:
            espacios = " " * max_digitos
            print(espacios * (len(coeficientes) - len(fila)), end="")

            for coeficiente in fila:
                print(f"{espacios}{coeficiente}", end=" ")
                espacios = " " * (max_digitos - len(str(coeficiente)))

            print()

    except ValueError:
        print("Por favor, ingrese un número entero válido.")


def ej38():
    rojo = 0
    verde = 0
    azul = 0

    n = int(input("Ingrese la cantidad de personas a realizar la votacion "))
    for i in range(n):
        rta = input("Ingrese cual color prefiere, rojo verde o azul ")
        if rta.lower() == "rojo" :
            rojo += 1
        elif rta.lower() == "verde" :
            verde += 1
        elif rta.lower() == "azul" :
            azul += 1
        else:
            print("Ingrese una respuesta valida")
    colores = {"rojo": rojo, "verde": verde, "azul": azul}
    colorMasVotado = max(colores, key=colores.get)
    
    print(f"personas cuyo color favorito es rojo: {rojo}\npersonas cuyo color favorito es verde: {verde}\npersonas cuyo color favorito es azul: {azul}")
    print(f"el color mas votado es {colorMasVotado}")

def ej39():
    notas = []
    for i in range (3):
        nota = int(input(f"ingrese la nota {i + 1}: "))
        notas.append(nota)

    promedio = sum(notas)/len(notas)
    print(f"el promedio es : {promedio}")

def ej40():
    monto = int(input("Ingrese monto: "))
    precioD = monto / 2.7
    precioE = monto / 4
    print(f"Monto en dolares: {precioD}\nMonto en euros: {precioE}")

def ej41():
    salario = int(input("Ingrese salario: "))
    des = salario * 0.2
    print(f"El valor del descuento es: {des}")
    print(f"Nuevo salario: {salario - des}")

def ej42():
    seg = int(input("Ingrese tiempo en segundos: "))
    horas = seg // 3600
    minutos = (seg % 3600) // 60
    segundos = seg % 60

    print(f"{seg} segundos equivalen a {horas} horas, {minutos} minutos y {segundos} segundos.")

def ej43():
    dinero = int(input("Ingrese la cantidad de dinero: "))
    cant = dinero // 15
    print(f"Num de entradas: {cant}")

def ej44():
    monto = 1000
    meses = int(input("Ingrese los meses: "))
    interes = monto * (meses * 0.02)
    total = monto + interes
    print(f"Intereses: {interes}\nTotal: {total}")

def ej45():
    alto = int(input("Ingrese alto de la pared: "))
    largo = int(input("Ingrese largo de la pared: "))
    arena = (alto * largo) * 0.25
    print(f"Arena necesaria: {arena} mt3")

def ej46():
    h = int(input("Horas: "))
    m = int(input("Minutos: "))
    s = int(input("Segundos: "))
    costo = ((h * 3600) +(m * 60) + s) * 0.25
    print(f"Costo total: {costo} ")

def ej47():
    mes = int(input("ingrese numero de mes"))
    dia = int(input("ingrese numero de dias"))

    tiempo = (((mes -1)* 30) + dia)

    print("los dias transcurridos son", tiempo)

def ej48():
    num = int(input("ingrese un numero de 3 cifras"))

    cen = (num - (num % 100))/100
    res = num % 100
    dec = (res - (res % 10))/10
    uni = res % 10

    print("centena", cen)
    print("decena", dec)
    print("unidad", uni)

def ej49():
    perimetro = int(input("ingrese perimetro"))
    apotema = int(input("ingrese apotema"))

    a = (perimetro * apotema)/2

    print("area", a,  "cm2")
    print("perimetro del hexagono")
    lado = int(input("lado"))

    p = 6 * lado

    print("perimetro :", p, "cm")

def ej50():
    print("area del cuadrado")
    lado = int(input("LADO"))

    a = lado * lado 
    print("area", a)

    print("PERIMETRO DEL CUADRADO")

    p = 4 * lado
    print("perimetro: ", p)

def ej51():
    print("AREA DEL TRAPESIO")
    BaseMayor = int(input("ingrese base mayor:"))
    BaseMenor = int(input("ingrese base menor:"))
    altura = int(input("ingrese altura:"))

    a = (((BaseMayor* BaseMenor) * altura) /2)

    print("area: ", a, "cm2")

    print("perimetro del trapesio")
    lado1 = int(input("ingrese lado1:"))
    lado2 = int(input("ingrese lado2:"))
    lado3 = int(input("ingrese lado3:"))
    lado4 = int(input("ingrese lado4:"))

    p = lado1 + lado2 + lado3 + lado4
    print("perimetro :", p , "cm")

def ej52():
    print("AREA DEL RECTANGULO")
    base = int(input("ingrese base"))
    altura = int(input("ingrese altura"))

    a = base * altura
    print("AREA: ", a, "cm")

    print("PERIMETRO DEL RECTANGULO")

    p = (2*altura) + (2*base)
    print("PERIMETRO", p, "cm")

def ej53():
    print("AREA DEL CUADRADO")
    lado = int(input("ingrese lado"))

    a = lado * lado
    print("AREA", a)

    print("PERIMETRO DEL CUADRADO")
    p = 4 * lado
    print("PERIMETRO", p)

def ej54():
    print("temperatura fahrenheit: ")
    fahrenheit = int(input("ingrese temperatura en fahrenheit"))
    calius = (fahrenheit - 32) * (5/9)
    print("CELIUS :", calius)

def ej55():
    celsius = int(input("GRADOS CELSIUS: "))

    f = (celsius*(9/5) + 32)
    print("A FAHRENHEIT: ",f)

def ej56():
    fecha_ingresada = input("Ingrese la fecha en formato YYYY-MM-DD: ")

    año, mes, dia = map(int, fecha_ingresada.split('-'))

    import datetime
    fecha_actual = datetime.datetime.now()

    diferencia = fecha_actual - datetime.datetime(año, mes, dia)
    dias_totales = diferencia.days

    años = dias_totales // 365

    dias_restantes = dias_totales % 365
    meses = dias_restantes // 30

    dias = dias_restantes % 30

    print(f"Años: {años}, Meses: {meses}, Días: {dias}")

def ej57():
    presupuesto = int(input("ingrese presupuesto : "))
    gine = presupuesto * 0.40
    trau = presupuesto * 0.30
    pedi = presupuesto * 0.30

    print("GINECOLOGIA    :$", gine)
    print("TRAUMATOLOGIA  :$", trau)
    print("PEDIATRIA      :$", pedi)

def ej58():
    print("AREA DEL ROMBO")
    diametroM = int(input("ingrese diametro mayor"))
    diametroMenor = int(input("ingrese diametro menor"))

    a = (diametroM * diametroMenor)/2
    print("AREA :",a, "cm")
    print("PERIMETRO DEL ROMBO")
    lado = int(input("ingrese lado"))
    p = 4 * lado

    print("PERIMETRO:", p, "cm")

def ej59():
    print("AREA DEL PENTAGONO")
    perimetro = int(input("ingrese perimetro: "))
    apotema =int(input("ingrese apotema"))

    a = (perimetro * apotema)/2
    print("AREA", a, "cm")
    print("PERIMETRO DEL PENTAGONO")
    lado = int(input("lado : "))
    p = 5*lado
    print("PERIMETRO", p,"cm")

def ej60():
    print("01 calcular el IGV")
    monto = int(input("ingrese monto de dinero : "))
    igv = monto * 0.18
    print("el IGV de 18%, es :", igv)

def ej61():
    print("AREA DEL PARALELOGRAMO")
    base = int(input("BASE"))
    altura = int(input("ALTURA"))
    a = base * altura
    print("AREA :", a, "cm")
    print("PERIMETRO DEL PARALELOGRAMO")
    P = (2*altura) + (2* base)
    print("PERIMETRO :", P, "cm")

def ej62():
    costo = int(input("costo de la casa: "))
    valorIva = int(input("valoe del iva"))

    total = costo + (costo*(valorIva/100))
    print("IVA DE", valorIva, "% :", (costo*(valorIva/100)))
    print("TOTAL A PAGAR :", total)

def ej63():
    pulgadas = int(input("ingrese pulgadas"))

    pies = pulgadas/12
    print("A PIES: ",pies)

def ej64():
    radio = int(input("ingrese radio: "))
    altura = int(input("ingrese altura: "))
    a = 2* 3,14* radio*(altura + radio)
    v = 3,14 * (radio * radio) * altura
    print("AREA TOTAL DEL CILINDRO ES :", a, "cm2")
    print("VOLUMEN TOTAL DEL CILINDRO ES :", v, "cm3")

def ej65():
    print("area del cuadrado")
    lado = int(input("LADO"))

    a = lado * lado 
    print("area", a)

    print("PERIMETRO DEL CUADRADO")

    p = 4 * lado
    print("perimetro: ", p)


def ej66():
    caracter = input("Ingrese el carácter para el triángulo: ")
    altura = int(input("Ingrese la altura del triángulo: "))
    for i in range(1, altura + 1):
            espacios = altura - i
            triangulo = ' ' * espacios + caracter * (2 * i - 1)
            print(triangulo)

def ej67():
    altura = int(input("Ingrese la altura del rombo (debe ser un número impar): "))

    if altura % 2 == 0:
        print("La altura debe ser un número impar. Añadiendo 1 para hacerla impar.")
        altura += 1

    for i in range(1, altura, 2):
        espacios = " " * ((altura - i) // 2)
        asteriscos = "*" * i
        print(espacios + asteriscos)

    for i in range(altura, 0, -2):
        espacios = " " * ((altura - i) // 2)
        asteriscos = "*" * i
        print(espacios + asteriscos)

def ej68():
    constante = 100
    diaLaborable = 25
    hijos = int(input("ingrese cuentos hijos tiene"))
    DiasN = int(input("ingrese la cantidad de dias que no asistio"))
    sBase = int(input("ingrese sueldo base"))
    total1 = ((hijos*constante) + (diaLaborable*DiasN) + sBase)
    print(f"el sueldo final es de {total1}")

def ej69():
    aprobados = int(input("ingrese la cantidad de alumnos aprobados"))
    desaprobados = int(input("ingrese la cantidad de alumnos desaprobados"))

    sum = aprobados + desaprobados
    porcentaje_aprobado = (aprobados / sum) * 100
    porcentaje_desaprobado = (desaprobados / sum) * 100
    print ("El porcentaje de alumnos aprobados es: ", porcentaje_aprobado, "%")
    print ("El porcentaje de alumnos desaprobados es: ", porcentaje_desaprobado, "%")

def ej70():
    try:
        nota1 = float(input("Ingrese la primera nota: "))
        nota2 = float(input("Ingrese la segunda nota: "))
        nota3 = float(input("Ingrese la tercera nota: "))

        promedio = (nota1 + nota2 + nota3) / 3

        print(f"El promedio de las notas es: {promedio:.2f}")

        if promedio >= 6:
            resultado = "Aprobado"
        else:
            resultado = "Desaprobado"

        print(f"Resultado: {resultado}")

    except ValueError:
        print("Por favor, ingrese notas válidas.")

def ej71():
    try:
        numero = int(input("Ingrese un número entero: "))

        if numero % 2 == 0:
            print(f"{numero} es un número par.")
        else:
            print(f"{numero} es un número impar.")

    except ValueError:
        print("Por favor, ingrese un número entero válido.")


def ej72():
    bandera1 = True

    while bandera1:
        try:
            nombre = input("Ingrese su nombre de usuario: ")
            clave = int(input("Ingrese su contraseña: "))
            
            if nombre == "admin" and clave == 1234567:
                print("ACCESO PERMITIDO")
                break
            else:
                print("ERROR DE ACCESO. INTENTE NUEVAMENTE.")
        except ValueError:
            print("Error en la entrada de datos, intente de nuevo")

        continuar = input("Desea intentarlo nuevamente? s/n: ").lower()
        if continuar != "s":
            break

def ej73():
    cantidadM = int(input("ingrese cantidad de minutos"))

    if (cantidadM <= 5):
        costo = cantidadM*0.9
    else: 
        costo = (5*0.9)+((cantidadM -5)*1.1)
        print ("el costo es", costo)

def ej74():
    numero = input("Ingrese un número: ")
    if numero == numero[::-1]:
        print(f"El número {numero} es capicúa.")
    else:
        print(f"El número {numero} no es capicúa.")

def ej75():
    monto_compra = float(input("Ingrese el monto de compra: "))

    if monto_compra > 350:
        descuento = 0.35  
    else:
        descuento = 0.10  
        
    monto_descuento = monto_compra * descuento
    monto_a_pagar = monto_compra - monto_descuento

    print(f"Monto de compra: ${monto_compra:.2f}")
    print(f"Descuento aplicado: ${monto_descuento:.2f}")
    print(f"Monto a pagar: ${monto_a_pagar:.2f}")

def ej76():
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    numero3 = float(input("Ingrese el tercer número: "))

    if numero1 <= numero2 <= numero3 or numero3 <= numero2 <= numero1:
        numero_intermedio = numero2
    elif numero2 <= numero1 <= numero3 or numero3 <= numero1 <= numero2:
        numero_intermedio = numero1
    else:
        numero_intermedio = numero3

    print(f"El número intermedio es: {numero_intermedio}")
 
def ej77():        
    nombre = input("Ingrese el nombre del trabajador: ")
    sueldo_basico = float(input("Ingrese el sueldo básico: "))
    num_hijos = int(input("Ingrese el número de hijos: "))

    if num_hijos > 0:
        bonificacion = 0.07 * sueldo_basico
    else:
        bonificacion = 0

    sueldo_final = sueldo_basico + bonificacion

    print(f"\nResumen para el trabajador {nombre}:")
    print(f"Sueldo Básico: ${sueldo_basico:.2f}")
    print(f"Bonificación (7% del sueldo básico): ${bonificacion:.2f}")
    print(f"Sueldo Final: ${sueldo_final:.2f}")

def ej78():
    edad = int(input("Ingrese su edad: "))

    if edad >= 18:
        print("Es mayor de edad.")
    else:
        print("Es menor de edad.")

def ej79():
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    if numero1 < numero2:
        mayor = numero2
        menor = numero1
    else:
        mayor = numero1
        menor = numero2


    print(f"\nNúmeros ordenados de mayor a menor: {mayor}, {menor}")

def ej80():
    monto_ventas = float(input("Ingrese el monto total de ventas: "))

    if monto_ventas > 2000:
        bonificacion = 0.10  
    else:
        bonificacion = 0.05 


    monto_bonificacion = monto_ventas * bonificacion

    print(f"\nMonto total de ventas: ${monto_ventas:.2f}")
    print(f"Bonificación aplicada ({bonificacion * 100}%): ${monto_bonificacion:.2f}")

def ej81():
    precio_unitario = float(input("Ingrese el precio unitario: "))
    cantidad = int(input("Ingrese la cantidad de compra: "))
    monto_total = precio_unitario * cantidad

    if monto_total > 100:
        igv = 0.18  
        monto_con_igv = monto_total * (1 + igv)
    else:
        igv = 0
        monto_con_igv = monto_total

    print(f"\nMonto total: S/.{monto_total:.2f}")
    print(f"IGV aplicado ({igv * 100}%): S/.{monto_total * igv:.2f}")
    print(f"Monto total con IGV: S/.{monto_con_igv:.2f}")

def ej82():
    monto_a_pagar = float(input("Ingrese el monto a pagar: "))

    if monto_a_pagar > 500:
        igv = 0.18 
        monto_con_igv = monto_a_pagar * (1 + igv)
    else:
        igv = 0
        monto_con_igv = monto_a_pagar

    print(f"\nMonto a pagar: ${monto_a_pagar:.2f}")
    print(f"IGV aplicado ({igv * 100}%): ${monto_a_pagar * igv:.2f}")
    print(f"Monto total con IGV: ${monto_con_igv:.2f}")

def ej83():
    numero = int(input("Ingrese un número entero: "))

    if numero % 2 == 0:
        print(f"\nEl número {numero} es par.")
    else:
        print(f"\nEl número {numero} es impar.")

def ej84():
    respuesta_usuario = input("¿Chile fue al mundial? (Ingrese 'verdadero' o 'falso'): ")
    respuesta_usuario = respuesta_usuario.lower()

    if respuesta_usuario == 'verdadero':
        print("Incorrecto. Chile no fue al mundial.")
    elif respuesta_usuario == 'falso':
        print("¡Correcto! Chile no participó en el último mundial.")
    else:
        print("Respuesta no válida. Por favor, ingrese 'verdadero' o 'falso'.")

def ej85():
    numero = float(input("Ingrese un número: "))

    if numero > 0:
        print(f"El número {numero} es positivo.")
    elif numero < 0:
        print(f"El número {numero} es negativo.")
    else:
        print("El número ingresado es cero.")

def ej86():
    numero_dia = int(input("Ingrese un número del 1 al 7: "))
    if 1 <= numero_dia <= 7:
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        dia_semana = dias_semana[numero_dia - 1]
        print(f"\nEl número {numero_dia} corresponde al día de la semana: {dia_semana}.")
    else:
        print("\nERROR: Ingrese un número válido del 1 al 7.")

def ej87():
    numero = int(input("Ingrese un número del 1 al 10: "))
    if 1 <= numero <= 10:
        simbolos_romanos = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
        
        numero_romano = simbolos_romanos[numero - 1]

        print(f"\n{numero} = {numero_romano}")
    else:
        print("\nERROR: Ingrese un número válido del 1 al 10.")

def ej88():
    numero = int(input("Ingrese un número del 1 al 4: "))
    if 1 <= numero <= 4:
        estaciones = ["VERANO", "OTOÑO", "INVIERNO", "PRIMAVERA"]
        estacion_actual = estaciones[numero - 1]

        print(f"\nEl número {numero} corresponde a la estación del año: {estacion_actual}")
    else:
        print("\nERROR: Ingrese un número válido del 1 al 4.")

def ej89():
    numero = int(input("Ingrese un número del 1 al 12: "))

    if 1 <= numero <= 12:
        nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Setiembre", "Octubre", "Noviembre", "Diciembre"]
        nombre_mes = nombres_meses[numero - 1]

        print(f"\nEl número {numero} corresponde al mes: {nombre_mes}")
    else:
        print("\nERROR: Ingrese un número válido del 1 al 12.")

def ej90():
    numero1 = int(input("Ingrese el primer número entero: "))
    numero2 = int(input("Ingrese el segundo número entero: "))

    operador = input("Ingrese un operador (+, -, *, /): ")

    if operador == "+":
        resultado = numero1 + numero2
    elif operador == "-":
        resultado = numero1 - numero2
    elif operador == "*":
        resultado = numero1 * numero2
    elif operador == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            print("ERROR: No se puede dividir entre cero.")
            resultado = None
    else:
        print("ERROR: Ingrese un operador válido.")

    if resultado is not None:
        print(f"\nResultado de la operación {numero1} {operador} {numero2}: {resultado}")

def ej91():
    zonas = {
        1: ("Estados Unidos", 0.13),
        2: ("Canadá", 0.11),
        5: ("América del Sur", 0.52),
        6: ("América Central", 0.99),
        8: ("México", 0.17),
        9: ("Europa", 0.17),
        10: ("Asia", 0.20),
        15: ("África", 0.59),
        20: ("Oceanía", 0.28)
    }

    zona_destino = int(input("Ingrese la zona de destino (número): "))
    duracion_llamada = float(input("Ingrese la duración de la llamada en minutos: "))

    if zona_destino in zonas:
        nombre_zona, costo_por_minuto = zonas[zona_destino]

        costo_total = costo_por_minuto * duracion_llamada

        print(f"\nCosto total de la llamada a la zona {zona_destino} ({nombre_zona}): ${costo_total:.2f}")
    else:
        print("\nERROR: Ingrese una zona de destino válida.")

def ej92():
    opciones_seguro = {
        'X': 45,
        'Y': 30,
        'Z': 15
    }

    opcion_seleccionada = input("Seleccione el tipo de seguro (X, Y, Z): ").upper()

    if opcion_seleccionada in opciones_seguro:
        costo_mensual = opciones_seguro[opcion_seleccionada]
        print(f"\nEl costo mensual del seguro {opcion_seleccionada} es de ${costo_mensual}.")
    else:
        print("\nERROR: Ingrese una opción de seguro válida (X, Y, Z).")

def ej93():
    letra = input("Ingrese una letra: ")

    lenguaje = ""

    if letra.upper() == 'V':
        lenguaje = 'Visual Basic'
    elif letra.upper() == 'P':
        lenguaje = 'Pascal'
    elif letra.upper() == 'C':
        lenguaje = 'C#'
    elif letra.upper() == 'J':
        lenguaje = 'Java'
    elif letra.upper() == 'F':
        lenguaje = 'Fortran'
    else:
        print("Error: La letra ingresada no corresponde a ningún lenguaje de programación.")

    if lenguaje:
        print(f"El lenguaje de programación correspondiente a la letra {letra.upper()} es: {lenguaje}")

def ej94():
    salario = float(input("Ingrese el salario del empleado: "))
    categoria = input("Ingrese la categoría del empleado (A, B, C o D): ").upper()
    bonificacion = {
        'A' : 0.10,
        'B' : 0.20,
        'C' : 0.30,
        'D' : 0.50
    }

    if categoria.upper() in bonificacion:
        salario_neto = salario * (1 + bonificacion[categoria])
    else:
        print("Error: Categoría no válida.")
    

    print(f"El salario neto con bonificación para la categoría {categoria} es: ${salario_neto:.2f}")

def ej95():
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))

    promedio = (nota1 + nota2 + nota3) / 3

    if 0 <= promedio <= 10:
        nivel_academico = "Malo"
    elif 11 <= promedio <= 13:
        nivel_academico = "Regular"
    elif 14 <= promedio <= 16:
        nivel_academico = "Bueno"
    elif 17 <= promedio <= 20:
        nivel_academico = "Muy bueno"
    else:
        nivel_academico = "Error: Promedio fuera de rango."

    print(f"El promedio de las notas es: {promedio:.2f}")
    print(f"Nivel académico: {nivel_academico}")

def ej96():
    cantidad_teclados = int(input("Ingrese la cantidad de teclados comprados: "))

    if cantidad_teclados > 8:
        costo_por_unidad = 10
    elif 4 <= cantidad_teclados <= 8:
        costo_por_unidad = 11
    else:
        costo_por_unidad = 15

    costo_total = cantidad_teclados * costo_por_unidad

    print(f"Número de teclados: {cantidad_teclados}")
    print(f"Costo total a pagar: {costo_total} soles")

def ej97():
    color_luz = input("Ingrese el color de la luz (Blanco, Verde, Negro, Celeste o Rojo): ").capitalize()
    valor_compra = float(input("Ingrese el valor total de su compra: "))

    if color_luz == 'Blanco':
        descuento_porcentaje = 100
    elif color_luz == 'Verde':
        descuento_porcentaje = 50
    elif color_luz == 'Negro':
        descuento_porcentaje = 40
    elif color_luz == 'Celeste':
        descuento_porcentaje = 5
    elif color_luz == 'Rojo':
        descuento_porcentaje = 0
    else:
        print("Error: Color de luz no válido. No se aplicará descuento.")
        descuento_porcentaje = 0

    descuento = valor_compra * (descuento_porcentaje / 100)
    total_pagar = valor_compra - descuento

    print(f"Descuento aplicado ({color_luz}): {descuento:.2f} soles ({descuento_porcentaje}%)")
    print(f"Total a pagar: {total_pagar:.2f} soles")

def ej98():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))

    area = 0.5 * base * altura

    print(f"Área del triángulo: {area:.2f} unidades cuadradas")
    print(f"Base del triángulo: {base} unidades")
    print(f"Altura del triángulo: {altura} unidades")

def ej99():
    cantidad_teclados = int(input("Ingrese la cantidad de teclados comprados: "))

    if cantidad_teclados > 8:
        costo_por_teclado = 10
    elif 4 <= cantidad_teclados <= 8:
        costo_por_teclado = 11
    else:
        costo_por_teclado = 15

    costo_total = cantidad_teclados * costo_por_teclado

    print(f"Número de teclados: {cantidad_teclados}")
    print(f"Costo por teclado: {costo_por_teclado} soles")
    print(f"Costo total a pagar: {costo_total} soles")

def ej100():
    numero = int(input("Ingrese un número entero de dos cifras: "))

    if 10 <= numero <= 99:
        unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
        decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]

        unidad = numero % 10
        decena = numero // 10

        if decena == 1 and unidad > 0:
            numero_en_letras = f"{decenas[decena]} y {unidades[unidad]}"
        else:
            numero_en_letras = f"{decenas[decena]} {unidades[unidad]}"

        print(f"El número {numero} en letras es: {numero_en_letras}")
    else:
        print("Error: Ingrese un número entero de dos cifras.")


def mostrar_menu():
    print("Seleccione un ejercicio (1-100):")

while True:
    mostrar_menu()
    
    try:
        seleccion = int(input("Ingrese el número del ejercicio (o 0 para salir): "))
        
        if seleccion == 0:
            break
        elif 1 <= seleccion <= 100:
            nombre_funcion = f"ej{seleccion}"
            globals()[nombre_funcion]()
        else:
            print("Número no válido. Intente de nuevo.")
    except ValueError:
        print("Por favor, ingrese un número entero.")

