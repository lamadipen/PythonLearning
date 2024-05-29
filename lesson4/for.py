travel_budget=[100,200,300,400,600,300,600,100,300]

total=0

for item in travel_budget:
    total = total + item

print(total)

for i in range(1,11):
    print(i)

print(len(travel_budget))

for item in range(len(travel_budget)):
    print("Position:: ", item + 1, "expensese:: ", travel_budget[item])

for item in travel_budget:
    if(item == 300):
        print("Found item you are looking for", item)
        break

count300=0

for item in travel_budget:
    if(item == 300):
        count300 = count300 + 1
        print("found 300:: ", count300, " time")
        continue

print(count300)

i=0

while i < 5:
    print(i)
    i = i +1


