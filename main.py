import pickle
import os
import random
from time import sleep
colunas, linhas = os.get_terminal_size()
carinha1 = r""" :( """ ; carinha2 = r""" :/ """ ; carinha3 = r""" :) """
cidade = r"""                                  ___________
   ____________                  |  ___      |       _________
  |            |                 | |   |     |      | = = = = |
  | |   |   |  |                 | |   |     |      |         |
  |            |                 |  --- ___  |      | |  || | |
  | |   |   |  |                 |     |   | |      |         |
  |            |        _______  |     |   | |      | |  || | |
  | |   |   |  |       /_____/ \ |      ---  |      |         |
  |            |       |+ ++|  | |  |~~~~~~| |      | |  || | |
  |            |       |+ ++|  | |  |~~~~~~| |      | |  || | |
~~|    (~~~~~) |~~~~~ ~| H  |_ |~|  | |||| | |~~~~~~|         |
  |    ( ||| ) |       ~~~~~~    |  | |||| | |      | ||||||| |
  ~~~~~~~~~~~~~________/  /_____ |  | |||| | |      | ||||||| |
                                 ~~~~~~~~~~~~~      ~~~~~~~~~~~"""
cidadefogos = r"""                                  ___________  .''.            
   ____________   .:,      '.\'/.|  ___      |:_\/_: _________ 
  |            |.'.;.`.    -= o =| |\o/|     |: /\ :| = = = = |
  | |   |   |  | `,:.'     .'/.\'| | | |     | '..' |         |
  |            |  ,            : |  --- ___  |    ; | | ||o/| |
  | |   |\o/|  | ,              ,|     |   | |     '|         |
  |            |,       _______  |     |\o/| |      | |  || | |
  | |   |   |  |       /_____/ \ |      ---  |      |         |
  |            |       |+ ++|  | |  |~~~~~~| |      | |  || | |
  |            |       |+ ++|  | |  |~~~~~~| |      | |\o|| | |
~~|    (~~~~~) |~~~~~~~| H  |_ |~|  | |||| | |~~~~~~|         |
  |    ( ||| ) |       ~~~~~~    |  | |||| | |      | ||||||| |
  ~~~~~~~~~~~~~________/  /_____ |  | |||| | |      | ||||||| |
                                 ~~~~~~~~~~~~~      ~~~~~~~~~~~"""
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
s = r"""

  _______                                            _______                           _______                       
 |       |                                          |   _   |                         |       |                      
 |    ___|                              __          |  |_|  |                         |    ___|                      
 |   |    __ __        ____            |  |         |   ____|                         |   |          __              
 |   |___|  |  |-----./  _|-----.   .--|  |-----.   |   |  .-----.--.--.----.-----.   |   |___ .---.|__|-----.-----. 
 |       |     |  -__|   _|  -__|   |  _  |  -__|   |   |  |  _  |  |  |  __|  _  |   |       |  _  |  |__ --|  -  | 
 |_______|__|__|_____|__| |_____|   |_____|_____|   |___|  |_____|_____|____|___._|   |_______|_____|__|_____|__|__| 
 
 
"""
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
shopping = r"""        __.|.__
    .-"'..':`..`"-.
  .' .' .  :  . `. `.
 / .   .   :   .   . \
/_ _._ _.._:_.._ _._ _\
  '   '    |    '   '
           |
           |
           |
           |
           |
         `=' """
emas = r"""       .--.                   .---.
   .---|__|           .-.     |~~~|
.--|===|--|_          |_|     |~~~|--.
|  |===|  |'\     .---!~|  .--|   |--|
|%%|   |  |.'\    |===| |--|%%|   |  |
|%%|   |  |\.'\   |   | |__|  |   |  |
|  |   |  | \  \  |===| |==|  |   |  |
|  |   |__|  \.'\ |   |_|__|  |~~~|__|
|  |===|--|   \.'\|===|~|--|%%|~~~|--|
^--^---'--^    `-'`---^-^--^--^---'--'"""
centroeventos = r"""   _______       __
 /   ------.   / ._`_
|  /         ~--~    \
| |             __    `.____________________ _^-----^
| |  I=|=======/--\=========================| o o o |
\ |  I=|=======\__/=========================|_o_o_o_|
 \|                   /                       ~    ~
   \       .---.    .
     -----'     ~~''"""
