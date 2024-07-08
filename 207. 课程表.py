import collections


class Solution:
    def canFinish(self,numCourses,prerequisites):
        numInedges =[0]*numCourses
        outEdges = [[] for _ in range(numCourses)]
        queue=collections.deque()
        for edge in prerequisites:
            numInedges[edge[0]]+=1
            outEdges[edge[1]].append(edge[0])
        for course in range(numCourses):
            if numInedges[course]==0:
                queue.append(course)
        while queue:
            course=queue.popleft()
            numCourses-=1
            for next in outEdges[course]:
                numInedges[next]-=1
                if numInedges[next]==0:
                    queue.append(next)
        return numCourses==0
