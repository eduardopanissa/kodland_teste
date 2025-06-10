# 🕹️ PGZero Game Project – Rogue/Platformer Style

## 📌 Sobre o Projeto

Olá!  
Este projeto foi desenvolvido como parte de uma tarefa de avaliação, cujo objetivo é demonstrar domínio da linguagem Python, respeito às boas práticas de programação (PEP8), responsabilidade no cumprimento das regras estabelecidas, e criatividade dentro dos limites propostos.

O jogo foi criado **sem uso de bibliotecas externas**, utilizando apenas:
- [x] **PgZero** – motor gráfico para jogos simples em Python
- [x] **random** – geração de comportamentos aleatórios
- [x] **math** – para eventuais cálculos matemáticos
- [x] **Rect do Pygame** – única exceção permitida

Todos os demais requisitos foram seguidos com rigor, conforme descrito abaixo.

---

## 🎮 Gênero do Jogo

Este jogo foi desenvolvido no estilo **[escolha entre: Roguelike / Rogue / Platformer]**, com:
- Visão [**lateral** ou **superior**]
- Personagem principal (herói) com animações
- Inimigos perigosos que se movem dentro de seu território

---

## 🧠 Mecânicas e Funcionalidades

✔️ Menu principal com botões clicáveis:  
- `Start` (Começar o jogo)  
- `Sound ON/OFF` (Ativa/Desativa som)  
- `Exit` (Sair do jogo)  

✔️ Sons e música de fundo:
- Música tocando em segundo plano
- Efeitos sonoros para eventos (coletar moedas, dano, morte, etc.)

✔️ Lógica de jogo funcional:
- Sistema de **pontuação**
- Sistema de **vidas**
- Game Over quando vidas = 0
- Inimigos que se movimentam de forma independente

✔️ Programação limpa e organizada:
- Nomes de funções, variáveis e classes em inglês e descritivos
- Uso adequado de classes para personagens e lógica de movimento
- Animação de sprites tanto para personagens em movimento quanto parados

---

## 📂 Estrutura do Projeto

```
├── game/
│   ├── main.py           # Arquivo principal do jogo
│   ├── assets/
│   │   ├── sounds/       # Arquivos de som e música
│   │   └── images/       # Sprites e fundos do jogo
├── README.md             # Este arquivo
```
## 🔒 Regras Atendidas

✅ Apenas bibliotecas permitidas foram utilizadas  
✅ Código 100% original, feito do zero  
✅ Sem copiar partes de projetos externos  
✅ Divisão lógica e clara do código (aprox. 100–200 linhas úteis)  
✅ Projeto funcional e sem bugs perceptíveis  

---

## 📎 Recursos úteis

- [Documentação oficial do PGZero](https://pygame-zero.readthedocs.io/en/stable/)
- [Guia de boas práticas PEP8](https://peps.python.org/pep-0008/)
- [Sprites e sons gratuitos](https://opengameart.org/)

---

## 🧾 Observações finais

> Este projeto foi feito com dedicação, respeitando todas as diretrizes propostas.  
> Espero que demonstre minha capacidade técnica, responsabilidade e ética profissional.

---

## ✅ Licença

Este projeto é de uso pessoal e educacional. Todos os assets (sons e imagens) utilizados são de uso livre ou criados exclusivamente para este projeto.

---

## 🚀 Como Executar o Projeto

### 1. Criar um ambiente virtual (recomendado)

```bash
python -m venv venv
```

### 2. Ativar o ambiente virtual

- **Windows:**
```bash
venv\Scripts\activate
```

- **Linux/macOS:**
```bash
source venv/bin/activate
```

### 3. Instalar a biblioteca necessária

```bash
pip install pgzero
```

### 4. Executar o jogo

No terminal, digite:

```bash
pgzrun mygame.py
```

> Certifique-se de estar na mesma pasta onde está localizado o `mygame.py`.

---
