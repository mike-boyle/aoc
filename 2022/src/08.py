from utils.api import get_input
import numpy

input_str = get_input(8)

trees = [list(map(int, [*line])) for line in input_str.split("\n")]
trees = numpy.array(trees)

visible_trees = numpy.zeros_like(trees, int)
viewable_trees = numpy.ones_like(trees, int)

for _ in range(4):
    for x, y in numpy.ndindex(trees.shape):
        lower_trees = [tree < trees[x, y] for tree in trees[x + 1 : :, y]]

        visible_trees[x, y] |= all(lower_trees)

        last_viewable_tree = len(lower_trees)
        for i, tree in enumerate(lower_trees):
            if ~tree:
                last_viewable_tree = i + 1
                break
        viewable_trees[x, y] *= last_viewable_tree

    trees, visible_trees, viewable_trees = map(
        numpy.rot90, [trees, visible_trees, viewable_trees]
    )

visible_tree_count = visible_trees.sum()
viewable_tree_count = viewable_trees.max()

print(visible_tree_count)
print(viewable_tree_count)
