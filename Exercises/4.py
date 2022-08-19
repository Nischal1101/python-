# wap to sort the following list using lambda function
cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'MItsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]


cars.sort(key=lambda x: x['year'])
print(cars)
