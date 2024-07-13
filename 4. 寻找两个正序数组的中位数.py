class Solution:
    def getKthElement(self,num1,nums2,k):
        m=len(num1)
        n=len(nums2)
        idx1,idx2=0,0
        while True:
            #穷尽其中一个退出或者就剩两个头
            if idx1==m:
                return nums2[idx2+k-1]#num1都小没了，输出num2的第k个就行
            if idx2==n:
                return num1[idx1+k-1]
            if k==1:
                return min(num1[idx1],nums2[idx2])
            maxidx1=min(idx1+k//2-1,m-1)
            maxidx2=min(idx2+k//2-1,n-1)#最大的位置
            max1,max2=num1[maxidx1],nums2[maxidx2]
            if max1<=max2:
                k-=maxidx1-idx1+1#排除这么多小的
                idx1=maxidx1+1 # 新的起点
            else:
                k-=maxidx2-idx2+1
                idx2=maxidx2+1
    def findMedianSortedArrays(self,nums1,nums2):
        m=len(nums1)
        n=len(nums2)
        l=m+n
        if l %2==1:
            return self.getKthElement(nums1,nums2,(l+1)//2)
        else:
            return (self.getKthElement(nums1,nums2,l//2)+self.getKthElement(nums1,nums2,l//2+1))/2


#hard
