import random
import datetime

# =========================
# Menu de Opções
# =========================

def menu():
    nome_arq = 'log.txt'
    while True:
        print('Monitor LogPy')
        print('1 - Gerar Logs')
        print('2 - Analisar Logs')
        print('3 - Gerar e Analisar Logs')
        print('4 - Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            try:
                qtd = int(input('Quantidade de logs: '))
                gerarArquivo(nome_arq, qtd)
            except:
                print('Qtd incorreta')

        elif opcao == '2':
            analisarLog(nome_arq)

        elif opcao == '3':
            try:
                qtd = int(input('Quantidade de logs: '))
                gerarArquivo(nome_arq, qtd)
                analisarLog(nome_arq)
            except:
                print('Qtd incorreta')

        elif opcao == '4':
            print('Até mais')
            break
        else:
            print('opção errada')

# =========================
# Gerar Logs
# =========================

def gerarArquivo(nome_arq, qtd):
    with open(nome_arq, 'w', encoding='UTF-8') as arq:
        for i in range(qtd):
            arq.write(montarLog(i) + '\n')
    print('Logs gerados')

def montarLog(i):
    data = gerarDataHora(i)
    ip = gerarIp(i)
    recurso = gerarRecurso(i)
    metodo = gerarMetodo(i)
    status = gerarStatus(i)
    tempo = gerarTempo(i)
    agente = gerarAgente(i)
    return f'[{data}] {ip} - {metodo} - {status} - {recurso} - {tempo} ms - 500mb - HTTP/1.1 - {agente} - /home'

def gerarDataHora(i):
    base = datetime.datetime(2026, 3, 30, 22, 8, 0)
    data = datetime.timedelta(seconds=i * random.randint(5, 20))
    return (base + data).strftime('%d/%m/%Y %H:%M:%S')

def gerarIp(i):
    r = random.randint(1,6)
    if i >= 20 and i <= 30:
        return '200.0.111.345'
    if r == 1:
        return '192.168.5.6'
    elif r == 2:
        return '192.168.5.8'
    elif r == 3:
        return '192.168.5.9'
    elif r == 4:
        return '192.168.25.8'
    elif r == 5:
        return '192.168.45.8'
    else:
        return '192.168.5.6'

def gerarRecurso(i):
    r = random.randint(1,6)
    if r == 1: return '/home'
    elif r == 2: return '/login'
    elif r == 3: return '/admin'
    elif r == 4: return '/private'
    elif r == 5: return '/settings'
    else: return '/dashboards'

def gerarMetodo(i):
    r = random.randint(1,4)
    if r == 1: return 'GET'
    elif r == 2: return 'POST'
    elif r == 3: return 'PUT'
    else: return 'DELETE'

def gerarStatus(i):
    r = random.randint(1,4)
    if r == 1: return '200'
    elif r == 2: return '403'
    elif r == 3: return '404'
    else: return '500'

def gerarTempo(i):
    return random.randint(200, 800)

def gerarAgente(i):
    r = random.randint(1,5)
    if r == 1: return 'Mozilla/5.0 (Windows) Chrome'
    elif r == 2: return 'Mozilla/5.0 (bot) Safari'
    elif r == 3: return 'Mozilla/5.0 (Linux) Chrome'
    elif r == 4: return 'Mozilla/5.0 (crawler) Chrome'
    else: return 'Mozilla/5.0 (iPhone) MobileSafari'

def analisarLog(nome_arq):
    with open(nome_arq, 'r', encoding='UTF-8')as arq:
        logs = arq.readlines()
    print("\n===== RELATÓRIO MONITOR LOGPY =====")
    print(f'Quantidade de Logs: {len(logs)}')
    sucessos = registroDsucessos(logs)
    erros = registroDeErros(logs)
    erros_criticos = registroDeErrosCriticos(logs)
    disponibilidade = disponibilidadeDsistema(logs)
    tempo_medio = tempoMedio(logs)
    maior_tempo, menor_tempo = maiorMenorTempo(logs)
    distribuicao_desempenho = distribuicaoDeDesempenho(logs)
    distribuicao_status = distribuicaoDeStatus(logs)
    top_recursos = topRecursos(logs)
    ip_ativo = ipMaisAtivo(logs)
    ip_erros = ipComMaisErros(logs)
    forca_bruta = tentativasDeForcaBruta(logs)
    acesso_indevido = acessoIndevido(logs)
    degradao_desempenho = degradaoDeDesempenho(logs)
    falha_critica = falhaCritica(logs)
    bot_detectado = detectarBot(logs)
    exploracao_rotas = detecaodexploracaoderotassensiveis(logs)
    taxa_erro = taxaErro(logs)
    classificacao_do_sistema = classificarSistema(erros_criticos, disponibilidade, distribuicao_desempenho.get('Lento', 0), forca_bruta)

    print(f'Sucessos: {sucessos}')
    print(f'Erros: {erros}')
    print(f'Erros Críticos: {erros_criticos}')
    print(f'Disponibilidade: {disponibilidade:.2f}%')
    print(f'Tempo Médio: {tempo_medio:.2f} ms')
    print(f'Maior Tempo: {maior_tempo} ms')
    print(f'Menor Tempo: {menor_tempo} ms')
    print(f'Distribuição de Desempenho: {distribuicao_desempenho}')
    print(f'Distribuição de Status: {distribuicao_status}')
    print(f'Top Recursos: {top_recursos}')
    print(f'IP Mais Ativo: {ip_ativo}')
    print(f'IP com Mais Erros: {ip_erros}')
    print(f'Tentativas de Força Bruta: {forca_bruta}')
    print(f'Acesso Indevido: {acesso_indevido}')
    print(f'Degradação de Desempenho: {degradao_desempenho}')
    print(f'Falha Crítica: {falha_critica}')
    print(f'Bot Detectado: {bot_detectado}')
    print(f'Exploração de Rotas: {exploracao_rotas}')
    print(f'Taxa de Erro: {taxa_erro:.2f}%')
    print(f'Classificação do Sistema: {classificacao_do_sistema}')


def classificarTempo(t):
    if t < 300:
        return 'Rápido'
    if t >= 300 and t < 600:
        return 'Médio'
    else:
        return 'Lento'
    
def classificarStatus(s):
    if s == '200':
        return 'Sucesso'
    elif s == '403':
        return 'Acesso Negado'
    elif s == '404':
        return 'Erro Leve'
    elif s == '500':
        return 'Erro Critico'

def registroDsucessos(logs):
    count = 0
    for log in logs:
        if '200' in log:
            count += 1
    return count

def registroDeErros(logs):
    count = 0
    for log in logs:
        if '200' not in log:
            count += 1
        return count
    
def registroDeErrosCriticos(logs):
    count = 0
    for linha in logs:
        if ' - ' in linha:
            pos_ip = linha.find(' - ')
            pos_metodo = linha.find(' - ', pos_ip + 1)
            inicio_status = pos_metodo + 3
            fim_status = linha.find(' - ', inicio_status)
            status = linha[inicio_status:fim_status].strip()
            if status == '500':
                count += 1
        return count
    
def disponibilidadeDsistema(logs):
    totalsucesso = registroDsucessos(logs)
    totalacesso = len(logs)
    disponibilidadeDsistema = (totalsucesso / totalacesso) * 100
    return disponibilidadeDsistema

def tempoMedio(logs):
    soma_ms = 0
    qtd_ms = 0
    for linha in logs:
        if ' ms - ' in linha:
            posicao_ms = linha.find(' ms - ')
            posicao_espaco = linha.rfind(' ', 0, posicao_ms - 1)
            trecho_numero = linha[posicao_espaco + 1:posicao_ms].strip()
            if trecho_numero.isdigit():
                soma_ms += int(trecho_numero)
                qtd_ms += 1
    if qtd_ms > 0:
        return soma_ms / qtd_ms
    else:
        return 0

def maiorMenorTempo(logs):
    for linha in logs:
        if ' ms - ' in linha:
            posicao_ms = linha.find(' ms - ')
            posicao_espaco = linha.rfind(' ', 0, posicao_ms - 1)
            trecho_numero = linha[posicao_espaco + 1:posicao_ms].strip()
            if trecho_numero.isdigit():
                tempo = int(trecho_numero)
                if 'maior' not in locals() or tempo > maior:
                    maior = tempo
                if 'menor' not in locals() or tempo < menor:
                    menor = tempo
    return maior, menor


def distribuicaoDeDesempenho(logs):
    for linha in logs:
        if ' ms - ' in linha:
            posicao_ms = linha.find(' ms - ')
            posicao_espaco = linha.rfind(' ', 0, posicao_ms - 1)
            trecho_numero = linha[posicao_espaco + 1:posicao_ms].strip()
            if trecho_numero.isdigit():
                tempo = int(trecho_numero)
                categoria = classificarTempo(tempo)
                if 'distribuicao' not in locals():
                    distribuicao = {'Rápido': 0, 'Médio': 0, 'Lento': 0}
                distribuicao[categoria] += 1
    return distribuicao


def distribuicaoDeStatus(logs):
    for linha in logs:
        if ' - ' in linha:
            pos_ip = linha.find(' - ')
            pos_metodo = linha.find(' - ', pos_ip + 1)
            inicio_status = pos_metodo + 3
            fim_status = linha.find(' - ', inicio_status)
            status = linha[inicio_status:fim_status].strip()
            categoria = classificarStatus(status)
            if 'distribuicao' not in locals():
                distribuicao = {'Sucesso': 0, 'Acesso Negado': 0, 'Erro Leve': 0, 'Erro Critico': 0}
            distribuicao[categoria] += 1
    return distribuicao

def topRecursos(logs):
    contagem_recursos = {}
    for linha in logs:
        if ' - ' in linha:
            pos_ip = linha.find(' - ')
            pos_metodo = linha.find(' - ', pos_ip + 1)
            pos_status = linha.find(' - ', pos_metodo + 1)
            inicio_recurso = pos_status + 3
            fim_recurso = linha.find(' - ', inicio_recurso)
            recurso = linha[inicio_recurso:fim_recurso].strip()
            if recurso:
                if recurso in contagem_recursos:
                    contagem_recursos[recurso] += 1
                else:
                    contagem_recursos[recurso] = 1
    return contagem_recursos


def ipMaisAtivo(logs):
    contagem_ip = {}
    for linha in logs:
        if ']' in linha and ' - ' in linha:
            inicio_ip = linha.find(']') + 2
            fim_ip = linha.find(' - ', inicio_ip)
            ip = linha[inicio_ip:fim_ip].strip()
            if ip:
                if ip in contagem_ip:
                    contagem_ip[ip] += 1
                else:
                    contagem_ip[ip] = 1
    ip_mais_frequente = ''
    max_repeticoes = 0
    for ip in contagem_ip:
        if contagem_ip[ip] > max_repeticoes:
            max_repeticoes = contagem_ip[ip]
            ip_mais_frequente = ip
    return ip_mais_frequente

def ipComMaisErros(logs):
    contagem_erros_ip = {}
    for linha in logs:
        if ']' in linha and ' - ' in linha:
            inicio_ip = linha.find(']') + 2
            fim_ip = linha.find(' - ', inicio_ip)
            ip = linha[inicio_ip:fim_ip].strip()
            depois_ip = linha.find(' - ', fim_ip + 1)
            inicio_status = depois_ip + 3
            fim_status = linha.find(' - ', inicio_status)
            status = linha[inicio_status:fim_status].strip()
            if status != '200':
                if ip in contagem_erros_ip:
                    contagem_erros_ip[ip] += 1
                else:
                    contagem_erros_ip[ip] = 1
ip_mais_erros = ''
max_erros = 0

def tentativasDeForcaBruta(logs):
    ultimo_ip = ''
    tentativas = 0
    ip_anterior = ''
    contador = 1
    for linha in logs:
        if ']' in linha and ' - ' in linha:
            inicio_ip = linha.find(']') + 2
            fim_ip = linha.find(' - ', inicio_ip)
            ip = linha[inicio_ip:fim_ip].strip()

            pos_metodo = linha.find(' - ', fim_ip + 1)
            pos_status = linha.find(' - ', pos_metodo + 1)
            inicio_caminho = pos_status + 3
            fim_caminho = linha.find(' - ', inicio_caminho)
            caminho = linha[inicio_caminho:fim_caminho].strip()
            if ip == ip_anterior and caminho == '/admin' and '403' in linha:
                contador += 1
                if contador >= 3:
                    tentativas += 1
                    ultimo_ip = ip
            else:
                contador = 1
        return {"total_tentativas": tentativas, "ultimo_ip": ultimo_ip}
    

def acessoIndevido(logs):
    eventos = 0
    for log in logs:
        if '403' in log and '/admin' in log:
            eventos += 1
    return eventos

def degradaoDeDesempenho(logs):
    eventos = 0
    for log in logs:
        if '500' in log and 'Lento' in log:
            eventos += 1
    return eventos

def falhaCritica(logs):
    eventos = 0
    for log in logs:
        if '500' in log and 'Erro Critico' in log:
            eventos += 1
    return eventos

def detectarBot(logs):
    eventos = 0
    for linha in logs:
        if 'bot' in linha or 'crawler' in linha:
            eventos += 1
    return eventos

def detecaodexploracaoderotassensiveis(logs):
    rotas_sensiveis = ['/admin', '/private', '/settings']
    eventos = 0
    eventos_malsucedidos = 0
    for log in logs:
        if any(rota in log for rota in rotas_sensiveis):
            eventos += 1
            if '403' in log or '404' in log:
                eventos_malsucedidos += 1
                return {"total_exploracoes": eventos, "total_malsucedidos": eventos_malsucedidos}
            
def taxaErro(logs):
    total_logs = len(logs)
    erros = sum(1 for log in logs if '200' not in log)
    return (erros / total_logs) * 100 if total_logs > 0 else 0

def classificarSistema(falhas_criticas, disponibilidade, acessos_lentos, acessos_suspeitos):
    if falhas_criticas >= 1 or disponibilidade < 70:
        return 'CRÍTICO'
    elif disponibilidade < 85 or acessos_lentos > 50:  
        return 'INSTÁVEL'
    elif disponibilidade < 95 or acessos_suspeitos > 0:
        return 'ATENÇÃO'
    else:
        return 'SAUDÁVEL'




menu()
