import xml.etree.ElementTree as etree

tree = etree.parse('map.osm')
root = tree.getroot()
print(root)

out = open('new_out.txt','w')

for child in root:
	#if 'addr:city' in child.attrib:
	#print(child)
	tags = child
	for i in tags:
		if(i.attrib['k']=='addr:city'):
			out.write('lat:'+str(child.attrib['lat'])+' lon:'+str(child.attrib['lon'])+'\n')
			print(child.attrib['lat'],child.attrib['lon'])
