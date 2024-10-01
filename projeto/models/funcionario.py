from abc import ABC, abstractmethod
from models.enums.Sexo import Sexo
from models.fisica import Fisica
from models.enums.setor import Setor
from models.endereco import Endereco

class Funcionario(Fisica, ABC):

    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, datanascimento: str, sexo: Sexo, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, datanascimento, sexo)
        self.matricula = matricula
        self.setor = Setor
        self.salario = salario

    @abstractmethod
    def salarioFinal(self) -> float:
        pass    


    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nMatricula: {self.matricula}"
                f"\nSetor: {self.setor}"
                f"\nSalário: {self.salario}"
                f"\nSalário final: {self.salarioFinal}")