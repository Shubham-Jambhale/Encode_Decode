import heapq

class Node:
    def __init__(self, freq, left=None, right=None):

        self.char = freq
 
        # node left of current node
        self.left = left
 
        # node right of current node
        self.right = right

def encode(s):
    
    if not s:
        return (None,None)
    
    if len(set(s)) == 1:
        return (str(1) * len(s),{s[0]: '1'})
    
    #creating a frequency list for each word
    frequency_dictionary = {}
    for ch in s:
        if ch in frequency_dictionary.keys():
            frequency_dictionary[ch] += 1
        else:
            frequency_dictionary[ch] = 1 
    #creating a heap that will store the count/frequency of the words, symbol and the encoded string for each word
    heap = [[count,[symbol,""]] for symbol,count in frequency_dictionary.items()]
    heapq.heapify(heap)
    #iterating over the loop poping the first 2 element and combining them and adding them back to the string.
    while len(heap) > 1:
        left_node =heapq.heappop(heap)
        right_node =heapq.heappop(heap)
        
        #adding codes to the nodes
        for pair_of_nodes in left_node[1:]:
            pair_of_nodes[1] = '0' + pair_of_nodes[1]
        
        for pair_of_nodes in right_node[1:]:
            pair_of_nodes[1] = '1' + pair_of_nodes[1]
        
        #pushing the combined elements into the list
        heapq.heappush(heap,[left_node[0]+right_node[0]]+left_node[1:]+right_node[1:])
        
    #combining all elements with encoded string
    main_list = left_node[1:] + right_node[1:]
#     print(main_list)
    main_dictionary ={}
    encoded_string = ""
    #creating dictionary
    for i in range(len(main_list)):
        main_dictionary[main_list[i][0]] = main_list[i][1]
    #creating encoded string and returning the tuple
    for i in s:
        encoded_string+= main_dictionary[i]

    return (encoded_string,main_dictionary)


#this decode is done using the brute force approach.
# def decode(s , d):
#     res = ""
#     while s:
#         for k,j in d.items():
# #             print(k)
#             if s.startswith(j):
#                 res += k
#                 s = s[len(j):]
#     return res




#creating the tree of dictionary. and iterating over the string
def decode(s , d):
    
    
    start= Node('*')
    for key, val in d.items():
        curr = start
        #if value 1 going right else left
        for i in range(len(val)):
            if val[i] == '1':
                if curr.right:
                    curr = curr.right
                else:
                    #if we are at end of the string then creating node with the key else creating node with dummy symbol
                    if i == len(val)-1:
                        new = Node(key)
                        curr.right = new
                        curr = curr.right
                    else:
                        new = Node('*')
                        curr.right = new
                        curr = curr.right
            else:
                if curr.left:
                    curr = curr.left
                else:
                    if i == len(val)-1:
                        new = Node(key)
                        curr.left = new
                        curr = curr.left
                    else:
                        new = Node('*')
                        curr.left = new
                        curr = curr.left
    #iterating over the string and creating the response
    res = ''
    curr = start
    for digit in s:
        if digit == '1':
            curr = curr.right
            if curr.char != '*':
                res += curr.char
                curr = start
                continue
        else:
            curr = curr.left
            if curr.char != '*':
                res += curr.char
                curr = start
                continue
    return res


print("---Output Begins---")
print()
output = encode("a")
print("Encoded string and dictionary is:", output )
response = decode(output[0],output[1])
print("Decode string is: ",response)
print()

output = encode("aaaaa")
print("Encoded string and dictionary is:", output )
response = decode(output[0],output[1])
print("Decode string is: ",response)
print()

output = encode("abcde")
print("Encoded string and dictionary is:", output )
response = decode(*encode("abcde"))
print("Decode string is: ",response)
print()

output = encode("aaabbbccc")
print("Encoded string and dictionary is:", output )
response = decode(output[0],output[1])
print("Decode string is: ",response)
print()

output = encode("abcdefghijklm")
print("Encoded string and dictionary is:", output )
response = decode(*encode("abcdefghijklm"))
print("Decode string is: ",response)
print()