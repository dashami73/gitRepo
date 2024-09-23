
class mathFunc(object):
    def __init__(self):
        pass
    def Fib(self, n):
        a, b  = 1, 1
        for i in range(1, n):
            a, b = a + b, a
            #print(a)
        return a


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


def dfs_test():
    graph = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8'],
        '8': []
    }
    visted = set()
    print("Following is the graph first search")
    dfs(visted, graph, '5')
def main():
    dfs_test()
    mF = mathFunc()
    F10 = mF.Fib(10)
    print(F10)

if __name__=="__main__":
    main()