graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':[],
    'D':[],
    'E':[],
    'F':[]
}
visited=[]

def dfs(graph,start):
    if start not in visited:
        visited.append(start)
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph,neighbour)
            
start_node='A'
dfs(graph,start_node)

for node,edges in graph.items():
    if node in visited:
        print(node,'was visited')
    else:
        print(node,'was not visited')
    
print('\nOrder of visitation')
[print(node,end="") for node in visited]