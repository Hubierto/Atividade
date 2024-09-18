from models.pessoa import Pessoa
class Juridica(Pessoa):

   def __init__(self, nome: str, telefone: str, email: str, endereco: str, cnpj: str, inscricaoEstadual: str) -> None:
      super().__init__(nome, telefone, email, endereco)
      self.cnpj = cnpj
      self.inscricaoEstadual = inscricaoEstadual

   def __str__(self) -> str:
      return(
            f"{super().__str__()}"
            f"\nCnpj: {self.cnpj}"
            f"\nInscrição Estadual: {self.inscricaoEstadual}"
            ) 
    
   
