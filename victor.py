import sys, ast

def correction_QCM_alice(reponse_Alice, reponses_valides):
    points = 0
    rep_fausses=[]
    for i in reponses_valides:
        if reponse_Alice[i] == reponses_valides.get(i): #regarde pour chaque question ça réponse et les compare avec reponses_valides 
            points+=3 #rajoute +1 points pour chaque bonne réponse
        elif reponse_Alice[i] != reponses_valides.get(i):
            rep_fausses.append(i)
            points-=1
    print(f'Réponses fausses: {rep_fausses}')
    print(f'Votre résultat est: {points}')


#utiliser la fonction dans le terminal 'cmd'
#cmd.exe-> py victor.py correction_QCM_alice {'Q1':'b','Q2':'a','Q3':'d','Q4':'c','Q5':'a'} {'Q1':'c','Q2':'a','Q3':'d','Q4':'c','Q5':'b'}
def main():
    if len(sys.argv) <= 2:
        print("Il vous manque quelque chose.")
    else:
        function = sys.argv[1]
        if function == "correction_QCM_alice":
            if len(sys.argv) < 4:
                print(sys.argv[2])
            else:

                print(f"Votre réponse: {ast.literal_eval(sys.argv[2])}") #ast convertis le string du dict en un dict
                rep1=ast.literal_eval(sys.argv[2])
                rep2=ast.literal_eval(sys.argv[3])
                correction_QCM_alice(rep1, rep2)


if __name__ == '__main__':
    main()
