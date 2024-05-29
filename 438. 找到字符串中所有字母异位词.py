class Solution:
    def findAnagrams(self,s,p):
        slen=len(s)
        plen  = len(p)
        if slen<plen:
            return []
        s_count = [0]*26
        p_count = [0]*26
        res = list()
        for i in range(plen):
            s_count[ord(s[i])-ord('a')]+=1
            p_count[ord(p[i]) - ord('a')] += 1
        if s_count == p_count:
            res.append(0)
        for i in range(slen-plen):
            j = i+plen
            s_count[ord(s[i])-ord('a')]-=1
            s_count[ord(s[j])-ord('a')]+=1
            if s_count==p_count:
                res.append(i+1)
        return res
sol  = Solution()
s = "cbaebabacd"
p = "abc"
print(sol.findAnagrams(s,p))

# 在Python中，使用[0] * 26
# 这样的列表乘法创建多个列表时，每个星号(*)
# 操作都会创建一个新的列表对象。所以，s_count和p_count是两个独立的列表，它们各自拥有独立的内存空间，尽管它们的内容初始化相同（每个元素都是0），但并不是指向同一个内存。
#
# 这意味着对p_count的修改不会影响到s_count，反之亦然
# 在Python中，两个列表（list）之间的比较操作 == 会逐元素检查两个列表的每个对应元素是否相等，并且要求两个列表的长度也必须相等。如果所有对应位置的元素都相等且两个列表长度一致，那么这两个列表就被视为相等。
