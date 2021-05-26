class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1,v2=version1.split('.'),version2.split('.')
        for x in range(max(len(v1),len(v2))):
            if x>len(v1)-1: a=0
            else: a=int(v1[x])
            if x>len(v2)-1: b=0
            else: b=int(v2[x])
            if a>b:
                return 1
            elif a<b:
                return -1
            else:
                continue
                
        return 0