catavento = r"""                      |-_'-'      
             _        |-_'/        
            /;-,_     |-_'        
           /-.-;,-,   |'          
          /;-;-;-;_;_/|\_ _ _ _ _ 
                    |_0_|`-;-;-;,|   
                    |\|/| `-;-;-'
                    -_| |     '-'
                   /-_| |
                  ,'-_| |
                 /-'-_| |
      _..,__________|___|_______..,_   """
tecnologia = r"""   ._________________.
   |.---------------.|
   ||               ||
   ||   -._ .-.     ||
   ||   -._| | |    ||
   ||   -._|"|"|    ||
   ||   -._|.-.|    ||
   ||_______________||
   /.-.-.-.-.-.-.-.-.\
  /.-.-.-.-.-.-.-.-.-.\
 /.-.-.-.-.-.-.-.-.-.-.\
/______/__________\___o_\
\_______________________/'"""
maconha = r"""    .===. (
    |   |  )
    |   | (
    |   | )
    |   \*/
  ,'    //.
 :~~~~~//~~;      
  `.  // .'
  `-------'"""
cruz = r"""               |
           \       /
             .---. 
        '-.  |   |  .-'
          ___|   |___
     -=  [           ]  =-
         `---.   .---' 
      __||__ |   | __||__
      '-..-' |   | '-..-'
        ||   |   |   ||
        ||_.-|   |-,_||
      .-"`   `"`'`   `"-.
    .'                   '."""
plantacao = r"""      ,,,                      ,,,
     {{{}}    ,,,             {{{}}    
  ,,, ~Y~    {{{}},,,      ,,, ~Y~   
 {{}}} |/,,,  ~Y~{{}}}    {{}}} |/,,,  
  ~Y~ \|{{}}}/\|/ ~Y~  ,,, ~Y~ \|{{}}}
  \|/ \|/~Y~  \|,,,|/ {{}}}\|/ \|/~Y~ 
  \|/ \|/\|/  \{{{}}/  ~Y~ \|/ \|/\|/  
  \|/\\|/\|/ \\|~Y~//  \|/ \|/\\|/\|/ 
  \|//\|/\|/,\\|/|/|// \|/ \|//\|/\|/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
praia = r"""          |
        \ _ /
      -= (_) =-
        /   \         _\/_
          |           //o\  _\/_
   _____ _ __ __ ____ _ | __/o\\ _
 =-=-_-__=_-= _=_=-=_,-'|"'""-|-,_
  =- _=-=- -_=-=_,-"          |
   =- =- -=.--'"""
ostra = r"""     ___---__---___
   --              --
  ~                  ~
 ~~                  ~~
(__       ,--,       __)
   ====- |#   | -====
(~~       `--'         )
\~~--___        ___--~~/ 
 ~~--___---__---___--~~
       --------"""
pesquisador = r"""                   __
                 .'  `'.
                /  _    |
                #_/.\==/.\
               (, \_/ \\_/
                |    -' |
                \   '=  /
                /`-.__.'
             .-'`-.___|__
            /    \       `."""
pesquisadort = r"""                   __
                 .'  `'.
                /  _    |
                #_/.\==/.\
               (, \_/ \\_/
                |    -' |
                \   ==  /
                /`-.__.'
             .-'`-.___|__
            /    \       `."""

def salvar(info):
    with open('save', 'wb') as fp:
        pickle.dump(info, fp)

def carregar():
    try:
        with open('save', 'rb') as fp:
            info = pickle.load(fp)
            return info
    except FileNotFoundError:
        info = [50000, 50, 0, 2, 3000, 10000, 0, 0 , "", "", 0, 0, 0, 0, 0]
        return info

