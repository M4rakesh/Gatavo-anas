class kubs:
    def __init__(self,malas_garums,kraasas_nosaukums):
        self.mal_g = malas_garums
        self.kraasa= kraasas_nosaukums
    
    def aprekinat_tilpumu(self):
        if self.mal_g in range(2,11):
            self.v = self.mal_g**3
            print(f"{self.v} kubikcentemetri")
        else:
            print("Kuba malas neatrodas intervala 2-10cm.")
        
    def likvide(self):
        print(f"Tik izdests kubs, kura krāsa ir {self.kraasa}")

    def info(self):
        print(f"Kuba īpašības\n Malas garums: {self.mal_g} \n krasa: {self.kraasa}\n Kuba tilpums: {self.v}") 
class Bloks(kubs):
    def __init__(self,malas_garums,kraasas_nosaukums,kubu_skaits,forma):
        super().__init__(malas_garums, kraasas_nosaukums)
        self.forma = forma
        self.kubu_skaits = kubu_skaits
        if kubu_skaits in range(1,5):
            self.__kubu_skaits = kubu_skaits
            self.nosaukums = str(self.kraasa + str(self.__kubu_skaits))
            print(self.nosaukums)
        else:
            print("Neatbilst nosacijumiem")
            self.__kubu_skaits = kubu_skaits
            self.nosaukums = str(self.kraasa + str(self.__kubu_skaits))
            print(self.nosaukums)

    def nosaukums_funk(self):
        self.nosaukums = str(self.kraasa + str(self.__kubu_skaits))
        print(self.nosaukums)    

    def der_funk(self):
        if self.forma in [11,12,13,14,22]:
            self.derigums = 0
            print(self.derigums)
        else:
            self.derigums = 1
            print(self.derigums)

    def bloka_tilpums(self):
        if self.mal_g in range(2,11):
            self.v = self.mal_g**3
        else:
            self.v = 2**3
        self.v_bloka = self.v * self.__kubu_skaits
        print(self.v_bloka)


kubg=kubs(10,"zaļš")
kubr=kubs(1,"sarkans")
kubg.aprekinat_tilpumu()
print(kubg.kraasa)
print(kubr.mal_g)
kubr.likvide()
kubr.aprekinat_tilpumu()
print(kubg.mal_g)

objekts1=Bloks(5,"oranžs",3,13)
objekts1.nosaukums_funk()
objekts1.bloka_tilpums()

objekts2=Bloks(7,"zils",5,23)
objekts2.nosaukums_funk()
objekts2.der_funk()

objekts3=Bloks(7,"zils",5,12)
objekts3.nosaukums_funk()
objekts3.der_funk()