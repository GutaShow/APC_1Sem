# IMPORTS
import msvcrt  # Usado para capturar teclas pressionadas (exclusivo do Windows)
import time    # Usado para atrasos e contagem de tempo
import sys     # Usado para manipular a saída padrão (print letra por letra)
import os      # Usado para limpar o terminal

# VARIÁVEIS
fim=sl1=sl2=sl3=change=restart=acertou=rodando= True
digit = 0.05     # Tempo entre letras ao exibir texto
txt = ''
cont = 0       # Contador da sala 2
chance = 5     # Tentativas na sala 3
ultimo_tempo = time.time()
i = 0

# CÓDIGO PRINCIPAL

os.system('cls')  # Limpa o terminal
nome = input('Insira o seu Nickname: ')  # Recebe o nome do jogador
os.system('cls')

# LOOP PRINCIPAL DO JOGO
while fim:
    
    # SALA 1
    while sl1:
        # Introdução da história
        txt = 'Você acorda em uma sala e não lembra de nada, nem de quem é e nem de como chegou ali. Então você percebe algo em seu bolso e lá está um cartão escrito'
        for letra in txt:
            sys.stdout.write(letra)
            sys.stdout.flush()
            time.sleep(digit)
        print()

        txt = f'"Olá {nome}, você deve estar se perguntando como veio parar aqui, bem isso não importa, mas o que precisa saber e que está em um teste para ver as suas capacidades de sobrevivência, tente passar pelas 3 salas e receberá uma recompensa"'
        time.sleep(1)
        for letra in txt:
            sys.stdout.write(letra)
            sys.stdout.flush()
            time.sleep(digit)
        print()

        txt = 'e ao olhar ao redor você vê nessa sala alguns móveis mas 3 coisas mais te chamam a atenção, esse itens são uma estante de livros raros, uma porta, e um baú e você sente que essas 3 coisas são importantes para poder escapar'
        time.sleep(1)
        for letra in txt:
            sys.stdout.write(letra)
            sys.stdout.flush()
            time.sleep(digit)
        print()
        dnv=''
        # Escolha do jogador
        option = int(input('Escolha um objeto: 1-Estante | 2-Porta | 3-Baú: '))
        
        if option == 1:
            # Caminho correto
            txt = 'Você escolhe o caminho 1. Quando você vê esses livros raros percebe que eles estão desorganizados, então decide organizar eles com o nome dos autores em ordem alfabética e percebe que juntando as iniciais dos títulos se forma "Saída", e a estante se revela uma porta secreta'
            time.sleep(1)
            for letra in txt:
                sys.stdout.write(letra)
                sys.stdout.flush()
                time.sleep(digit)
            print()
            time.sleep(1)
            os.system('cls')
            sl1 = False  # Sai da sala 1
            option = ''
        
        elif option == 2:
            # Morte pelo leão
            txt = 'Você escolhe o caminho 2. você vai em direção a porta com ansiedade acreditando que esse era o caminho para a saída, mas ao abrir a porta se depara com um leão faminto, então você gela e consumido pelo medo vc nao consegue mexer as suas pernas para tentar fugir e você devorado'
            time.sleep(1)
            for letra in txt:
                sys.stdout.write(letra)
                sys.stdout.flush()
                time.sleep(digit)
            print()
            
            # Menu de reinício
            while restart:
                dnv = input('VOCÊ MORREU... Tentar novamente? (S/N): ')
                if dnv == 's':
                    restart = False
                    os.system('cls')
                elif dnv == 'n':
                    i+=100
                    restart=sl1=sl2=sl3=fim=False  # Termina tudo
                else:
                    print('Tecla inválida. Tente novamente.')
                    time.sleep(1)
                    os.system('cls')
        
        elif option == 3:
            # Morte pelas cobras
            txt = 'Você escolhe o caminho 3. ao perceber o baú a sua frente vc acredita que nele possa ter alguma resposta para a sua saída ou então alguma coisa que possa lhe agradar, mas ao abrir o baú você é surpreendido com um monte de cobras venenosas que pulam na sua cara'
            time.sleep(1)
            for letra in txt:
                sys.stdout.write(letra)
                sys.stdout.flush()
                time.sleep(digit)
            print()

            while restart:
                dnv = input('VOCÊ MORREU... Tentar novamente? (S/N): ')
                if dnv == 's':
                    restart = False
                    os.system('cls')
                elif dnv == 'n':
                    i+=100
                    restart=sl1=sl2=sl3=fim=False
                else:
                    print('Tecla inválida. Tente novamente.')
                    time.sleep(1)
                    os.system('cls')
        
        else:
            print('Número inválido. Tente novamente.')
            time.sleep(1.5)
            os.system('cls')
    # SALA 2
    while sl2:
        txt = 'As portas se fecham, começa uma contagem regressiva de 30 segundos, logo você percebe as paredes se fechando lentamente… e uma voz em uma caixa de som ecoa na sala… Este é seu próximo desafio para tentar sobreviver e ver a luz do dia novamente, há 3 opções para você escapar, um tubo de metal no chão, um alçapão que está escondido embaixo de toda essa água e uma porta inalcançável, tão distante que você não será capaz de correr o suficiente para alcançá-la. Boa sorte jogador, que os jogos comecem….'
        for letra in txt:
            sys.stdout.write(letra)
            sys.stdout.flush()
            time.sleep(digit)
        print()

        option = ''
        rodando = True
        dnv=''

        # Inicia contagem de tempo (15 segundos)
        while rodando and cont < 15:
            agora = time.time()
            if agora - ultimo_tempo >= 1:
                cont += 1
                ultimo_tempo = agora

            # Atualiza linha no terminal
            sys.stdout.write(f'\rContador: {cont:<3} | Digite: {option} ')
            sys.stdout.flush()

            # Captura tecla do jogador
            if msvcrt.kbhit():
                tecla = msvcrt.getwch()
                if tecla == '\r' and option.strip():
                    rodando = False
                elif tecla == '\b':
                    option = option[:-1]
                elif tecla in '\x00\xe0':
                    msvcrt.getwch()  # Ignora teclas especiais
                else:
                    option += tecla

                # Avalia a escolha
                if rodando == False:
                    if option == '1':
                        txt='\nVocê escolheu o caminho 1. Você vê um tubo de metal bem resistente e no desespero bota ele contra as paredes que estão se aproximando ele suporta por um tempo, mas logo as paredes voltam a se mexer e você é esmagado'
                        time.sleep(1)
                        for letra in txt:
                            sys.stdout.write(letra)
                            sys.stdout.flush()
                            time.sleep(digit)
                        print()
                        while restart:
                            dnv=input('VOCE MORREU... Deseja tentar novamente? Digite S para tentar novamente|Digite N para desistir: ')
                            if dnv=='s':
                                restart=False
                                os.system('cls')
                            elif dnv=='n':
                                i+=100
                                restart=sl1=sl2=sl3=fim=False
                            else:
                                print('Tecla Invalida. Tente novamente')
                                time.sleep(1)
                                os.system('cls')
                    elif option == '2':
                        txt='\nVocê escolheu o caminho 2. Ao saber que tem um alçapão embaixo da água que cobria os seus pés começa uma busca desesperada por ele e após uma longa procura você o encontra, e ao abrir você simplesmente pula pois não tem tempo de pensar, mas ao perceber vc estava pulando em um incinerador'
                        time.sleep(1)
                        for letra in txt:
                            sys.stdout.write(letra)
                            sys.stdout.flush()
                            time.sleep(digit)
                        print()
                        while restart:
                            dnv=input('VOCE MORREU... Deseja tentar novamente? Digite S para tentar novamente|Digite N para desistir: ')
                            if dnv=='s':
                                restart=False
                                os.system('cls')
                            elif dnv=='n':
                                i+=100
                                restart=sl1=sl2=sl3=fim=False
                            else:
                                print('Tecla Invalida. Tente novamente')
                                time.sleep(1)
                                os.system('cls')
                    elif option == '3':
                        txt='\nVocê escolhe o caminho 3. Desesperado por não conseguir pensar direito você apenas corre enquanto a pessoa falava no auto falante e com isso dando de chegar bem a tempo e se salvando da morte certa'
                        time.sleep(1)
                        for letra in txt:
                            sys.stdout.write(letra)
                            sys.stdout.flush()
                            time.sleep(digit)
                        print()
                        time.sleep(1)
                        os.system('cls')
                        sl1=sl2=rodando=False
                    else:
                        txt='\nVocê hesita ou digita algo incorreto. Enquanto pensa, as paredes se fecham e te esmagam.'
                        time.sleep(1)
                        for letra in txt:
                            sys.stdout.write(letra)
                            sys.stdout.flush()
                            time.sleep(digit)
                        print()
                        while restart:
                            dnv=input('VOCE MORREU... Deseja tentar novamente? Digite S para tentar novamente|Digite N para desistir: ')
                            if dnv=='s':
                                restart=False
                                os.system('cls')
                            elif dnv=='n':
                                i+=100
                                restart=sl1=sl2=sl3=fim=False
                            else:
                                print('Tecla Invalida. Tente novamente')
                                time.sleep(1)
                                os.system('cls')


    # SALA 3
    while sl3:
        txt = 'Ao entrar na sala, você percebe que ela é diferente das anteriores, nessas sala só existe um piano e onde era pra ter uma partitura apenas diz para adivinhar qual a sequência de letras para poder escapar antes que a sala exploda, e ao olhar para as teclas você percebe que cada uma delas corresponde a uma letra'
        for letra in txt:
            sys.stdout.write(letra)
            sys.stdout.flush()
            time.sleep(digit)
        print()

        chance=5
        acertou=True

        while chance > 0 and acertou:
            # Coleta as 3 letras do jogador
            tl1 = input(f'Você tem {chance} chances | Letra 1: ')
            tl2 = input(f'Você tem {chance} chances | Letra 2: ')
            tl3 = input(f'Você tem {chance} chances | Letra 3: ')

            if tl1 == 'e' and tl2 == 'x' and tl3 == 't':
                # Acertou a sequência
                os.system('cls')
                txt = 'Ao acertar a sequência uma porta se abre que de lá sai uma luz brilhante e ofuscante e quando você percebe, estava sonhando e acaba de acordar de um terrível pesadelo…'
                time.sleep(1)
                for letra in txt:
                    sys.stdout.write(letra)
                    sys.stdout.flush()
                    time.sleep(digit)
                print()
                acertou=sl3=False
                dnv=''
            else:
                # Errou
                print('Você errou. Tente novamente.')
                chance -= 1
                time.sleep(1)
                os.system('cls')
                if chance <= 0:
                    # Sem mais chances — fim
                    print('Você perdeu todas as chances. A sala explode!')
                    while restart:
                        dnv = input('VOCÊ MORREU... Tentar novamente? (S/N): ')
                        if dnv == 's':
                            restart = False
                            os.system('cls')
                        elif dnv == 'n':
                            i+=100
                            restart=sl1=sl2=sl3=fim=False
                        else:
                            print('Tecla inválida. Tente novamente.')
                            time.sleep(1)
                            os.system('cls')

    # CRÉDITOS FINAIS
    creditos = [
        "Escape Room o Jogo",
        "",
        "Diretora: Prof. Marcia",
        "Produtor: Gustavo",
        "Roteiro: Nicolas",
        "Elenco de nomes aleatórios:",
        "  - Leonardo DiCaprio",
        "  - Taylor Swift",
        "  - Cristiano Ronaldo",
        "  - Oprah Winfrey",
        "  - Elon Musk",
        "  - Emma Watson",
        "  - Barack Obama",
        "",
        "Música Original: Banda Sem Instrumentos",
        "",
        "Agradecimentos Especiais:",
        "  - Comunidade Python",
        "  - Você, espectador!",
        "  - Univille!",
        "",
        "FIM"
    ]

    os.system('cls')
    while i < len(creditos) + 10:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa terminal

        # Mostra até 10 linhas por vez no estilo "rolando"
        inicio = max(0, i - 10)
        for linha in creditos[inicio:i]:
            print(linha.center(80))

        time.sleep(0.5)
        i += 1
        fim = False