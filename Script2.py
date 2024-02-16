class Nodo:
    """
    Representa un nodo dentro de un árbol.
    Cada nodo contiene un valor a hijo izquierdo y derecho.
    """
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioOrdenado:
    """
    Árbol binario que mantiene elementos ordenados.
    """
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        """
        Recursivamente encuentra lugar y agrega valor.
        """
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar(valor, self.raiz)

    def _agregar(self, valor, nodo):
        """
        Recursivamente encuentra lugar y agrega valor.
        """
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._agregar(valor, nodo.izquierdo)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._agregar(valor, nodo.derecho)

    def recorrido_preorden(self):
        """
        Realiza un recorrido preorden del árbol, retornando una lista con los valores.
        """
        elementos = []
        self._recorrido_preorden(self.raiz, elementos)
        return elementos

    def _recorrido_preorden(self, nodo, elementos):
        """
        Método auxiliar recursivo para recorrido preorden.
        
        :param: El nodo actual en la recursión.
        :param: Lista acumulativa de elementos recorridos.
        """
        if nodo:
            elementos.append(nodo.valor)
            self._recorrido_preorden(nodo.izquierdo, elementos)
            self._recorrido_preorden(nodo.derecho, elementos)

    def recorrido_inorden(self):
        """
        Realiza un recorrido inorden del árbol, retornando una lista con los valores.
        """
        elementos = []
        self._recorrido_inorden(self.raiz, elementos)
        return elementos

    def _recorrido_inorden(self, nodo, elementos):
        """
        Método auxiliar recursivo para recorrido inorden.
        :param: El nodo actual en la recursión.
        :param: Lista acumulativa de elementos.
        """
        if nodo:
            self._recorrido_inorden(nodo.izquierdo, elementos)
            elementos.append(nodo.valor)
            self._recorrido_inorden(nodo.derecho, elementos)

    def recorrido_postorden(self):
        """
        Realiza un recorrido postorden del árbol, retornando una lista con los valores.
        """
        
        elementos = []
        self._recorrido_postorden(self.raiz, elementos)
        return elementos

    def _recorrido_postorden(self, nodo, elementos):
        """
        Método auxiliar recursivo para recorrido postorden.
        
        :param: El nodo actual en la recursión.
        :param: Lista acumulativa de elementos.
        """
        if nodo:
            self._recorrido_postorden(nodo.izquierdo, elementos)
            self._recorrido_postorden(nodo.derecho, elementos)
            elementos.append(nodo.valor)

def contar_valles(caminata):
    """
    Cuenta el número de valles en la caminata del caminante.
    Un valle empieza cuando el caminante desciende bajo el nivel del mar y termina cuando regresa a él.
    
    :param caminata: Cadena que representa la caminata, compuesta por 'U' (subida) y 'D' (bajada).
    :return: Verdadero si el proceso fue exitoso, Falso si hubo un error en la entrada.
    """
    
    nivel = 0
    valles = 0
    en_valle = False

    for paso in caminata:
        if paso == 'U':
            nivel += 1
        else:
            nivel -= 1

        if nivel == 0 and en_valle:
            valles += 1
            en_valle = False
        elif nivel < 0 and not en_valle:
            en_valle = True

    return valles

def main():
    # Caso de uso de la función contar_valles
    print("Demostración de contar valles")
    caminata = "DDUDUDUUDDUDUDUU"
    valles = contar_valles(caminata)
    print(f"La caminata '{caminata}' tiene {valles} valles.\n")

    # Creación y manipulación del árbol binario ordenado
    print("Demostración del Árbol Binario Ordenado")
    arbol = ArbolBinarioOrdenado()
    elementos = [10, 5, 15, 2, 7, 12, 18, 1, 3, 6, 8, 11, 13, 17, 20]
    print(f"Agregando elementos al árbol: {elementos}")
    for elemento in elementos:
        arbol.agregar(elemento)

    # Realizar recorridos en el árbol
    print("Recorrido Preorden:", arbol.recorrido_preorden())
    print("Recorrido Inorden:", arbol.recorrido_inorden())
    print("Recorrido Postorden:", arbol.recorrido_postorden())

if __name__ == "__main__":
    main()

