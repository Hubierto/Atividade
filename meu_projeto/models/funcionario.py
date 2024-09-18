from abc import ABC, abstractmethod
from models.enums.Sexo import Sexo
from models.fisica import Fisica
from models.enums.setor import Setor

class Funcionario(Fisica, ABC):

    def __init__(self, nome: str, telefone: str, email: str, endereco: str, cpf: str, rg: str, datanascimento: str, sexo: Sexo, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, datanascimento, sexo)
        self.matricula = matricula
        self.setor = Setor
        self.salario = salario

    @abstractmethod
    def salarioFinal(self) -> float:
        pass    


    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nNome: {self.nome}" 
                f"\nTelefone: {self.telefone}" 
                f"\nE-mail: {self.email}"
                f"\nEndereço: {self.endereco}"  
                f"\nCPF: {self.cpf}"   
                f"\nRG: {self.rg}"    
                f"\nData de nascimento: {self.dataNascimento}"    
                f"\nSexo: {self.sexo}"
                f"\nMatricula: {self.matricula}"
                f"\nSetor: {self.setor}"
                f"\nSalário: {self.salario}")
    