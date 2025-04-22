# Floyd Warshall Algorithm

INF = 9999

def printSolution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == INF:
                print('INF', end=' ')
            else:
                print(distance[i][j], end=' ')
        print()

def FloydWarshall(nV, G):
    distance = G
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
    printSolution(nV, distance)



