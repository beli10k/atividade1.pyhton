import random

print("🎯 Bem-vindo ao Jogo de Adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 20.")
print("Você terá no máximo 5 tentativas.")

numero_secreto = random.randint(1, 20)
tentativas = 0

while True:
    tentativa_str = input("\nDigite seu palpite: ")

    if tentativa_str.strip() == "":
        print("⚠️ Entrada vazia! Digite um número.")
        continue

    if not tentativa_str.isdigit():
        print("⚠️ Digite apenas números inteiros!")
        continue

    tentativa = int(tentativa_str)

    if tentativa < 1 or tentativa > 20:
        print("⚠️ O número deve estar entre 1 e 20!")
        continue

    tentativas += 1

    if tentativa == numero_secreto:
        print(f"🎉 Parabéns! Você acertou em {tentativas} tentativa(s)!")
        break
    elif tentativa < numero_secreto:
        print("📈 O número secreto é MAIOR.")
    else:
        print("📉 O número secreto é MENOR.")

    if tentativas >= 5:
        print(f"❌ Suas tentativas acabaram! O número era {numero_secreto}.")
        break
