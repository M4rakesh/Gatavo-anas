import itertools
import datetime
from datetime import time
class car:
    def __init__(self,zimols,modelis,reg_dat,pil_masa,deg_veids):
        self.auto_zimols = zimols
        self.model = modelis
        self.regestr_datums = reg_dat
        self.pilna_masa = pil_masa
        self.degviel_veids = deg_veids
        
    def info_car(self):
        print(f"Zimols: {self.auto_zimols} \n Modelis: {self.model} \n Registracijas datums: {self.regestr_datums}\n Pilna masa: {self.pilna_masa}\n Degvielas veids{self.degviel_veids}")

a=car("Audi","A4","22.10.2019","1800","Bg")
a.info_car()