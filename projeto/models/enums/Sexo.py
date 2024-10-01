from enum import Enum

class Sexo(Enum):

    MASCULINO = ("Masculino", "M")
    FEMININO  = ("Feminino", "F") 

    def __init__(self, caractere, texto) -> None:
        super().__init__()
        self.texto = texto
        self.caractere = caractere

    def __str__(self):
        return f"{self.texto} | ({self.caractere})" 

