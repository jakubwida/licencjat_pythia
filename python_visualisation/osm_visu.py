import matplotlib.pyplot as plt
import math

def line_to_dict(line):
	segments=line.split(" ")
	dictionary={}
	for i in segments:
		split= i.split(":")
		dictionary[split[0]]=split[1]
	return dictionary




data_file = open("new_out.txt","r")
lines = data_file.readlines()



#plt.axis([-math.pi,math.pi,-5,10])
plt.ylabel("lat")
plt.xlabel("lon")

for i in lines:
	dictionary = line_to_dict(i)
	lat = dictionary["lat"]
	lon = dictionary["lon"]

	#phi-> x, eta->y, pt->rozmiar kropki

	#temp
	#phi = float(phi)
	#phi = phi+2*math.pi
	#

	#phi powinno byc w zakresie 0-2pi
	#eta tak okolo 0-10

	plt.plot(lat, lon, 'ro')
plt.show()
		
