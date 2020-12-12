import re


class BagProcessor(object):
    def __init__(self, input_file='input.txt'):
        self.input_file = input_file

    def execute(self):
        rules = self.read_rules()
        tree = self.make_tree(rules, root='shiny gold')
        return self.get_num_unique_nodes(tree, colors=set())

    def read_rules(self):
        parent_exp = re.compile('''^(.+) bags contain''')
        child_exp = re.compile('''(?:contain|,)? ([0-9]+) ([a-z ]+) bag(?:s?)''')
        f = open(self.input_file, "r")
        rules = {}
        for line in f:
            parent = parent_exp.findall(line)[0]
            children = child_exp.findall(line)
            childs = []
            for child in children:
                childs.append(child[1])
            rules[parent] = childs
        f.close()
        return rules

    def make_tree(self, all_subtrees, root):
        tree = {}
        tree[root] = {}
        return self.walk_tree(tree, root, all_subtrees)

    def walk_tree(self, tree, root, all_subtrees):

        for parent, children in all_subtrees.items():
            if root in children and parent not in tree.get(root, []):
                tree[root][parent] = {}

        for subparent, _ in tree[root].items():
            subtree = self.walk_tree(tree={subparent: {}}, root=subparent, all_subtrees=all_subtrees)
            tree[root][subparent] = subtree[subparent]

        return tree

    def get_num_unique_nodes(self, tree, colors):
        for p, c in tree.items():
            colors.add(p)
            if c and isinstance(c, dict):
                self.get_num_unique_nodes(c, colors)
        return len(colors) - 1


# result = BagProcessor(input_file='input_test.txt').execute()
result = BagProcessor().execute()
print(result)
