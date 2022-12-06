# Process Hunter
#
# You can monitor memory usage and hunt 
# the top memory consuming process
#
# github.com/fkvd	06.12.2022

import psutil, time
from math import floor

percantage_threshold = 70
refresh_rate = 3
wait_after_kill = 10

def getMaxPID():
	pidList = psutil.pids()

	max_pid = -1
	max_memory = 0

	for pid in pidList:
		pidMemoryUsage = psutil.Process(pid).memory_info()[0]
		if(pidMemoryUsage > max_memory):
			max_pid = pid
			max_memory = pidMemoryUsage
			
	max_memory = floor(max_memory / (2.0**20))
	return max_pid, psutil.Process(max_pid).name(), max_memory 

def getMemoryUsage():
	return psutil.virtual_memory().percent


while(True):
	usage = getMemoryUsage()
	
	if(usage > percantage_threshold):
		pid, name, size  = getMaxPID()
		psutil.Process(pid).kill()
		print("pid:" + str(pid) + " size:" + str(size) + "MB " + name + " is hunted!")
		time.sleep(wait_after_kill)
	else:
		time.sleep(refresh_rate)
	


