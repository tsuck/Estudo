document.addEventListener('DOMContentLoaded', function() {
    // Adiciona a classe 'carregado' ao body após carregar a página
    document.body.classList.add('carregado');
    
    // Animação para elementos da página
    const animarElementos = () => {
        const elementos = document.querySelectorAll('.card, .botao, .titulo-principal, .subtitulo');
        
        elementos.forEach((elemento, index) => {
            setTimeout(() => {
                elemento.classList.add('visivel');
            }, 100 * index);
        });
    };
    
    // Inicia as animações
    animarElementos();
    
    // Eventos para os botões
    const botoes = document.querySelectorAll('.botao');
    botoes.forEach(botao => {
        botao.addEventListener('mouseenter', function() {
            this.classList.add('hover');
        });
        
        botao.addEventListener('mouseleave', function() {
            this.classList.remove('hover');
        });
        
        botao.addEventListener('click', function() {
            this.classList.add('clicado');
            setTimeout(() => {
                this.classList.remove('clicado');
            }, 300);
        });
    });
    
    // Efeito de hover para itens de opção
    const opcoes = document.querySelectorAll('.opcao-item');
    opcoes.forEach(opcao => {
        opcao.addEventListener('click', function() {
            // Desmarca todas as opções
            opcoes.forEach(op => op.classList.remove('selecionado'));
            
            // Marca a opção clicada
            this.classList.add('selecionado');
            
            // Seleciona o radio button dentro da opção
            const radio = this.querySelector('input[type="radio"]');
            if (radio) {
                radio.checked = true;
            }
        });
    });
    
    // Adiciona efeito de animação ao submeter o formulário
    const form = document.querySelector('.opcoes-form');
    if (form) {
        form.addEventListener('submit', function(event) {
            const botaoSubmit = this.querySelector('button[type="submit"]');
            
            if (botaoSubmit) {
                botaoSubmit.classList.add('submetendo');
                
                // Verifica se alguma opção foi selecionada
                const opcaoSelecionada = form.querySelector('input[type="radio"]:checked');
                
                if (!opcaoSelecionada) {
                    event.preventDefault();
                    alert('Por favor, selecione uma opção antes de prosseguir.');
                    botaoSubmit.classList.remove('submetendo');
                }
            }
        });
    }
    
    // Adiciona efeito de ripple aos botões
    const adicionarRipple = (elemento) => {
        elemento.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            ripple.classList.add('ripple');
            this.appendChild(ripple);
            
            const rect = this.getBoundingClientRect();
            const diameter = Math.max(rect.width, rect.height);
            const radius = diameter / 2;
            
            ripple.style.width = ripple.style.height = `${diameter}px`;
            ripple.style.left = `${e.clientX - rect.left - radius}px`;
            ripple.style.top = `${e.clientY - rect.top - radius}px`;
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    };
    
    document.querySelectorAll('.botao').forEach(adicionarRipple);
});