"""Dictionary comprehension : convert Kilogram to pounds"""

weight_in_kg = {'book': 0.5, 'milk': 2.0, 'tv': 10.0}
weight_in_Pounds = {key: value*2.2 for (key, value) in weight_in_kg.items()}
print(weight_in_Pounds)

