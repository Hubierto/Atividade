from models.enums.unidadefederativa import UnidadeFederativa
class Endereco:

    def __init__(self, logradouro: str, numero:str, complemento: str, cep: str, cidade: str, uf: UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numeero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.UnidadeFederativa =uf
