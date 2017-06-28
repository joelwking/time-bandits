#!/usr/local/bin/python3

#
# time-bandits
# calculate 24hour periods of a given time window for feeding Cisco Tetration
#
# Copyright (C) 2017 World Wide Technology, Inc
# Nick Thompson - nick.thompson@wwt.com
# Consulting Systems Engineer
# World Wide Technology
#

import dateutil.parser as dp

# Define our Start (t1) and End (t2) times
t1 = "2017-03-27T09:00:00-0700"
t2 = "2017-05-27T16:00:00-0700"

def CalculateTimePeriods(t1,t2):
	# Convert t1 and t2 to seconds since epoch
	epoch_t1 = dp.parse(t1).timestamp()
	epoch_t2 = dp.parse(t2).timestamp()

	# Calculate total number of 24 hr periods between the provided timestamps
	complete_days = ((int(epoch_t2) - int(epoch_t1)) // 86400)

	# Calculate remaining time after the last full 24 hr period and t2
	remaining_time = ((int(epoch_t2) - int(epoch_t1)) % 86400)

	# I heard you like lists, so I made a list for your lists
	timepairs = ([],[])

	# If we have 1 or more full 24 hour periods, loop through them
	if complete_days > 0:
		loop_start_time = int(epoch_t1)
		for x in range(complete_days):
			start_time = loop_start_time
			timepairs[0].append(start_time)
			# Add 24 hrs to the loop start time to define the end time and the
			# start time of the next loop
			loop_start_time = (int(loop_start_time)+86400)
			end_time = loop_start_time
			timepairs[1].append(end_time)
		# Last we need to add our final start and end time pair based on the remaining time
		timepairs[0].append(end_time)
		timepairs[1].append(end_time+remaining_time)
	else:
		timepairs[0].append(int(epoch_t1))
		timepairs[1].append(int(epoch_t1)+remaining_time)

	if len(timepairs[0]) == len(timepairs[1]):
		return timepairs
	else:
		raise ValueError('Timestamp List Mismatch')

def main():

	timepairs = CalculateTimePeriods(t1,t2)
	
	for i in range(len(timepairs[0])):
		print(timepairs[0][i],timepairs[1][i],sep=",")

if __name__ == '__main__':
	main()
