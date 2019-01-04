'''
Suppose you have a random list of people standing in a queue.
Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people in front of this person who have a height greater 
than or equal to h.
Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

'''

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # Sort first based on height 
        # then sort it number of people with height greater than the person
        sorted_queue = sorted(sorted(people, key = lambda x : x[1]), key = lambda x : x[0], reverse = True)
        print(sorted_queue)
        ans = []
        # ans.append(sorted_queue[0])

        for i,item in enumerate(sorted_queue):
            # list.insert does an append when the position is larger than the current size
            ans.insert(item[1],item)
        print(ans)

Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])