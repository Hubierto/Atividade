from models.enums.Sexo import Sexo
from models.enums.setor import Setor
from models.funcionario import Funcionario

class Medico(Funcionario):
    BONIFICACAO = 0.5

    def __init__(self, nome: str, telefone: str, email: str, endereco: str, cpf: str, rg: str, datanascimento: str, sexo: Sexo, matricula: str, setor: Setor, salario: float, crm: str) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, datanascimento, sexo, matricula, setor, salario)
        self.crm = crm

    def salarioFinal(self) -> float:
        resultado = self.salarioFinal * self.BONIFICACAO
        return resultado

    def __str__(self) -> str:
        return (
                f"{super().__str__()}"
                f"\nCRM: {self.crm}")