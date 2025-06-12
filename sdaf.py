alfabets='AĀBCČDĒEFGĢHIĪJKĶLĻMNŅOPRSŠTUŪVZŽ'
alfabets1=list(alfabets)

s=[]

while True:
    vards= input("Ievadit vardu: ")
    if vards == '':
        break
    if vards[0].isupper() and vards.isalpha():
        s.append(vards)
    else:
        print("Ievadiet atbilstošu cilvēka vārdu!")

s.sort(alfabets)

print(f"Vārdi alfabēta secība:{s}")
#for i in s:asdfsd