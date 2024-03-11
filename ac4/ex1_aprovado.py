def ler_nome():
    return input("Informe o seu nome: ")


def ler_notas():
    ap1 = float(input("Inrira a sua nota da AP1: "))
    ap2 = float(input("Insira a sua nota da AP2: "))
    asub = float(input("Inria a sua nota da AS: "))
    ac = float(input("Insira a sua nota da AC: "))
    return ap1, ap2, asub, ac


def notas_sao_validas(ap1, ap2, asub, ac):
    if ap1 > 0 and ap1 < 10:
        return True
    if ap2 > 0 and ap2 < 10:
        return True
    if asub > 0 and asub < 10:
        return True
    if ac > 0 and ac < 10:
        return True
    return False


def duas_maiores_notas(ap1, ap2, asub):
    if asub > ap1 or asub > ap2:
        if ap1 > ap2 and asub >= ap2:
            ap2 = asub
            return ap1, ap2
        if ap1 < ap2 and asub >= ap1:
            ap1 = asub
            return ap1, ap2
        if ap1 == ap2 and asub >= ap1:
            return ap1, asub
    return ap1, ap2
        

def calcular_media(prova1, prova2, ac):
    return (prova1 + prova2) * 0.4 + ac * 0.2


def aluno_foi_aprovado(media):
    return media >= 7


def main():
    nome = ler_nome()
    if nome: 
        ap1, ap2, asub, ac = ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            prova1, prova2 = duas_maiores_notas(ap1, ap2, asub)
            media = calcular_media(prova1, prova2, ac)
            if aluno_foi_aprovado(media):
                print(f"Parabéns {nome}, você foi aprovado! sua média final é {media}")
            else:
                print("Aluno foi reprovado!")

main()
