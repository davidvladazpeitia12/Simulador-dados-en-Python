"""
Módulo: Simulador de Lanzamiento de Dados
Propósito: Aplicación de consola interactiva para simular lanzamientos de dados (D4 a D20).
"""
import random
from rich.console import Console
from rich.panel import Panel
import time
from rich.live import Live

console = Console()

# Constantes para los tipos de dados
D4 = 4
D6 = 6
D8 = 8
D10 = 10
D12 = 12
D20 = 20

total_lanzamientos = 0
total_dados = 0
suma_historica = 0
# Bucle principal del programa
while True:
    print("Lanzador de ddados")
    print("1. Lanzar dados")
    print("2. Estadisticas")
    print("3. Salir")


    opcion = input("Elige una opción (1-3): ")
    if opcion == "3":
            print("hasta pronto")
            break


    elif opcion == "2":
        if total_lanzamientos == 0:
            console.print("[yellow]Aún no hay estadísticas.[/yellow]")
        else:
            promedio_hist = suma_historica / total_dados
            stats = f"Tiradas: {total_lanzamientos}\nDados: {total_dados}\nSuma: {suma_historica}\nPromedio: {promedio_hist:.2f}"
            console.print(Panel(stats, title="[yellow]Estadísticas[/yellow]", expand=False))
       
        break
    elif opcion == "1":
        caras = 0
        while caras == 0:
            try:
                tipo = int(input("Elige el tipo de dado (4, 6, 8, 10, 12, 20): "))
                if tipo == D4:
                    caras = D4
                elif tipo == D6:
                    caras = D6
                elif tipo == D8:
                    caras = D8
                elif tipo == D10:
                    caras = D10
                elif tipo == D12:
                    caras = D12
                elif tipo == D20:
                    caras = D20
                else:
                    print("Tipo de dado no valido")
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

        with Live(refresh_per_second=15) as live:
            for frame in range(12):
                texto_anim = ""
                for i in range(cantidad):
                    texto_anim += str(random.randint(1, caras)) + "   "
                live.update(Panel(f"Lanzando dados\n\n{texto_anim}", title="Lanzazdor", expand=False))
                time.sleep(0.1)

        texto_resultado = ""
        total_tirada = 0
        for i in range(cantidad):
            valor_final = random.randint(1, caras)
            total_tirada += valor_final

            if valor_final == 1:
                color = "red"
            elif valor_final == caras:
                color = "green"
            else:
                color = "yellow"

            texto_resultado += f"[{color}][ {valor_final} ][/{color}]   "

        promedio = total_tirada / cantidad
        resumen = f"{texto_resultado}\n\nTotal: {total_tirada}\nPromedio: {promedio:.2f}"
        console.print(Panel(resumen, title="Resultado Final", expand=False))
        total_lanzamientos += 1
        total_dados += cantidad
        suma_historica += total_tirada
    else:
        print("Opción no válida.")
        