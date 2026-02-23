# o algoritmo funciona assim [a,b,c,d]
#               ponteiro l | a  ->   d  | ponteiro r
#                             [d, b, c, a] 
#                                 b -> c
#                               [d, c, b, a]               
p = "abcd 1234 abvc"
l , r =0,0
palavra_revesa =""
while len(p) > r:
    if(p[r] != " "):
        # adiciona um sempre que nao tiver espaco em branco 
        
        r+=1
        continue
    palavra_revesa +=(p[l:r:][::-1])
    # inverte a p
    r +=1
    l = r
    palavra_revesa += " "
palavra_revesa +=(p[l:r:][::-1])
# inverter a ultima palavra ja que o while acaba mas o r e l ja estao setados

print(palavra_revesa)