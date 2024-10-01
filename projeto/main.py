import os
from models.juridica import Juridica
from models.medico import Medico
from models.enums.Sexo import Sexo
from models.enums.setor import Setor
import sys
sys.path.append


os.system("cls || clear")
juridica1 = Juridica("a", "0", "@", "...", "123", "999")
medico1 = Medico("a","1","a","a","1","a","a",Sexo.FEMININO,"a",Setor.ENGENHARIA, 2.000, "a")

print(medico1)
print(juridica1)
