def net_node_balance():
    node, edge = map(int, input().split())
    incoming = [0] * node
    outgoing = [0] * node


    from_list = list(map(int, input().split()))
    to_list = list(map(int, input().split()))


    for i in range(edge):
        outgoing[from_list[i] - 1] += 1
        incoming[to_list[i] - 1] += 1


    for i in range(node):
        print(incoming[i] - outgoing[i], end=" ")


net_node_balance()
