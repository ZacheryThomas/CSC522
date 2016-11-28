import csv
with open('Salaries_1.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	my_dict={}
	count=0
	for row in reader:
		if row['JobTitle'].lower() in my_dict.keys():
			my_dict[row['JobTitle'].lower()] += 1
		else:
			my_dict[row['JobTitle'].lower()] = 1
	for key in my_dict.keys():
		if(my_dict[key] <= 2):
			del my_dict[key]
print(row['JobTitle'], row['TotalPay'])
		