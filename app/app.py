# app.py
from flask import Flask, Response
from prometheus_client import Counter, generate_latest, Gauge
import time
import random

app = Flask(__name__)

# Crie métricas para o Prometheus
# Counter para contar o numero de requisições
REQUESTS_PROCESSED = Counter('app_requests_total', 'Total de requisições processadas.')
# Gauge para medir o tempo de processamento
REQUEST_TIME = Gauge('app_request_processing_seconds', 'Tempo de processamento da requisição em segundos.')

@app.route('/')
def home():
    """Rota para a pagina inicial."""
    # Aumenta o contador de requisições
    REQUESTS_PROCESSED.inc()
    return "Olá, mundo! Este é um aplicativo de exemplo para Prometheus."

@app.route('/metrics')
def metrics():
    """
    Exponha as métricas no formato Prometheus.
    O Prometheus fará um 'scrape' desta URL para coletar os dados.
    """
    # Exemplo de uma métrica dinâmica: tempo de processamento aleatório
    with REQUEST_TIME.time():
        time.sleep(random.uniform(0.1, 0.5))
    
    # Gere e retorne as métricas com o Content-Type correto
    return Response(generate_latest(), mimetype='text/plain; version=0.0.4; charset=utf-8')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
