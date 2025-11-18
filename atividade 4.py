#1

while True:
    print("\n=== Cálculo de Média do Aluno ===")

    nome = input("Digite o nome do aluno: ")

    n1 = float(input("Digite a 1ª nota: "))
    n2 = float(input("Digite a 2ª nota: "))
    n3 = float(input("Digite a 3ª nota: "))

    media = (n1 + n2 + n3) / 3

    print(f"\nMédia de {nome}: {media:.2f}")

    if media >= 7:
        print("Situação: Aprovado")
    elif 5 <= media < 7:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")

    repetir = input("\nCalcular média de outro aluno? (s/n): ").lower()
    if repetir != "s":
        break

print("\nPrograma encerrado.")

#2

def ler_notas():
    notas = []
    for i in range(1, 4):
        nota = float(input(f"Digite a {i}ª nota: "))
        notas.append(nota)
    return notas


def calcular_media(notas):
    return sum(notas) / len(notas)


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif 5 <= media < 7:
        return "Recuperação"
    else:
        return "Reprovado"


def mostrar_resultado(nome, media, situacao):
    print("\n=== Resultado ===")
    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")


# Fluxo principal
while True:
    nome = input("\nDigite o nome do aluno: ")

    notas = ler_notas()
    media = calcular_media(notas)
    situacao = verificar_situacao(media)

    mostrar_resultado(nome, media, situacao)

    repetir = input("\nCalcular média de outro aluno? (s/n): ").lower()
    if repetir != "s":
        break

print("\nPrograma encerrado.")

#3

def ler_notas():
    notas = []
    for i in range(1, 4):
        nota = float(input(f"Digite a {i}ª nota: "))
        notas.append(nota)
    return notas


def calcular_media(notas):
    return sum(notas) / len(notas)


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif 5 <= media < 7:
        return "Recuperação"
    else:
        return "Reprovado"


def mostrar_resultado(nome, media, situacao):
    print("\n=== Resultado ===")
    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

#4

medias_gerais = []

while True:
    print("\n=== Cálculo de Média do Aluno ===")

    nome = input("Digite o nome do aluno: ")

    notas = ler_notas()
    media = calcular_media(notas)
    situacao = verificar_situacao(media)

    mostrar_resultado(nome, media, situacao)

    medias_gerais.append((nome, media))

    repetir = input("\nCalcular média de outro aluno? (s/n): ").lower()
    if repetir != "s":
        break

print("\n=== Resumo Geral ===")
for aluno, media in medias_gerais:
    print(f"{aluno}: {media:.2f}")

print("\nPrograma encerrado.")