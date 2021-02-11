Problem Statement:

Given a BST satisfying 2 properties:
(i) Nodes just have distinct integers
(ii) This tree will not be balanced.
Given such a BST, we need to find all the sequences of the integers that are in the node.

Test Cases:

(i)[6,4,7,3,5,8]
     
     6
    / \
    4   7 
    / \   \
    3   5   8


[[6, 4, 7, 3, 5, 8], 
[6, 4, 7, 3, 8, 5], 
[6, 4, 7, 5, 3, 8], 
[6, 4, 7, 5, 8, 3], 
[6, 4, 7, 8, 3, 5], 
[6, 4, 7, 8, 5, 3],
[6, 4, 3, 7, 5, 8],
[6, 4, 3, 7, 8, 5],
[6, 4, 3, 5, 7, 8],
[6, 4, 5, 7, 3, 8], 
[6, 4, 5, 7, 8, 3], 
[6, 4, 5, 3, 7, 8], 
[6, 7, 4, 8, 3, 5], 
[6, 7, 4, 8, 5, 3], 
[6, 7, 4, 3, 8, 5], 
[6, 7, 4, 3, 5, 8], 
[6, 7, 4, 5, 8, 3], 
[6, 7, 4, 5, 3, 8], 
[6, 7, 8, 4, 3, 5], 
[6, 7, 8, 4, 5, 3]]



(ii) [2,1,3] 

    2
    / \
    1   3
  
o/p sequences:
[2,1,3], [2,3,1]


Methodology/logic: 

(i)	The parent should always come before its children, with this order preserved we can get a list of viable solutions.
(ii)	And, at every level of the tree, we will have certain choices which we can make as follows:
At first, we pick up the root node and let’s say it has only one or no child then our choice will expand by adding that one child or nothing otherwise, if the root node has 2 children,
we have a choice to select either of the children (left/right). 
case 1:

(if we choose left child, then explore/get the children of the left child) 
If left child is not a leaf node
then our choices will expand to (root's right child) or (root's left child's children) 
case2:

(if we choose right child, then explore/get the children of the right child)
If right child is not a leaf node
then our choices will expand to (root's left child) or (root's right child's children) 


And we keep on doing this till we traverse all the nodes of the BST or our choices get exhausted.
