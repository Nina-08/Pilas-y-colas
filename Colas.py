from collections import deque

class Cola:
    def __init__(self):
        self.items = deque()

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.popleft()

    def ver_frente(self):
        if not self.esta_vacia():
            return self.items[0]


# Ejemplo de uso
cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)

print("Frente de la cola:", cola.ver_frente())  # Salida: 1

print("Desencolando elementos:")
while not cola.esta_vacia():
    print(cola.desencolar())  # Salida: 1 2 3
