from heapq import heappush, heappop
from itertools import count
import networkx as nx


def bidirectionalDijkstra(network, log, weight='weight'):
    graph = network.graph
    source = network.source
    target = network.target
    coordinates = network.coordinates

    if source == target:
        log('Matching Source and Destination')
        log('The distance is zero.')
        return 0, [source]

    dirEnum = {
        0: 'forward',
        1: 'backward',
    }



    # stores the distances by node and based on the visit direction
    dists = {
        'forward': {},
        'backward': {},
    }

    # stores the available paths
    paths = {
        'forward': {source: [source]},
        'backward': {target: [target]},
    }

    # heap of (distance, node) tuples for extracting next node to expand
    fringe = {
        'forward': [],
        'backward': [],
    }

    # nodes who have already been seen and investigated
    visited = {
        'forward': {source: 0},
        'backward': {target: 0},
    }

    # neighs for extracting correct neighbor information
    neighs = {
        'forward': graph.successors_iter,
        'backward': graph.predecessors_iter,
    }

    c = count()

    # setup the fringe heap
    heappush(fringe['forward'], (0, next(c), source))
    heappush(fringe['backward'], (0, next(c), target))

    # variables to hold shortest discovered path
    finalPath = []
    directionNum = 1
    finalDist = 0
    while fringe['forward'] and fringe['backward']:
        # choose directionection
        # direction == 0 is forward directionection and direction == 1 is back
        directionNum = 1 - directionNum

        direction = dirEnum[directionNum]
        log('\n\n --- Reversing the lookup')
        log('Visiting direction set to ' + direction)

        # extract closest to expand
        (dist, _, v) = heappop(fringe[direction])
        log('\nExpanding main node ===> ' + str(coordinates[v]))
        if v in dists[direction]:
            # Shortest path to v has already been found
            log('Shortest path already been found ')
            continue
        # update distance
        dists[direction][v] = dist
        if v in dists[dirEnum[1 - directionNum]]:
            log('Node ' + str(coordinates[v]) + ' expanded bidirectionally')
            # node bidirectionally expanded and checked, thus the shorted path is found
            log('\n\nShortest path found ' + str(finalPath))
            log('Global distance ' + str(finalDist))
            return finalDist, finalPath

        log('Checking node ' + str(coordinates[v]) + ' neighbours')
        for w in neighs[direction](v):
            log('\nExpanding node ---> ' + str(coordinates[w]))
            if direction == 'forward':  # forward
                minWeight = graph[v][w].get(weight, 1)
            else:  # back, must remember to change v,w->w,v
                minWeight = graph[w][v].get(weight, 1)
            vwLength = dists[direction][v] + minWeight  # graph[w][v].get(weight,1)
            log('Calculating distance ' + str(vwLength))

            # catches the exception caused by negative paths in djkstras
            if w in dists[direction]:
                if vwLength < dists[direction][w]:
                    log('\n\n\nWarning: Djkstra does NOT support negative weights. Please check the input.')
                    raise ValueError("Wrong input provided: negative weights?")

            elif w not in visited[direction] or vwLength < visited[direction][w]:
                log('Adding the new distance ' + str(vwLength))
                log('Mapping updated')
                # relaxing
                visited[direction][w] = vwLength
                heappush(fringe[direction], (vwLength, next(c), w))
                paths[direction][w] = paths[direction][v] + [w]
                if w in visited['forward'] and w in visited['backward']:
                    log('Merging paths as middle node has been found')
                    totalDistance = visited['forward'][w] + visited['backward'][w]
                    if finalPath == [] or finalDist > totalDistance:
                        finalDist = totalDistance
                        reversePath = paths['backward'][w]
                        reversePath.reverse()
                        finalPath = paths['forward'][w] + reversePath[1:]
    log("No path between %s and %s." % (source, target))
    raise nx.NetworkXNoPath("No path between %s and %s." % (source, target))
