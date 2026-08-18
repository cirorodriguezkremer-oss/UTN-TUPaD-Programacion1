print("=" * 40)
print("PROGRAMACIÓN 1")
print("Trabajo Práctico- Repetitivas, Condicionales y Secuenciales")
print("=" * 40)



print("=" * 40)
print("EJERCICIO 1")
print("Caja de Kiosco")
print("=" * 40)


# Pedimos el nombre del cliente
# Se pide antes del while para tener algo que validar
nombre = input("Cliente: ")

# Mientras el nombre este vacío
# se vuelve a pedir
while nombre == "" or not nombre.isalpha():
    print("Error: el nombre debe contener solo letras y no puede estar vacío.")
    nombre = input("Cliente: ")


# Pedimos la cantidad de productos
# Primero lo pedimos como texto para validarlo
# antes de convertilo a número
cantidad_str = input("Cantidad de productos: ")


# .isdigit() valida que sea un número entero
# int(cantidad_str) == 0 valida que no haya puesto 0
while not cantidad_str.isdigit() or int(cantidad_str) == 0:
    print("Error: ingrese un número entero mayor a 0.")
    cantidad_str = input("Cantidad de productos: ")

# Una vez validado, se convierte a entero
cantidad = int(cantidad_str)

total_sin_descuento = 0
total_con_descuento = 0.0

# Cargamos cada producto
for i in range(1, cantidad + 1):
    # Precio: se pide como texto para validar antes de convertirlo
    precio_str = input(f"Producto {i} - Precio: ")
    while not precio_str.isdigit():
        print("Error: el precio debe ser un número entero.")
        precio_str = input (f"Producto {i} - Precio: ")
    precio = int(precio_str)

    # Descuento: acepta S o N, mayúsculas/minúsculas
    descuento = input("Descuento (S/N): ")
    while descuento.lower() not in ("s", "n"):
        print("Error: ingrese S o N.")
        descuento = input("Descuento (S/N): ")

    # Acumular totales
    total_sin_descuento += precio
    if descuento.lower() == "s":
        precio_final = precio * 0.9  # aplica 10% de descuento
    else:
        precio_final = precio
    total_con_descuento += precio_final


# Mostramos los resultados
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print()
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")




print("=" * 40)
print("EJERCICIO 2")
print("Acceso al campus y menú seguro")
print("=" * 40)

# Definimos credenciales fijas
usuario_correcto = "alumno"
clave_correcta = "python123"

# bandera para saber si logro entrar
acceso = False

