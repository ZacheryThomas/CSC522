import csv
with open('Salaries.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	my_dict={}
	my_list={}
	count=0
	# Adding to dict
	for row in reader:
		if row['JobTitle'].lower() in my_dict.keys():
			my_dict[row['JobTitle'].lower()][2] += 1
			my_dict[row['JobTitle'].lower()][3] = float(my_dict[row['JobTitle'].lower()][3])+float(row['TotalPayBenefits'])
		else:
			my_list=[row['TotalPayBenefits'],row['Status'].upper(),1,float(row['TotalPayBenefits'])]
			my_dict[row['JobTitle'].lower()] = my_list
			#print row['Status']
	#removing uncommon and calculating avg
	for key in my_dict.keys():
		if(my_dict[key] <= 2):
			del my_dict[key]
		my_dict[key][3]=float(my_dict[key][3])/float(my_dict[key][2])
		#fill status
	for row in reader:
		if row['JobTitle'].lower() in my_dict.keys():
			if(my_dict['JobTitle'][1]==''):
				if(row['TotalPayBenefits'] < my_dict[row['JobTitle']][3]):
					my_dict['JobTitle'][1]='PT'
				else:
					my_dict['JobTitle'][1]='FT'
print my_dict
		