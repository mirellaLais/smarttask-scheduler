# SmartTask Scheduler

Projeto acadêmico desenvolvido em Python para implementar e comparar algoritmos de escalonamento de tarefas em equipes empresariais.

## Objetivo

Analisar diferentes estratégias de distribuição de tarefas entre colaboradores, considerando o tempo total de execução, a distribuição da carga de trabalho e o cumprimento de prazos.

## Algoritmos implementados

- **FIFO (First In, First Out):** executa as tarefas conforme a ordem de chegada.
- **SJF (Shortest Job First):** prioriza as tarefas de menor duração.
- **GREEDY:** utiliza uma estratégia gulosa baseada em prioridade, prazo e duração das tarefas.

## Tecnologias utilizadas

- Python 3
- Visual Studio Code
- Git e GitHub

## Funcionalidades

- Simulação de tarefas empresariais.
- Distribuição automática de tarefas entre colaboradores.
- Cálculo do tempo total de execução (*makespan*).
- Identificação de tarefas atrasadas.
- Análise da distribuição da carga de trabalho.
- Comparação entre algoritmos de escalonamento.

## Como executar

Clone o repositório:

```bash
git clone https://github.com/mirellaLais/smarttask-scheduler.git
```

Entre na pasta:

```bash
cd smarttask-scheduler
```

Execute o programa:

```bash
python smarttask_scheduler.py
```

No Windows, caso necessário, utilize:

```bash
py smarttask_scheduler.py
```

## Resultados da simulação inicial

Experimento realizado com 12 tarefas e 3 colaboradores.

| Métrica | FIFO | SJF | GREEDY |
|---|---:|---:|---:|
| Tempo total (horas) | 10 | 11 | 11 |
| Tarefas atrasadas | 1 | 3 | 0 |
| Desvio padrão da carga | 0,47 | 1,25 | 0,94 |

### Análise

O FIFO apresentou o menor tempo total de execução, enquanto o GREEDY obteve o melhor resultado no cumprimento dos prazos, sem registrar tarefas atrasadas.

Os resultados demonstram que diferentes estratégias de escalonamento apresentam vantagens distintas, dependendo dos critérios considerados.

## Considerações

O projeto utiliza dados simulados e considera colaboradores com capacidade equivalente, sem dependências entre tarefas ou interrupção de atividades.

Os resultados são restritos às condições estabelecidas no experimento.
