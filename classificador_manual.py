import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob
x= glob.glob('/Users/alexander/Documents/Inteligentes/proyecto final/Selfie-dataset/images/10245*.jpg')
print(len(x))
file=open("/Users/alexander/Documents/Inteligentes/proyecto final/Selfie-dataset/classif_4_caract.txt", "a+")
x_copia=x
x_copia.sort()
for photo in x_copia[600:630]:
    plt.imshow(mpimg.imread(photo))
    plt.ion()
    plt.show()
    temp=photo[77:]
    print("selfie quality 1:good 0:bad")
    sq=input()
    print("only face:1 full body:0  upper:2")
    cu=input()
    print("none:0 b/w:1 vintage:2 sepia:3 Contrast:4 blur:5 weather:6 focus:7")
    flt=input()
    print("Brigness low:0 normal:1 high:2")
    brg=input()
    file.write("%s %s %s %s %s\n"%(temp,sq,cu,flt,brg))
    plt.close()
file.close()    