from part1 import BinNode, load, list_to_tree

# --- PART 1

def test_load_simple():
    assert load('[1,2]') == [1,2]

def test_load_simple_nested():
    assert load('[[1,2],3]') == [[1,2],3]
    assert load('[9,[8,7]]') == [9,[8,7]]
    assert load('[[1,9],[8,5]]') == [[1,9],[8,5]]
    
def test_load_multi_nested():
    assert load('[[[[1,2],[3,4]],[[5,6],[7,8]]],9]') == [[[[1,2],[3,4]],[[5,6],[7,8]]],9]
    assert load('[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]') == [[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
    assert load('[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]') == [[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]

def test_list_to_tree_simple():
    node: BinNode = list_to_tree(load('[1,2]'))
    assert node.left == 1
    assert node.right == 2
    assert node.prev == None
    assert node.depth == 0
    
def test_simple_binNode_equality():
    node1: BinNode = list_to_tree(load('[1,2]'))
    node2: BinNode = list_to_tree(load('[1,2]'))
    
    assert node1 == node2
    
def test_simple_binNode_inequality():
    node1: BinNode = list_to_tree(load('[1,2]'))
    node2: BinNode = list_to_tree(load('[1,3]'))
    node3: BinNode = list_to_tree(load('[2,2]'))
    
    assert node1 != node2
    assert node1 != node3
    assert node2 != node3
    
def test_list_to_tree_nested():
    node: BinNode = list_to_tree(load('[1,[2,[3,4]]]'))
    assert node.left == 1
    assert node.right == list_to_tree(load('[2,[3,4]]'))
    assert node.right.left == 2
    assert node.right.right == list_to_tree(load('[3,4]'))
    assert node.right.right.left == 3
    assert node.right.right.right == 4
    
    assert node.prev == None
    assert node.depth == 0
    assert node.right.prev == node
    assert node.right.depth == 1
    assert node.right.right.prev == node.right
    assert node.right.right.depth == 2
    
def test_nested_binNode_equality():
    assert list_to_tree(load('[1,[2,3]]')) == list_to_tree(load('[1,[2,3]]'))
    assert list_to_tree(load('[1,[2,[3,4]]]')) == list_to_tree(load('[1,[2,[3,4]]]'))
    assert list_to_tree(load('[[0,1],[2,[3,4]]]')) == list_to_tree(load('[[0,1],[2,[3,4]]]'))
    
def test_nested_binNode_inequality():
    node1 = list_to_tree(load('[1,[2,3]]'))
    node2 = list_to_tree(load('[1,[4,3]]'))
    node3 = list_to_tree(load('[1,[2,[0,1]]]'))
    
    assert node1 != node2
    assert node1 != node3
    assert node2 != node3

def test_explode_happening():
    assert list_to_tree(load('[[[[[9,8],1],2],3],4]')).explode() == True
    
def test_explode():
    node1: BinNode = list_to_tree(load('[[[[[9,8],1],2],3],4]'))
    node1.explode()
    assert node1 == list_to_tree(load('[[[[0,9],2],3],4]'))
    
    node2: BinNode = list_to_tree(load('[7,[6,[5,[4,[3,2]]]]]'))
    node2.explode()
    assert node2 == list_to_tree(load('[7,[6,[5,[7,0]]]]'))
    
    node3: BinNode = list_to_tree(load('[[6,[5,[4,[3,2]]]],1]'))
    node3.explode()
    assert node3 == list_to_tree(load('[[6,[5,[7,0]]],3]'))
    
    node4: BinNode = list_to_tree(load('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'))
    node4.explode()
    assert node4 == list_to_tree(load('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'))
    
    node5: BinNode = list_to_tree(load('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'))
    node5.explode()
    assert node5 == list_to_tree(load('[[3,[2,[8,0]]],[9,[5,[7,0]]]]'))
    
def test_split_happening():
    assert list_to_tree(load('[[[[0,7],4],[15,[0,13]]],[1,1]]')).split() == True
    
def test_split():
    node1: BinNode = list_to_tree(load('[[[[0,7],4],[15,[0,13]]],[1,1]]'))
    node1.split()
    assert node1 == list_to_tree(load('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]'))

    node2: BinNode = list_to_tree(load('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]'))
    node2.split()
    assert node2 == list_to_tree(load('[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]'))
    
def test_reduce():
    node: BinNode = list_to_tree(load('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'))
    node.reduce()
    assert node == list_to_tree(load('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'))
    
def test_magnitude():
    node1: BinNode = list_to_tree(load('[[1,2],[[3,4],5]]'))
    node1.reduce()
    assert node1.get_magnitude() == 143
    
    node2: BinNode = list_to_tree(load('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'))
    node2.reduce()
    assert node2.get_magnitude() == 1384
    
    node3: BinNode = list_to_tree(load('[[[[1,1],[2,2]],[3,3]],[4,4]]'))
    node3.reduce()
    assert node3.get_magnitude() == 445
    
    node4: BinNode = list_to_tree(load('[[[[3,0],[5,3]],[4,4]],[5,5]]'))
    node4.reduce()
    assert node4.get_magnitude() == 791
    
    node5: BinNode = list_to_tree(load('[[[[5,0],[7,4]],[5,5]],[6,6]]'))
    node5.reduce()
    assert node5.get_magnitude() == 1137
    
    node6: BinNode = list_to_tree(load('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'))
    node6.reduce()
    assert node6.get_magnitude() == 3488
    
def test_part1_aoc_official_example():
    with open("day 18/test.txt", 'r') as inFile:
        numList = [load(_.strip()) for _ in inFile.readlines()]
        
        node: BinNode = list_to_tree(numList.pop(0))
        assert node == list_to_tree(load('[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]'))
        node.reduce()
        
        print("step 1")
        nodeToAdd: BinNode = list_to_tree(numList.pop(0))
        assert nodeToAdd == list_to_tree(load('[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]'))
        node = list_to_tree(load(f"[{repr(node)}, {repr(nodeToAdd)}]"))
        node.reduce()
        assert node == list_to_tree(load('[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]'))
        
        print("step 2")
        nodeToAdd = list_to_tree(numList.pop(0))
        assert nodeToAdd == list_to_tree(load('[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]'))
        node = list_to_tree(load(f"[{repr(node)}, {repr(nodeToAdd)}]"))
        node.reduce()
        assert node == list_to_tree(load('[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]'))
        
        print("step 3")
        nodeToAdd = list_to_tree(numList.pop(0))
        assert nodeToAdd == list_to_tree(load('[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]'))
        node = list_to_tree(load(f"[{repr(node)}, {repr(nodeToAdd)}]"))
        print(node)
        node.reduce()
        print(node)
        assert node == list_to_tree(load('[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]'))
        
        print("step 4")
        nodeToAdd = list_to_tree(numList.pop(0))
        assert nodeToAdd == list_to_tree(load('[7,[5,[[3,8],[1,4]]]]'))
        node = list_to_tree(load(f"[{repr(node)}, {repr(nodeToAdd)}]"))
        print(node)
        node.reduce()
        print(node)
        assert node == list_to_tree(load('[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]'))
        
        print("step 5")
        nodeToAdd = list_to_tree(numList.pop(0))
        assert nodeToAdd == list_to_tree(load('[[2,[2,2]],[8,[8,1]]]'))
        node = list_to_tree(load(f"[{repr(node)}, {repr(nodeToAdd)}]"))
        print(node)
        node.reduce()
        print(node)
        assert node == list_to_tree(load('[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]'))
        
        print("step 6")
        nodeToAdd = list_to_tree(numList.pop(0))
        assert nodeToAdd == list_to_tree(load('[2,9]'))
        node = list_to_tree(load(f"[{repr(node)}, {repr(nodeToAdd)}]"))
        print(node)
        node.reduce()
        print(node)
        assert node == list_to_tree(load('[[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]'))
        
        print("step 7")
        nodeToAdd = list_to_tree(numList.pop(0))
        assert nodeToAdd == list_to_tree(load('[1,[[[9,3],9],[[9,0],[0,7]]]]'))
        node = list_to_tree(load(f"[{repr(node)}, {repr(nodeToAdd)}]"))
        print(node)
        node.reduce()
        print(node)
        assert node == list_to_tree(load('[[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]'))
        
        print("step 8")
        nodeToAdd = list_to_tree(numList.pop(0))
        assert nodeToAdd == list_to_tree(load('[[[5,[7,4]],7],1]'))
        node = list_to_tree(load(f"[{repr(node)}, {repr(nodeToAdd)}]"))
        print(node)
        node.reduce()
        print(node)
        assert node == list_to_tree(load('[[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]'))
        
        print("step 9")
        nodeToAdd = list_to_tree(numList.pop(0))
        assert nodeToAdd == list_to_tree(load('[[[[4,2],2],6],[8,7]]'))
        node = list_to_tree(load(f"[{repr(node)}, {repr(nodeToAdd)}]"))
        print(node)
        node.reduce()
        print(node)
        assert node == list_to_tree(load('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'))

def test_part1_aoc_official_example_2():
    with open("day 18/test2.txt", 'r') as inFile:
        numList = [load(_.strip()) for _ in inFile.readlines()]
        
        node: BinNode = list_to_tree(numList.pop(0))
        node.reduce()
        while len(numList) > 0:
            node = list_to_tree(load(f"[{repr(node)}, {repr(numList.pop(0))}]"))
            node.reduce()
        
        print(node)
        assert node.get_magnitude() == 4140

def test_addition():
    numList = [load(_) for _ in ['[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]']]
    
    node: BinNode = list_to_tree(numList.pop(0))
    assert node == list_to_tree(load('[[[[4,3],4],4],[7,[[8,4],9]]]'))
    node.reduce()
    nodeToAdd: BinNode = list_to_tree(numList.pop(0))
    assert nodeToAdd == list_to_tree(load('[1,1]'))
    node = list_to_tree(load(f"[{repr(node)}, {repr(nodeToAdd)}]"))
    assert node == list_to_tree(load('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'))
    node.reduce()
    assert node == list_to_tree(load('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'))