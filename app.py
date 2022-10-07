print (' Tamerat Petros ')
print (' Yosef Mulugeta ')
print (' Abenezer Abera ')
print (' Nardos Melaku ')
print ("Write the person's name to see detail info? ")
answer = input()
if(answer== 'Tamerat Petros') :
    print ('Name: Tamerat Petros')
    print('Age: 16')
    print('Gender: Male')
    print('Address: Hawassa; Ethiopia')
    print('School: St.D.Comboni')

elif(answer== 'Abenezer Abera') :
    print('Name: Abenezer Abera')
    print('Age: 16')
    print('Gender: Male')
    print('Address: Hawassa; Ethiopia')
    print('School: St.D.Comboni')
elif(answer== 'Yosef Mulugeta') :
    print('Name: Yosef Mulugeta')
    print('Age: 16')
    print('Gender: Male')
    print('Address: Hawassa; Ethiopia')
    print('School: St.D.Comboni')
elif(answer== 'Nardos Melaku') :
    print('Name: Nardos Melaku')
    print('Age: 16')
    print('Gender: Female')
    print('Address: Hawassa; Ethiopia')
    print('School: St.D.Comboni')
else:print('sorry; ur input is not correct. ')

print (' Is ' + answer + ' Your friend, "Y" for Yes and "N" for No. ')
answer1 = input ()

print('!!!!!!!!!!!!!!!!!!!!Have a nice time !!!!!!!!!!!!!!!')

if(answer1== 'Y') :
    print ('Your friendship with ' + answer + ' is good, Continue your relation ship ')
elif(answer1== 'N') :
    print ("That is not bad but why don't you start friendship ")
else:print('sorry; ur input is not correct. ')

if(answer== 'Yosef Mulugeta') :
    import numpy as np
    import cv2 as cv

    img = cv.imread('JS.png', 1)
    cv.imshow('image', img)
    cv.waitKey(0)
elif(answer== 'Tamerat Petros') :
    import numpy as np
    import cv2 as cv

    img = cv.imread('TP.png', 1)
    cv.imshow('image', img)
    cv.waitKey(0)
elif(answer=='Abenezer Abera') :
    import numpy as np
    import cv2 as cv

    img = cv.imread('AA.jpg', 1)
    cv.imshow('image', img)
    cv.waitKey(0)
elif(answer=='Nardos Melaku') :
    import numpy as np
    import cv2 as cv

    img = cv.imread('NM.png', 1)
    cv.imshow('image', img)
    cv.waitKey(0)