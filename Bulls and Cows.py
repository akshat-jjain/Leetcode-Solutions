class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret=list(secret)
        guess=list(guess)
        
        b=sum([1 for x in range(len(guess)) if secret[x]==guess[x]] )
        c=0
        for x in guess:
            if x in secret:
                secret.remove(x)
                c+=1
        c=c-b                
           
        s=str(b)+'A'+str(c)+'B'
        return s
