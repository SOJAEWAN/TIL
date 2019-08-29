DFS_Recursive(G,v):
    visited[v] = 1 #

    for each all w in adjacency(G,v)
        if visited[w] != 1:
            DFS_Recursive(G,w)