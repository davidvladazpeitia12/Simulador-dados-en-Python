"""
Módulo: Simulador de Lanzamiento de Dados
Propósito: Aplicación de consola interactiva para simular lanzamientos de dados (D4 a D20).
"""

# Bucle principal del programa
while True:
    print("Lanzador de ddados")
    print("1. Lanzar dados")
    print("2. Salir")
    
    opcion = input("Elige una opción (1-3): ")
    
    if opcion == "2":
        print(" Hasta pronto.")
        break
    elif opcion == "1":
        print("Vamos a lanzar...")
    else:
        print("Opción no válida.")