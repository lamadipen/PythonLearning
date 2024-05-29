def calculate_total(input):
    total =0;
    for item in input:
        total = total + item
    return total


travel_budget1=[100,200,300,400]
travel_budget2=[300,400,500,900]

total1= calculate_total(travel_budget1)
total2= calculate_total(travel_budget2)

print(total1)
print(total2)

def sayHello():
    print("Hello User")

sayHello()

def sum(a, b=1):
    return a + b

result = sum(9,3)
print(result)

result = sum(b=4,a=1)
print(result)

result= sum(20)
print(result)

result = sum(20,2)
print(result)

total=0
def subtract(a, b):
    total = a - b
    print("inside subtract:: ", total)
    return total

print(total)
sub_total = subtract(5,3)
print(total)




