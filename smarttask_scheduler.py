"""
Aplicação para comparar FIFO, SJF e GREEDY na distribuição
de demandas entre colaboradores com diferentes níveis de experiência.

    - A ordem de cadastro define a chegada das demandas (FIFO).
    - SJF prioriza a menor duração.
    - GREEDY prioriza maior prioridade, depois menor prazo e menor duração.
    - Uma demanda só pode ser atribuída a um colaborador cujo nível seja
    igual ou superior ao nível de complexidade da demanda.
    - Entre os colaboradores compatíveis, escolhe-se quem tem menor carga.
"""

from statistics import pstdev
import sys

NIVEIS = {
    "iniciante": 1,
    "intermediario": 2,
    "intermediário": 2,
    "avancado": 3,
    "avançado": 3,
}

PRIORIDADES = {
    "baixa": 1,
    "media": 2,
    "média": 2,
    "alta": 3,
}

NOME_NIVEL = {1: "Iniciante", 2: "Intermediário", 3: "Avançado"}
NOME_PRIORIDADE = {1: "Baixa", 2: "Média", 3: "Alta"}


def ler_inteiro(mensagem, minimo=1):
    """lê um num int e valida o valor min."""
    while True:
        try:
            valor = int(input(mensagem))
            if valor < minimo:
                print(f"Informe um número maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def ler_numero(mensagem, minimo=0.01):
    """Lê um número positivo; aceita vírgula ou ponto decimal."""
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor < minimo:
                print(f"Informe um valor maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número.")


def ler_opcao(mensagem, opcoes):
    permitidas = {opcao.lower(): valor for opcao, valor in opcoes.items()}
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in permitidas:
            return permitidas[resposta]
        print("Opção inválida. Escolha uma das opções apresentadas.")


def cadastrar_equipe():
    print("\n=== CADASTRO DA EQUIPE ===")
    quantidade = ler_inteiro("Quantos colaboradores fazem parte da equipe? ")
    equipe = []

    for indice in range(quantidade):
        print(f"\nColaborador {indice + 1}")
        nome = input("Nome: ").strip()
        while not nome:
            print("O nome não pode ficar vazio.")
            nome = input("Nome: ").strip()

        nivel = ler_opcao(
            "Nível de experiência (iniciante/intermediario/avancado): ",
            NIVEIS,
        )
        equipe.append({
            "name": nome,
            "skill": nivel,
            "load": 0.0,
        })

    return equipe


def cadastrar_demandas():
    print("\n=== CADASTRO DAS DEMANDAS ===")
    quantidade = ler_inteiro("Quantas demandas serão distribuídas? ")
    demandas = []

    for indice in range(quantidade):
        print(f"\nDemanda {indice + 1}")
        nome = input("Nome da demanda: ").strip()
        while not nome:
            print("O nome da demanda não pode ficar vazio.")
            nome = input("Nome da demanda: ").strip()

        duracao = ler_numero("Duração estimada em horas: ")
        prioridade = ler_opcao(
            "Prioridade (baixa/media/alta): ",
            PRIORIDADES,
        )
        complexidade = ler_opcao(
            "Complexidade (simples/intermediaria/avancada): ",
            {
                "simples": 1,
                "intermediaria": 2,
                "intermediária": 2,
                "avancada": 3,
                "avançada": 3,
            },
        )
        prazo = ler_numero("Prazo em horas a partir do início do planejamento: ")

        demandas.append({
            "id": f"D{indice + 1:02d}",
            "name": nome,
            "duration": duracao,
            "priority": prioridade,
            "complexity": complexidade,
            "deadline": prazo,
            "arrival": indice,
        })

    return demandas


def schedule(policy, tasks, team):
    #ordenar e atribui cada demanda ao colaborador compatível com menor carga acumulada
    
    if not team:
        raise ValueError("A equipe precisa ter pelo menos um colaborador.")

    if policy == "FIFO":
        ordered = sorted(tasks, key=lambda task: task["arrival"])
    elif policy == "SJF":
        ordered = sorted(
            tasks,
            key=lambda task: (task["duration"], task["arrival"]),
        )
    elif policy == "GREEDY":
        ordered = sorted(
            tasks,
            key=lambda task: (
                -task["priority"],
                task["deadline"],
                task["duration"],
                task["arrival"],
            ),
        )
    else:
        raise ValueError("Política inválida. Use FIFO, SJF ou GREEDY.")

    
    workers = [
        {"name": person["name"], "skill": person["skill"], "load": 0.0}
        for person in team
    ]
    allocation = []
    unassigned = []

    for task in ordered:
        compatible = [
            worker for worker in workers
            if worker["skill"] >= task["complexity"]
        ]

        if not compatible:
            unassigned.append({
                "task": task["name"],
                "required_skill": task["complexity"],
                "reason": "Nenhum colaborador possui nível compatível.",
            })
            continue

        worker = min(
            compatible,
            key=lambda person: (person["load"], person["name"].casefold()),
        )
        start = worker["load"]
        finish = start + task["duration"]
        worker["load"] = finish

        allocation.append({
            "task": task["name"],
            "worker": worker["name"],
            "worker_skill": worker["skill"],
            "required_skill": task["complexity"],
            "priority": task["priority"],
            "start": start,
            "finish": finish,
            "deadline": task["deadline"],
            "late": finish > task["deadline"],
            "tardiness": max(0.0, finish - task["deadline"]),
        })

    loads = [worker["load"] for worker in workers]
    late_count = sum(item["late"] for item in allocation)
    makespan = max(loads, default=0.0)

    return {
        "policy": policy,
        "allocation": allocation,
        "unassigned": unassigned,
        "loads": loads,
        "worker_loads": [
            {"name": worker["name"], "load": worker["load"]}
            for worker in workers
        ],
        "makespan": makespan,
        "load_std_dev": pstdev(loads) if loads else 0.0,
        "late_tasks": late_count,
        "average_tardiness": (
            sum(item["tardiness"] for item in allocation) / len(allocation)
            if allocation else 0.0
        ),
    }


def formatar_horas(valor):
    return f"{valor:.2f}".rstrip("0").rstrip("," if "," in f"{valor:.2f}" else ".")


def exibir_resultado(result):
    print("\n" + "=" * 64)
    print(f"RESULTADO — {result['policy']}")
    print("=" * 64)

    print("\nDistribuição das demandas:")
    if not result["allocation"]:
        print("Nenhuma demanda foi atribuída.")
    for item in result["allocation"]:
        status = "ATRASADA" if item["late"] else "No prazo"
        print(
            f"- {item['task']} -> {item['worker']} | "
            f"{item['start']:.2f}h–{item['finish']:.2f}h | "
            f"Prazo: {item['deadline']:.2f}h | {status}"
        )

    print("\nCarga por colaborador:")
    for item in result["worker_loads"]:
        print(f"- {item['name']}: {item['load']:.2f} horas")

    if result["unassigned"]:
        print("\nDemandas sem colaborador compatível:")
        for item in result["unassigned"]:
            print(
                f"- {item['task']} | nível exigido: "
                f"{NOME_NIVEL[item['required_skill']]} "
                f"| {item['reason']}"
            )

    print("\nIndicadores:")
    print(f"- Tempo total (makespan): {result['makespan']:.2f} horas")
    print(f"- Tarefas atrasadas: {result['late_tasks']}")
    print(f"- Demandas não atribuídas: {len(result['unassigned'])}")
    print(f"- Desvio padrão das cargas: {result['load_std_dev']:.2f} horas")
    print(f"- Atraso médio das tarefas atribuídas: "
          f"{result['average_tardiness']:.2f} horas")


def executar_sistema():
    print("=" * 64)
    print("SMARTTASK SCHEDULER")
    print("Distribuição inteligente de demandas em equipes")
    print("=" * 64)
    print("\nCadastre a equipe e as demandas para comparar os algoritmos.")

    equipe = cadastrar_equipe()
    demandas = cadastrar_demandas()

    print("\n\nos três algoritmos serão executados com os mesmos dados.")
    resultados = []

    for algoritmo in ("FIFO", "SJF", "GREEDY"):
        resultado = schedule(algoritmo, demandas, equipe)
        resultados.append(resultado)
        exibir_resultado(resultado)

    print("\n" + "=" * 64)
    print("COMPARAÇÃO FINAL")
    print("=" * 64)
    print(
        f"{'Algoritmo':<12} {'Horas':>10} {'Atrasadas':>12} "
        f"{'Não atribuídas':>16} {'Desvio':>10}"
    )
    for result in resultados:
        print(
            f"{result['policy']:<12} "
            f"{result['makespan']:>10.2f} "
            f"{result['late_tasks']:>12} "
            f"{len(result['unassigned']):>16} "
            f"{result['load_std_dev']:>10.2f}"
        )

    print("\nObservação: os prazos são medidos em horas a partir do início")
    print("do planejamento. Cada colaborador executa uma demanda por vez.")
    print("A capacidade técnica é representada pelo nível de experiência.")


def executar_testes():
    """testes básicos automatizados da lógica de escalonamento."""
    import unittest

    class TestSmartTaskScheduler(unittest.TestCase):
        def setUp(self):
            self.team = [
                {"name": "Ana", "skill": 1},
                {"name": "Bia", "skill": 2},
                {"name": "Caio", "skill": 3},
            ]
            self.tasks = [
                {
                    "id": "D1", "name": "Tarefa avançada", "duration": 3,
                    "priority": 3, "complexity": 3, "deadline": 8, "arrival": 0,
                },
                {
                    "id": "D2", "name": "Tarefa simples", "duration": 1,
                    "priority": 1, "complexity": 1, "deadline": 5, "arrival": 1,
                },
            ]

        def test_todos_algoritmos_executam(self):
            for policy in ("FIFO", "SJF", "GREEDY"):
                result = schedule(policy, self.tasks, self.team)
                self.assertEqual(len(result["allocation"]), 2)

        def test_respeita_competencia(self):
            result = schedule("FIFO", self.tasks, self.team)
            for item in result["allocation"]:
                self.assertGreaterEqual(
                    item["worker_skill"], item["required_skill"]
                )

        def test_demanda_sem_profissional_compativel(self):
            equipe = [{"name": "Ana", "skill": 1}]
            result = schedule("FIFO", self.tasks[:1], equipe)
            self.assertEqual(len(result["unassigned"]), 1)
            self.assertEqual(len(result["allocation"]), 0)

        def test_politica_invalida(self):
            with self.assertRaises(ValueError):
                schedule("ABC", self.tasks, self.team)

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSmartTaskScheduler)
    resultado = unittest.TextTestRunner(verbosity=2).run(suite)
    return resultado.wasSuccessful()


if __name__ == "__main__":
    if "--testes" in sys.argv:
        sucesso = executar_testes()
        sys.exit(0 if sucesso else 1)
    executar_sistema()