s =  "gustavvossaa"
r,l = 0,0
a = {}
while r < len(s):
    c = s[r]
    if not a.get(c):
        a[c] = [1]
        r+=1
        continue
    else:
        a[c][0] +=1
        r+=1
        if not a[c][0] >=3:
            continue
        
    
    while l < r:
        b = s[l]
        if not a[c] == a[b]:
            a[b][0] -=1
            l+=1
            continue
        else:
            a[c][0] -=1
            l+=1
            break
            

print(s[l:r])