class Acao():

    def __init__(self):
        self.escolha=0
        self.acoes = []
        self.acionistas = [('Luis Felipe Nuns', 190, ['bb'], [112])]
        self.operacoesPendentes = [('Venda', 'bb', 1, 2, ('Luis Felipe Nuns', 190, ['bb'], [112])), ('Compra', 'bb', 1, 3, ('Luis Felipe Nuns', 190, ['bb'], [112]))]
        self.operacoesAprovadas = []
    def cadastrarAcao(self):
        acaoNome = input('Nome da ação: ')
        acaoSigla = input('Sigla da ação: ')
        acaoDesc = input('Descrição da ação: ')
        acaoValor = input('Valor da ação: ')
        acaoDados = (acaoNome, acaoSigla, acaoDesc, acaoValor)
        self.acoes.append(acaoDados)
        print('Ação adicionada com sucesso!\n')
        self.menu()

    def cadastrarAcionista(self):
        acionistaNome = input('Nome do acionista: ')
        acionistaDinheiro = int(input('Dinheiro para corretagem do acionista: '))
        acionistaAcoes = []
        querAdicionarMais = True
        
        while querAdicionarMais:
            acao = input('Ações do acionista: ')
            
            if self.verificaSeTemAcao(acao):
                acionistaAcoes.append(acao)
            else:
                print('Nao temos essa ação :(')

            if acionistaAcoes:
                op = int(input('Insira 1 para cadastrar outra ação ou 0 para voltar: '))

                if op != 1 or 0:
                    print('Opção invalida!')
                    op = int(input('Insira 1 para cadastrar outra ação ou 0 para voltar: '))

                if op == 0:
                    break

        acionistaQtdAcoes = []
        for acao in acionistaAcoes:
              qdt = int(input(f'Quantidade de ações no {acao} do acionista'))
              acionistaQtdAcoes.append(qdt)

        acionistaDados = (acionistaNome, acionistaDinheiro, acionistaAcoes, acionistaQtdAcoes)
        self.acionistas.append(acionistaDados)
        print('Acionista adicionado(a) com sucesso!\n')
        self.menu()

    def cadastraTransacao(self):
        transacao = int(input('Compra (1) ou venda(2)?: '))

        match transacao:
            case 1:
                tipoTransacao = "Compra"
            case 2:
                tipoTransacao = "Venda"

        acaoNegociada = input('Ação a ser negociada: ')

        quantidadeDeAcoes = int(input('Quantidade de ação: '))
        precoDaAcao = int(input('Preço da ação: '))

        print('Acionistas: ')
        
        for index, acionistas in enumerate(self.acionistas):
            print(f'[{index}] - {acionistas[0]}')
        
        acionista = int(input('Quem est[a cadastrando: '))
        quemCadastrou = self.acionistas[acionista]

        operacao = (tipoTransacao, acaoNegociada, quantidadeDeAcoes, precoDaAcao, quemCadastrou)
        self.operacoesPendentes.append(operacao)
        print(self.operacoesPendentes)
        self.menu()
    
    def validaTransacao(self):
        while self.operacoesPendentes:
            operaco = self.operacoesPendentes.pop()
            aprovada = False
        
            tipoTransacao, acaoNegociada, quantidadeDeAcoes, precoDaAcao, quemCadastrou = operaco

            if tipoTransacao == 'Compra':
                print('TIPO IGUAL A COMPRA')
                if not self.verificaSeTemAcao(acaoNegociada):
                    # Nao tem acao
                    print('Operação negada: O a ação solicitada na compra não existe.')
                    return

                acaoNome, acaoSigla, acaoDesc, acaoValor = self.retornaAcao(acaoNegociada)

                if int(acaoValor) < int(precoDaAcao):
                    # Preço maior 
                    print('Operação negada: O preço da ação é maior.')
                    return
                
                if quemCadastrou[1] < (precoDaAcao * quantidadeDeAcoes):
                    # Nao pode comprar por que a acao e mais cara
                    print(f'Operação negada: O {quemCadastrou[0]} não tem dinheiro suficiente para fazer a compra.')
                    return

                # Atualizar as informação do acionista
                acionistaNome, acionistaDinheiro, acionistaAcoes, acionistaQtdAcoes = self.retornaAcionista(quemCadastrou)
                precoAcaodoAcionista = acionistaDinheiro - (precoDaAcao * quantidadeDeAcoes)

                for indexDaQdtAcoes, acaoDoAcionista in enumerate(acionistaAcoes):
                    if acaoDoAcionista == acaoNegociada:
                        acionistaQtdAcoes[indexDaQdtAcoes] = acionistaQtdAcoes[indexDaQdtAcoes] + quantidadeDeAcoes

                novosDadosDoAcionista = (acionistaNome, precoAcaodoAcionista, acionistaAcoes, acionistaQtdAcoes)
                self.atualizarDadosAcionista(acionistaNome, novosDadosDoAcionista)
                aprovada = True

            else:
                acionistaNome, acionistaDinheiro, acionistaAcoes, acionistaQtdAcoes = self.retornaAcionista(quemCadastrou)
                # Verificar se ele tem a acao que esta querendo vender
                # Verificar se ele tem a quantidade de acoes que ele esta querendo vender   
                podeValidar = False
                for index, acao in enumerate(acionistaAcoes):
                    if acaoNegociada == acao and acionistaQtdAcoes[index] >= quantidadeDeAcoes:
                        podeValidar = True
                        # Atualiza os dados
                    else:
                        return

                if podeValidar:
                    # Aumentar o dindin
                    # diminuir as acaos que ele esta vendendo
                    acionistaNome, acionistaDinheiro, acionistaAcoes, acionistaQtdAcoes = self.retornaAcionista(quemCadastrou)
                    precoAcaodoAcionista = acionistaDinheiro + (precoDaAcao * quantidadeDeAcoes)

                    for indexDaQdtAcoes, acaoDoAcionista in enumerate(acionistaAcoes):
                        if acaoDoAcionista == acaoNegociada:
                            acionistaQtdAcoes[indexDaQdtAcoes] = acionistaQtdAcoes[indexDaQdtAcoes] - quantidadeDeAcoes

                    novosDadosDoAcionista = (acionistaNome, precoAcaodoAcionista, acionistaAcoes, acionistaQtdAcoes)
                    self.atualizarDadosAcionista(acionistaNome, novosDadosDoAcionista)
                    aprovada = True
                else:
                    print('Operação negada: transação negada.')
            
            if aprovada: 
                self.operacoesAprovadas.append(operaco)
        self.menu()
   
    def listarAcoes(self): 
        acoesTotal = 0
        precoTotal = 0

        for operacao in self.operacoesAprovadas:
            tipoTransacao, acaoNegociada, quantidadeDeAcoes, precoDaAcao, quemCadastrou = operacao

            if tipoTransacao == 'Compra':
                precoTotal += precoDaAcao
                acoesTotal += quantidadeDeAcoes


        print('Total Acões: ', acoesTotal)
        print('Preço Acões: ', precoTotal)
        self.menu()
    # 
    def verificaSeTemAcao(self, acaoCheck):
        
        if not self.acoes:
            return False

        if self.retornaAcao(acaoCheck):
            return True

        return False

    def retornaAcao(self, acaoCheck):
        for acao in self.acoes:
            if acaoCheck == acao[1]:
                return acao

    def retornaAcionista(self, acionistaCheck):
        nomeCheck, acionistaDinheiro, acionistaAcoes, acionistaQtdAcoes = acionistaCheck

        for acionista in self.acionistas:
            if nomeCheck == acionista[0]:
                return acionista

    def atualizarDadosAcionista(self, nomeDoAcionista, novosDados):
        for i, (acionistaNome, acionistaDinheiro, acionistaAcoes, acionistaQtdAcoes) in enumerate(self.acionistas):
            if acionistaNome == nomeDoAcionista:
                self.acionistas[i] = novosDados

    def atualizaDadosAcao(self, silgaAcaoCheck, novosDados):
        for i, (acionistaNome, acionistaDinheiro, acionistaAcoes, acionistaQtdAcoes) in enumerate(self.acionistas):
            if acionistaNome == silgaAcaoCheck:
                self.acionistas[i] = novosDados
        ...

    def menu(self):
        escolha = int(input('[1] - Cadastrar uma ação\n[2] - Cadastrar um acionista\n[3] - Cadastrar uma operação de compra ou venda de ações\n[4] - Efetivar transações\n[5] - Listar ações\n[6] - Encerrar programa\n-> '))

        while escolha!=6:
            
            match escolha:
                case 1:
                    self.cadastrarAcao()
                case 2:
                    self.cadastrarAcionista()
                case 3:
                    self.cadastraTransacao()
                case 4:
                    self.validaTransacao()
                case 5:
                    self.listarAcoes()
                case 6:
                    print('Programa encerrado!')
                    break
                case _:
                    print('Comando não reconhecido, por favor tente novamente!\n')                              


programa = Acao()
programa.menu()