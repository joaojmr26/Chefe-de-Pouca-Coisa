import os
import random
from time import sleep
colunas, linhas = os.get_terminal_size()
carinha1 = r""" :( """ ; carinha2 = r""" :/ """ ; carinha3 = r""" :) """
sortudo = r"""___________________________________
|#######====================#######|
|#(1)*BANCO AUXILIAR DO BRASIL*(1)#|
|#**          /===\   ********  **#|
|*# {G}      | (") |             #*|
|#*  ******  | /v\ |   U M       *#|
|#(1)         \===/            (1)#|
|##=========UM TROCADO===========##|
------------------------------------"""
sortepouca = r"""   _
    \________
 ~   \######/       
  ~   |####/
 ~    |____.
______o____o__________"""
trem = r"""       .-.               
       ] [    .-.      _    .-----.
     .'   ''''   '''''' ''''| .--`
    (:--:--:--:--:--:--:--:-| [___    .------------------------.
     |C&O  :  :  :  :  :  : [_9_] |'='|.----------------------.|
    /|.___________________________|___|'--.___.--.___.--.___.-'| 
   / ||_.--.______.--.______.--._ |---\'--\-.-/==\-.-/==\-.-/-'/--
  /__;^=(==)======(==)======(==)=^~^^^ ^^^^(-)^^^^(-)^^^^(-)^^^ 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
alcool = r"""  _
 {_}
 |(|
 |=|
/   \
|.--|
||  |
||  |    .    ' .
|'--|  '     \~~~/
'-=-' \~~~/   \_/
       \_/     Y
        Y     _|_
       _|_"""
cigarro = r"""            .-.
           /  /
          /. /
 )       /c\/
  (     /'\/
 )     /  /
