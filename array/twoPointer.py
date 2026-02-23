# o algoritmo funciona assim [a,b,c,d]
#               ponteiro l | a  ->   d  | ponteiro r
#                             [d, b, c, a] 
#                                 b -> c
#                               [d, c, b, a]               
palavra = "abcd 1234 abvc"
left , right =0,0
palavra_revesa =""
while len(palavra) > right:
    if(palavra[right] != " "):
        # adiciona um sempre que nao tiver espaco em branco 
        
        right+=1
        continue
    palavra_revesa +=(palavra[left:right:][::-1])
    # inverte a palavra
    right +=1
    left = right
    palavra_revesa += " "
palavra_revesa+=(palavra[left:right:][::-1])
# inverter a ultima palavra ja que o while acaba mas o r e l ja estao setados

print(palavra_revesa)