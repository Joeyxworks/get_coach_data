import os
os.chdir('E:\\Python\\Head First Python\\hfpy_ch6_data')

def sanitize(time_string):						#定义sanitize函数，当列表中值包含‘-’‘：’将其替换为‘.’
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
	(mins, secs) = time_string.split(splitter)
	return(mins + '.' + secs)

class Athlete:
	def __init__(self, a_name, a_dob=None, a_times=[]):
		self.name = a_name
		self.dob = a_dob
		self.times = a_times

	def top3(self):
		return(sorted(set([sanitize(each_time) for each_time in self.times]))[0:3])

	def add_time(self, time_value):
		self.times.append(time_value)

	def add_times(self, list_of_times):
		self.times.extend(list_of_times)

def get_coach_data(filename):							#定义open_lol函数
	try:
		with open(filename) as f:
			data = f.readline()
			d = data.strip().split(',')
			return(Athlete(d.pop(0), d.pop(0), d))
	except IOError as ioerr:
		print('File error: ', +str(ioerr))
		return(None)	


james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

print(james.name + "'s fastest time are: " +str(james.top3()))
print(julie.name + "'s fastest time are: " +str(julie.top3()))
print(mikey.name + "'s fastest time are: " +str(mikey.top3()))
print(sarah.name + "'s fastest time are: " +str(sarah.top3()))


#james = add_time('2.21')
#sarah = add_times('2.01', '1.91', '1.99')