import numpy as np

def main():
    for i in range(1, 11):
        create_matriz(2 ** i)

def create_matriz(n):
    filename = f"{n}x{n}.txt"
    try:
        with open(filename, 'w') as writer:
            random = np.random.default_rng()
            for _ in range(n):
                for _ in range(n):
                    random_number = random.integers(100000, 999999)  # Generar número aleatorio de 6 dígitos
                    writer.write(f"{random_number:06d}\t")  # Formatear el número como una cadena de 6 dígitos
                writer.write("\n")  # Nueva línea después de cada fila
        print(f"Se ha creado el archivo '{filename}' con una matriz {n}x{n} de números aleatorios.")
    except IOError as e:
        print(f"Error al crear el archivo: {e}")

def leer_matriz(archivo):
    try:
        return np.loadtxt(archivo)
    except IOError as e:
        print(f"Error al leer el archivo: {e}")
        return np.array([])

def guardar_tiempo(nombre_algoritmo, execution_time, fichero):
    try:
        with open("Tiempo_Ejecucion.txt", 'r') as file:
            lines = file.readlines()
        with open("Tiempo_Ejecucion.txt", 'w') as file:
            for line in lines:
                if f"{nombre_algoritmo} [{fichero}]" in line:
                    file.write(f"{nombre_algoritmo} [{fichero}] -> Tiempo: {execution_time} nanosegundos\n")
                else:
                    file.write(line)
        print("La línea ha sido modificada correctamente.")
    except IOError as e:
        print(f"Error al guardar el tiempo: {e}")

if __name__ == "__main__":
    main()
