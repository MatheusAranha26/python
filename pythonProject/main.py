from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

@app.route('/')
def index():
    # Ler o arquivo CSV usando pandas
    df = pd.read_csv('spotify.csv')

    # Criar o gráfico de dispersão usando Plotly
    fig = px.scatter(df, x='released_year', y='in_spotify_charts',
                     title='Correlação entre Ano de Lançamento e Presença nas Playlists do Spotify',
                     labels={'released_year': 'Ano de Lançamento', 'in_spotify_charts': 'Presença nas Playlists (0 = Não, 1 = Sim)'},
                     height=500, width=1000)

    # Converter o gráfico para HTML
    graph_html = pio.to_html(fig, full_html=False)

    # Renderizar o template com o gráfico
    return render_template('index.html', graph_html=graph_html)

if __name__ == '__main__':
    app.run(debug=True)