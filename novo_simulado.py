import time

velocidade = 0.5

verde = "\033[1;32m"
vermelho = "\033[1;31m"
azul = "\033[1;34m"
amarelo = "\033[1;33m"
reset = "\033[0m"

def apresentar (numero, exercicio, objetivo, cenario, regras):
    print()
    time.sleep(velocidade)
    print("-" * 30)
    print (f"{amarelo}⭐ Exercicio {numero}{reset}: {exercicio}\n")
    print (f"{amarelo}Objetivo:{reset} {objetivo}")
    print (f"{amarelo}Cenário:{reset} {cenario}")
    print (f"{amarelo}Regras:{reset}\n{regras}\n")
    time.sleep(velocidade)

def dados_entrada(textos):
    print (f"{amarelo}Dados de Entrada:{reset}")
    for texto in textos:
        time.sleep(velocidade)
        print (f"{vermelho}- {texto}{reset}")

looping = True

while looping:

    print (60*'=' + "\n")
    print (f"📌- Atividades para praticar limpeza de dados:\n")
    time.sleep(velocidade*2)
    escolha = input(f"{azul}Digite o número do exercício desejado ou 0 para sair:{reset}\n")
    print ()

    if escolha == "0":
        time.sleep(velocidade)
        print ("Encerrando o programa. Até a próxima!")
        looping = False
        break

    elif escolha == "1":
        apresentar(
            1,
            "Limpeza de Comentários de Clientes",
            "Transformar dados 'sujos' em limpos para a IA ler.",
            "Você recebeu comentários de clientes mas eles estão bagunçados (letras maiúsculas misturadas, espaços no começo e fim). Sua missão é padronizar tudo.",
            "- Remova os espaços extras das pontas (começo e fim).\n- Deixe todo o texto em letras minúsculas.\n- Filtre e mantenha apenas os comentários que contêm a palavra 'ruim' (para análise de qualidade).",
        )

        comentarios = [
            "  A comida estava ótima! ",
            "O lanche chegou FRIO e RUIM",
            "Demorou muito  ",
            "Sabor muito ruim e atendimento péssimo   ",
            "Nota 10, adorei!"
        ]

        dados_entrada(comentarios)

        comentarios_limpos = []
        comentarios_tratado = []

        print (f"{amarelo}\nDados Tratados:{reset}")
        for comentario in comentarios:
            time.sleep(velocidade)
            comentario_tratado = comentario.strip().lower()
            comentarios_tratado.append(comentario_tratado)
            print (f"{verde} -> {comentario_tratado}{reset}")
            if "ruim" in comentario_tratado:
                comentarios_limpos.append(comentario_tratado)

        time.sleep(velocidade)
        print (f"\n{azul}Comentários finais para análise de qualidade:{reset} {amarelo}{comentarios_limpos}{reset}")
        
    elif escolha == "2":
        apresentar(
            2,
            "O Faxina nos CPFs",
            "Praticar manipulação de strings e condicionais.",
            "O banco de dados de uma empresa tem CPFs cadastrados de qualquer jeito (com ponto, sem ponto, com letra errada).",
            "- Limpar a pontuação e guardar numa lista nova apenas os CPFs válidos (que sobraram apenas números e têm exatamente 11 dígitos)."
        )

        cpfs_sujos = [
            "123.456.789-00",
            "11122233344",
            "abc.123.456-78",
            "999.888.777-6"
        ]

        dados_entrada(cpfs_sujos)

        cpfs_limpos = []

        print ("\nDados Tratados:\n")
        for cpf in cpfs_sujos:
            time.sleep(velocidade)
            cpf_limpo=cpf.replace(".", "").replace("-", "")
            if cpf_limpo.isdigit() and len(cpf_limpo) == 11:
                cpfs_limpos.append(cpf_limpo)
                print (f"{verde} -> {cpf_limpo}{reset}")
        time.sleep(velocidade)
        print (f"\n{azul}CPFs Válidos:{reset} {amarelo}{cpfs_limpos}{reset}")

    elif escolha == "3":
        apresentar (
            3,
            "O Conversor de Preços",
            "Praticar manipulação de strings e conversão de tipos.",
            "O sistema recebeu valores em Reais (R$ 10,00) com vírgula, mas para cálculos precisamos deles como Float puro (10.00).",
            "- Transformar em números decimais.\n- Tirar os espaços.\n- Tirar o 'R$'.\n- Trocar a vírgula por ponto.\n- Converter o texto final para número."
        )
        precos_texto = ["R$ 19,90", "R$ 5,00", " 10,50 "]
        precos_formatados = []

        dados_entrada(precos_texto)

        print ("\nDados Tratados:\n")
        for preco in precos_texto:
            preco_formatado = preco.replace("R$","").replace(",",".").strip()
            preco_float = float(preco_formatado)
            precos_formatados.append(preco_float)
            time.sleep(velocidade)
            print (f"{verde} -> {preco_float}{reset}")

        print (f"\n{azul}Preços Formatados:{reset} {amarelo}{precos_formatados}{reset}")

    elif escolha == "4":
        apresentar (
            4,
            "O Tratador de Números de Telefone",
            "Praticar manipulação de strings.",
            "Uma lista de números de telefone está bagunçada, com parênteses, traços, espaços e até código do país (+55).",
            "- Limpar todos os caracteres especiais.\n- Deixar apenas os números puros (exemplo: 11999998888)."
        )
        telefones = [
            "(11) 99999-8888",
            "+5511999998888",
            "11 99999-8888"
        ]

        dados_entrada(telefones)

        print ("\nDados Tratados:\n")
        telefones_tratados = []
        for telefone in telefones:
            telefone_tratado = telefone.replace("(","").replace(")","").replace("-","").replace(" ","").replace("+55","").strip()
            telefones_tratados.append(telefone_tratado)
            time.sleep(velocidade)
            print (f"{verde} -> {telefone_tratado}{reset}")

    elif escolha == "5":
        apresentar (
            5,
            "O Validador de E-mails",
            "Praticar manipulação de strings e condicionais.",
            "Precisamos limpar os e-mails e garantir que eles sejam minimamente válidos antes de salvar.",
            "- Tirar espaços e deixar minúsculo.\n- Verificar: O e-mail tem que ter @ E tem que ter . (ponto).\n- Salvar na lista nova se tiver os dois."
        )

        emails = [
            "  ANA@gmail.com  ",
            "joao.silva",
            "maria@bol",        
            "SUPORTE@empresa.com.br"
        ]

        dados_entrada(emails)

        for email in emails:
            time.sleep(velocidade)
            print (f"{vermelho}- {email}{reset}")

        print ("\nDados Tratados:\n")
        emails_validos=[]
        for email in emails:
            email_tratado = email.strip().lower()
            if "@" in email_tratado and "." in email_tratado:
                emails_validos.append(email_tratado)
                time.sleep(velocidade)
                print (f"{verde} -> {email_tratado}{reset}")
    elif escolha == "6":
        apresentar (
            6,
            "O Extrator de Primeiros Nomes",
            "Praticar manipulação de strings e listas.",
            "Um restaurante quer personalizar o atendimento chamando os clientes pelo primeiro nome.",
            "- Separar o primeiro nome do nome completo.\n- Salvar numa lista nova apenas os primeiros nomes."
        )

        nomes_completos = [
            "Mayara Alicia",
            "João Silva Souza",
            "Ana"
        ]

        dados_entrada(nomes_completos)

        time.sleep(velocidade)
        for nome in nomes_completos:
            print (f"{vermelho}- {nome}{reset}")    

        primeiros_nomes = []
        print ("\nDados Tratados:\n")
        for nome in nomes_completos:
            pedacos = nome.split()
            primeiros_nomes.append(pedacos[0])
            time.sleep(velocidade)
            print (f"{verde} -> {pedacos[0]}{reset}")
    elif escolha == "7":
        apresentar (
            7,
            "O Calculador de Fretes",
            "Praticar manipulação de strings, listas e condicionais.",
            "Um restaurante quer calcular o frete baseado na distância em km.",
            "- Se a distância for até 5 km (inclusive): O Frete é 0.00.\n- Se for maior que 5 km e até 10 km (inclusive): O Frete é 5.00.\n- Se for maior que 10 km: O Frete é 10.00.\n- Salvar num dicionário: {'Distancia': 7.5, 'Frete': 5.00}."
        )
        distancias = [2.5, 6.0, 12.0, 5.0, 9.9]
        fretes = []

        for distancia in distancias:
            if distancia <= 5:
                frete = 0.00
            elif distancia <= 10:
                frete = 5.00
            else:
                frete = 10.00
            
            viagem = {
                "Distancia": distancia,
                "Frete": frete
            }

            time.sleep(velocidade)
            print (f"{verde} -> Km: {distancia} | Valor: R$ {frete}{reset}")
            fretes.append(viagem)

    elif escolha == "8":
        apresentar (
            8,
            "O Calculador de Descontos",
            "Praticar manipulação de strings, listas e condicionais.",
            "Um restaurante quer aplicar um desconto de R$ 10,00 em pedidos acima de R$ 30,00.",
            "- Verificar o valor do pedido.\n- Se for maior que 30, aplicar desconto de 10.\n- Salvar num dicionário: {'valor_original': 50.00, 'valor_final': 40.00, 'desconto_aplicado': True/False}."
        )

        pedidos = [25.00, 40.00, 100.00, 29.90]
        resultados = []

        for pedido in pedidos:
            
            valor_final = pedido
            aplicou_desconto = False
            
            if pedido > 30:
                valor_final = pedido - 10
                aplicou_desconto = True
                
            resultado = {
                "valor_original": pedido,
                "valor_final": valor_final,
                "desconto_aplicado": aplicou_desconto
            }
            resultados.append(resultado)

            time.sleep(velocidade)
            print (f"{verde} -> Original: R$ {pedido} | Final: R$ {valor_final} | Desconto Aplicado: {aplicou_desconto}{reset}")
    elif escolha == "9":
        apresentar (
            9,
            "O Calculador de Tempos de Entrega",
            "Praticar manipulação de strings, listas e condicionais.",
            "Um restaurante quer calcular o tempo total de entrega baseado na distância em km.",
            "- O tempo base é 20 minutos.\n- Para cada km, adicionar 2 minutos ao tempo total.\n- Salvar num dicionário: {'km': 5, 'minutos_totais': 30}."
        )

        distancias_km = [5, 10, 2, 15]
        tempos = []

        for distancia in distancias_km:
            tempo = {"km": distancia,
            "minutos_totais": 20+(distancia*2)}
            tempos.append(tempo)
            time.sleep(velocidade)
            print (f"{verde} -> Km: {distancia} | Minutos Totais: {20+(distancia*2)}{reset}")
    elif escolha == "10":
        apresentar (
            10,
            "O Classificador de Clientes",
            "Praticar manipulação de strings, listas e condicionais.",
            "Um restaurante quer classificar seus clientes em 'Bronze', 'Prata' ou 'Ouro' baseado na quantidade de pedidos feitos no último mês.",
            "- Se o cliente fez até 10 pedidos (inclusive), a categoria é 'Bronze'.\n- Se fez entre 11 e 50 pedidos (inclusive), a categoria é 'Prata'.\n- Se fez mais de 50 pedidos, a categoria é 'Ouro'.\n- Salvar num dicionário: {'qtd_pedidos': 55, 'categoria': 'Ouro'}."
        )

        historico_pedidos = [2, 55, 12, 8, 49]
        classificacoes = []

        for pedido in historico_pedidos:
            if pedido <= 10:
                classificacao = "Bronze"
            elif pedido <= 50:
                classificacao = "Prata"
            else:
                classificacao = "Ouro"
            informacoes = {"qtd_pedidos": pedido,
            "categoria": classificacao}
            classificacoes.append(informacoes)
            time.sleep(velocidade)
            print (f"{verde} -> Pedidos: {pedido} | Categoria: {classificacao}{reset}")
    elif escolha == "11":
        apresentar (
            11,
            "O Filtrador de Pedidos",
            "Praticar manipulação de strings, listas e condicionais.",
            "Um restaurante quer filtrar os pedidos que começam com a letra 'A' para uma promoção especial.",
            "- Limpar espaços.\n- Verificar se o pedido começa com 'A'.\n- Salvar numa lista nova apenas os pedidos que começam com 'A'.")
        pedidos_sujos = ["  A123", "b456", "  A999 ", "C000", "a777"]
        pedidos_limpos = []

        dados_entrada(pedidos_sujos)
        print ("\nDados Tratados:\n")
        for pedido in pedidos_sujos:
            pedido_limpo = pedido.strip()
            if pedido_limpo[0] == 'A':
                pedidos_limpos.append(pedido_limpo)
                time.sleep(velocidade)
                print (f"{verde} -> {pedido_limpo}{reset}")
    elif escolha == "12":
        apresentar (
            12,
            "O Monitor de Entregas",
            "Praticar manipulação de strings, listas e condicionais.",
            "Um restaurante quer monitorar os tempos de entrega dos seus pedidos. Se o tempo for maior que 45 minutos, o pedido está atrasado.",
            "- Verificar cada tempo na lista.\n- Se o tempo for maior que 45, status é 'Atrasado'.\n- Se for menor ou igual, status é 'No Prazo'.\n- Criar dicionário: {'tempo': 50, 'status': 'Atrasado'}."
        )

        tempos_entregas = [30, 45, 50, 20, 65]
        relatorios = []

        for tempo_entrega in tempos_entregas:
            time.sleep(velocidade)
            if tempo_entrega > 45:
                status = "Atrasado"
                print (f"{vermelho} -> Tempo: {tempo_entrega} | Status: {status}{reset}")
            else:
                status = "No Prazo"
                print (f"{verde} -> Tempo: {tempo_entrega} | Status: {status}{reset}")
            relatorio = {"tempo": tempo_entrega,
            "status": status}
            relatorios.append(relatorio)
    elif escolha == "13":
        apresentar (
            13,
            "O Classificador de Notas",
            "Praticar manipulação de strings, listas e condicionais.",
            "Um restaurante quer classificar seus clientes em 'Comum' ou 'Super' baseado na nota que deram ao pedido.",
            "- Se a nota for menor que 4.5, a avaliação é 'Comum'.\n- Se for maior ou igual, a avaliação é 'Super'.\n- Criar dicionário: {'nota': 4.8, 'selo': 'Super'}.")

        notas = [4.8, 3.5, 5.0, 4.2, 4.5]
        classificacao = []

        for nota in notas:
            if nota < 4.5:
                avaliacao = "Comum"
            else:
                avaliacao = "Super"
            selo = {"nota": nota,
            "selo": avaliacao}
            time.sleep(velocidade)
            print (f"{verde} -> Nota: {nota} | Selo: {avaliacao}{reset}")
            classificacao.append(selo)
    elif escolha == "14":
        apresentar (
            14,
            "O Classificador de Pedidos",
            "Praticar manipulação de strings, listas e condicionais.",
            "Um restaurante quer classificar seus pratos em 'Barato' ou 'Caro' baseado no preço.",
            "- Separar nome do prato e preço.\n- Limpar espaços.\n- Converter preço para float.\n- Se o preço for menor que 40, categoria é 'Barato'.\n- Se for maior ou igual, categoria é 'Caro'.\n- Criar dicionário: {'nome': 'Pizza', 'preco': 35.00, 'categoria': 'Barato'}."
        )

        pedidos_sujos = [
            "  Pizza - R$ 40,00 ",
            "Hambúrguer - R$ 25,50",
            "  Sushi - R$ 60,00  ",
            "Salada - R$ 15,00"
        ]
        resultados = []

        dados_entrada(pedidos_sujos)

        print ("\nDados Tratados:\n")

        for pedido in pedidos_sujos:
            pedacos = pedido.split("-")
            nome_prato = pedacos[0].strip()
            
            preco_texto = pedacos[1].replace("R$","").replace(",",".").strip()
            preco = float(preco_texto)
            
            if preco < 40:
                categoria = "Barato"
            else:
                categoria = "Caro"
            resultado = {"nome": nome_prato,
            "preco": preco,
            "categoria": categoria}
            time.sleep(velocidade)
            print (f"{verde} -> Prato: {nome_prato} | Preço: R$ {preco} | Categoria: {categoria}{reset}")
            
            resultados.append(resultado)
    elif escolha == "15":
        apresentar (
            15,
            "O Gerenciador de RH",
            "Praticar manipulação de strings, listas e condicionais.",
            "Uma empresa quer classificar seus funcionários em 'Analista' ou 'Estagiário' baseado no salário.",
            "- Separar nome do salário.\n- Limpar espaços.\n- Converter salário para float.\n- Se o salário for maior que 2500, cargo é 'Analista'.\n- Se for menor ou igual, cargo é 'Estagiário'.\n- Criar dicionário: {'nome': 'Ana Souza', 'salario': 3000.00, 'cargo': 'Analista'}."
        )

        dados_rh = [
            "Ana Souza | R$ 3.000,00",
            "  Beto Lima | R$ 1.500,00 ",
            "Carla Dias | R$ 5.500,50"
        ]

        folhas = []
            
        for dado in dados_rh:
            divide = dado.split("|")
            nome = divide[0].strip()
            
            salario_txt = divide[1].replace(".","").replace(",",".").replace("R$","").strip()
            salario = float(salario_txt)
            
            if salario>2500:
                status= "Analista"
            else:
                status= "Estagiário"
            
            folha = {"nome": nome,
            "salario": salario,
            "cargo": status}

            time.sleep(velocidade)
            print (f"{verde} -> Nome: {nome} | Salário: R$ {salario} | Cargo: {status}{reset}")
            
            folhas.append(folha)
    elif escolha == "16":
        apresentar (
            16,
            "O Gerenciador de Estoque",
            "Praticar manipulação de strings, listas e condicionais.",
            "Uma loja quer monitorar o estoque dos seus produtos. Se a quantidade for menor que 10, precisa comprar mais.",
            "- Separar nome do item e quantidade.\n- Limpar espaços.\n- Converter quantidade para inteiro.\n- Verificar se precisa comprar mais (quantidade < 10).\n- Criar dicionário: {'item': 'Notebook Dell', 'quantidade': 5, 'Status': 'Comprar'/'OK'}."
        )
        estoque_sujo = [
            "Notebook Dell : 5 ",
            "Mouse Logitech: 30",
            "  Teclado Mecânico : 8  "
        ]
        relatorio_estoque = []
        dados_entrada(estoque_sujo)
        print ("\nDados Tratados:\n")
        for item in estoque_sujo:
            quebra = item.split(":")
            nome_item = quebra[0].strip()
            
            quantidade_text = quebra[1].strip()
            quantidade = int(quantidade_text)
            
            if quantidade < 10:
                condicao = "Comprar"
            else:
                condicao = "OK"
            
            relatorio = {"item": nome_item,
            "quantidade": quantidade,
            "Status": condicao}
            time.sleep(velocidade)
            print (f"{verde} -> Item: {nome_item} | Quantidade: {quantidade} | Status: {condicao}{reset}")
            relatorio_estoque.append(relatorio)

    elif escolha == "17":

        apresentar (
            17,
            "O Ranking de Pedidos",
            "Praticar loops e condicionais.",
            "Um restaurante quer saber quais foram os itens mais pedidos no dia.",
            "- Contar quantas vezes cada item foi pedido."
        )

        pedidos_do_dia = [
            "Pizza", "Hambúrguer", "Pizza", "Refrigerante", 
            "Pizza", "Hambúrguer", "Açaí", "Refrigerante", "Pizza"
        ]
        ranking = {}

        for item in pedidos_do_dia:
            if item in ranking:
                ranking[item] = ranking[item] + 1
            else:
                ranking[item] = 1
            time.sleep(velocidade)
            print (f"{verde} -> {item}: {ranking[item]}{reset}")
    elif escolha == "18":
        apresentar (
            18,
            "A Urna Eletrônica",
            "Praticar loops e condicionais.",
            "Houve uma votação para líder da turma. Os votos foram escritos em papéis e digitados numa lista.",
            "- Contar quantos votos cada candidato teve.")

        votos = [
            "Ana", "Bia", "Ana", "Carlos", 
            "Ana", "Bia", "Carlos", "Ana"
        ]
        apuracao = {}

        for voto in votos:
            if voto in apuracao:
                apuracao[voto] = apuracao[voto]+1
            else:
                apuracao[voto] = 1
            time.sleep(velocidade) 
            print (f"{verde} -> {voto}: {apuracao[voto]}{reset}")
    elif escolha == "19":
        apresentar (
            19,
            "O Contador de Frutas",
            "Praticar loops e condicionais.",
            "Uma feira quer saber quantas frutas de cada tipo foram vendidas no dia.",
            "- Contar quantas frutas de cada tipo foram vendidas."
        )
        esteira = [
            "Maçã", "Laranja", "Maçã", "Maçã", 
            "Banana", "Laranja", "Banana"
        ]
        relatorio_frutas = {}

        for fruta in esteira:
            if fruta in relatorio_frutas:
                relatorio_frutas[fruta] = relatorio_frutas[fruta] + 1
            else:
                relatorio_frutas[fruta] = 1
            time.sleep(velocidade)
            print (f"{verde} -> {fruta}: {relatorio_frutas[fruta]}{reset}")
    elif escolha == "20":
        apresentar (
            20,
            "O Classificador de Veículos",
            "Praticar loops e condicionais.",
            "Um sistema de pedágio precisa classificar os veículos que passam por ele.",
            "- Se o número for múltiplo de 3, é 'Moto'.\n- Se for múltiplo de 5, é 'Bike'.\n- Se for múltiplo de 3 e 5, é 'Carro'.\n- Se não for nenhum dos anteriores, mostrar o número."
        )
        lista = range(1,21)

        for itens in lista:

            time.sleep(velocidade)
            print (30*'-')
            if itens %3 == 0 and itens %5 == 0:
                print (f"{verde} -> Carro {reset}")
            elif itens %3 == 0:
                print (f"{verde} -> Moto {reset}")
            elif itens %5 == 0:
                print (f"{verde} -> Bike {reset}")
            else:
                print (f"{verde} -> {itens}{reset}")
    elif escolha == "21":
        apresentar (
            21,
            "O Desafio dos Preços que Somam o Cupom",
            "Praticar loops aninhados e condicionais.",
            "O cliente tem um cupom de desconto de R$ 20,00 que só vale se ele comprar exatamente dois pratos que, somados, dêem R$ 20,00.",
            "- Encontre e mostre quais são os dois preços que somam o valor do cupom.")

        precos = [5, 12, 8, 15, 3]
        cupom = 20

        for i in range(len(precos)):
            for j in range(len(precos)):
                if precos[i] + precos[j] == cupom and i > j:
                    time.sleep(velocidade)
                    print (f"\n{amarelo}Combinação encontrada:{reset}")
                    print (f"{verde}Preço 1 = {precos[i]}\nPreço 2 = {precos[j]}\nTotal: {precos[j]+precos[i]}{reset}")
                    print (60*'-')
                    
    elif escolha == "22":
        apresentar (
            22,
            "O Relatório de Vendas",
            "Praticar manipulação de strings, listas e condicionais.",
            "Uma empresa quer gerar um relatório de vendas a partir de uma lista bruta de pedidos com valores em Reais (R$).",
            "- Separar o ID do pedido e o valor.\n- Limpar o valor (tirar 'R$', trocar vírgula por ponto, tirar espaços).\n- Converter o valor para número decimal.\n- Calcular o faturamento total, quantidade de pedidos e ticket médio."
        )

        vendas_brutas = [
            "Pedido #101: R$ 45,00",
            "Pedido #102: R$ 20,50",
            "Pedido #103: R$ 100,00",
            "Pedido #104: R$ 5,50"
        ]

        dados_entrada(vendas_brutas)

        print ("\nDados Tratados:\n")
        faturamento_total = 0
        for venda in vendas_brutas:
            divide = venda.split(":")
            id_pedido = divide[0].replace("Pedido","").replace("#","").strip()
            
            valor_pedido = divide[1].replace("R$","").replace(",",".").strip()
            valor = float(valor_pedido)
            faturamento_total = faturamento_total + valor

            time.sleep(velocidade)
            print (f"{verde} -> ID Pedido: {id_pedido} | Valor: R$ {valor}{reset}")

        time.sleep(1)
        print ("\nRelatório Final:\n")
        relatorio_final = {"Faturamento Total": faturamento_total,
        "Quantidade de pedidos": len(vendas_brutas),
        "Ticket Médio:": faturamento_total/len(vendas_brutas)
        }
        print (f"\n{verde} -> Faturamento Total: R$ {faturamento_total}{reset}")
        time.sleep(velocidade)
        print (f"{verde} -> Quantidade de pedidos: {len(vendas_brutas)}{reset}")
        time.sleep(velocidade)
        print (f"{verde} -> Ticket Médio: R$ {faturamento_total/len(vendas_brutas)}{reset}")

    elif escolha == "23":
        apresentar (
            23,
            "O Desafio do Entregador Mais Rápido",
            "Praticar loops e condicionais.",
            "Uma empresa quer saber qual entregador foi o mais rápido e a diferença de tempo para o mais lento.",
            "- Percorrer a lista de entregas.\n- Comparar os tempos para achar o mais rápido e o mais lento.\n- Mostrar o nome do mais rápido e a diferença de tempo para o mais lento."
        )
        entregas = [
            {"nome": "João", "tempo": 45},
            {"nome": "Ana", "tempo": 32},
            {"nome": "Carlos", "tempo": 50},
            {"nome": "Bia", "tempo": 28},
            {"nome": "Pedro", "tempo": 60}
        ]

        mais_rapido = {"nome": "",
        "tempo": 10000}
        mais_lento = {"nome": "",
        "tempo": 0}

        for entrega in entregas:
            if entrega["tempo"] < mais_rapido["tempo"]:
                mais_rapido["tempo"] = entrega["tempo"]
                mais_rapido["nome"] = entrega["nome"]
                
            if entrega["tempo"] > mais_lento["tempo"]:
                mais_lento["tempo"] = entrega["tempo"]
                mais_lento["nome"] = entrega["nome"]
                
        print (f"{verde}O mais rápido foi {mais_rapido['nome']} e a diferença para o mais lento é {mais_lento['tempo'] - mais_rapido['tempo']} minutos.{reset}")
    else:
        time.sleep(velocidade)
        print (vermelho + "Opção inválida. Tente novamente." + reset)