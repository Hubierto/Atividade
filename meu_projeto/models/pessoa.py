from abc import ABC

class Pessoa(ABC):

    def __init__(self, nome: str, telefone: str, email: str, endereco: str) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        return  (
                 f"Nome: {self.nome}"
                 f"telefone: {self.telefone}"
                 f"E-mail: {self.email}"
                 f"Endereço: {self.endereco}")
       

 