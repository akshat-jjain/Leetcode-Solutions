class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a=[]
        for x in range(1,n+1):
            if x%5==0 and x%3==0:
                a.append('FizzBuzz')
            elif x%3==0 :
                a.append('Fizz')
            elif x%5==0:
                a.append('Buzz')
            else:
                a.append(str(x))
                
        return a
