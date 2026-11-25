# Importações

from Forms.F_HospedeObsDesign import Form 
from typing import TYPE_CHECKING    

if TYPE_CHECKING:
    
    from Forms.F_Principal import F_principal

#--------------------------------- F_HospedeObs -----------------------------------------------------------------------------------/
 
class F_HospedeObs(Form):

    def __init__(self, master, fp: "F_principal"):
       
        self.InicializarComponentes(master)