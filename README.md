Sistema de Estudos - Prova de Conhecimentos

Este projeto implementa um sistema de provas baseado em Flask. Ele permite que os usuários respondam a questões de múltiplas escolhas, com questões extraídas de arquivos JSON. O sistema possui funcionalidades como cálculo de pontuação, controle de tempo de prova e exibição de resultados.





Funcionalidades
Carregamento de questões: As questões são carregadas a partir de três arquivos JSON: inteligenciaartificial.json, lgcomputacional.json e progcomputadores.json.
Prova de múltiplas escolhas: O usuário deve responder a questões de múltiplas escolhas.
Pontuação: Cada questão vale 10 pontos. O sistema calcula a pontuação total do usuário.
Controle de tempo: O tempo de início e término da prova é registrado, e o tempo total gasto é exibido ao final.
Resultado: Ao final da prova, o usuário recebe seu desempenho, a pontuação total e a aprovação (baseada em uma pontuação mínima de 60 pontos).
Requisitos


Para rodar este projeto, você precisa ter o Python instalado. Também são necessárias as seguintes bibliotecas:
Flask
JSON



Você pode instalar o Flask executando o comando abaixo:
pip install flask


Estrutura de Diretórios

│
├── app.py                # Arquivo principal do servidor Flask
├── inteligenciaartificial.json # Arquivo JSON contendo as questões sobre Inteligência Artificial
├── lgcomputacional.json  # Arquivo JSON contendo questões sobre Lógica Computacional
├── progcomputadores.json # Arquivo JSON contendo questões sobre Programação de Computadores
├── templates/            # Pasta contendo os arquivos HTML
│   ├── index.html        # Página inicial
│   ├── instrucoes.html   # Página de instruções
│   ├── prova.html        # Página da prova
│   └── resultado.html    # Página de resultado
└── static/               # Pasta para arquivos estáticos (CSS, JS)
    ├── css/
    │   └── style.css     # Arquivo de estilo CSS
    └── js/
        └── script.js     # Arquivo de script JavaScript



Como Rodar o Projeto

Se você ainda não tiver o Flask instalado, execute o seguinte comando:
pip install flask

Execute o servidor Flask:

Execute o comando abaixo para iniciar o servidor:

python app.py
Acesse a aplicação:

Após iniciar o servidor, abra seu navegador e acesse:
http://127.0.0.1:5000/

Como Funciona
Página Inicial: Quando o usuário acessa a página inicial, ele pode iniciar a prova, que consiste em questões de múltiplas escolhas.
Instruções: O usuário pode acessar as instruções da prova a partir do link disponível na interface.
Prova: O usuário responderá a uma sequência de 10 questões, sendo que cada questão é aleatória. A pontuação é calculada automaticamente após a submissão da resposta.
Resultado: Ao final, o sistema exibirá a pontuação total, o tempo total de prova e se o usuário foi aprovado ou não.
Arquivos JSON

O sistema utiliza três arquivos JSON para carregar as questões:

inteligenciaartificial.json: Contém questões sobre Inteligência Artificial.
lgcomputacional.json: Contém questões sobre Lógica Computacional.
progcomputadores.json: Contém questões sobre Programação de Computadores.

Cada arquivo JSON deve ter a seguinte estrutura:

[
  {
    "pergunta": "Texto da pergunta",
    "opcoes": ["Opção 1", "Opção 2", "Opção 3", "Opção 4"],
    "resposta_correta": "Opção correta"
  },
  ...
]



Licença
Este projeto está licenciado sob a MIT License.
