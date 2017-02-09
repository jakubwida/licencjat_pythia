import matplotlib.pyplot as plt
import math

def line_to_dict(line):
	segments=line.split(" ")
	dictionary={}
	for i in segments:
		split= i.split(":")
		dictionary[split[0]]=split[1]
	return dictionary




data_file = open("output.txt","r")
lines = data_file.readlines()



plt.axis([-math.pi,math.pi,-5,10])
plt.ylabel("eta")
plt.xlabel("phi")

for i in lines:
	dictionary = line_to_dict(i)
	ids = dictionary["id"]
	eta = dictionary["eta"]
	phi = dictionary["phi"]
	pt = dictionary["pt"]

	#phi-> x, eta->y, pt->rozmiar kropki

	#temp
	#phi = float(phi)
	#phi = phi+2*math.pi
	#

	#phi powinno byc w zakresie 0-2pi
	#eta tak okolo 0-10


	print(str(ids)+" "+str(eta)+" "+str(phi))
	plt.plot(phi, eta, 'ro',ms=pt)
plt.show()
		
