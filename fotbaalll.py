i = 30
bord = 0
bakht = 0
mosaui = 0

while True:
    em = int(input("emtiaz ra vared on :"))
    if em == 0 or em == 1 or em == 3:
        if em == 0:
            bakht+=1
            i-=1
        elif em == 1:
            mosaui+=1
            i-=1
        elif em == 3:
            bord+=1
            i-=1
    else:
        print('emtiaz na motabar')
        continue
    if i == 0:
        break
    else:
        continue

print('bord:', bord, 'bakht:', bakht, 'mosaui', mosaui)
    
                    
                
