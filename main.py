from levels import *

nome_jogador = ""
xp_total = 0
nivel = 1
erros = 0
erros_totais = 0

def game_over(escolha_das_casas):
    global xp_total, erros, nivel, erros_totais

    print('\n💀 - GAME OVER! A conexão com Pythonwarts foi perdida...')
    print(f'Você cometeu 3 ou mais erros no Nível {nivel}.')

    opcao = input('\nDeseja tentar novamente?\nA) Sim\nB) Não\n')

    if opcao == 'a' or opcao == 'A':
        erros = 0
        if nivel == 1:
            xp_total = 0
            print('\n🔄 Reiniciando o Nível 1...')
            nivel_1(escolha_das_casas)
        elif nivel == 2:
            xp_total = 50
            print('\n🔄 Reiniciando o Nível 2...')
            nivel_2(escolha_das_casas)
        elif nivel == 3:
            xp_total = 100
            print('\n🔄 Reiniciando o Nível 3...')
            nivel_3(escolha_das_casas)
        elif nivel == 4:
            xp_total = 150
            print('\n🔄 Reiniciando o Nível 4...')
            nivel_4(escolha_das_casas)
    elif opcao == 'b' or opcao == 'B':
        print('\n🧙👋 Até logo, as portas do Pythonwarts sempre estarão abertas!')
    else:
        print('🧙❌ Opção inválida! Digite A ou B.')
        game_over(escolha_das_casas)


def registro():
    global nome_jogador

    print('🧙 - Bem-vindo(a) à Escola de Magia Pythonwarts!')
    escolha = int(input('🧙 - Deseja realizar seu registro?\n[1] - Sim | [2] - Não\n'))

    if escolha == 1:
        nome_jogador = input('Digite seu nome:\n')
        escolha_das_casas = casas()

        print('\n--- SUAS INFORMAÇÕES ---')
        print('・📜 Bruxo(a):', nome_jogador)
        print('・🏰 Casa:', escolha_das_casas)
        
        nivel_1(escolha_das_casas)
    elif escolha == 2:
        print('🧙 - Ok. Te aguardamos em outro momento.')
    else:
        print('❌ - Opção inválida.')
        registro()

def casas():
    escolha_da_casa = ''

    print ('🧙 - Todo bruxo, ao adentrar em Pythonwarts, é denominado para uma casa...\nEm tempos antigos, isso seria feito de forma aleatória.\nEntretanto, vamos te dar o poder de escolher para onde quer ir...\n')
    print('🧙 - Escolha sua casa:')
    print('')
    print('[1] - 🦁 Grifinória dos Dados')
    print('[2] - 🐍 Sonserina dos Portais')
    print('[3] - 🦅 Corvinal dos Ciclos')
    print('[4] - 🦡 Lufa-Lufa das Funções')
    print('')
    casa = int(input('🧙 - Qual sua escolha final: '))
    print('')
    if casa == 1:
        escolha_da_casa = '🦁・Grifinória dos Dados'
    elif casa == 2:
        escolha_da_casa = '🐍・Sonserina dos Portais'
    elif casa == 3:
        escolha_da_casa = '🦅・Corvinal dos Ciclos'
    elif casa == 4:
        escolha_da_casa = '🦡・Lufa-Lufa das Funções'
    else:
        escolha_da_casa = '👨・Trouxa Digital'

    return escolha_da_casa    
    

def nivel_1(escolha_das_casas):
    global xp_total, erros, nivel, erros_totais
    nivel = 1
    erros = 0

    nv1() 

    num_pergunta = 1
    
    while num_pergunta <= 5 and erros < 3:
        
        if num_pergunta == 1:
            resposta = input('🦉 - 1) Qual tipo de dado armazena textos em Python?\nA) int\nB) str\nC) bool\n')
            if resposta == 'b' or resposta == 'B':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1
        elif num_pergunta == 2:
            resposta = input('\n🦉 - 2) Qual valor representa um número decimal?\nA) 10\nB) "5.5"\nC) 5.5\n')
            if resposta == 'c' or resposta == 'C':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1
        elif num_pergunta == 3:
            resposta = input('\n🦉 - 3) Qual operador representa soma?\nA) +\nB) ==\nC) %\n')
            if resposta == 'a' or resposta == 'A':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1
        elif num_pergunta == 4:
            resposta = input('\n🦉 - 4) Qual tipo representa verdadeiro ou falso?\nA) str\nB) bool\nC) float\n')
            if resposta == 'b' or resposta == 'B':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1
        elif num_pergunta == 5:
            resposta = input('\n🦉 - 5) Qual comando cria uma variável?\nA) nome = "Harry"\nB) int nome\nC) var(nome)\n')
            if resposta == 'a' or resposta == 'A':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1

        num_pergunta += 1

    if erros >= 3:
        game_over(escolha_das_casas)
    elif xp_total >= 30:
        print('\n🦉・Você passou para o Nível 2!')
        nivel_2(escolha_das_casas)


