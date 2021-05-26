mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())


print(round(mealCost + (tipPercent/100)*mealCost + (taxPercent/100)*mealCost))