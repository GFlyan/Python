class Nacionalidade:
    def __init__(self, estado, pais):
        self.estado = estado
        self.pais = pais

class Pessoa:
    def __init__(self, endereco: Nacionalidade):
        self.endereco = endereco

