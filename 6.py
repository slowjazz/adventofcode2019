inp = open('6.in', 'r').readlines()

# dic mapping node : # of orbits - counts
# dic mapping orbit : orbit - center 
# while orbits[node] != None, plus one to counts[node] and go to orbits[node]

counts = {}
orbits = {}
parents = {'YOU':{}, 'SAN':{}} # nodes: dist

def putParents(t, node, dist):
    if node not in parents[t]:
        parents[t][node] = 0
    parents[t][node] = dist
    #print(node)
    if node in orbits:
        putParents(t, orbits[node], dist +1)

def travel(center, orbit, orig, dist):
    #print(center, orbit)
    if center not in counts:
        counts[center] = 0
    if orbit not in counts:
        counts[orbit] = 0
    counts[center] += counts[orig] +1
    
    if orbit not in orbits:
        orbits[orbit] = center
    if center in orbits: 
        travel(orbits[center], center, orig, dist + 1)


    

for i in inp:
    center, orbit = [x.strip() for x in i.split(')')] # b orbits a
    #print('starting: ',center, orbit)
    travel(center, orbit, orbit, 0)
    #print(center, orbit, counts)

[putParents(x, orbits[x], 0) for x in ['YOU','SAN']]

ret = 0
for k,v in counts.items():
    ret += v
#print(ret)
nodedist = []
for x in parents['YOU'].keys():
    if x in parents['SAN']:
        nodedist.append((parents['YOU'][x] + parents['SAN'][x], x) )
print(parents)
print(min(nodedist, key = lambda x: x[0]))
