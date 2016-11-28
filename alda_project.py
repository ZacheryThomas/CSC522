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

			#print my_dict[temp]
job=''
salary=0.0
status=''

with open('Salaries_new.csv', 'w') as csvfile:
    fieldnames = ['JobTitle', 'Salary','Status']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    with open('Salaries.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			job=row['JobTitle'].lower()
			salary=row['TotalPayBenefits']
			status=row['Status']
			if job in my_dict.keys():
				if(status==''):
					if(salary < my_dict[job][3]):
						status='PT'
					else:
						status='FT'
				writer.writerow({'JobTitle': job, 'Salary': salary , 'Status': status })
				print job, salary, status

		 