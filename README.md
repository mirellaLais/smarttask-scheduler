# SmartTask Scheduler

Sistema desenvolvido em Python para simular e comparar algoritmos de escalonamento de tarefas, com foco na distribuição de atividades entre colaboradores de uma equipe.

O projeto busca analisar como diferentes estratégias de escalonamento influenciam a distribuição da carga de trabalho, o tempo total de execução e o cumprimento de prazos.

## Objetivo

Desenvolver uma aplicação capaz de organizar tarefas e distribuí-las entre colaboradores, permitindo comparar diferentes algoritmos de escalonamento e observar seus resultados em diferentes cenários.

## Algoritmos implementados

O sistema implementa três estratégias de escalonamento:

- **FIFO (First In, First Out):** executa as tarefas conforme a ordem de entrada.
- **SJF (Shortest Job First):** prioriza as tarefas com menor duração.
- **GREEDY:** utiliza uma estratégia gulosa para selecionar tarefas considerando critérios de prioridade, prazo e duração.

## Funcionalidades

- Cadastro de colaboradores.
- Definição do nível de experiência dos colaboradores.
- Cadastro de tarefas com duração, prioridade, complexidade e prazo.
- Distribuição de tarefas conforme a compatibilidade entre a experiência do colaborador e a complexidade da atividade.
- Comparação dos resultados dos algoritmos FIFO, SJF e GREEDY.
- Identificação de tarefas não atribuídas.
- Cálculo da carga de trabalho por colaborador.
- Cálculo do tempo total de execução (*makespan*).
- Identificação de tarefas atrasadas.
- Cálculo do desvio padrão da distribuição de carga.
- Cálculo do atraso médio das tarefas.

## Tecnologias utilizadas

- Python 3
- Biblioteca `unittest` para testes automatizados

## Como executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/mirellaLais/smarttask-scheduler.git
   ```

2. Acesse a pasta do projeto:

   ```bash
   cd smarttask-scheduler
   ```

3. Execute o programa:

   ```bash
   python smarttask_scheduler.py
   ```

4. Siga as instruções apresentadas no terminal para cadastrar os colaboradores e as tarefas.

## Testes automatizados

O projeto possui testes automatizados desenvolvidos com a biblioteca `unittest`, contemplando:

- Execução das políticas de escalonamento.
- Verificação da restrição de compatibilidade entre colaboradores e tarefas.
- Identificação de tarefas sem colaboradores compatíveis.
- Validação de políticas de escalonamento inválidas.

Para executar os testes:

```bash
python smarttask_scheduler.py --testes
```

## Avaliação dos resultados

A aplicação permite comparar o comportamento dos três algoritmos a partir dos mesmos dados de entrada.

Os resultados são apresentados considerando indicadores como:

- Distribuição da carga de trabalho.
- Tempo total de execução.
- Quantidade de tarefas atrasadas.
- Desvio padrão da carga de trabalho.
- Atraso médio das tarefas.

Essa comparação permite observar as diferenças entre as estratégias e compreender como cada algoritmo pode influenciar a organização das atividades de uma equipe.

## Limitações

O sistema utiliza níveis de experiência e complexidade como critérios simplificados de compatibilidade. Esses níveis não representam especializações técnicas específicas.

Além disso, a simulação considera tarefas sem dependências entre si e não contempla interrupções ou ausências de colaboradores.

**SmartTask Scheduler — Organização inteligente de tarefas e distribuição de trabalho.**
