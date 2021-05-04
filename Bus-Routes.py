class Solution(object):
    """
    815. Bus Routes

    You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.
    For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence
    1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
    You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop
    target. You can travel between bus stops by buses only.
    Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

    Constraints:

        -   1 <= routes.length <= 500.
        -   1 <= routes[i].length <= 105
        -   All the values of routes[i] are unique.
        -   sum(routes[i].length) <= 105
        -   0 <= routes[i][j] < 106
        -   0 <= source, target < 106
    """

    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """

        bus_stops = {}

        n = len(routes)     # number of buses

        for i in range(n):
            for stop in routes[i]:
                if stop in bus_stops:
                    bus_stops[stop].append(i)
                else:
                    bus_stops[stop] = [i]

        neighbor_buses = [[] for _ in range(n)]

        for neighbors in bus_stops.values():
            if len(neighbors) >= 2 :  # at least 2 buses meet?
                p = len(neighbors)
                for b1 in neighbors:
                    for b2 in neighbors:
                        if b1 != b2 and b2 not in neighbor_buses[b1]:
                            neighbor_buses[b1].append(b2)

        buses_to_take = []
        buses_already_taken = [-1 for _ in range(n)]    # -1 if not taken yet, else positve number (number of buses taken in total)
        last_possible_buses = set()

        if source not in bus_stops or target not in bus_stops:  # Initialization for BFS
            return -1
        elif target == source:
            return 0
        else:
            buses_to_take = bus_stops[source]
            for bus in buses_to_take:
                buses_already_taken[bus] = 1
            last_possible_buses = set(bus_stops[target])

        while buses_to_take:

            curr_bus = buses_to_take.pop(0)

            if curr_bus in last_possible_buses:     # Last Bus?
                return buses_already_taken[curr_bus]
            
            for neighbor in neighbor_buses[curr_bus]:
                if buses_already_taken[neighbor] < 0:   # not already taken?

                    buses_to_take.append(neighbor)
                    buses_already_taken[neighbor] = buses_already_taken[curr_bus] + 1

        return -1
        

sol = Solution()
print(sol.numBusesToDestination([[1,7],[3,5]], 5, 5))
                
        