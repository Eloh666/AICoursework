from heapq import heappush, heappop
from Algorithms.AlgorithmWrapper import AlgorithmWrapper

class Dijkstra(AlgorithmWrapper):

    def bidirectionalDijkstra(self, stepping=False):

        if self.finished:
            self.log('\n\nComputation already complete')
            return

        if self.source == self.target:
            self.log('Matching Source and Destination')
            self.log('The distance is zero.')
            return 0, [self.source]

        while self.fringe['forward'] and self.fringe['backward']:
            # choose directionection
            # direction == 0 is forward directionection and direction == 1 is back
            self.directionNum = 1 - self.directionNum

            direction = self.dirEnum[self.directionNum]
            self.log('\n\n--- Visiting direction set to ' + direction)

            # extract closest to expand
            (dist, _, v) = heappop(self.fringe[direction])
            self.log('\nExpanding main node ===> ' + str(self.coordinates[v]))
            if v in self.dists[direction]:
                # Shortest path to v has already been found
                self.log('Shortest path already been found ')
                continue
            # update distance
            self.dists[direction][v] = dist
            if v in self.dists[self.dirEnum[1 - self.directionNum]]:
                self.log('Node ' + str(self.coordinates[v]) + ' expanded bidirectionally')
                # node bidirectionally expanded and checked, thus the shorted path is found
                self.log('\n\nShortest path found ' + str(self.finalPath))
                self.log('Global distance ' + str(self.finalDist))
                self.finished = True
                self.renderer.plotGraph(network=self.network, path=self.finalPath)
                return self.finalDist

            self.log('Checking node ' + str(self.coordinates[v]) + ' neighbors')
            if stepping:
                self.renderer.plotGraph(network=self.network, primaryVisited=[v],
                                        secondaryVisisted=list(self.neighs[direction](v)))
            for w in self.neighs[direction](v):
                self.log('\nExpanding node ---> ' + str(self.coordinates[w]))
                if direction == 'forward':  # forward
                    minWeight = self.graph[v][w].get(self.weight, 1)
                else:  # back, must remember to change v,w->w,v
                    minWeight = self.graph[w][v].get(self.weight, 1)
                vwLength = self.dists[direction][v] + minWeight  # self.graph[w][v].get(weight,1)
                self.log('Calculating distance ' + str(vwLength))

                # catches the exception caused by negative paths in djkstras
                if w in self.dists[direction]:
                    if vwLength < self.dists[direction][w]:
                        self.log('\n\n\nWarning: Djkstra does NOT support negative weights. Please check the input.')
                        raise ValueError("Wrong input provided: negative weights?")

                elif w not in self.visited[direction] or vwLength < self.visited[direction][w]:
                    self.log('Adding the new distance ' + str(vwLength))
                    self.log('Mapping updated')
                    # relaxing
                    self.visited[direction][w] = vwLength
                    heappush(self.fringe[direction], (vwLength, next(self.c), w))
                    self.paths[direction][w] = self.paths[direction][v] + [w]
                    if w in self.visited['forward'] and w in self.visited['backward']:
                        self.log('Merging paths as middle node has been found')
                        totalDistance = self.visited['forward'][w] + self.visited['backward'][w]
                        if self.finalPath == [] or self.finalDist > totalDistance:
                            self.finalDist = totalDistance
                            reversePath = self.paths['backward'][w]
                            reversePath.reverse()
                            self.finalPath = self.paths['forward'][w] + reversePath[1:]
            if stepping:
                self.log('\n')
                return None
        # if not self.fringe['forward'] or self.fringe['backward']:
        #     self.failed = True
        self.log("No path between %s and %s." % (self.source, self.target))
        self.finished = True
        self.renderer.plotGraph(network=self.network, noPath=True)
        return -1
        # raise nx.NetworkXNoPath("No path between %s and %s." % (self.source, self.target))
