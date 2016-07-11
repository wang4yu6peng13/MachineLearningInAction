import fpGrowth

rootNode = fpGrowth.treeNode('pyramid', 9, None)
rootNode.children['eye'] = fpGrowth.treeNode('eye', 13, None)
rootNode.disp()
rootNode.children['phoenix'] = fpGrowth.treeNode('phoenix', 3, None)
rootNode.disp()