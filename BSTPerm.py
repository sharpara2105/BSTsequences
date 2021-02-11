def sequenceHelper(array, currentSol, resultantSolution):
    if not len(array) and len(currentSol):
        resultantSolution.append(currentSol)
    else:
        for i in range(len(array)):
            """ select all the nodes except the node pointed by 'i' since we have processed it and 
            append it in the newArray. Also, append the removed node in our newSol(containing temporary viable solution)"""

            newArray = array[:i] + array[i + 1:]
            newSol = currentSol + [array[i].value]

            """ now our choices array (newArray) will expand because we can add the children of this removed node(node[i]) [if exists] 
            (newArray = remaining elements after removing node[i] and children of the removed node) """
            if array[i].left:
                newArray.append(array[i].left)
            if array[i].right:
                newArray.append(array[i].right)
            """ since, we now have elements that can be a viable solution,
            call recursively the function to get all the permutations with this 
            newArray formed and subsequently we will append all the output sequences 
            in the resultantSolution's array """
            sequenceHelper(newArray, newSol, resultantSolution)


def generateSequences(root):
    if root is None:
        return

    """initialise the sol array with root and pass the children of the root for further processing"""
    sol, resultant_solution, children = [], [], []
    sol.append(root.value)

    """append the children of the root"""
    if root.left:
        children.append(root.left)
    if root.right:
        children.append(root.right)

    """call the helper method to generate all the output sequences possible satisfying the constraint"""
    sequenceHelper(children, sol, resultant_solution)

    return resultant_solution


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


# Test case 1:
root = Node(6)
root.left = Node(4)
root.right = Node(7)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.right = Node(8)
""" 6
   / \
  4   7 
 / \   \
3   5   8"""

# Test case 2:
# root = Node(2)
# root.left=Node(1)
# root.right=Node(3)

# Test case 3:
# root = Node(4)
# root.left=Node(2)
# root.right=Node(5)
# root.left.left=Node(1)
# root.left.right=Node(3)
# root.right.right=Node(6)

# Test case 4:
# root = Node(2)
# root.left=Node(1)


print(generateSequences(root))

""" Rough work:

# def permutationHelper(array,currentSol,resultantSolution):
#     if not len(array) and len(currentSol):
#         resultantSolution.append(currentSol)
#     else:
#         for i in range(len(array)):
#             newArray = array[:i] + array[i+1:]
#             newSol= currentSol+[array[i]]
#             permutationHelper(newArray,newSol,resultantSolution)


# def getPermutations(array):
#     permutations=[]
#     permutationHelper(array,[],permutations)
#     return permutations
#
# print(getPermutations([1,2,3]))


# def permutationHelper(q,sol,resultant_solution):
#     if len(q)==0:
#         resultant_solution.append(sol)
#     new_solution= sol
#     for i in range(len(q)):
#         for j in range(i,len(q)):
#             temp = []
#             q[i],q[j]=q[j],q[i]   #swap
#             for index in range(1,len(q)):
#                 temp.append(q[index])
#             #process the first element for its children:
#             if q[0].left:
#                 temp.append(q[0].left)
#             if q[0].right:
#                 temp.append(q[0].right)
#             new_solution.append(q[0].value)
#
#             permutationHelper(temp,new_solution,resultant_solution)
#             # sol.pop() #undo the solution created
#             q[i],q[j]=q[j],q[i]   #undo the swap
"""

