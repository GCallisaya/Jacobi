def jacobi(A, b, tol=1e-10, max_iterations=1000):
    """
    Resuelve el sistema de ecuaciones Ax = b usando el método de Jacobi.

    Parámetros:
    A -- Matriz de coeficientes (nxn) como una lista de listas.
    b -- Vector de constantes (n) como una lista.
    tol -- Tolerancia para la convergencia.
    max_iterations -- Número máximo de iteraciones permitidas.

    Retorna:
    x -- Solución aproximada del sistema.
    """
    n = len(b)
    x = [0.0] * n  # Inicializar x en cero
    x_old = [0.0] * n

    for iteration in range(max_iterations):
        for i in range(n):
            # Calcula la suma de los términos conocidos
            sum1 = sum(A[i][j] * x_old[j] for j in range(i))
            sum2 = sum(A[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i][i]

        # Verificar la convergencia
        if all(abs(x[i] - x_old[i]) < tol for i in range(n)):
            print(f"es convergente")
            return x

        x_old[:] = x
    
    raise Exception("El método de Jacobi no convergió en el número máximo de iteraciones.")

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo de matriz A y vector b
    A = [
        [52, 20, 25],
        [30, 50, 20],
        [18, 30, 55]
    ]
    b = [4800, 5810, 5690]
    
    x = jacobi(A, b)
    print("La solución es:", x)
