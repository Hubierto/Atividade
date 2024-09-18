from models.enums.Sexo import Sexo
from models.fisica import Fisica

class Cliente(Fisica):

    def __init__(self, nome: str, telefone: str, email: str, endereco: str, cpf: str, rg: str, datanascimento: str, sexo: Sexo, protocoloAtendimento: int) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, datanascimento, sexo)
        self.protocoloAtendimento = protocoloAtendimento

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nProtocolo atendimento: {self.protocoloAtendimento}")    
