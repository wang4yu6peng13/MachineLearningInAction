import kMeans

'''
geoResults = kMeans.geoGrab('1 VA Center', 'Augusta, ME')
print geoResults
print geoResults['ResultSet']['Error']
print geoResults['ResultSet']['Results'][0]['longitude']
print geoResults['ResultSet']['Results'][0]['latitude']
kMeans.massPlaceFind('portlandClubs.txt')
'''

kMeans.clusterClubs(5)