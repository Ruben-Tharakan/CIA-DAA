 def edge(a, b, c):
	graph.append([a, b, c])

def printMatrix(distance):
	print("Vertex Distance from Source")
	for i in range(V):
		print("{0}\t\t{1}".format(i, distance[i]))

def BF(Source):
	distance = [float("Inf")] * V
	distance[Source] = 0

	for _ in range(V - 1):
		for a, b, c in graph:
			if distance[a] != float("Inf") and distance[a] + c < distance[b]:
				distance[b] = distance[a] + c

	for a, b, c in graph:
		if distance[a] != float("Inf") and distance[a] + c < distance[b]:
			print("Graph has -ve weight cycle")
			return

	printMatrix(distance)

if __name__ == '__main__':
    V=6 
    graph=[]
    edge(0, 1, 10)
    edge(0, 5, 8)
    edge(1, 3, 2)
    edge(2, 1, 1)
    edge(3, 2, -2)
    edge(4, 1, -4)
    edge(4, 3, -1)
    edge(5, 4, 1)

    BF(0)