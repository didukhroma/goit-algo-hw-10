import pulp

model = pulp.LpProblem("Maximize profit", pulp.LpMaximize)

Lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
Fruit_juice = pulp.LpVariable("Fruit_juice", lowBound=0, cat="Integer")

model += Lemonade + Fruit_juice, "Profit"

model += 2*Lemonade + 1*Fruit_juice <= 100, "Water constrains"
model += 1*Lemonade <= 50, "Sugar constrains"
model += 1*Lemonade <= 30, "Lemon juice constrains"
model += 2*Fruit_juice <= 40, "Fruit puree constrains"

model.solve()

print(pulp.value(Lemonade))
print(pulp.value(Fruit_juice))
