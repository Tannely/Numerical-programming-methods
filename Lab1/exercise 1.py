import math
def f(x1, x2):
    deltax_1 = abs(x1 - math.sqrt(83))
    deltax_2 = abs(x2 - 6/11)
    print('Граничні абсолютні похибки з надлишком')
    print(deltax_1) 
    print(deltax_2)
    vidx_1 = abs(deltax_1 / x1)
    vidx_2 = abs(deltax_2 / x2) 
    print('\n Граничні відносні похибки ')
    print(vidx_1)
    print(vidx_2)  
    if vidx_1 > vidx_2:
        print('\n  рівність 6/11 є більш точною')
    else:
        print('\n рівність 6/11 не точна')    
f (9.11, 0.545) 
print('\n Оскільки гранична відносна похибка(vidx_2) є більшою за 1(vidx_1) то: рівність sqrt(83) - Є більш точною ')
 


