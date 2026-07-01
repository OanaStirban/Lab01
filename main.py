import random
class Punteggio:
    def __init__(self,nickname,punteggio):
        self.nickname = nickname
        self.punteggio = int(punteggio)

class Domanda:
    def __init__(self, domanda, difficolta,risposta_giusta, risposte_sbagliate):
        self.domanda=domanda
        self.difficolta=int(difficolta)
        self.risposta_giusta=risposta_giusta
        self.risposte=risposte_sbagliate
        self.risposte.append(self.risposta_giusta)
        random.shuffle(self.risposte)
    def print(self):
        print(f"Livello {self.difficolta}) {self.domanda}")
        for i, r in enumerate(self.risposte):
            print(f"\t{i + 1}. {r}")

    def giusta(self,numero):
        if 4 >= numero > 0:
            r = self.risposte[numero-1]
            return r == self.risposta_giusta
        else:
            return False
    def indice_giusta(self):
        return self.risposte.index(self.risposta_giusta)+1

domande = []
score = 0
with open("domande.txt") as dom:
    i = 0
    domanda=[]
    for line in dom:
        if i < 6:
            i+=1
            domanda.append(line.strip())
        elif i==6:
            i=0
            d = Domanda(domanda[0],domanda[1],domanda[2],domanda[3:])
            domande.append(d)
            domanda.clear()


domande.sort(key=lambda do: do.difficolta)

domandedict ={}
for d in domande:
    if d.difficolta in domandedict:
        domandedict[d.difficolta].append(d)
    else:
        domandedict[d.difficolta] = [d]
diff_curr = 0
while True:
    if diff_curr in domandedict:
        listacorrente = domandedict[diff_curr]
        g = random.choice(listacorrente)
        diff_curr+=1
        g.print()
        risp_utente= int(input("Inserisci la risposta corretta: "))

        if g.giusta(risp_utente):
            print("Risposta corretta!")
            diff_ult=g.difficolta
            score+=1
        else:
            print(f"Risposta sbagliata! La risposta corretta era: {g.indice_giusta()}")
            break

    else:
        break

print(f"Hai totalizzato {score} punti!")
nickname = input("Inserisci il tuo nickname: ")
s=[]

with open("punti.txt") as p:
    for line in p:
        gesu = line.strip().split(" ")
        punt = Punteggio(gesu[0],gesu[1])
        s.append(punt)

s.append(Punteggio(nickname,score))
s.sort(key=lambda p: p.punteggio, reverse=True)

with open("punti.txt", "w") as p:
    for i in s:
        p.write(f"{i.nickname} {i.punteggio} \n")