from meu_projeto.models.enums.Sexo import Sexo
from models.fisica import Fisica

class Cliente(Fisica):

    def __init__(self, nome: str, telefone: str, email: str, endereco: str, cpf: str, rg: str, datanascimento: str, sexo: Sexo, protocoloAtendimento: int) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, datanascimento, sexo)
        self.protocoloAtendimento = protocoloAtendimento

    def __str__(self) -> str:
        return (
                f"\nNome: {self.nome}" 
                f"\nTelefone: {self.telefone}" 
                f"\nE-mail: {self.email}"
                f"\nEndereço: {self.endereco}"  
                f"\nCPF: {self.cpf}"   
                f"\nRG: {self.rg}"    
                f"\nData de nascimento: {self.dataNascimento}"    
                f"\nSexo: {self.sexo}"
                f"\nProtocolo atendimento: {self.protocoloAtendimento}")    
