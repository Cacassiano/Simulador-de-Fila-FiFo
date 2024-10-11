        # Simualando a fila de um banco, com listas (FIFO)
def simuladorDeFila(filaInicial:list): 
    print("\n\tSIMULADOR DE FILA\n")
    fila = filaInicial[:]
    clientesAdicionados = 0
    clientesAtendidos = 0
    # loop principal do Simulador
    while True:
        # se a lista estiver vazia ele acaba a simulção automaticamente
        if not fila:
             #chama a função que finaliza a simulação. Recebe a fila antes das alterações(fila inicial) e depois das alteração(fila) alem do quantitativo de clientes que foi adicionado pelo user e o quantitativo dos que foram removidos/atendidos pelo mesmo
            fimDeSimulação(filaInicial, fila, clientesAtendidos,clientesAdicionados)
            #finaliza o loop e, consequentemente, o programa.
            break 
        # pergunta o que usuaio deseja fazer: adicionar cliente, retiarar/atender cliente ou sair do programa
        resposta= int(input("Se deseja adicionar mais alguma pessoa a fila digite 1\nSe deseja atender a primeira pessoa da fila digite 2\nSe quiser finalizar a simulação digite 0\nDigite aqui: "))
        # se o usuario digitar 0 ele finaliza a simulação
        if resposta == 0:
            #chama a função que finaliza a simulação. Recebe a fila antes das alterações(fila inicial) e depois das alteração(fila) alem do quantitativo de clientes que foi adicionado pelo user e o quantitativo dos que foram removidos/atendidos pelo mesmo
            fimDeSimulação(filaInicial, fila, clientesAtendidos,clientesAdicionados)
            # finaliza o loop e, consequentemente, o programa
            break 
        # se ele quiser adicionar alguém a fila.
        elif resposta == 1:
            # chama a função de adicionar clientes. recebe a fila de clientes
            adicionarCliente(fila)
            #adiciona 1 ao quantitativo e clientes adicionados pelo usuario
            clientesAdicionados += 1
        # se o user quiser remover/atender uma pessoa da fila 
        elif resposta == 2:
            # chama a função de remover o cliente
            removerCliente(fila)
            # adiciona 1 ao quantitativo de clientes que foram atendidos/removidos
            clientesAtendidos += 1
        # se o user  não escreveu nenhuma das 3 opções o programa da erro e finaliza
        else:
            print("Erro você escreveu algo de errado.")
            #finaliza o loop e, consequentemente, o programa.
            break
# Recebe a fila de clientes e devolve a fila + 1 elemento que o usuario escolhe
def adicionarCliente(fila:list):   
    # while true permite que eu faça uma validaçao de formulario
    while True:
        # nome do cliente que vai ser adicionado
        clienteNome= input("Digite aqui o nome deste cliente: ")
        # serve para validar se o user realmente quer adicionar o nome que escreveu. Se escrever 1 o nome é salvo se não ele pode escrever outro nome
        confirmação = int(input("Tem certeza de que deseja adicionar %s a fila(1 para confirmar e qualquer outro numero para escrever outro nome): " % clienteNome))
        # se ele escrever 1 ele confirma que quer adicionar o nome em questão a fila
        if confirmação == 1:
            # adiciona o nome a fila
            fila.append(clienteNome)
            print("O cliente %s foi adicionado ao fim da fila\n" % fila[-1])
            # finalizaa a funçao e voltamos para o simulador
            break
        # se ele não confirmar o nome
        else:
            print("tente novamente")
            # ao final o programa recomeça e ele pode escrever outro nome o variavel "clienteNome"
# remove o cliente mais velho da lista
def removerCliente(fila:list):
    # apaga o cliente mais antigo (ou sendo, o primeiro cliente e guarda o seu valor, ou seja, seu nome)
    atendido = fila.pop(0)
    # mostra qual  cliente foi atendido
    print("Você atendeu o cliente: %s\n" % atendido)
# essa função diz tudo o que o usuario fez até que o programa fosse finalizado, tipo umas estatistica de um jogo.
def fimDeSimulação(filaInicial:list, fila: list,clientesAtendidos:int, clientesAdicionados:int):
    # mostra todos os feitos do usuario dentro da simulação
    print("Fim da simulação!\nSua fila inicial foi: ",filaInicial,"\nSua fila final foi: ",fila,"\nAtendeu um total de %d clientes\nE adicionou %d clientes a fila" % (clientesAtendidos,clientesAdicionados))
    # checa e diz se o usuario atendeu todos os clientes
    if not fila:
        print("Você atendeu todos os clientes.")
    else:
        print("Você não atendeu todos os clientes")
# essa função tem o dever de criar a fila inicial e inicializar a simulação
def IniciandoPrograma():
    filaInicial = []
    # serve para indicar para o usuario qual é a posição do item que ele esta inserindo. 1 primeira posição, 2 segundo e etc
    numDaFila = 1
     # while true permite que eu faça uma validaçao de formulario e tambem permite o usuario adicionar quantos nomes quiser na lista inicial
    while True:  
        # Recebe o nome que o user quer adicionar e fala qual a sua posição com '%d°'
        nomes = input("Escreva aqui o nome do %d° cliente que vai fazer parte da sua fila de atendimentos(digite \"/start\" para começar a simulação): "% numDaFila)
        # checa se o usuario pode iniciar o simulador. Isto é, se ele escreveu o comando /start e tem ao menos 1 cliente na fila
        if nomes == "/start" and filaInicial:
            # inicializa o simulador
            simuladorDeFila(filaInicial)
            # para o loop depois de usar o simulador
            break
        # mensagem de erro aparece se tentar iniciar a simulação com a fila vazia 
        elif nomes == "/start" and not filaInicial:
            print("Você não pode iniciar o programa sem ao menos 1 nome dentro da sua fila inicial")
        # Analisa o nome que o usuario escreveu e faz uma validação
        else:    
            # pede a confirmação do user para adicionar o nome a lista dele
            confirmar = int(input("Tem certeza de querer adicionar o nome %s a sua fila (1 para sim e 0 para não): " % nomes))
            # se o usuario quiser mudar/escrever outro nome 
            if confirmar == 0:
                print("Tente Novamente.")
                # iguala o numero que vai aparecer la em cima para o usuario escrever sem nenhuma confusão
                numDaFila -= 1
            # confirma para que não haja nomes me branco
            elif nomes == "":
                print("Nome invalido. Tente novamente.")
                # iguala o numero que vai aparecer la em cima para o usuario escrever sem nenhuma confusão
                numDaFila -=1
            # se passsar pela validação de formulario adiciona o nome a lista
            else: 
                # adiciona o nome escrito a fila inicial
                filaInicial.append(nomes)
            # a cada loop adiciona 1 ao numero que se refere ao indice dentro da fila. (Cassio do futuro, me desculpa, não sei explicar em plalavras,mas se você ler o código você vai entender)
            numDaFila +=1
# inicializa a função de iniciar o programa
IniciandoPrograma()