def nivel_2(escolha_das_casas):
    global xp_total, erros, nivel, erros_totais
    nivel = 2
    erros = 0 

    nv2()

    num_pergunta = 1

    while num_pergunta <= 5 and erros < 3:
        
        if num_pergunta == 1:
            resposta = input('🦉 - 1) Qual estrutura é usada para decisões?\nA) for\nB) if\nC) print\n')
            if resposta == 'b' or resposta == 'B':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1
        elif num_pergunta == 2:
            resposta = input('\n🦉 - 2) Qual operador significa igual a?\nA) =\nB) ==\nC) !=\n')
            if resposta == 'b' or resposta == 'B':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1
        elif num_pergunta == 3:
            resposta = input('\n🦉 - 3) Qual operador significa diferente?\nA) !=\nB) >\nC) <\n')
            if resposta == 'a' or resposta == 'A':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1
        elif num_pergunta == 4:
            resposta = input('\n🦉 - 4) O que faz o elif?\nA) Nova condição\nB) Repetição\nC) Soma valores\n')
            if resposta == 'a' or resposta == 'A':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1
        elif num_pergunta == 5:
            resposta = input('\n🦉 - 5) No dia a dia de um programador, para que serve uma estrutura condicional (como o if) em um programa?\nA) Para fazer o computador adivinhar o nome do usuário.\nB) Para fazer o código tomar uma decisão com base em uma condição (se algo for verdadeiro, faça isso; se não, faça aquilo).\nC) Para transformar todos os números do programa em texto automaticamente.\n')
            if resposta == 'b' or resposta == 'B':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1

        num_pergunta += 1

    if erros >= 3:
        game_over(escolha_das_casas)
    else:
        print('\n🦉・Você passou para o Nível 3!')
        nivel_3(escolha_das_casas)


def nivel_3(escolha_das_casas):
    global xp_total, erros, nivel, erros_totais
    nivel = 3
    erros = 0 

    nv3() 

    num_pergunta = 1

    while num_pergunta <= 5 and erros < 3:
        
        if num_pergunta == 1:
            resposta = input("🦉 - 1) Qual laço continua enquanto a condição for verdadeira?\nA) for\nB) if/else\nC) while\n")
            if resposta == 'c' or resposta ==  'C':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1
        elif num_pergunta == 2:
            resposta = input("\n🦉 - 2) O que impede um while True de rodar para sempre?\nA) stop\nB) break\nC) end\n")
            if resposta == 'b' or resposta == 'B':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1
        elif num_pergunta == 3:
            resposta = input("\n🦉 - 3) Quantas vezes for i in range(1, 6) executa?\nA) 6\nB) 4\nC) 5\n")
            if resposta == 'c' or resposta ==  'C':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1
        elif num_pergunta == 4:
            resposta = input("\n🦉 - 4) O que o break faz dentro de um laço?\nA) Pula para a próxima repetição\nB) Encerra o laço\nC) Reinicia o laço\n")
            if resposta == 'b' or resposta == 'B':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1
        elif num_pergunta == 5:
            resposta = input("\n🦉 - 5) O que acontece se a condição do while nunca for falsa?\nA) O programa encerra\nB) O laço roda para sempre\nC) O Python ignora\n")
            if resposta == 'b' or resposta == 'B':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1

        num_pergunta += 1

    if erros >= 3:
        game_over(escolha_das_casas)
    else:
        print('\n🦉・Você passou para o Nível 4!')
        nivel_4(escolha_das_casas)