def inova(dinheiro, lucro, felicidade): #Função para pesquisas
   l = ("Tijolo de casca de acerola", "Milho transgênico", "Mini porco de estimação", "Guarda chuva a prova d'água", "Remédio para calvície",
        "Refrigerante Diet", "Vacina contra antivacina", "Caneca do bolsonaro", "Toalha do lula","Levantador de bilola", "Parafuseta limpa")
   x = 0
   while x>= 0:
        os.system('cls||clear')
        print("você tem: ", sisdecimais(dinheiro))
        print(tecnologia)
        print("Dê um pequeno subsídio para os cientistas e eles produziram coisas muito úteis! (Ou não)")
        print("[1] Investir 50.000,00 R$")
        print("[0] Voltar")
        acao = input()
        os.system('cls||clear')
        if acao == "1":
            if dinheiro >= 50000:
                os.system('cls||clear')
                print(pesquisador)
                print("Pesquisando...")
                sleep(2)
                os.system('cls||clear')
                a = random.randint(0, 10)
                dinheiro -=50000
                if a>5:
                    item = random.randrange(0,11)
                    print(pesquisador)
                    print("Parabéns, seus pesquisadores descobriram o(a) {}".format(l[item]))
                    lucro += 5000
                    felicidade += 5
                    sleep(3)
                    os.system('cls||clear')
                else:
                    item = random.randrange(0,11)
                    os.system('cls||clear')
                    print(pesquisadort)
                    print("Seus pesquisadores não conseguiram desenvolver o(a) {}".format(l[item]))
                    sleep(3)
                    os.system('cls||clear')
            else:
                print("Você não tem dinheiro pra isso...")
                sleep(2)
                os.system('cls||clear')
        elif acao == "0":
            print("Voltando...")
            sleep(1)
            os.system('cls||clear')
            return(dinheiro, lucro, felicidade)
        else:
            print("Opção não encontrada...")
            sleep(2)
            os.system('cls||clear')

def cidadepar(nomecidade): #Função que faz a passagem para o marco de cidade
    os.system('cls||clear')
    print(cidadefogos)
    print("Meus parabéns, {} se tornou uma cidade!".format(nomecidade))
    sleep(4)
    acao = -1
    os.system('cls||clear')
    return acao, 1

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
    CRED = '\033[92m' #Cor verde
    CEND = '\033[0m' #Volta ao normal
    print(CRED +'\n'.join(l.center(colunas-1) for l in s.splitlines()) + CEND) #Titulo centralizado com cores
    print(" ")
    print(" ")
    NovoJogo = "[1] Iniciar Novo Jogo".center(colunas)
    ContJogo = "[2] Continuar jogo salvo".center(colunas)
    sair = "[0] Sair do Jogo".center(colunas)
    print(NovoJogo)
    print(" ")
    print(ContJogo)
    print(" ")
    print(sair)
    acao = input()
    if acao == "0":
        info = [50000, 50, 0, 2, 3000, 10000, 0, -1]
        return info
    elif acao == "1":
        info = [50000, 50, 0, 2, 3000, 10000, 0, 0 , "", "", 0, 0, 0, 0, 0]
        return info
    elif acao == "2":
        info = carregar()
        return info

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

