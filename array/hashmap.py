palavra = "adadwdaw"
count = {}
for key, letra in enumerate(palavra):
    if not count.get(letra):
        count[letra] = [key, 1]
    else:
        count[letra][1] +=1
    
for letra, dados in count.items():
    print(f"{letra} : {dados}")