"""
Módulo: Simulador de Lanzamiento de Dados
Propósito: Aplicación de consola interactiva para simular lanzamientos de dados (D4 a D20).
"""
import random

# Constantes para los tipos de dados
D4 = 4
D6 = 6
D8 = 8
D10 = 10
D12 = 12
D20 = 20

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
        caras = 0
        while caras == 0:
            try:
                tipo = int(input("Elige el tipo de dado (4, 6, 8, 10, 12, 20): "))
                if tipo == D4: caras = D4
                elif tipo == D6: caras = D6
                elif tipo == D8: caras = D8
                elif tipo == D10: caras = D10
                elif tipo == D12: caras = D12
                elif tipo == D20: caras = D20
                else: print("Tipo de dado no valido")
            except ValueError:
                print("Error: Debes introducir un número entero")
                cantidad = 0
        while cantidad <= 0:
            try:
                cantidad = int(input("¿Cuántos dados quieres lanzar?: "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor que 0")
            except ValueError:
                print("Error: Debes introducir un número entero.")
                texto_resultado = ""
        total_tirada = 0
        
        for i in range(cantidad):
            valor_final = random.randint(1, caras)
            total_tirada += valor_final
            texto_resultado += f"[ {valor_final} ]   "
            
        promedio = total_tirada / cantidad
        print(f"Resultados: {texto_resultado}")
        print(f"Total: {total_tirada} | Promedio: {promedio:.2f}")
       
    else:
        print("Opción no válida.")
        