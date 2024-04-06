def solution(info, edges):

    # iterate `info` to make `tree`
    tree = [[] for _ in range(len(info))]
    for a, b in edges:
        tree[a].append(b)

    # initialize
    stack = [(1, 0, 0, set(tree[0]))]
    max_sheep = 0

    # loop `stack`
    while stack:
        sheep, wolves, current_node, childe_nodes = stack.pop()
        max_sheep = max(max_sheep, sheep)    

        # visit `child_node`
        for next_node in list(childe_nodes):
            # compare `sheep` and `wolves`
            next_sheep = sheep + (info[next_node] == 0)
            next_wolves = wolves + (info[next_node] == 1)
            
            # travel only when sheep is bigger then wolves
            if next_sheep > next_wolves:
                future_node = childe_nodes.union(set(tree[next_node])) - {next_node}
                stack.append((next_sheep, next_wolves, next_node, future_node))
                
    return max_sheep
