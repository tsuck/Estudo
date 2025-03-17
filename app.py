from flask import Flask, render_template, request, redirect, url_for, session
import random
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_sessao'

# Carregar as questões do arquivo JSON
def carregar_questoes():
    questoes = []
    
    # Carregar do arquivo 'inteligenciaartificial.json'
    with open('inteligenciaartificial.json', 'r', encoding='utf-8') as arquivo:
        questoes += json.load(arquivo)  # Adiciona as questões desse arquivo
    
    # Carregar do arquivo 'lgcomputacional.json'
    with open('lgcomputacional.json', 'r', encoding='utf-8') as arquivo:
        questoes += json.load(arquivo)  # Adiciona as questões desse outro arquivo
    
    # Carregar do arquivo 'progcomputadores.json'
    with open('progcomputadores.json', 'r', encoding='utf-8') as arquivo:
        questoes += json.load(arquivo)  # Adiciona as questões desse outro arquivo
    
    return questoes

@app.route('/')
def pagina_inicial():
    return render_template('index.html')

@app.route('/instrucoes')
def instrucoes():
    return render_template('instrucoes.html')

@app.route('/iniciar_prova')
def iniciar_prova():
    questoes = carregar_questoes()  # Agora carrega questões dos dois arquivos
    questoes_aleatorias = random.sample(questoes, 10)  # Pega 10 questões aleatórias
    
    # Armazena as questões na sessão
    session['questoes'] = questoes_aleatorias
    session['questao_atual'] = 0
    session['pontuacao'] = 0
    session['hora_inicio'] = datetime.now().isoformat()
    session['respostas'] = []
    
    return redirect(url_for('prova'))

@app.route('/prova', methods=['GET', 'POST'])
def prova():
    if 'questoes' not in session:
        return redirect(url_for('pagina_inicial'))
    
    if 'hora_inicio' not in session:  # Só define a hora de início na primeira questão
        session['hora_inicio'] = datetime.now().strftime("%H:%M:%S")

    questoes = session['questoes']
    questao_atual = session['questao_atual']
    
    if questao_atual >= len(questoes):
        return redirect(url_for('resultado'))
    
    if request.method == 'POST':
        resposta_usuario = request.form.get('resposta')
        resposta_correta = questoes[questao_atual]['resposta_correta']
        
        session['respostas'].append({
            'questao': questoes[questao_atual]['pergunta'],
            'resposta_usuario': resposta_usuario,
            'resposta_correta': resposta_correta,
            'correto': resposta_usuario == resposta_correta
        })
        
        if resposta_usuario == resposta_correta:
            session['pontuacao'] += 10  # Cada questão vale 10 pontos
        
        session['questao_atual'] += 1
        return redirect(url_for('prova'))
    
    return render_template('prova.html', 
                          questao=questoes[questao_atual], 
                          numero_questao=questao_atual + 1, 
                          total_questoes=len(questoes),
                          hora_inicio=session['hora_inicio'])  # Enviando a hora para o template

@app.route('/resultado')
def resultado():
    if 'questoes' not in session:
        return redirect(url_for('pagina_inicial'))
    
    pontuacao = session['pontuacao']
    hora_inicio = session.get('hora_inicio')
    hora_fim = datetime.now()

    # Converter a string armazenada em datetime
    if hora_inicio:
        hora_inicio = datetime.fromisoformat(hora_inicio)
        tempo_total = hora_fim - hora_inicio
        tempo_decorrido = str(tempo_total).split('.')[0]  # Remove milissegundos
    else:
        tempo_decorrido = "Indisponível"

    respostas = session['respostas']
    aprovado = pontuacao >= 60

    return render_template('resultado.html', 
                           pontuacao=pontuacao, 
                           hora_inicio=hora_inicio.strftime("%H:%M:%S"),
                           hora_fim=hora_fim.strftime("%H:%M:%S"),
                           tempo_decorrido=tempo_decorrido,
                           respostas=respostas,
                           aprovado=aprovado)

if __name__ == '__main__':
    app.run(debug=True)