# Analisador de Sentimentos com Streamlit

Este projeto permite analisar o sentimento de um comentário textual em inglês usando o VADER do NLTK, com uma interface interativa em Streamlit.

## 🚀 Como usar

1. **Criar ambiente virtual (apenas na primeira vez):**

```bash
python -m venv venv
```

2. **Ativar ambiente virtual**

```bash
venv\Scripts\activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Executar a aplicação**

```bash
streamlit run sentiment_analysis.py
```

5. Tecnologias usadas

    Python

    Streamlit

    NLTK (SentimentIntensityAnalyzer / VADER)

    matplotlib

    pandas

📝 Notas

    O ficheiro sentiment_analysis.py permite introduzir uma review e obter:

        Uma classificação (positiva, negativa, neutra)

        O score compound

        Um gráfico de distribuição de sentimentos (pizza ou barras)

    Para atualizar este ficheiro de dependências após instalar um novo pacote:

    pip freeze > requirements.txt
