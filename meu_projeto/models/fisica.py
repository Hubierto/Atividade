from models.enums.Sexo import Sexo
from models.pessoa import Pessoa
from abc import ABC

class Fisica(ABC, Pessoa):

    def __init__(self, nome: str, telefone: str, email: str, endereco: str, cpf: str, rg: str, datanascimento: str, sexo: Sexo) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf
        self.rg = rg
        self.dataNascimento = datanascimento
        self.sexo = Sexo

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCPF: {self.cpf}"   
                f"\nRG: {self.rg}"    
                f"\nData de nascimento: {self.dataNascimento}"    
                f"\nSexo: {self.sexo}")    

