### Manager->Person
'''
input1=Frank->Mary,Mary->Sam,Mary->Bob,Sam->Katie,Sam->Pete,Bob->John,Bob,Katie

input2=Sam->Pete,Pete->Nancy,Sam->katie,Mary->Bob,Frank->Mary,Mary->Sam,Bob->John,Sam,John

idea hashmap
'''

input1='Frank->Mary,Mary->Sam,Mary->Bob,Sam->Katie,Sam->Pete,Bob->John,Bob,Katie'
input2='Sam->Pete,Pete->Nancy,Sam->katie,Mary->Bob,Frank->Mary,Mary->Sam,Bob->John,Sam,John'

##extract information

def parse(input):
    relation =input.split(',')
    a,b = relation[-1],relation[-2]
    relation =relation[0:len(relation)-2]
    ####create a hashmap
    match={}
    for i in relation:
        Manager,Person=i.split("->")
        match[Person]=Manager        # key is the person while manager is the value

    return match,a,b


def find_manager(rels, emp1, emp2):

    for employees,manager in rels.iteritems():
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

print find_manager(parse(input1)[0],parse(input1)[1],parse(input1)[2])










