#Computer

class Computer():
    def __init__(self,status = "Off",ovoz = 0,dastur = "Telegram",ochiq_dasturlar = ["Telegram","Syder","OBS Studio"]):
        self.status = status
        self.ovoz = ovoz
        self.dastur = dastur
        self.ochiq_dasturlar = ochiq_dasturlar
    def __str__(self):
        return f""" --- INFO ---
Status: {self.status}
Ovoz: {self.ovoz}
Ishlatilinayotgan dastur: {self.dastur}
Ochiq dasturlar: {self.ochiq_dasturlar}"""
    def __len__(self):
        return len(self.ochiq_dasturlar)
    def comp_on_off_(self):
        if(self.status == "Off"):
            self.status = "On"
            print("Computer Yoqildi!!!")
        elif(self.status == "On"):
            self.status = "Off"
            print("Computer ochirildi!!!")
            
    def ovoz_ozgartir(self):
        while(True):
            belgi = input("+ | -:")
            if(belgi == "+"):
                if(self.ovoz <10):
                    self.ovoz += 1
                print("Ovoz holati: ",self.ovoz)
            elif(belgi == "-"):
                if(self.ovoz > 0):
                    self.ovoz -= 1
                    print("Ovoz holati: ",self.ovoz)
            else:
                print("Ovoz holati yangilandi...")
                break
    def dastur_och(self):
        yangiDastur = input("Dastur nomi: ")
        if(len(yangiDastur) != 0 and yangiDastur != " "):
            self.ochiq_dasturlar.append(yangiDastur)
            print(f"{yangiDastur} muvaffaqiyatli ochildi !")
    def dastur_ozgartir(self):
        belgi = input("Qaysi dasturga o'tay: ")
        if(belgi in self.ochiq_dasturlar):
            a = self.ochiq_dasturlar.index(belgi)
            self.dastur = self.ochiq_dasturlar[a]
            print(self.dastur,"Dasturga o'tildi!")
        else:
            print("Bunaqa dastur mavjud emas!")
print("""--- Computer ---

1. Computer On/Off
2. Show Info
3. Ovoz Ozgartirish
4. Dasturni Ochish
5. Dasturni O'zgartirish
6. Ochiq dasturlar sonini ko'rish

Chiqish -> 'q'  """)
c = Computer()

while True:
    tanlov = input("Tanlang: ")
    if(tanlov == '1'):
        c.comp_on_off_()
    elif(tanlov == '2'):
        print(c)
    if(c.status == "On"):
        if(tanlov == '3'):
            c.ovoz_ozgartir()
        elif(tanlov == '4'):
            c.dastur_och()
        elif(tanlov == '5'):
            c.dastur_ozgartir()
        elif(tanlov == '6'):
            print(len(c),"ta dastur mavjud!")
        elif(tanlov == 'q'):
            print("Computer To'xtatildi!!!")
            break
    elif(c.status != "On" and tanlov != "1"):
        print("Computerni yoqing!")
    else:
        print("Noto'g'ri tanlov!")