def menuvila(nomecidade, info): #Função com o menu para a vila
    asfalto = info[10] ; escolaef = info[11]; parquearbo = info[12]; sanea = info[13]; ceram = info[14] ; lvl = info[7]
    x = 0 ; dinheirosalvo = info[0] ; felicidade = info[1] ; qntdmelhorias = info[2] ; taxades = info[3] ; habitantes = info[4] ; lucro = info[5] ; meses = info[6]
    dinheiro = sistemamon(x, dinheirosalvo)
    acao = "0"
    while int(acao) >= 0: #Loop para manter o menu 
        texto_dinheiro = sisdecimais(dinheiro)
        os.system('cls||clear')
        print("Você tem {}".format(texto_dinheiro))
        print("[1] Informações de", nomecidade)
        print("[2] Melhorias")
        print("[3] Políticas de Governo")
        print("[4] Passar o mês")
        print("[0] Sair")
        acao = input()
        os.system('cls||clear')
        if acao == "1" or acao == "2" or acao == "3" or acao == "4" or acao == "5" or acao == "0": 
            if int(acao) == 1: #Informações da Vila
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
                if asfalto == 1:
                    print("[#] Asfaltar Ruas")
                else:
                    print("[1] Asfaltar ruas")
                if escolaef == 1:
                    print("[#] Construir escola de ensino fundamental")
                else: 
                    print("[2] Construir escola de ensino fundamental")
                if parquearbo == 1:
                    print("[#] Construir parque arborizado")
                else:
                    print("[3] Construir parque arborizado")
                if sanea == 1:
                    print("[#] Criar sistema de saneamento")
                else:
                    print("[4] Criar sistema de saneamento")
                if ceram == 1:
                    print("[#] Criar oficina de cêramica")
                else:
                    print("[5] Criar oficina de cêramica")
                print("[0] Voltar")
                acao2 = int(input())
                if acao2 == 0:
                    acao = acao2
                elif acao2 == 1: #Asfaltar ruas menu adicional
                    os.system('cls||clear')
                    if asfalto == 1:
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
                                asfalto = 1
                                print("Comprado!")
                                sleep(1)
                            else:
                                print("Não tem o dinheiro necessário.")
                                print("Voltando ao menu")
                                sleep(2)
                elif acao2 == 2: #Escola EF menu adicional
                    os.system('cls||clear')
                    if escolaef == 1:
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
                                escolaef = 1
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
                    if parquearbo == 1:
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
                                parquearbo = 1
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
                    if sanea == 1:
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
                                sanea = 1
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
                    if ceram == 1:
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
                                ceram = 1
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
                salvar(info)
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
                if habitantes>=10000 and qntdmelhorias>= 5:
                    acao, lvl = cidadepar(nomecidade)
            elif int(acao) == 0: #Sair
                info = [dinheiro, felicidade, qntdmelhorias, taxades, habitantes, lucro, meses, lvl, info[8], info[9], info[10], info[11], info[12], info[13], info[14]]
                salvar(info)
                return info
            else:
                print("Opção não encontrada, tente novamente.")
        else:
            print("Opção não encontrada, tente novamente.")
            acao = 0
        os.system('cls||clear')
    lvl += 1
    info = [dinheiro, felicidade, qntdmelhorias, taxades, habitantes, lucro, meses, lvl, info[8], info[9], 0, 0, 0, 0, 0]
    salvar(info)
    return info
        
