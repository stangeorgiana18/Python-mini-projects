# Create a program that will create a graph or network from a series of links.

# value = dictionary[key]


def check_node(node, graph):

    # check if a node is in a graph 
    if node in graph:
        return True
    return False


def dictionary_graph(links):

    '''
    take in a list of links as lists or tuples, with 2 elements as the connected dots, 
    return a graph as a dictionary

    eg. input: [(1,2),(1,4),(2,3),(3,4)] or [[1,2],[1,4],[2,3],[3,4]]
    
    eg. output (from input): {1:[2,4],2:[1,3],3:[2,4],4:[1,3]}
    '''

    # empty dictionary to represent the graph
    # the keys = the nodes in the graph
    # the values associated with each key = the list of nodes that the key is connected to
    graph = {}

    # iterate through the input links (lists in list or tuple unpacking)
    for link in links:
        # check if each node is in the graph, otherwise add it
        for node in link:

            # true if the node is NOT in the graph
            if not check_node(node, graph):
                # initialie an empty list as its corresponding value
                # the node has no connections/edges at the moment
                graph[node] = []

        # for both ends of the link, add the other end to the node's connections
        graph[link[0]].append(link[1]) # for the first eg. link = (1, 2): graph[1].append(2) --> add 2 to the list , graph[1] become [2]
        graph[link[1]].append(link[0])

        # after the first iteration, the graph: {1: [2], 2: [1]}

    print(graph) # for debugging purposes
    return graph 



# tests
# test if condition returns True, if not, the program will raise an AssertionError

assert(dictionary_graph([(1,2),(1,4),(2,3),(3,4)]) == {1:[2,4],2:[1,3],3:[2,4],4:[1,3]})
assert(dictionary_graph([[1,2],[1,4],[2,3],[3,4]]) == {1:[2,4],2:[1,3],3:[2,4],4:[1,3]})