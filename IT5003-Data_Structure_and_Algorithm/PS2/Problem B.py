orderdict ={"nafn": 0, "id": 1, "flokkur":2, "dagsetning":3}
Skrimsli = ["Venjulegt", "Ahrifa", "Bodunar", "Samruna", "Samstillt", "Thaeo", "Penduls", "Tengis"]
Galdur = ["Venjulegur", "Bunadar", "Svida", "Samfelldur", "Bodunar", "Hradur"]
Gildra = ["Venjuleg", "Samfelld", "Mot"]
Annad = []

card =[]
num = int(input())

def index_type(card):
    for c in card:
#        print(card[i][2])
        type_name = c[2][0].strip()
        if type_name == "Annad":
            c[2] = (3,-1)
        else:
            subtype = c[2][1].strip()
#        print(type_name,subtype)
            if type_name == "Skrimsli":
                type_rank = 0
                subtype_rank = Skrimsli.index(subtype)
                c[2] = (type_rank,subtype_rank)
            elif type_name == "Galdur":
                type_rank = 1
                subtype_rank = Galdur.index(subtype)
                c[2] = (type_rank,subtype_rank)
            elif type_name == "Gildra":
                type_rank = 2
                subtype_rank = Gildra.index(subtype)
                c[2] = (type_rank,subtype_rank)
    return card
            
for i in range(num):
    newcard = input().split(",")
    newcard[1] = int(newcard[1])
    newcard[2] = newcard[2].split("-")
#    print(newcard) 
    card.append(newcard)
    
#print(f"card={card}")
order = input().split()

index_type(card)
#print(card)

card.sort(key=lambda x: (x[orderdict[order[0]]], x[orderdict[order[1]]], x[orderdict[order[2]]],x[orderdict[order[3]]]))
for i in range(num):
    print(card[i][0])
