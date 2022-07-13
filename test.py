from datetime import datetime , timedelta

def get_date():
	ini_time_for_now = datetime.now()
 
	# printing initial_date
	print ("initial_date", str(ini_time_for_now))
 
	# Some another datetime
	new_final_time = ini_time_for_now + \
                	 timedelta(seconds = 2)

    #seconds
	#minutes
	#hours
	#days

 
	# printing new final_date
	print ("new_final_time", str(new_final_time))
 
	difference = str(new_final_time - ini_time_for_now)

	print('Time difference:', difference)
	if difference == '2 days, 0:00:00' :
	# printing calculated past_dates
		print('Time difference:', difference)
	# Using current time
get_date()