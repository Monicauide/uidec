INICIO
  saldo ← 1000
  repetir
    mostrar "1. Consultar saldo"
    mostrar "2. Retirar dinero"
    mostrar "3. Depositar dinero"
    mostrar "4. Salir"
    leer opcion

    SI opcion = 1 ENTONCES
      mostrar "Saldo actual: ", saldo
    SINO SI opcion = 2 ENTONCES
      mostrar "Ingrese monto a retirar:"
      leer retiro
      SI retiro > saldo ENTONCES
        mostrar "Fondos insuficientes"
      SINO
        saldo ← saldo - retiro
        mostrar "Retiro exitoso"
      FIN SI
    SINO SI opcion = 3 ENTONCES
      mostrar "Ingrese monto a depositar:"
      leer deposito
      saldo ← saldo + deposito
      mostrar "Depósito exitoso"
    FIN SI
  hasta que opcion = 4
FIN
🔁 Diagrama de flujo
(Descripción textual del diagrama de flujo para representar visualmente)

Inicio

Inicializar saldo = 1000

Mostrar menú

Leer opción

IF opción = 1 → mostrar saldo

IF opción = 2 → leer retiro → ¿retiro > saldo?

Sí → “Fondos insuficientes”

No → saldo = saldo - retiro

IF opción = 3 → leer depósito → saldo = saldo + depósito

IF opción ≠ 4 → volver a menú

Fin si opción = 4

(Si necesitas el diagrama como imagen, te lo puedo generar en PNG.)

🐍 Código en Python
python
Copiar
Editar
# Cajero automático básico

saldo = 1000

while True:
    print("\n--- MENÚ CAJERO AUTOMÁTICO ---")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        print(f"Su saldo actual es: ${saldo}")
    elif opcion == "2":
        retiro = float(input("Ingrese el monto a retirar: "))
        if retiro > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= retiro
            print(f"Retiro exitoso. Saldo restante: ${saldo}")
    elif opcion == "3":
        deposito = float(input("Ingrese el monto a depositar: "))
        saldo += deposito
        print(f"Depósito exitoso. Saldo actual: ${saldo}")
    elif opcion == "4":
        print("Gracias por usar el cajero. ¡Hasta pronto!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