def nivel_4(escolha_das_casas):
    global xp_total, erros, nivel, erros_totais
    nivel = 4
    erros = 0 

    nv4()

    num_pergunta = 1

    while num_pergunta <= 5 and erros < 3:
        
        if num_pergunta == 1:
            resposta = input('🦉 - 1) Como retornar múltiplos valores de uma função?\nA) Múltiplos returns\nB) return_all\nC) Separar por vírgula no return\n')
            if resposta == 'c' or resposta == 'C':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1
        elif num_pergunta == 2:
            resposta = input('\n🦉 - 2) Objetivo da modularização?\nA) Aumentar complexidade\nB) Facilitar manutenção\nC) Reduzir legibilidade\n')
            if resposta == 'b' or resposta == 'B':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1
        elif num_pergunta == 3:
            resposta = input('\n🦉 - 3) Sintaxe correta para criar uma função?\nA) function minha_funcao():\nB) def minha_funcao():\nC) create minha_funcao():\n')
            if resposta == 'b' or resposta == 'B':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1
        elif num_pergunta == 4:
            resposta = input('\n🦉 - 4) Diferença entre parâmetro e argumento?\nA) Parâmetro na função, argumento ao chamar\nB) Parâmetro repete loops\nC) São a mesma coisa\n')
            if resposta == 'a' or resposta == 'A':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1
        elif num_pergunta == 5:
            resposta = input('\n🦉 - 5) O que é um parâmetro?\nA) Um tipo de loop\nB) Um valor recebido pela função\nC) Um comentário\n')
            if resposta == 'b' or resposta ==  'B':
                print(f'🧙✅・Correto! +10 Pontos para {escolha_das_casas}')
                xp_total += 10
            else:
                print('🧹❌・Resposta Errada, você ainda quer ser um bruxo de respeito?!')
                erros += 1
                erros_totais += 1

        num_pergunta += 1

    if erros >= 3:
        game_over(escolha_das_casas)
    else:
        print('\n🏆 | Você completou todos os níveis com sucesso!')
        final(escolha_das_casas)

def final(escolha_das_casas):
    global nome_jogador, total, erros_totais
    print("\n🏆 | Parabéns! {} da {} você completou todos os níveis com sucesso!".format(nome_jogador,escolha_das_casas))
    print("\n🏆 | Voce terminou o jogo com {} de XP e com {} erros!!!".format(xp_total, erros_totais))
    print('\n💀 | Lord Voldemort foi derrotado por toda a eternidade! Graças a você, Pythonwarts está a salvo por toda a eternidade!')

def regras():
    print('---'*26)
    print ('')
    print ('                              📌 | REGRAS DO JOGO | 📌                                       ')
    print('')
    print(' ➡️  | Responda com A, B, C ou D ')
    print(' ➡️  | Complete os 4 níveis para vencer ')
    print(' ➡️  | Cada nível possui um total de 5 questões ')
    print(' ➡️  | Com a vitória do Pythonwarts voce se torna um bruxo nível | \033[31mDUMBLEDORE\033[m | ')
    print('')
    print('---'*26)

def lore():
   print('                                  🏰🧙 | COMO TUDO COMEÇOU...                                 ')
   print('')
   print('📜╺╸Dizem que o tempo cura todas as feridas, mas ele também esconde segredos terríveis...')
   print('📜╺╸Após mais de um século de paz, o eco de um nome proibido volta a sussurrar nos corredores.')
   print('📜╺╸Lord Voldemort encontrou uma brecha na eternidade. Uma última Horcrux, oculta não por magia, mas por enigmas.')
   print('📜╺╸As varinhas são inúteis aqui. Onde o destino se decide hoje, o conhecimento é a única arma que resta.')
   print('📜╺╸Aproxime-se, jovem... Vejo em seus olhos a chama da curiosidade.')
   print('📜╺╸O futuro depende da sua capacidade de decifrar o que ninguém mais ousou entender.')
   print('📜╺╸Prepare-se. A verdadeira aventura começa agora...')
   print('')

def main():
    print ('-=-'*20)
    print ('\033[31m🎮 ┊ PROJETO DESENVOLVIDO POR: JOSÉ ROBERTO E JOÃO VICTOR ┊ 🎮\033[m')
    print ('              \033[31m🎮 ┊ 🌵 - UAST - UFRPE ┊ 🎮\033[m                     ')
    print ('-=-'*20)
    print('')
    print ('          ==== ✅ ┊ SEJA MUITO BEM VINDO AO  ┊ ✅ ====         ')
    print('        ===== 🔮 PYTHONWARTS: O ENIGMA DO CÓDIGO 🔮 =====')
    
    while True:
        escolha = int(input('\n🧙 - Deseja iniciar sua aventura no mundo de Pythonwarts?\n[1] - Sim\n[2] - Não\n[3] - Regras do jogo\n'))
    
        if escolha == 1:
            print('')
            print('---'*35)
            lore()
            print('---'*35)
            print('')
            registro()
        elif escolha == 2:
            print('\n🧙 - Até sua próxima aventura.')
            break
        elif escolha == 3:
            regras()

main()
