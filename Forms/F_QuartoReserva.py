
#importações

from Forms.F_QuartoReservaDesign import Form
from typing import TYPE_CHECKING    

if TYPE_CHECKING:
    
    from Forms.F_Principal import F_principal

class F_QuartoReserva(Form):

    def __init__(self, master, fp: "F_principal"):
       
        self.InicializarComponentes(master)
        
        self.F_Reserva.wait_window()











