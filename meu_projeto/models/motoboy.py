from meu_projeto.models.enums.Sexo import Sexo
from meu_projeto.models.enums.setor import Setor
from models.funcionario import Funcionario

class Motoboy(Funcionario):
    BONIFICACAO = 2.0

    def __init__(self, nome: str, telefone: str, email: str, endereco: str, cpf: str, rg: str, datanascimento: str, sexo: Sexo, matricula: str, setor: Setor, salario: float, cnh: str) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, datanascimento, sexo, matricula, setor, salario)
        self.cnh = cnh

    def salarioFinal(self) -> float:
        resultado = self.salarioFinal * self.BONIFICACAO
        return resultado    
    
    def __str__(self) -> str:
        return (
                f"{super().__str__()}"
                f"\nCNH: {self.cnh}")