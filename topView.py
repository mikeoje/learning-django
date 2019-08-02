def topView(root):
    this_level = [(root, 0)]
    scores = {}
    while this_level:
        for _ in range(len(this_level)):
            node, score = this_level.pop(0)
            if not node:
                continue
            if score not in scores:
                scores[score] = node.info
            this_level.extend(
                [(node.left, score - 1),
                (node.right, score + 1)])

    for _, value in sorted(list(scores.items())):
        print(value, end=' ')