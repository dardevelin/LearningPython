class Node
  attr_accessor :key, :parent, :left, :right

  def initialize(key, parent)
    @key = key
    @parent = parent
  end
end

class Tree
  def initialize(root)
    @root = root
  end

  def print_with_constant_space
    current, old = @root, nil
    while current do
      # Going UP
      if old && old.parent == current
        # Go right if exists
        # otherwise continue up
        next_node = (current.right || current.parent)
        current, old = next_node, current

      # Going DOWN
      else
        puts current.key

        # Go left if exists
        # otherwise go right if exists
        # otherwise go up
        next_node = (current.left || current.right || current.parent)
        current, old = next_node, current
      end
    end
  end
end

root         = Node.new(0, nil)
root.left    = (node_1  = Node.new(1, root))
node_1.left  = (node_2  = Node.new(2, node_1))
node_2.right = (node_3  = Node.new(3, node_1))
node_3.left  = (node_4  = Node.new(4, node_3))

node_1.right = (node_5  = Node.new(5, root))
node_5.left  = (node_6  = Node.new(6, node_5))
node_6.right = (node_7  = Node.new(7, node_5))
node_7.right = (node_8  = Node.new(8, node_5))
node_8.left  = (node_9  = Node.new(9, node_8))
node_9.right = (node_10 = Node.new(10, node_8))
node_8.right = (node_11 = Node.new(11, node_5))

node_5.right = (node_12 = Node.new(12, root))
node_12.left = (node_13 = Node.new(13, node_12))

tree = Tree.new(root)
tree.print_with_constant_space