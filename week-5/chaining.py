rules = [
    (["fever", "cough"], "flu"),
    (["flu"], "rest_and_fluids"),
]

facts = {"fever", "cough"}


def forward(facts):
    facts = set(facts)
    added = True
    while added:
        added = False
        for premises, conclusion in rules:
            if conclusion in facts:
                continue
            ok = True
            for p in premises:
                if p not in facts:
                    ok = False
                    break
            if ok:
                facts.add(conclusion)
                added = True
    return facts


def backward(goal):
    if goal in facts:
        return True
    for premises, conclusion in rules:
        if conclusion == goal:
            ok = True
            for p in premises:
                if not backward(p):
                    ok = False
                    break
            if ok:
                return True
    return False

print("Can this goal be proven from the facts and rules")
print("Forward:", forward(facts))
print("Backward, rest_and_fluids:", backward("rest_and_fluids"))