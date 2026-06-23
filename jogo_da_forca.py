import random

print("========== JOGO DA FORCA ==========")

palavras = ["GATINHOS", "COMPUTADOR", "PENSAMENTOS"]

def iniciar_jogo():
     """Escolhe a palavra e cria os dados iniciais do jogo."""

     palavra_sorteada = random.choice(palavras)
     palavra_escondida = ["_"] * len(palavra_sorteada)
     letras_tentadas = set()  # Escolhi set porque ele não permite duplicação de letras e torna a verificação de letras já tentadas mais eficiente.
     vidas = 6
     
     return palavra_sorteada, palavra_escondida, letras_tentadas, vidas

def processar_tentativa(letra, palavra_sorteada, palavra_escondida, letras_tentadas, vidas):
    """Verifica a letra e atualiza o jogo."""

    if letra in letras_tentadas:
        print("Você já tentou essa letra!")
        return palavra_escondida, letras_tentadas, vidas

    letras_tentadas.add(letra)

    if letra in palavra_sorteada:
        for i in range(len(palavra_sorteada)):
            if palavra_sorteada[i] == letra:
                palavra_escondida[i] = letra
        print("Acertou!")
    else:
        vidas -= 1
        print("Errou!")

    return palavra_escondida, letras_tentadas, vidas

palavra_sorteada, palavra_escondida, letras_tentadas, vidas = iniciar_jogo()


while vidas > 0 and "_" in palavra_escondida:

    print("\nPalavra:", " ".join(palavra_escondida))
    print("Tentativas:", letras_tentadas)
    print("Vidas:", vidas)

    letra = input("Digite uma letra: ").upper()

    palavra_escondida, letras_tentadas, vidas = processar_tentativa(
        letra,
        palavra_sorteada,
        palavra_escondida,
        letras_tentadas,
        vidas
    )

if "_" not in palavra_escondida:
    print("\nVocê venceu! A palavra era:", palavra_sorteada)
else:
    print("\nVocê perdeu! A palavra era:", palavra_sorteada)