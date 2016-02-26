import csv
mycsv = csv.reader(open('people_01033020100.csv'))
isFirstrow = True
total_population = 0 #variable declaration for Cognitive
cognitive_yes = 0
cognitive_no = 0
cognitive_na = 0
ambu_na=0 #Variable declaration for Ambu
ambu_no=0
ambu_yes=0
count_1 = 0#variable declaration for vison difficulty 
count_2 = 0
other_count = 0
hearing_yes = 0 #variable declaration for hearing disability
hearing_no = 0
hearing_na = 0
for row in mycsv:
	if isFirstrow:
		isFirstrow = False
		continue 
	', '.join(row)
	#cognitive
	drem_value = row[252]
	if drem_value == '1':
		cognitive_yes += 1
	elif drem_value == '2':
		cognitive_no += 1
	else:	
		cognitive_na += 1
	#ambu
	ambu_value = row[249] 
	if ambu_value=='1':  #Yes for Ambu
        	ambu_yes+=1
    	elif ambu_value=='2': #N/A for Ambu
        	ambu_no+=1
    	else: #No for Ambu
        	ambu_na+=1
    #Vison effect Deye
    #Deye for vision
	deye_count = row[247]
	if deye_count == '1':
		count_1 += 1
	elif deye_count == '2':
		count_2 += 1
	else:
		other_count += 1
	#Hearing difficulty
	#dear
	dear_value=row[246]
	if dear_value == '1':
		hearing_yes += 1
	elif dear_value == '2':
		hearing_no += 1
	else:	
		hearing_na += 1
#total_population is the same for all difficulties
total_population += cognitive_yes + cognitive_no + cognitive_na
#average cognitive difficulty
avg_cogn_yes = (float(cognitive_yes) / total_population) * 100
avg_cogn_no = (float(cognitive_no) / total_population) * 100
avg_cogn_na = (float(cognitive_na) / total_population) * 100
#average ambulatory difficulty
avg_ambu_yes = (float(ambu_yes) / total_population) * 100 
avg_ambu_no = (float(ambu_no) / total_population) * 100
avg_ambu_na = (float(ambu_na) / total_population) * 100
#average vision difficulty
vision_difficulty_yes = (float(count_1) / total_population) * 100
vision_difficulty_no = (float(count_2) / total_population) * 100
vision_na = (float(other_count) / total_population) * 100
#average hearing difficulty
avg_hear_yes = (float(hearing_yes)/total_population)*100
avg_hear_no = (float(hearing_no)/total_population)*100
avg_hear_na = (float(hearing_na)/total_population)*100