(     /  /
 )   /  /
  ( /. /
   .`.'.
   `'``"""
s = r"""   _____ _           __           _        _____                         _____      _           
  / ____| |         / _|         | |      |  __ \                       / ____|    (_)          
 | |    | |__   ___| |_ ___    __| | ___  | |__) |__  _   _  ___ __ _  | |     ___  _ ___  __ _ 
 | |    | '_ \ / _ \  _/ _ \  / _` |/ _ \ |  ___/ _ \| | | |/ __/ _` | | |    / _ \| / __|/ _` |
 | |____| | | |  __/ ||  __/ | (_| |  __/ | |  | (_) | |_| | (_| (_| | | |___| (_) | \__ \ (_| |
  \_____|_| |_|\___|_| \___|  \__,_|\___| |_|   \___/ \__,_|\___\__,_|  \_____\___/|_|___/\__,_|"""
gato = r"""   |\---/|
   | ,_, |
    \_`_/-..----.
 ___/ `   ' ,""+ \ 
(__...'   __\    |`.___.';
  (_,...'(_,.`__)/'.....+"""
pote = r""" .=================.       
 |;;|#H#|;;;;;;;;: |      
 .=================.    .=================.
  |;|#H#|;;;;;;;: |     |_________________|
   |;|#H#|;;;;;: |       |               |
   |;|#H#|;;;;;: |        |             |
    |;|#H#|;;;: |         |             |
    |;|#H#|;;;: |          |           |
     |;|#H#|;: |           |           |
      =========             |_________|"""
cano = r""" .__   .-".
(o\"\  |  |
   \_\ |  |
  _.---:_ |
 ("-..-" /
  "-.-" /
    /   |
    "--" """
arvore = r"""               ,@@@@@@@,
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
   ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
   %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
   %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
   `&%\ ` /%&'    |.|        \ '|8'
       |o|        | |         | |
       |.|        | |         | |
    \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_"""
vila = r""" ~         ~~          __
       _T      .,,.    ~--~ ^^
 ^^   // \                    ~
      ][O]    ^^      ,-~ ~
   /''-I_I         _II____
__/_  /   \ ______/ ''   /'\_,__
  | II--'''' \,--:--..,_/,.-{ },
; '/__\,.--';|   |[] .-.| O{ _ }
:' |  | []  -|   ''--:.;[,.'\,/
'  |[]|,.--'' '',   ''-,.    |
  ..    ..-''    ;       ''. '"""
relogio = r"""         _____
      _.'_____`._
    .'.-'  12 `-.`.
   /,' 11      1 `.\
  // 10      /   2 \\
 ;;         /       ::
 || 9  ----O      3 ||
 ::                 ;;
  \\ 8           4 //
   \`. 7       5 ,'/
    '.`-.__6__.-'.'
      '-._____.-'
"""
rua = r""" ___  ,--.  __________________________/   ,   /_______
    'O---O'~
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   ,--.   _ _ _ _ _
         ____                        ~'O---O'
 _______<____| _____        __________________________
           ||      /   ,   /"""
livro = r"""        _.-"\
    _.-"     \
 ,-"          \
( \            \
 \ \            \
  \ \            \
   \ \         _.-;
    \ \    _.-"   :
     \ \,-"    _.-"
      \(   _.-" 
       `--"
"""

def sisdecimais(dinheiro): #Separa as casas decimais, deixa mais agradável aos olhos
    txt = f'R${dinheiro:_.2f}'
    txt = txt.replace('.',',').replace('_','.')
    return(txt)

def eventoaleatorio(): #Evento aleatório com o passar dos meses
    sorte = random.random()
    ganhou = False
    if ganhou and sorte>0.3:
        ganhou = False
    elif ganhou and sorte<0.3:
        ganhou = True
    else:
        if sorte>0.9:
            os.system('cls||clear')
            print(sortudo)
            ganhou = True
            print(" ")
            print("Um admirador quis te ajudar e te fez uma doação de 15000 R$")
            return "sortudo"
        elif sorte<=0.4 and sorte>= 0.3:
            os.system('cls||clear')
            ganhou = True
            print(sortepouca)
            print(" ")
            print("Os habitantes estão mais felizes por aproveitarem promoções que estão acontecendo!")
            return "sortepouca"

def intro(): #Menu inicial
    print('\n'.join(l.center(colunas-1) for l in s.splitlines())) #Centraliza o titulo
    print(" ")
    jogar = "[1] Jogar"
    jogar = jogar.center(colunas)
    sair = "Pressione qualquer outra tecla para sair"
    sair  = sair.center(colunas)
    print(jogar)
    print(sair)
    acao = input()
    if acao == "1":
        return True
    else:
        return False

def sistemacresc(habitantes, taxades, qntdmelhorias, felicidade): #Sistema de crescimento de habitantes e do "Desemprego"
    n = random.random()
    cresc = 80
    des = taxades
    pessoas = habitantes
    a = n*10000//10
    b = a//5
    fel = felicidade/100
    total = int((b*qntdmelhorias)*fel)
    novo = pessoas + total + cresc
    if total+cresc >= 300:
        desnovo = random.randint(1, 6)
        desdim = random.randint(1, 6)
        des += desnovo - desdim
    elif total+cresc <= 100:
        desnovo = random.randint(1, 3)
        desdim = random.randint(1, 4)
        des += desnovo - desdim
    else:
        desnovo = random.randint(1, 3)
        desdim = random.randint(1, 3)
        des += desnovo - desdim
    if des <= 0:
        des = 0
    elif des > 20:
        des -= 2
    return(novo, des)
    
def sistemafelicidade(felicidade): #Sistema para a felicidade não passar de 100
    if felicidade > 100:
        felicidade = 100
    else:
        felicidade = felicidade
    return felicidade

def sistemacarinha(felicidade): #Sistema para as carinhas
    if felicidade<35:
        carinha = carinha1
    elif felicidade>= 35 and felicidade<= 70:
        carinha = carinha2
    elif felicidade> 70:
        carinha = carinha3
    return carinha

def sistemamon(x, dinheirosalvo): #Função para o sistema monetário
    dinheirosalvo += x
    return dinheirosalvo

def introducao(nomecidade): #Função de introdução ao jogador
    print(vila)
    nomecidade = input("Seja muito bem vindo(a) a vila de ")
    print("A vila de", nomecidade, "tem atualmente 3000 habitantes!")
    sleep(1)
    print("Seu objetivo é desenvolver essa vila ao máximo, todos os habitantes contam com você!")
    sleep(2)
    print("Suas decisões impactam diretamente a vida deles, então escolha sabiamente.")
    sleep(2)
    print("Boa sorte com sua administração! Não que eu ache que você precise, é claro.")
    sleep(3)
    tcon = input("Continuar? ")
    os.system('cls||clear')
    return(nomecidade) #Retorna o nome escolhido

def menu(nome, nomecidade): #Função com o menu do jogo
    asfalto = False; escolaef = False; parquearbo = False; sanea = False; ceram = False
    lucro = 10000
    dinheirosalvo = 50000
    x = 0 ; meses = 0 ; felicidade = 50 ; qntdmelhorias = 0 ; taxades = 2 ; habitantes = 3000
    dinheiro = sistemamon(x, dinheirosalvo)
    acao = 0
    while int(acao) >= 0:
        texto_dinheiro = sisdecimais(dinheiro)
        os.system('cls||clear')
        print("Você tem {}".format(texto_dinheiro))
        print("[1] Informações de", nomecidade)
        print("[2] Melhorias")
        print("[3] Políticas de Governo")
        print("[4] Passar o mês")
        print("[5] Sair")
        acao = input()
        os.system('cls||clear')
        if acao == "1" or acao == "2" or acao == "3" or acao == "4" or acao == "5": 
            if int(acao) == 1: #Informações da Cidade
                print(vila)
                felicidade = sistemafelicidade(felicidade)
                carinha = sistemacarinha(felicidade)
                print("Tempo de Governo: {} meses".format(meses))
                print("Felicidade dos Habitantes: {}/100{}".format(felicidade,carinha))
                print("Quantidade de melhorias feitas: {}".format(qntdmelhorias))
                print("Taxa de desemprego: {}%".format(taxades))
                print("Quantidade de Habitantes: {}".format(habitantes))
                print("[0] Voltar")
                acao = input()
                os.system('cls||clear')
            elif int(acao) == 2: #Melhorias
                if asfalto:
                    print("[#] Asfaltar Ruas")
                else:
                    print("[1] Asfaltar ruas")
                if escolaef:
                    print("[#] Construir escola de ensino fundamental")
                else: 
                    print("[2] Construir escola de ensino fundamental")
                if parquearbo:
                    print("[#] Construir parque arborizado")
                else:
                    print("[3] Construir parque arborizado")
                if sanea:
                    print("[#] Criar sistema de saneamento")
                else:
                    print("[4] Criar sistema de saneamento")
                if ceram:
                    print("[#] Criar oficina de cêramica")
                else:
                    print("[5] Criar oficina de cêramica")
                print("[0] Voltar")
                acao2 = int(input())
                if acao2 == 0:
                    acao = acao2
                elif acao2 == 1: #Asfaltar ruas menu adicional
                    os.system('cls||clear')
                    if asfalto:
                        print("Melhoria ja comprada")
                        sleep(2)
                        os.system('cls||clear')
                    else:
                        print("Você tem {}".format(texto_dinheiro))
                        print(" ")
                        print("Asfaltar ruas")
                        print(rua)
                        print("Custo: 30.000")
                        print("Aumenta a felicidade em 10")
                        print("Custo de manutenção de 1000,00 R$ por mês")
                        print("[1] Comprar")
                        print("[0] Voltar")
                        acao3 = int(input())
                        os.system('cls||clear')
                        if acao3 == 1: #Comprar 
                            if dinheiro >= 30000:
                                x = -30000
                                dinheiro = sistemamon(x, dinheiro)
                                dinheirosalvo = dinheiro
                                felicidade += 10
                                lucro -= 1000
                                qntdmelhorias += 1
                                asfalto = True
                                print("Comprado!")
                                sleep(1)
                            else:
                                print("Não tem o dinheiro necessário.")
                                print("Voltando ao menu")
                                sleep(2)
                elif acao2 == 2: #Escola EF menu adicional
                    os.system('cls||clear')
                    if escolaef:
                        print("Melhoria ja comprada")
                        sleep(2)
                        os.system('cls||clear')
                    else:
                        os.system('cls||clear')
                        print("Você tem {}".format(texto_dinheiro))
                        print(" ")
                        print("Construir escola de ensino fundamental")
                        print(livro)
                        print("Custo: 150.000,00 R$")
                        print("Aumenta a felicidade em 20")
                        print("Gera um lucro de 10.000,00 R$ por mês")
                        print("[1] Comprar")
                        print("[0] Voltar")
                        acao3 = int(input())
                        os.system('cls||clear')
                        if acao3 == 1: #Comprar
                            if dinheiro >= 150000:
                                x = -150000
                                dinheiro = sistemamon(x, dinheiro)
                                dinheirosalvo = dinheiro
                                felicidade += 20
                                lucro += 10000
                                qntdmelhorias += 1
                                escolaef = True
                                print("Comprado!")
                                sleep(1)
                            else:
                                print("Não tem o dinheiro necessário.")
                                print("Voltando ao menu")
                                sleep(2)
                        else:
                            acao = acao3
                elif acao2 == 3: #Parque Arborizado menu adicional
                    os.system('cls||clear')
                    if parquearbo:
                        print("Melhoria ja comprada")
                        sleep(2)
                        os.system('cls||clear')
                    else:
                        os.system('cls||clear')
                        print("Você tem {}".format(texto_dinheiro))
                        print(" ")
                        print("Construir parque arborizado")
                        print(arvore)
                        print("Custo: 2.000,00 R$")
                        print("Aumenta a felicidade em 10")
                        print("Custo de manutenção de 250,00 R$ por mês")
                        print("[1] Comprar")
                        print("[0] Voltar")
                        acao3 = int(input())
                        os.system('cls||clear')
                        if acao3 == 1: #Comprar
                            if dinheiro >= 2000:
                                x = -2000
                                dinheiro = sistemamon(x, dinheiro)
                                dinheirosalvo = dinheiro
                                lucro -= 250
                                felicidade += 10
                                qntdmelhorias += 1
                                parquearbo = True
                                print("Comprado!")
                                sleep(1)
                            else:
                                print("Não tem o dinheiro necessário.")
                                print("Voltando ao menu")
                                sleep(2)
                        else:
                            acao = acao3
                elif acao2 == 4: #Saneamento menu adicional
                    os.system('cls||clear')
                    if sanea:
                        print("Melhoria ja comprada")
                        sleep(2)
                        os.system('cls||clear')
                    else:
                        os.system('cls||clear')
                        print("Você tem {}".format(texto_dinheiro))
                        print(" ")
                        print("Construir sistema de saneamento")
                        print(cano)
                        print("Custo: 30.000,00 R$")
                        print("Aumenta a felicidade em 20")
                        print("Custo de manutenção de 1.250,00 R$ por mês")
                        print("[1] Comprar")
                        print("[0] Voltar")
                        acao3 = int(input())
                        os.system('cls||clear')
                        if acao3 == 1: #Comprar
                            if dinheiro >= 30000:
                                x = -30000
                                dinheiro = sistemamon(x, dinheiro)
                                dinheirosalvo = dinheiro
                                felicidade += 20
                                lucro -= 1250
                                qntdmelhorias += 1
                                sanea = True
                                print("Comprado!")
                                sleep(1)
                            else:
                                print("Não tem o dinheiro necessário.")
                                print("Voltando ao menu")
                                sleep(2)
                        else:
                            acao = acao3
                elif acao2 == 5: #Cerâmica menu adicional
                    os.system('cls||clear')
                    if ceram:
                        print("Melhoria ja comprada")
                        sleep(2)
                        os.system('cls||clear')
                    else:
                        os.system('cls||clear')
                        print("Você tem {}".format(texto_dinheiro))
                        print(" ")
                        print("Construir oficina de cêramica")
                        print(pote)
                        print("Custo: 25.000,00 R$")
                        print("Aumenta a felicidade em 5")
                        print("Gera um lucro de 5.000,00 R$ por mês")
                        print("[1] Comprar")
                        print("[0] Voltar")
                        acao3 = int(input())
                        os.system('cls||clear')
                        if acao3 == 1: #Comprar
                            if dinheiro >= 25000:
                                x = -25000
                                dinheiro = sistemamon(x, dinheiro)
                                dinheirosalvo = dinheiro
                                lucro += 5000
                                felicidade += 5
                                qntdmelhorias += 1
                                ceram = True
                                print("Comprado!")
                                sleep(1)
                            else:
                                print("Não tem o dinheiro necessário.")
                                print("Voltando ao menu")
                                sleep(2)
                        else:
                            acao = acao3
                os.system('cls||clear')
            elif int(acao) == 3: # Políticas de Governo
                print("[1] Proibir gatos ao ar livre")
                print("[2] Proibir fumar em locais fechados")
                print("[3] Proibir o consumo de álcool")
                print("[4] Incentivar a exportação")
                print("[0] Voltar")
                acao2 = int(input())
                if acao2 == 0:
                    acao = acao2
                elif acao2 == 1: #Proibir Gatos
                    os.system('cls||clear')
                    print("Proibir gatos ao ar livre")
                    print(gato)
                    print("Diminui a felicidade em 10")
                    print("Aumenta as vendas de artigos para gato!")
                    print("[1] Implantar")
                    print("[0] Voltar")
                    acao3 = int(input())
                    os.system('cls||clear')
                    if acao3 == 1: #Implantar
                        felicidade -= 10
                        lucro += 500
                    else:
                        acao = acao3
                elif acao2 == 2: #Proibir fumar em locais fechados
                    os.system('cls||clear')
                    print("Proibir fumar em locais fechados")
                    print(cigarro)
                    print("Aumenta a felicidade em 15")
                    print("Diminui a venda de cigarros")
                    print("[1] Implantar")
                    print("[0] Voltar")
                    acao3 = int(input())
                    os.system('cls||clear')
                    if acao3 == 1: #Implantar
                        felicidade += 15
                        lucro -= 150
                    else:
                        acao = acao3
                elif acao2 == 3: #Proibir alcool
                    os.system('cls||clear')
                    print("Proibir o consumo de alcool")
                    print(alcool)
                    print("Diminui a felicidade em 5")
                    print("Acaba com a venda de álcool")
                    print("[1] Implantar")
                    print("[0] Voltar")
                    acao3 = int(input())
                    os.system('cls||clear')
                    if acao3 == 1: #Implantar
                        felicidade -= 5
                        lucro -= 300
                    else:
                        acao = acao3
                elif acao2 == 4: #Incentivar a exportação
                    os.system('cls||clear')
                    print("Incentivar a exportação")
                    print(trem)
                    print("Diminui a felicidade em 5")
                    print("Aumenta o lucro das empresas locais")
                    print("[1] Implantar")
                    print("[0] Voltar")
                    acao3 = int(input())
                    os.system('cls||clear')
                    if acao3 == 1: #Implantar
                        felicidade -= 5
                        lucro += 400
                    else:
                        acao = acao3
                os.system('cls||clear')
            elif int(acao) == 4: #Passar o mês
                meses += 1
                dinheiro += lucro 
                print(relogio)
                print("Passando o mês.")
                sleep(1)
                os.system('cls||clear')
                print(relogio)
                print("Passando o mês..")
                sleep(1)
                os.system('cls||clear')
                print(relogio)
                print("Passando o mês...")
                sleep(1)
                os.system('cls||clear')
                sorte = eventoaleatorio()
                if sorte == "sortepouca":
                    felicidade += 5
                    sleep(2)
                elif sorte == "sortudo":
                    dinheiro += 15000
                    sleep(2)
                else:
                    print("")
                
                habitantes, taxades = sistemacresc(habitantes, taxades, qntdmelhorias, felicidade)
            elif int(acao) == 5: #Sair
                return 
            else:
                print("Opção não encontrada, tente novamente.")
        else:
            print("Opção não encontrada, tente novamente.")
            acao = 0
        os.system('cls||clear')
        
def main():
    os.system('cls||clear')
    acao = intro()
    os.system('cls||clear')
    if acao:
        nomecidade = "Error"
        confirma = "N"
        while confirma != "S":
            nome = input("Como você gostaria de ser chamado? ")
            print("Deseja que seu nome seja", nome, "? Você não poderá mudar depois. (S/N)")
            confirma = input().upper()
            os.system('cls||clear') #Limpa o terminal
        nomecidade = introducao(nomecidade) #Chamando a introdução do jogo
        os.system('cls||clear')
        menu(nome, nomecidade)
    else:
        print("Fechando o jogo...")
        os.system('cls||clear')
        return
main()