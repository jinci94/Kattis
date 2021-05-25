N = int(input())
# 2016->2018->...->2026 -> 2029->2031->...->2039 -> 2042->2044->...
years_from_2016 = (N-2016)
print('yes') if (((years_from_2016//13)%2==0 and years_from_2016%13 != 12 and years_from_2016%2==0) or 
        ((years_from_2016//13)%2==1 and years_from_2016%13 != 12 and years_from_2016%2==1)) else print('no')
