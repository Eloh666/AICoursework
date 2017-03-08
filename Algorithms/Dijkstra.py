from heapq import heappush, heappop
from itertools import count
import networkx as nx


dirEnum = {
    0: 'forward',
    1: 'backward',
}


def bidirectionalDijkstra(G, source, target, weight='weight'):
    if source == target:
        return 0, [source]

    # stores the distances by node and based on the visit direction
    dists = {
        0: {},
        1: {},
    }

    # stores the available paths
    paths = {
        0: {source: [source]},
        1: {target: [target]},
    }

    # heap of (distance, node) tuples for extracting next node to expand
    fringe = {
        0: [],
        1: [],
    }

    # nodes who have already been seen and investigated
    visited = {
        0: {source: 0},
        1: {target: 0},
    }

    # neighs for extracting correct neighbor information
    neighs = {
        0: G.successors_iter,
        1: G.predecessors_iter,
    }

    c = count()

    # setup the fringe heap
    heappush(fringe[0], (0, next(c), source))
    heappush(fringe[1], (0, next(c), target))

    # variables to hold shortest discovered path
    finalPath = []
    direction = 1
    finalDist = 0
    while fringe[0] and fringe[1]:
        # choose directionection
        # direction == 0 is forward directionection and direction == 1 is back
        direction = 1 - direction
        # extract closest to expand
        (dist, _, v) = heappop(fringe[direction])
        if v in dists[direction]:
            # Shortest path to v has already been found
            continue
        # update distance
        dists[direction][v] = dist  # equal to visited[direction][v]
        if v in dists[1 - direction]:
            # if we have scanned v in both directionections we are done
            # we have now discovered the shortest path
            print(dists)
            print(paths)
            print(fringe)
            return finalDist, finalPath

        for w in neighs[direction](v):
            if direction == 0:  # forward
                minWeight = G[v][w].get(weight, 1)
            else:  # back, must remember to change v,w->w,v
                minWeight = G[w][v].get(weight, 1)
            vwLength = dists[direction][v] + minWeight  # G[w][v].get(weight,1)

            if w in dists[direction]:
                if vwLength < dists[direction][w]:
                    raise ValueError(
                        "Contradictory paths found: negative weights?")
            elif w not in visited[direction] or vwLength < visited[direction][w]:
                # relaxing
                visited[direction][w] = vwLength
                heappush(fringe[direction], (vwLength, next(c), w))
                paths[direction][w] = paths[direction][v] + [w]
                if w in visited[0] and w in visited[1]:
                    # see if this path is better than than the already
                    # discovered shortest path
                    totaldist = visited[0][w] + visited[1][w]
                    if finalPath == [] or finalDist > totaldist:
                        finalDist = totaldist
                        revpath = paths[1][w][:]
                        revpath.reverse()
                        finalPath = paths[0][w] + revpath[1:]
    raise nx.NetworkXNoPath("No path between %s and %s." % (source, target))