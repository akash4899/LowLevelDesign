from node import Node

class Driver:
    def __init__(self):
        self.dict = {}
        self.mn_x = 0
        self.mx_x = 0
        self.mn_y = 0
        self.mx_y = 0
        self.x = 0

    def print_binary_tree(self, node):
        self.helper(node,  0)
        for key, node in self.dict.items():
            print(key)
            if node is "*":
                print(node)
            else:
                print(node.val)


        print(self.mx_y)
        print(self.mx_x)
        print("***********************************************************************")

        for y in range(0, self.mx_y+1):
            for x in range(0, self.mx_x+1):
                if self.dict.get((x, y)):
                    if self.dict[(x, y)] is "*":
                        print("*", end="")
                    else:
                        print(self.dict[(x, y)].val, end="")
                else:
                    print(" ", end="")
            print("\n")



    def helper(self, node, y):
        if node is None:
            return

        self.mn_y = min(y, self.mn_y)
        self.mx_y = max(y, self.mx_y)
        # self.mx_x = max(x, self.mx_x)


        if node.left is not None:
            self.helper(node.left,y+1)
        else:
            # print('*')
            self.dict[(self.x, y+1)] = '*'
            self.mx_y = max(self.mx_y, y+1)
            self.x = self.x+1

        # print(node.val)
        self.dict[(self.x, y)] = node
        self.x = self.x+1
        self.mx_x = self.x
        if node.right:
            self.helper(node.right, y+1)
        else:
            # print('*')
            self.dict[(self.x, y+1)] = '*'
            self.x += 1
            self.mx_y = max(self.mx_y, y + 1)

        return




    def run(self):
        print('-' * 80)
        print('Example tree with 5 nodes and big numbers')
        n5 = Node(5343, None, None)
        n2 = Node(202, None, n5)
        n4 = Node(40232, None, None)
        n3 = Node(32, None, n4)
        n1 = Node(1923, n2, n3)
        self.print_binary_tree(n1)

driver = Driver()
driver.run()