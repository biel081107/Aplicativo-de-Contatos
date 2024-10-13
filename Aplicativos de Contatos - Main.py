#APLICATIVOS DE CONTATO

from MinhasFunções.texto import titulo,menu,linha,cronometro
opc = ['VER LISTA DE CONTATOS','ADICIONAR NOVO CONTATO','EDITAR CONTATO','APAGAR CONTATO','FINALIZAR PROGRAMA']

while True:
    #ESCOLHA DO USUARIO
    titulo('BEM VINDO A SUA LISTA DE CONTATOS','\033[1;95m')
    menu(opc,'\033[1;3;95m')
    linha('\033[1;95m',20)
    escolha = int(input('\033[1;97mQUAL VOCE ESCOLHE: \033[m'))
    cronometro(2,'RESPOSTA ENVIADA COM SUCESSO','\033[1;92m')

    #VERIFICANDO SE O USUARIO DIGITOU AS RESPOSTAS CORRETAMENTE
    if escolha > len(opc) - 1 or escolha < 0:
        while escolha > len(opc) - 1 or escolha < 0:
            print('\033[1;91mOPÇÃO INVALIDA!! VERIFIQUE SE DIGITOU CORRETAMENTE E TENTE NOVAMENTE')
            escolha = int(input('\033[1;97mQUAL VOCE ESCOLHE: \033[m'))
        cronometro(2,'RESPOSTA ENVIADA COM SUCESSO','\033[1;92m')

    #ABRIR LISTA DE CONTATOS (ARQUIVO MODO LEITURA)
    if escolha == 0:
        try:
            x = open('listadecontatos.txt','rt') #TENTAR ABRIR O CODIGO PARA A LEITURA
            y = x.readlines() #TRANSFORMO TODAS AS LINHAS EM LISTAS
            if len(y) == 0:
                z = open('listadecontatos.txt','wt')
                print(f'\033[1;91mNÃO HÁ NENHUM CONTATO, ADICIONE SEUS PRIMEIROS CONTATOS')
                nome = str(input('\033[1;97mQUAL SERA O NOME DO CONTATO: '))
                numero = int(input('QUAL SERA O NUMERO DO CONTATO: \033[m'))
                z.write(f'\033[1;94m{f'{nome:<46}'.upper()}\033[m \033[1;91m{numero}\033[m\n')
                z.close()
                print(f'\033[1;93mESTAMOS CRIANDO SEUS CONTATOS..\033[m')
                cronometro(3,'CONTATO CRIADO COM SUCESSO!','\033[1;92m')

            #DEIXAR BONITO
            titulo('LISTA DE CONTATOS', '\033[1;94m')
            for v,c in enumerate(y):
                print(f'\033[1;97m{v} - {c.replace('\n','')}')
        except:
            print(f'\033[1;93mESTAMOS CRIANDO UM ARQUIVO PARA SEUS CONTATOS: ')
            cronometro(3,'ARQUIVO CRIADO COM SUCESSO','\033[1;93m')
            x = open('listadecontatos.txt','x') #CRIAR O ARQUIVO CASO NÃO EXISTA

    #ADICIONAR NOVO CONTATO ( ARQUIVO MODO APPEND )
    elif escolha == 1:
        x = open('listadecontatos.txt','at')
        z = open('listadecontatos.txt','rt')
        y = z.readlines()
        nome = str(input('\033[1;97mQUAL SERA O NOME DO CONTATO: '))
        numero = int(input('QUAL SERA O NUMERO DO CONTATO: \033[m'))
        x.write(f'\033[1;94m{f'{nome:<46}'.upper()}\033[m \033[1;91m{numero}\033[m\n')
        x.close()
        z.close()
        print(f'\033[1;92mADICIOANDO NOVO CONTATO...\033[m')
        cronometro(3, 'CONTATO ADICIONADO COM SUCESSO!', '\033[1;92m')

    #EDITAR UM CONTATO JA EXISTE
    elif escolha == 2:
        z = open('listadecontatos.txt','rt')
        y = z.readlines() #CRIEI UMA LISTA COM TODOS OS CONTATOS

        #MOSTRAR LISTA DE CONTATOS PARA O USUARIO ESCREVER QUAL DESEJA EDITAR
        titulo('LISTA DE CONTATOS', '\033[1;94m')
        for v, c in enumerate(y):
            print(f'\033[1;97m{v} - {c.replace('\n', '')}')

        #PERGUNTAR QUAL ELE DESEJA EDITAR COM TRATAMENTO DE ERRO
        w = str(input('\033[1;95mDIGITE O NUMERO DO CONTATO QUE VOCÊ DESEJA EDITAR: \033[m'))
        try:
            w = int(w) #TENTEI TRANSFORMAR EM NUMERO, CASO DER ERRO É PQ FUI INSERIDO UM CARACTERE
        except:
            print(f'\033[1;91mOCORREU UM ERRO, VERIFIQUE SE DIGITOU O NUMERO CORRTAMENTE')
            while not w.isnumeric():
                print(f'\033[1;91mOCORREU UM ERRO, VERIFIQUE SE DIGITOU O NUMERO CORRTAMENTE')
                w = str(input('DIGITE O \033[1;91mNUMERO\033[m DO CONTATO QUE VOCÊ DESEJA EDITAR: '))

        #TRANSFORMA A STRING EM UM NUMERO
        w = int(w)

        #VERIFICAR SE O NUMERO DE W ESTA ENTRE OS NUMEROS POSSIVEIS DE CONTATOS
        if w > len(y) or w < 0:
            while w > len(y) or w < 0:
                print(f'\033[1;91mO NUMERO DIGITADO ULTRAPAÇOU OU É MENOR QUE O NUMERO DE CONTATOS')
                w = int(input('\033[1;95mDIGITE O NUMERO DO CONTATO QUE VOCÊ DESEJA EDITAR: \033[m'))


        #COMEÇAR A EDIÇÃO
        nome = str(input('\033[1;97mDIGITE UM NOVO NOME PARA O CONTATO: \033[m'))
        numero = int(input('\033[1;97mDIGITE UM NOVO NUMERO PARA O CONTATO: \033[m'))
        y[w] = f'\033[1;94m{f'{nome:<46}'.upper()}\033[m \033[1;91m{numero}\033[m\n'
        print(f'\033[1;92mEDITANDO CONTATO...\033[m')
        cronometro(3,'CONTATO EDITADO COM SUCESSO','\033[1;92m')

        #ABRIR LISTA PARA EDIÇÃO
        x = open('listadecontatos.txt','wt')
        novo = x.writelines(y) #EDITA COM TODAS AS LINHAS
        z.close()
        x.close()


    #APAGAR CONTATO
    elif escolha == 3:
        z = open('listadecontatos.txt', 'rt')
        y = z.readlines()  # CRIEI UMA LISTA COM TODOS OS CONTATOS

        # MOSTRAR LISTA DE CONTATOS PARA O USUARIO ESCREVER QUAL DESEJA APAGAR
        titulo('LISTA DE CONTATOS', '\033[1;94m')
        for v, c in enumerate(y):
            print(f'\033[1;97m{v} - {c.replace('\n', '')}')


        #PEGANDO NUMERO DO CONTATO QUE DESEJA SER APAGADO
        w = str(input('\033[1;95mDIGITE O NUMERO DO CONTATO QUE VOCÊ DESEJA APAGAR: \033[m'))
        try:
            w = int(w)  # TENTEI TRANSFORMAR EM NUMERO, CASO DER ERRO É PQ FUI INSERIDO UM CARACTERE
        except:
            print(f'\033[1;91mOCORREU UM ERRO, VERIFIQUE SE DIGITOU O NUMERO CORRTAMENTE')
            while not w.isnumeric():
                print(f'\033[1;91mOCORREU UM ERRO, VERIFIQUE SE DIGITOU O NUMERO CORRTAMENTE')
                w = str(input('DIGITE O \033[1;91mNUMERO\033[m DO CONTATO QUE VOCÊ DESEJA APAGAR: '))
        # TRANSFORMA A STRING EM UM NUMERO
        w = int(w)

        # VERIFICAR SE O NUMERO DE W ESTA ENTRE OS NUMEROS POSSIVEIS DE CONTATOS
        if w > len(y) or w < 0:
            while w > len(y) or w < 0:
                print(f'\033[1;91mO NUMERO DIGITADO ULTRAPAÇOU OU É MENOR QUE O NUMERO DE CONTATOS')
                w = int(input('\033[1;95mDIGITE O NUMERO DO CONTATO QUE VOCÊ DESEJA APAGAR: \033[m'))


        #APAGA A POSIÇÃO DO CONTATO NA LISTA
        del y[w]

        # ABRIR LISTA PARA EDIÇÃO
        x = open('listadecontatos.txt', 'wt')
        novo = x.writelines(y) #EDITA COM TODAS AS LINHAS
        z.close()
        x.close()

        #MENSAGENZINHA PARA DEIXAR UMA INTERAÇÃO LEGAL
        print(f'\033[1;31mESTAMOS APAGANDO O CONTATO...')
        cronometro(3,'CONTATO APAGADO','\033[1;91m')

    #FINALIZAR PROGRAMA
    elif escolha == 4:
        print(f'\033[1;91mFINALIZANDO PROGRAMA...\033[m')
        cronometro(5,'PROGRAMA FINALIZADO COM SUCESSO','\033[1;92m')
        break

#AGRADECIMENTO
titulo('TENHA UMA OTIMA NOITE - MUITO OBRIGADO!!!','\033[1;3;95m')


