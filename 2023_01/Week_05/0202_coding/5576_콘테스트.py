w_ = []
k_ = []

for i in range(10):
    w = int(input())
    w_.append(w)
    w_ = sorted(w_)
    
for i in range(10):
    k = int(input())
    k_.append(k)
    k_ = sorted(k_)


print(w_[7] +w_[8]+w_[9],k_[7]+k_[8]+k_[9])
