### Guia Completo: Projeto de Monitoramento com Prometheus e Grafana
Este projeto é um exemplo prático de como configurar uma stack de monitoramento completa usando Docker, Prometheus e Grafana. O objetivo é monitorar uma pequena aplicação em Python (Flask) e o servidor hospedeiro, simulando um ambiente de produção real.

## Tecnologias Utilizadas
- Docker & Docker Compose: Ferramentas essenciais para containerizar a aplicação e todos os serviços de monitoramento. Garante que o ambiente seja portátil e replicável em qualquer máquina.

- Prometheus: Um sistema de monitoramento e alerta de código aberto. Ele coleta métricas de alvos configurados (como nossa aplicação e o Node Exporter) e armazena esses dados.

- Grafana: Uma plataforma de análise e visualização. Ele se conecta ao Prometheus para criar dashboards interativos e dinâmicos, permitindo visualizar o estado e o desempenho dos serviços em tempo real.

- Node Exporter: Um "exporter" oficial do Prometheus que coleta métricas de hardware e sistema operacional (como CPU, memória, disco e rede) do servidor.

- Python (Flask): Uma aplicação web simples, usada aqui para demonstrar como expor métricas personalizadas para o Prometheus.

## Estrutura do Projeto
A seguir, a estrutura de diretórios do projeto. Cada arquivo desempenha uma função crucial na configuração da stack.

````
.
├── app/
│   ├── app.py
│   └── Dockerfile
├── docker-compose.yml
└── prometheus.yml
````
````app/app.py:```` A aplicação web em Python que gera métricas.

````app/Dockerfile:```` As instruções para criar a imagem Docker da nossa aplicação Python.

````docker-compose.yml:```` O arquivo de configuração principal que define e orquestra todos os serviços (Prometheus, Grafana, Node Exporter, aplicação).

````prometheus.yml:```` O arquivo de configuração do Prometheus, que especifica quais alvos ele deve "scrapear" (coletar métricas).

# Pré-requisitos
Para executar este projeto, você deve ter as seguintes ferramentas instaladas em sua máquina:

- Docker & Docker Compose: Instale o Docker Desktop que já inclui o Docker Compose.

- Git: Para clonar o repositório.

# Passo a Passo para Subir o Ambiente
Siga as instruções abaixo para colocar a sua stack de monitoramento no ar.

Clone o Repositório
Abra seu terminal e execute o comando:
````
git clone <URL_DO_SEU_REPOSITORIO>
````
Navegue até o Diretório do Projeto
````
cd <NOME_DO_SEU_REPOSITORIO>
````
Execute o Docker Compose
Este comando vai construir as imagens necessárias e iniciar todos os contêineres em segundo plano (-d).
````
docker compose up -d --build
````
" up: " Inicia os serviços definidos no docker-compose.yml.

" -d: " Executa os contêineres em segundo plano (modo "detached").

" --build: " Força a reconstrução das imagens, garantindo que as alterações no código da aplicação sejam aplicadas.

Verifique os Contêineres
Confirme se todos os contêineres estão rodando corretamente com o comando:
````
docker ps
````
Você deve ver minha-aplicacao, prometheus, grafana e node-exporter com o status ````Up````.

## Acessando os Serviços
Agora que os serviços estão rodando, você pode acessá-los no seu navegador:

- Aplicação de Teste: http://localhost:8080

  - Você verá a mensagem "Olá, mundo!".

  - Para ver as métricas, acesse: http://localhost:8080/metrics

- Prometheus: http://localhost:9090

  - Verifique se os alvos estão "UP" em Status > Targets.

- Grafana: http://localhost:3000

  - O login padrão é ````admin```` e a senha é ````admin````.

## Configurando o Grafana
Para visualizar os dados, você precisa conectar o Grafana ao Prometheus e importar um dashboard.

1- Adicionar o Prometheus como Fonte de Dados

- No Grafana, clique no ícone de engrenagem.

- Selecione "Data Sources" e clique em "Add data source".

- Escolha "Prometheus".

- No campo URL, digite http://prometheus:9090.

- Clique em "Save & Test".

2- Importar Dashboard do Node Exporter

- Clique no ícone de "Dashboards" (quatro quadrados) no menu lateral.

- Clique em "Import" e digite o ID 1860.

- Clique em "Load" e, na próxima tela, selecione o Prometheus como fonte de dados.

- Clique em "Import" para finalizar.

3- Criar um Dashboard para a sua Aplicação

- Clique em "Dashboards" > "New dashboard".

- Adicione um novo painel.

- No campo "Query", digite app_requests_total para ver o contador de requisições ou app_request_processing_seconds para ver a latência.

- Personalize o painel e salve-o.

# Como Enriquecer o Projeto
Para tornar este projeto ainda mais robusto, você pode:

- Adicionar Mais Métricas: Inclua mais métricas personalizadas na sua aplicação, como número de erros, usuários ativos, ou o tamanho de filas de processamento.

- Configurar Alertas: Use o Prometheus Alertmanager para enviar notificações (via e-mail, Slack, etc.) quando uma métrica atingir um limite (ex: CPU > 80%).

- Persistir os Dados: Configure volumes no docker-compose.yml para que os dados do Prometheus e do Grafana persistam mesmo se os contêineres forem removidos.

Este projeto serve como uma base sólida para qualquer necessidade de monitoramento. Sinta-se à vontade para explorar e modificar as configurações para atender aos seus próprios casos de uso.
