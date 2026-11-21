from statistics import pstdev

TASKS = [
    {"id":"T01","name":"Atualizar sistema","duration":4,"priority":5,"deadline":6,"arrival":1},
    {"id":"T02","name":"Corrigir relatório","duration":2,"priority":3,"deadline":8,"arrival":2},
    {"id":"T03","name":"Revisar cadastro","duration":1,"priority":1,"deadline":20,"arrival":3},
    {"id":"T04","name":"Corrigir integração","duration":3,"priority":5,"deadline":5,"arrival":4},
    {"id":"T05","name":"Documentar processo","duration":2,"priority":2,"deadline":20,"arrival":5},
    {"id":"T06","name":"Validar faturamento","duration":3,"priority":5,"deadline":6,"arrival":6},
    {"id":"T07","name":"Atualizar permissões","duration":2,"priority":3,"deadline":12,"arrival":7},
    {"id":"T08","name":"Testar correção","duration":4,"priority":4,"deadline":16,"arrival":8},
    {"id":"T09","name":"Ajustar consulta","duration":1,"priority":2,"deadline":16,"arrival":9},
    {"id":"T10","name":"Revisar evidências","duration":2,"priority":2,"deadline":24,"arrival":10},
    {"id":"T11","name":"Corrigir cadastro","duration":3,"priority":4,"deadline":12,"arrival":11},
    {"id":"T12","name":"Gerar relatório","duration":2,"priority":1,"deadline":30,"arrival":12},
]

def schedule(policy, tasks=TASKS, worker_count=3):
    if policy == "FIFO":
        ordered = sorted(tasks, key=lambda t: t["arrival"])
    elif policy == "SJF":
        ordered = sorted(tasks, key=lambda t: (t["duration"], t["arrival"]))
    elif policy == "GREEDY":
        ordered = sorted(
            tasks,
            key=lambda t: (-t["priority"], t["deadline"],
                           t["duration"], t["arrival"])
        )
    else:
        raise ValueError("Use FIFO, SJF ou GREEDY.")

    workers = [{"name": f"Colaborador {i+1}", "load": 0}
               for i in range(worker_count)]
    allocation = []

    for task in ordered:
        worker = min(workers, key=lambda w: (w["load"], w["name"]))
        start = worker["load"]
        finish = start + task["duration"]
        worker["load"] = finish
        allocation.append({
            "task": task["name"],
            "worker": worker["name"],
            "start": start,
            "finish": finish,
            "deadline": task["deadline"],
            "late": finish > task["deadline"]
        })

    loads = [w["load"] for w in workers]
    late_count = sum(item["late"] for item in allocation)
    return {
        "allocation": allocation,
        "loads": loads,
        "makespan": max(loads),
        "load_std_dev": pstdev(loads),
        "late_tasks": late_count
    }

if __name__ == "__main__":
    for policy in ("FIFO", "SJF", "GREEDY"):
        result = schedule(policy)
        print(f"\\n{policy}")
        print("Cargas por colaborador:", result["loads"])
        print("Tempo total (h):", result["makespan"])
        print("Tarefas atrasadas:", result["late_tasks"])
        for item in result["allocation"]:
            print(item)
