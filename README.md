````markdown
# 🎯 Jogo de Adivinhação

Um jogo no terminal onde o jogador tenta adivinhar um número secreto entre **1 e 20** com no máximo **5 tentativas**.

---

## 🚀 Como usar
1. Instale o Python 3.x no seu computador.
2. Baixe o arquivo `main.py`.
3. Abra o terminal e vá até a pasta onde está o arquivo.
4. Execute o comando:
```bash
python main.py
````

5. Siga as instruções exibidas na tela.

---

## 🔍 Estruturas utilizadas

**Loop (`while`)**
Mantém o jogo ativo até que o jogador acerte o número ou acabe o número de tentativas.

**Controle de fluxo (`break` e `continue`)**

* `continue`: usado quando a entrada é inválida (vazia, não numérica ou fora do intervalo).
* `break`: usado quando o jogador acerta ou esgota as tentativas.

**Validação de entrada**

* Impede que a entrada seja vazia com `strip()`.
* Garante que o valor seja numérico com `.isdigit()`.
* Verifica se o número está dentro do intervalo permitido.

**Condicionais (`if`, `elif`, `else`)**

* `if` para verificar acerto.
* `elif` para informar se o número secreto é maior ou menor que o palpite.
* `else` para outros casos possíveis.

---

## 📌 Fluxo do jogo

1. Mensagem inicial com instruções.
2. Entrada do palpite com validações.
3. Comparação com o número secreto.
4. Encerramento com mensagem de vitória ou derrota.

```
```
