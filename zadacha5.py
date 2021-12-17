def sorti(array, NN, z):
    ind = 0
    con = 0
    col = 0
    while ind < NN:
        if array[ind] == z:
            nachind = conind = ind
            j = ind + 1
            while array[j] == z:
                j += 1
                conind += 1
            ind = conind
    
            suml = 0; k = con
            while k < nachind:
                suml += array[k]
                k += 1
   
            sumr = 0; k = conind + 1
            while k < NN:
                if array[k] == z:
                    break
                sumr += array[k]
                k += 1
            for v in range(nachind, conind + 1):
                array[v] = 0.5*(suml + sumr)
            con = conind + 1
        ind += 1
    
def proverka(a,m,y):
    k = 0
    for i in range(m):
        if a[i] == y:
            k+= 1
    return k 

f = open(r"C:\Users\superuser\Desktop\5\test5.txt","r+")
N = int(f.readline())
x = int(f.readline())
arr = []
arr = list(map(int, f.read().split()))
if N < 1 or proverka(arr, N, x) == 0:
    print('Error!!!')
else:
    sorti(arr, N, x)
    print(arr)
    for p in arr:
        f.write(str(p)+'\n')
f.close()               
a = [-4, 0, -1, 2, 2, 4, 3]
sorti(a,7,2)
if a == [-4, 0, -3, 1, 1, 4, 3]:
    print('autotest passed')
else:
    print(a)
    print('autotest failed')
