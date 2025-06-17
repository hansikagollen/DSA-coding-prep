class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod=1000000007
        if n==1:
            return m
        if m==1:
            if k==n-1:
                return 1
            else:
                return 0

        if k==0:
            return int(m*(m-1)**(n-1)%mod)

        prev_row=[0]*(k+1)

        for i in range(1,n+1):
            current_row=[m*((m-1)**(i-1))%(mod)] + [0] *k
            for j in range(1,k+1):
                current_row[j]=(prev_row[j]*(m-1)+prev_row[j-1]) % (mod)

            prev_row=current_row
        return prev_row[-1] % mod        