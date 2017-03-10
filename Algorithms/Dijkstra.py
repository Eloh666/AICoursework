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
            # choose direction
            # direction == 0 is forward direction and direction == 1 is back
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
                # the shorted path is found
                self.log('\n\nBidirectional scan complete.')
                self.log('\Shortest path found ' + str(self.finalPath))
                self.log('Global distance ' + str(self.finalDist))
                self.finished = True
                if not stepping:
                    self.reRender()
                return self.finalDist

            self.log('Checking node ' + str(self.coordinates[v]) + ' neighbors')
            if stepping:
                self.primaryVisited = [v]
                self.secondaryVisited = list(self.neighs[direction](v))
                self.path = []
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
                    if direction == 'forward':
                        self.log('Adding new distance from source: ' + str(vwLength))
                    else:
                        self.log('Adding new distance from target: ' + str(vwLength))
                    self.log('Mapping updated')
                    # relaxing
                    self.visited[direction][w] = vwLength
                    heappush(self.fringe[direction], (vwLength, next(self.c), w))
                    self.paths[direction][w] = self.paths[direction][v] + [w]
                    if w in self.visited['forward'] and w in self.visited['backward']:
                        totalDistance = self.visited['forward'][w] + self.visited['backward'][w]
                        self.log('Source --> Destination path found')
                        self.log('The distance is: ' + str(totalDistance))
                        if self.finalPath:
                            self.log('Comparing new path to previous ones')
                            self.log('Older option: ' + str(self.finalDist))
                        if self.finalPath == [] or self.finalDist > totalDistance:
                            if self.finalDist > totalDistance:
                                self.log('The new path is better, selecting')
                            else:
                                self.log('Selecting the path as current best')
                            self.finalDist = totalDistance
                            reversePath = self.paths['backward'][w]
                            reversePath.reverse()
                            self.finalPath = self.paths['forward'][w] + reversePath[1:]
                            self.log('New temporary best path: ')
                            self.log(str(self.finalPath))
                        else:
                            self.log('The previous options are better')
                            self.log('Discarding')

            if stepping:
                self.log('\n')
                return None
        self.log("No path between %s and %s." % (self.source, self.target))
        self.finished = True
        self.noPath = True
        return -1