for intento in range(1, 4): # 3 intentos: 1, 2, 3
    usuario = input(f"Intento  {intento}/3 - Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
        break # corta el for apenas acierta
    else:
        print("Error: credenciales inválidas.")

# si termino el for sin haber accedido, se agotaron los intentos
if not acceso:
    print("Cuenta bloqueada")


# Menú repetitivo (solo si accedió)
if acceso:
    salir = False

    while not salir:
        print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion_str = input("Opción: ")

        # Debe ser un número
        while not opcion_str.isdigit():
            print("Error: ingrese un número válido.")
            opcion_str = input("Opción: ")

        opcion = int(opcion_str)

        # Validación: debe estar entre 1 y 4
        while opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            opcion_str = input("Opción: ")
            while not opcion_str.isdigit():
                print("Error: ingrese un número válido.")
                opcion_str = input("Opción: ")
            opcion = int(opcion_str)

        # ejecutar la opción elegida
        if opcion == 1:
            print("Inscripto")

        elif opcion == 2:
            nueva_clave = input("Nueva clave: ")

            # validar longitud mínima de 6 caracteres
            while len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres")
                nueva_clave = input("Nueva clave: ")

            confirmacion = input("Confirmar clave: ")

            if nueva_clave == confirmacion:
                clave_correcta = nueva_clave # se actualiza la clave
                print("Clave cambiada con éxito.")
            else:
                print("Error: las claves no coinciden.")

        elif opcion == 3:
        # mensaje motivacional
            print("¡Vos podés, seguí así!")

        elif opcion == 4:
            # salir
            print("Saliendo del sistema...")
            salir = True # corta el while en la próxima vuelta




print("=" * 40)
print("EJERCICIO 3")
print("Agenda de turnos con nombre")
print("=" * 40)


# nombramos el operador (solo letras)
operador = input("Nombre del operador: ")
while operador == "" or not operador.isalpha():
    print("Error: el nombre debe contener solo letras.")
    operador = input("Nombre del operador: ")


# variables de la agenda

lunes1 = ""
lunes2 = ""
lunes3 = "" 
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""


# hacemos el menú repetitivo
salir = False

while not salir:
    print()
    print("1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")

    opcion_str = input("Opción: ")

    # Validamos que sea número
    while not opcion_str.isdigit():
        print("Error: ingrese un número válido.")
        opcion_str = input("Opción: ")

    opcion = int(opcion_str)

    # Validar rango de 1 a 5
    while opcion < 1 or opcion > 5:
        print("Error: opción fuera de rango.")
        opcion_str = input("Opción: ")
        while not opcion_str.isdigit():
            print("Error: ingrese un número válido.")
            opcion_str = input("Opción: ")
        opcion = int(opcion_str)

    if opcion == 1:
        dia_str = input("Día (1=Lunes, 2=Martes): ")
        while not dia_str.isdigit() or int(dia_str) not in (1, 2):
            print("Error: ingrese 1 o 2.")
            dia_str = input("Día (1=Lunes, 2=Martes): ")
        dia = int(dia_str)

        paciente = input("Nombre del paciente: ")
        while paciente == "" or not paciente.isalpha():
            print("Error: el nombre debe contener solo letras.")
            paciente = input("Nombre del paciente: ")

        if dia == 1:
            if paciente in (lunes1, lunes2, lunes3, lunes4):
                print("Error: el paciente ya tiene turno el lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                print(f"Turno reservado: Lunes, {paciente}.")
            elif lunes2 == "":
                lunes2 = paciente
                print(f"Turno reservado: Lunes, {paciente}.")
            elif lunes3 == "":
                lunes3 = paciente
                print(f"Turno reservado: Lunes, {paciente}.")
            elif lunes4 == "":
                lunes4 = paciente
                print(f"Turno reservado: Lunes, {paciente}.")
            else:
                print("Error: no hay turnos disponibles el lunes.")

        else:
            if paciente in (martes1, martes2, martes3):
                print("Error: el paciente ya tiene turno el martes.")
            elif martes1 == "":
                martes1 = paciente
                print(f"Turno reservado: Martes, {paciente}.")
            elif martes2 == "":
                martes2 = paciente
                print(f"Turno reservado: Martes, {paciente}.")
            elif martes3 == "":
                martes3 = paciente
                print(f"Turno reservado: Martes, {paciente}.")
            else:
                print("Error: no hay turnos disponibles el martes.")

    # Cancelar turno
    elif opcion == 2:
        dia_str = input("Día (1=Lunes, 2=Martes): ")
        while not dia_str.isdigit() or int(dia_str) not in (1, 2):
            print("Error: ingrese 1 o 2.")
            dia_str = input("Día (1=Lunes, 2=Martes): ")
        dia = int(dia_str)

        paciente = input("Nombre del paciente: ")
        while paciente == "" or not paciente.isalpha():
            print("Error: el nombre debe contener solo letras.")
            paciente = input("Nombre del paciente: ")

        encontrado = False

        if dia == 1:
            if lunes1 == paciente:
                lunes1 = ""
                encontrado = True
            elif lunes2 == paciente:
                lunes2 = ""
                encontrado = True
            elif lunes3 == paciente:
                lunes3 = ""
                encontrado = True
            elif lunes4 == paciente:
                lunes4 = ""
                encontrado = True

        else:
            if martes1 == paciente:
                martes1 = ""
                encontrado = True
            elif martes2 == paciente:
                martes2 = ""
                encontrado = True
            elif martes3 == paciente:
                martes3 = ""
                encontrado = True

        if encontrado:
            print(f"Turno de {paciente} cancelado.")
        else:
            print("Error: el paciente no tiene turno ese día.")

    # Ver agenda del día
    elif opcion == 3:
        dia_str = input("Día (1=Lunes, 2=Martes): ")
        while not dia_str.isdigit() or int(dia_str) not in (1, 2):
            print("Error: ingrese 1 o 2.")
            dia_str = input("Día (1=Lunes, 2=Martes): ")
        dia = int(dia_str)

        if dia == 1:
            print("Agenda del Lunes:")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")

        else:
            print("Agenda del Martes:")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    # resumen general
    elif opcion == 4:
        ocupados_lunes = (lunes1 != "") + (lunes2 != "") + (lunes3 != "") + (lunes4 != "")
        ocupados_martes = (martes1 != "") + (martes2 != "") + (martes3 != "")

        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print("Resumen general:")
        print(f"Lunes  -> Ocupados: {ocupados_lunes}, Disponibles: {disponibles_lunes}")
        print(f"Martes -> Ocupados: {ocupados_martes}, Disponibles: {disponibles_martes}")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes.")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes.")
        else:
            print("Empate entre Lunes y Martes.")

    # cerrar sistema
    elif opcion == 5:
        print("Cerrando sistema...")
        salir = True


print("=" * 40)
print("EJERCICIO 4")
print("Escape Room: La Bóveda")
print("=" * 40)

# Nombramos nuestro agente
agente = input("Nombre del agente: ")
while agente == "" or not agente.isalpha():
    print("Error: solo se permiten letras.")
    agente = input("Nombre del agente: ")

# Variables iniciales del juego
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

# Variable extra para la relga anti-spam
forzados_seguidos = 0

# Variable para saber si el juego se bloqueó por alarma
bloqueado = False

# ciclo principal del juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:
    print()
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3")
    print("1) Forzar cerradura")
    print("2) Hackear panel")
    print("3) Descansar")

    opcion_str = input("Opción: ")

    # Validamos que sea un número
    while not opcion_str.isdigit():
        print("Error: ingrese un número válido.")
        opcion_str = input("Opción: ")

    opcion = int(opcion_str)

    # Validamos el rango de 1 a 3
    while opcion < 1 or opcion > 3:
        print("Error: opción fuera de rango")
        opcion_str = input("Opción: ")
        while not opcion_str.isdigit():
            print("Error: ingrese un número válido.")
            opcion_str = input("Opción: ")
        opcion = int(opcion_str)

    # Forzamos cerradura
    if opcion == 1:
        forzados_seguidos += 1

        if forzados_seguidos == 3:
            energia -= 20
            tiempo -= 2
            print("La cerradura se trabó por forzarla demasiadas veces seguidas.")
            alarma = True
            forzados_seguidos = 0

        elif energia < 40:
            print("¡Riesgo de alarma! La energía está baja.")
            numero_str = input("Elegí un número (1-3): ")
            while not numero_str.isdigit() or int(numero_str) not in (1, 2, 3):
                print("Error: ingrese un número entre 1 y 3.")
                numero_str = input("Elegí un número (1-3): ")
            numero = int(numero_str)

            energia -= 20
            tiempo -= 2

            if numero == 3:
                print("¡Activaste la alarma!")
                alarma = True
            else:
                cerraduras_abiertas += 1
                print("Cerradura forzada con éxito.")

        else:
            energia -= 20
            tiempo -= 2
            cerraduras_abiertas += 1
            print("Cerradura forzada con éxito.")

    # Hackeamos el panel
    elif opcion == 2:
        forzados_seguidos = 0  
        energia -= 10
        tiempo -= 3

        print("Hackeando el panel...")
        for paso in range(1, 5): 
            codigo_parcial += "A"
            print(f"Progreso: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Código completo! Se abrió una cerradura automáticamente.")

    # Descansar
    elif opcion == 3:
        forzados_seguidos = 0  # corta la racha de "forzar seguidas"
    
        energia += 15
        if energia > 100:
            energia = 100  # tope máximo de energía
    
        tiempo -= 1
    
        if alarma:
            energia -= 10
            print("Descansaste, pero la alarma sigue activa y te quita energía extra.")
        else:
            print("Descansaste y recuperaste energía.")

    # Chequeo de bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado = True
        print("¡ALARMA! El sistema se bloqueó. No lograste abrir la bóveda a tiempo.")

# Evaluar cómo terminó el juego
print()
if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! {agente} logró abrir la bóveda.")
elif bloqueado:
    print(f"DERROTA (bloqueo). {agente} quedó atrapado por la alarma.")
else:
    print(f"DERROTA. {agente} se quedó sin energía o sin tiempo.")


print("=" * 40)
print("EJERCICIO 5")
print("Escape Room: La Arena")
print("=" * 40)

# Configuración del personaje
print("--- BIENVENIDO A LA ARENA ---")
nombre = input("Nombre del Gladiador: ")
while nombre == "" or not nombre.isalpha():
    print("Error: solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

# Inicializamos las estadísticas
vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_ataque_pesado = 15
danio_enemigo = 12
turno_gladiador = True

# Ciclo de combate
print("=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print()
    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion_str = input("Opción: ")

    # Validamos que sea un número
    while not opcion_str.isdigit():
        print("Error: Ingrese un número válido.")
        opcion_str = input("Opción: ")

    opcion = int(opcion_str)

    # Validamos el rango de 1 a 3
    while opcion < 1 or opcion > 3:
        print("Error: opción fuera de rango.")
        opcion_str = input("Opción: ")
        while not opcion_str.isdigit():
            print("Error: Ingrese un número válido.")
            opcion_str = input("Opción: ")
        opcion = int(opcion_str)
    
    # ataque pesado
    if opcion == 1:
        # Si la vida del enemigo es menor a 20, hay golpe crítico
        if vida_enemigo < 20:
            danio_final = danio_ataque_pesado * 1.5 
            print("¡Golpe Crítico!")
        else:
            danio_final = danio_ataque_pesado  

        vida_enemigo -= danio_final
        print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")

    # ráfaga
    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for golpe in range(3):  
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    # curación
    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print(f"Te curaste 30 puntos de vida. Pociones restantes: {pociones}")
        else:
            print("¡No quedan pociones!")

    # Turno del enemigo
    vida_enemigo_estaba_viva = vida_enemigo > 0  # chequeo antes de que ataque

    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")

# Fin del juego
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")

print("=" * 40)
print("PROGRAMACIÓN 1")
print("Trabajo Práctico- Repetitivas, Condicionales y Secuenciales")
print("=" * 40)