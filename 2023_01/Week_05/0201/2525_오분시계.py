h,m = map(int,input().split())
m2 = int(input())
m3 = m+m2
m4 = (m3%60)

if h <= 23 and m3 < 60:
    print(h,m3)
elif h < 23 and m3 >=60:
    print(h+int(m3/60),m4)
elif h >= 23 and m3 >= 60 :
    print(0,m4)





# 1. h시 m3이 60 넘지 않을때
# 2. h시 m3가 60을 넘을 때t
# 3. 0시 m3이 60 넘지 않을 때
# 4. 0시 m3가 60을 넘을 때
    