def menucid(nomecidade, info): #Função com o menu para a cidade
    shop = info[10] ; escolaem = info[11]; centroeve = info[12]; peolico = info[13]; centrotec = info[14]
    x = 0 ; dinheirosalvo = info[0] ; felicidade = info[1] ; qntdmelhorias = info[2] ; taxades = info[3] ; habitantes = info[4] ; lucro = info[5] ; meses = info[6] ; lvl = info[7]
    dinheiro = sistemamon(x, dinheirosalvo)
    acao = "0"
    while int(acao) >= 0: #Loop para manter o menu 
        texto_dinheiro = sisdecimais(dinheiro)
        os.system('cls||clear')
        print("Você tem {}".format(texto_dinheiro))
        print("[1] Informações de", nomecidade)
        print("[2] Melhorias")
        print("[3] Políticas de Governo")
        print("[4] Passar o mês")
        print("[0] Sair")
        acao = input()
        os.system('cls||clear')
        if acao == "1" or acao == "2" or acao == "3" or acao == "4" or acao == "5" or acao == "0": 
            if int(acao) == 1: #Informações da Cidade
                print(cidade)
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
                if shop == 1:
                    print("[#] Construir Shopping")
                else:
                    print("[1] Construir Shopping")
                if escolaem == 1:
                    print("[#] Construir escola de ensino médio")
                else: 
                    print("[2] Construir escola de ensino médio")
                if centroeve == 1:
                    print("[#] Construir centro de eventos")
                else:
                    print("[3] Construir centro de eventos")
                if peolico == 1:
                    print("[#] Construir parque eólico")
                else:
                    print("[4] Construir parque eólico")
                if centrotec == 1:
                    print("[#] Criar Centro tecnológico")
                    print("[6] Inovações")
                else:
                    print("[5] Criar Centro tecnológico")
                    print("[#] #########")
                print("[0] Voltar")
                acao2 = int(input())
                if acao2 == 0:
                    acao = acao2
                elif acao2 == 1: #Shopping menu adicional
                    os.system('cls||clear')
                    if shop == 1:
                        print("Melhoria ja comprada")
                        sleep(2)
                        os.system('cls||clear')
                    else:
                        print("Você tem {}".format(texto_dinheiro))
                        print(" ")
                        print("Construir Shopping")
                        print(shopping)
                        print("Custo: 100.000,00 R$")
                        print("Aumenta a felicidade em 10")
                        print("Gera um lucro de 5000,00 R$ por mês")
                        print("Aumenta o crescimento da cidade, por influênciar a modernização do que está ao seu redor")
                        print("[1] Comprar")
                        print("[0] Voltar")
                        acao3 = int(input())
                        os.system('cls||clear')
                        if acao3 == 1: #Comprar 
                            if dinheiro >= 100000:
                                x = -100000
                                dinheiro = sistemamon(x, dinheiro)
                                dinheirosalvo = dinheiro
                                felicidade += 10
                                lucro += 5000
                                qntdmelhorias += 1
                                shop = 1
                                print("Comprado!")
                                sleep(1)
                            else:
                                print("Não tem o dinheiro necessário.")
                                print("Voltando ao menu")
                                sleep(2)
                elif acao2 == 2: #Escola EM menu adicional
                    os.system('cls||clear')
                    if escolaem == 1:
                        print("Melhoria ja comprada")
                        sleep(2)
                        os.system('cls||clear')
                    else:
                        os.system('cls||clear')
                        print("Você tem {}".format(texto_dinheiro))
                        print(" ")
                        print("Construir escola de ensino médio")
                        print(emas)
                        print("Custo: 250.000,00 R$")
                        print("Aumenta a felicidade em 15")
                        print("Gera um lucro de 10.000,00 R$ por mês")
                        print("[1] Comprar")
                        print("[0] Voltar")
                        acao3 = int(input())
                        os.system('cls||clear')
                        if acao3 == 1: #Comprar
                            if dinheiro >= 250000:
                                x = -250000
                                dinheiro = sistemamon(x, dinheiro)
                                dinheirosalvo = dinheiro
                                felicidade += 15
                                lucro += 10000
                                qntdmelhorias += 1
                                escolaem = 1
                                print("Comprado!")
                                sleep(1)
                            else:
                                print("Não tem o dinheiro necessário.")
                                print("Voltando ao menu")
                                sleep(2)
                        else:
                            acao = acao3
                elif acao2 == 3: #Centro de Eventos menu adicional
                    os.system('cls||clear')
                    if centroeve == 1:
                        print("Melhoria ja comprada")
                        sleep(2)
                        os.system('cls||clear')
                    else:
                        os.system('cls||clear')
                        print("Você tem {}".format(texto_dinheiro))
                        print(" ")
                        print("Construir Centro de Eventos")
                        print(centroeventos)
                        print("Custo: 50.000,00 R$")
                        print("Aumenta a felicidade em 25")
                        print("Custo de manutenção de 500,00 R$ por mês")
                        print("[1] Comprar")
                        print("[0] Voltar")
                        acao3 = int(input())
                        os.system('cls||clear')
                        if acao3 == 1: #Comprar
                            if dinheiro >= 50000:
                                x = -50000
                                dinheiro = sistemamon(x, dinheiro)
                                dinheirosalvo = dinheiro
                                lucro -= 500
                                felicidade += 25
                                qntdmelhorias += 1
                                centroeve = 1
                                print("Comprado!")
                                sleep(1)
                            else:
                                print("Não tem o dinheiro necessário.")
                                print("Voltando ao menu")
                                sleep(2)
                        else:
                            acao = acao3
                elif acao2 == 4: #Parque Eólico menu adicional
                    os.system('cls||clear')
                    if peolico == 1:
                        print("Melhoria ja comprada")
                        sleep(2)
                        os.system('cls||clear')
                    else:
                        os.system('cls||clear')
                        print("Você tem {}".format(texto_dinheiro))
                        print(" ")
                        print("Construir parque eólico")
                        print(catavento)
                        print("Custo: 100.000,00 R$")
                        print("Aumenta a felicidade em 5")
                        print("Custo de manutenção de 5.350,00 R$ por mês")
                        print("[1] Comprar")
                        print("[0] Voltar")
                        acao3 = int(input())
                        os.system('cls||clear')
                        if acao3 == 1: #Comprar
                            if dinheiro >= 100000:
                                x = -100000
                                dinheiro = sistemamon(x, dinheiro)
                                dinheirosalvo = dinheiro
                                felicidade += 5
                                lucro -= 5350
                                qntdmelhorias += 1
                                peolico = 1
                                print("Comprado!")
                                sleep(1)
                            else:
                                print("Não tem o dinheiro necessário.")
                                print("Voltando ao menu")
                                sleep(2)
                        else:
                            acao = acao3
                elif acao2 == 5: #Centro Tecnológico menu adicional
                    os.system('cls||clear')
                    if centrotec == 1:
                        print("Melhoria ja comprada")
                        sleep(2)
                        os.system('cls||clear')
                    else:
                        os.system('cls||clear')
                        print("Você tem {}".format(texto_dinheiro))
                        print(" ")
                        print("Construir Centro Tecnológico")
                        print(tecnologia)
                        print("Custo: 350.000,00 R$")
                        print("Aumenta a felicidade em 10")
                        print("Gera um lucro de 12.500,00 R$ por mês")
                        print("[1] Comprar")
                        print("[0] Voltar")
                        acao3 = int(input())
                        os.system('cls||clear')
                        if acao3 == 1: #Comprar
                            if dinheiro >= 350000:
                                x = -350000
                                dinheiro = sistemamon(x, dinheiro)
                                dinheirosalvo = dinheiro
                                lucro += 12500
                                felicidade += 10
                                qntdmelhorias += 1
                                centrotec = 1
                                print("Comprado!")
                                sleep(1)
                            else:
                                print("Não tem o dinheiro necessário.")
                                print("Voltando ao menu")
                                sleep(2)
                        else:
                            acao = acao3
                elif acao2 == 6: #Inovações menu adicional
                    if centrotec == 1:
                        dinheiro, lucro, felicidade = inova(dinheiro, lucro, felicidade) #Chama a função de pesquisas
                        os.system('cls||clear')
                    else:
                        print("Para desbloquear essa seção compre o Centro Tecnológico")
                        os.system('cls||clear')
            elif int(acao) == 3: # Políticas de Governo
                print("[1] Legalizar a maconha")
                print("[2] Reduzir impostos sobre atividades religiosas")
                print("[3] Incentivar a pesquisa agrícola")
                print("[4] Proibir o uso de caixas de som em praias públicas")
                print("[5] Regulamentar a extração de pérolas")
                print("[0] Voltar")
                acao2 = int(input())
                if acao2 == 0:
                    acao = acao2
                elif acao2 == 1: #Legalizar a maconha
                    os.system('cls||clear')
                    print("Legalizar a maconha")
                    print(maconha)
                    print("Diminui a felicidade em 15")
                    print("Gera lucro pelo imposto sobre a maconha")
                    print("[1] Implantar")
                    print("[0] Voltar")
                    acao3 = int(input())
                    os.system('cls||clear')
                    if acao3 == 1: #Implantar
                        felicidade -= 15
                        lucro += 500
                    else:
                        acao = acao3
                elif acao2 == 2: #Reduzir impostos religiosos
                    os.system('cls||clear')
                    print("Reduzir impostos sobre atividades religiosas")
                    print(cruz)
                    print("Aumenta a felicidade em 15")
                    print("Diminui a arrecadação de impostos")
                    print("[1] Implantar")
                    print("[0] Voltar")
                    acao3 = int(input())
                    os.system('cls||clear')
                    if acao3 == 1: #Implantar
                        felicidade += 15
                        lucro -= 1000
                    else:
                        acao = acao3
                elif acao2 == 3: #Incentivar a pesquisa agrícola
                    os.system('cls||clear')
                    print("Incentivar a pesquisa agrícola")
                    print(plantacao)
                    print("Diminui a felicidade em 5")
                    print("Aumenta os gastos com pesquisas")
                    print("[1] Implantar")
                    print("[0] Voltar")
                    acao3 = int(input())
                    os.system('cls||clear')
                    if acao3 == 1: #Implantar
                        felicidade -= 5
                        lucro -= 750
                    else:
                        acao = acao3
                elif acao2 == 4: #Proibir o uso de caixas de som em praias públicas
                    os.system('cls||clear')
                    print("Proibir o uso de caixas de som em praias públicas")
                    print(praia)
                    print("Aumenta a felicidade em 5")
                    print("Não tem efeito sobre a economia")
                    print("[1] Implantar")
                    print("[0] Voltar")
                    acao3 = int(input())
                    os.system('cls||clear')
                    if acao3 == 1: #Implantar
                        felicidade += 5
                        lucro += 0
                    else:
                        acao = acao3
                elif acao2 == 5: #Regulamentar a extração de pérolas
                    os.system('cls||clear')
                    print("Regulamentar a extração de pérolas")
                    print(ostra)
                    print("Diminui a felicidade em 15")
                    print("Cria um imposto sobre a extração de pérolas")
                    print("[1] Implantar")
                    print("[0] Voltar")
                    acao3 = int(input())
                    os.system('cls||clear')
                    if acao3 == 1: #Implantar
                        felicidade -= 15
                        lucro += 100
                    else:
                        acao = acao3
                os.system('cls||clear')
            elif int(acao) == 4: #Passar o mês
                salvar(info)
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
                if habitantes>=50000 and qntdmelhorias>= 12:
                    acao = cidadepar(nomecidade)
            elif int(acao) == 0: #Sair
                return 0
            else:
                print("Opção não encontrada, tente novamente.")
        else:
            print("Opção não encontrada, tente novamente.")
            acao = 0
        os.system('cls||clear')
    lvl += 1
    info = [dinheiro, felicidade, qntdmelhorias, taxades, habitantes, lucro, meses, lvl, info[8], info[9], 0, 0, 0, 0, 0]
    salvar(info)
    return info
        
def main():
    os.system('cls||clear')
    info = intro()
    lvl = info[7]
    os.system('cls||clear')
    if info[7] == 0:
        nomecidade = "Error"
        confirma = "N"
        while confirma != "S":
            nome = input("Como você gostaria de ser chamado? ")
            print("Deseja que seu nome seja", nome, "? Você não poderá mudar depois. (S/N)")
            confirma = input().upper()
            os.system('cls||clear') #Limpa o terminal
            info[7] = 1
        info[8] = introducao(nomecidade) #Chamando a introdução do jogo
        info[9] = nome
        os.system('cls||clear')
        nomecidade = info[8]
        lvl = info[7]
        if lvl == 1:
            info = menuvila(nomecidade, info) #Chama o jogo como vila
        elif lvl == 2:
            info = menucid(nomecidade, info) #Chama o jogo como cidade
            
    elif lvl == 1:
        nomecidade = info[8]
        info = menuvila(nomecidade, info) #Continua o jogo como vila
    elif lvl == 2:
        nomecidade = info[8]
        info = menucid(nomecidade, info) #Continua o jogo como cidade
    else:
        print("Fechando o jogo...")
        os.system('cls||clear')
        return
main()