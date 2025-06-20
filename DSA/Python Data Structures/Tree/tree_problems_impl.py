
# 1. Extent tree class built in our main tutorial so that it takes name and designation in data part of TreeNode class. Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree. As shown below,

class TreeNode:
    def __init__(self, data, designation):
        self.data = data
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, format='both'):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print( (prefix + self.data) if format == 'name'
              else((prefix + self.designation) if format == 'designation'
                   else (prefix + f'{self.data} ({self.designation})') ) )
        if self.children:
            for child in self.children:
                child.print_tree(format)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)



def build_management_tree():
    # CTO Hierarchy
    infra_head = TreeNode("Vishwa","Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval","Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    cto = TreeNode("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Gels","HR Head")

    hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    ceo = TreeNode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo

if __name__ == '__main__':
    root_node = build_management_tree()
    print("printing name")
    root_node.print_tree("name") # prints only name hierarchy
    print("\nprinting designation hierarchy")
    root_node.print_tree("designation") # prints only designation hierarchy
    print("\nprinting both")
    root_node.print_tree("both") # prints both (name and designation) hierarchy
	
	
	
	