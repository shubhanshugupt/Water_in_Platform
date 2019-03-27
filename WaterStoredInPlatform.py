import numpy as np
from func import extractfloor, count_i, fall, modify

platform = np.array([[5,5,5,5,5],
		[9,1,1,1,5],
		[5,1,5,1,5],
		[5,1,1,1,5],
		[5,5,5,5,5]])

def WaterStoredInPlatform(platform):
	water = 0
	floors = platform.max()
	print "No. of floors", floors

	for floor in range(2, floors+1):
		current_floor = extractfloor(platform, floor, floors)
		print current_floor

		count = count_i(current_floor, floors)
		print count

		for i in range(count):
			current_floor = fall(current_floor, platform, floors)
			#print current_floor

		count = count_i(current_floor, floors)
		print "No of unit water in", floor, "floor:", count

		platform = modify(current_floor, platform, 2, floors)
		print platform

		water += count

	print "Total water stored:", water

	return water