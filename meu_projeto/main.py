import os
from models.cliente import Cliente

from models.enums.Sexo import Sexo



os.system("cls||clear")
cliente1 = Cliente("A", "1", "a", "0", "1", "0", "01", Sexo.MASCULINO, 000)

print(cliente1)