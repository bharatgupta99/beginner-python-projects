from math import ceil

weight_unit = input('enter g for grams or p for pounds ')

while weight_unit != 'g' and weight_unit != 'p':
	print('enter proper units!')
	weight_unit = input('g->grams/p->pounds ')

weight_of_pennies = float(input('enter weight of pennies: ')) * (453.6 if weight_unit == 'p' else 1)
weight_of_nickels = float(input('enter weight of nickles: ')) * (453.6 if weight_unit == 'p' else 1)
weight_of_dimes = float(input('enter weight of dimes: ')) * (453.6 if weight_unit == 'p' else 1)
weight_of_quaters = float(input('enter weight of quaters: ')) * (453.6 if weight_unit == 'p' else 1)

currencies = ['penny', 'quater', 'dime' , 'nickel']
currencies_plural = ['pennies', 'quaters', 'dimes', 'nickels']

details = {
	'penny' : [weight_of_pennies, 2.500, 125.0],
	'quater' : [weight_of_nickels, 5.670, 226.8],
	'dime' : [weight_of_dimes, 2.268, 113.4],
	'nickel' : [weight_of_quaters, 5.0, 200.0],
}

for i in range(0, len(details)):
	no_of_wrappers = ceil( details[currencies[i]][0] / details[currencies[i]][2] )
	no_of_currency = ceil( details[currencies[i]][0] / details[currencies[i]][1] )
	print('you need ' + str(no_of_wrappers) + ' ' + currencies[i] + ' wrappers and have ' + str(no_of_currency) + ' ' + (currencies_plural[i] if no_of_currency > 1 else currencies[i])) 
