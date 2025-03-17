from flask import Flask, render_template, request, redirect, url_for, session
import random
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_sessao'

# Carregar as questões do arquivo JSON
def carregar_questoes():
    with open('questoes.json', 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

@app.route('/')
def pagina_inicial():
    return render_template('index.html')

@app.route('/instrucoes')
def instrucoes():
    return render_template('instrucoes.html')

@app.route('/iniciar_prova')
def iniciar_prova():
    questoes = carregar_questoes()
    questoes_aleatorias = random.sample(questoes, 10)  # Pega 10 questões aleatórias
    
    # Armazena as questões na sessão
    session['questoes'] = questoes_aleatorias
    session['questao_atual'] = 0
    session['pontuacao'] = 0
    session['hora_inicio'] = datetime.now().strftime("%H:%M:%S")
    session['respostas'] = []
    
    return redirect(url_for('prova'))

@app.route('/prova', methods=['GET', 'POST'])
def prova():
    if 'questoes' not in session:
        return redirect(url_for('pagina_inicial'))
    
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
                          total_questoes=len(questoes))

@app.route('/resultado')
def resultado():
    if 'questoes' not in session:
        return redirect(url_for('pagina_inicial'))
    
    pontuacao = session['pontuacao']
    hora_inicio = session['hora_inicio']
    hora_fim = datetime.now().strftime("%H:%M:%S")
    respostas = session['respostas']
    aprovado = pontuacao >= 60
    
    return render_template('resultado.html', 
                          pontuacao=pontuacao, 
                          hora_inicio=hora_inicio,
                          hora_fim=hora_fim,
                          respostas=respostas,
                          aprovado=aprovado)

if __name__ == '__main__':
    app.run(debug=True)