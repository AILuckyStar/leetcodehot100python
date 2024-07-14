import heapq


class Solution:
    def topKFrequent(self,nums,k):
        dic={}
        for i in range(len(nums)):
            dic[nums[i]]=dic.get(nums[i],0)+1
        pre_que=[]
        for num,freq in dic.items():
            heapq.heappush(pre_que,(freq,num))
            if len(pre_que)>k:
                heapq.heappop(pre_que)
        # res=[0]*k
        # for i in range(k-1,-1,-1):
        #     res[i]=heapq.heappop(pre_que)[1]
        return [x for _,x in pre_que]
