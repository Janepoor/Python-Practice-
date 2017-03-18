

def find_manager(rels, emp1, emp2):
    for manager,employees in rels.iteritems():
        if emp1 in employees:
            manager1 = manager
        if emp2 in employees:
            manager2 = manager
    if manager1 == emp2:
        return manager1
    if manager2 == emp1:
        return manager2
    if manager1 == manager2:
        return manager1
    return find_manager(rels, manager1, manager2)

def parse(str):
    rels = dict()
    for rel in str.split(','):
        m,e = rel.split('->')
        if m not in rels:
            rels[m] = e
        else:
            rels[m] += ',' + e
    return rels