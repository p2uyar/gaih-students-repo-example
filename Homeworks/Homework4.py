import random as rnd
RandomQuestion1=["ayva","çilek","karpuz","lamba","ayna"]
RandomQuestion2=["Kapı Kolu","Makyaj Aynası","Av Tüfeği","Trafik Lambası"]
class HangMan:
    def __init__(self, question):
        self.question = question.upper()
        self.life = 11
        self.answer = []
        self.result = False
        self.template_add()

    def template_add(self):
        for i in self.question:
            if i == " ":
                self.answer.append(i)
            else:
                self.answer.append("_")


    def answer_add(self, letter):
        index = 0
        letter=letter.upper()
        check = letter in self.question
        if check == True:
            for i in range(len(self.question)):
                if letter == self.question[i]:
                    self.answer[i] = letter
            print(self.answer)
        else:
            self.wrong_answer()

    def guess_add(self,guess):
        if self.question == guess.upper():
            self.result = True
        else:
            self.wrong_answer()

    def wrong_answer(self):
        self.life = self.life-1
        if self.life == 0:
            print("Üzgünüz Kaybettiniz. Doğru Cevap: ",self.question)
            self.result = True
        else:
            print("Yanlış cevap! Kalan Hakkınız:", self.life)

menu = """
(1) Yeni Oyun
(2) Çık
"""
game = """
        (1) Tek Kişilik
        (2) İki Kişilik
        """
level = """
        (1) Kolay
        (2) Zor
        """
while True:
    print(menu)
    mchoice = input("Seçiniz: ")
    if mchoice == "1":
        print(game)
        multiple = input("Seçiniz: ")
        if multiple == "1":
            print(level)
            easy = input("Seçiniz: ")
            if easy == "1":
                question=rnd.choice(RandomQuestion1)

            if easy == "2":
                question = rnd.choice(RandomQuestion2)
            man = HangMan(question)

        if multiple == "2":
            question = input("Tahmin edilecek kelimeyi giriniz: ")
            man = HangMan(question)

        answer = ""
        while (man.result != True):
            if man.life == 1:
                answer = input("Son Hakkınız Tahmin giriniz: ")
                man.guess_add(answer)
            else:
                choice = input("1.Harf mi?\n2.Tahmin mi? : ")
                if choice == "1":
                    answer = input("Harf giriniz: ")
                    man.answer_add(answer)
                if choice == "2":
                    answer = input("Tahmin giriniz: ")
                    man.guess_add(answer)
                    if man.result == True:
                        print("Tebrikler! Doğru Cevap")
    if mchoice == "2":
        print("Güle Güle")
        break







