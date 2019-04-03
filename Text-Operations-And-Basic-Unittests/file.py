import math

#FuzzBuzz implement

def FuzzBuzz(start,stop):
    if type(start) not in [int] or type(stop) not in [int]:
        raise TypeError("Value must be an int")
    
    if start < 0 or stop < 0:
        raise ValueError("Value must be > 0 and was ")



    for i in range(start,stop):
        if i % 3 == 0 and i % 5 == 0:
            print(i," FuzzBuzz " );
        elif i % 3 == 0:
            print(i," Fuzz");
        elif i % 5 == 0:
            print(i," Buzz");
        else:
            print(i);

FuzzBuzz(1,101);
    


print("\n")



txt="Marta tries very hard to combine coding with passion for science, cooking and dancing. In her free time she walks on stilts and makes balloon animals for children. Wants to own a restaurant some day. She is and always will be the optimist. The hoper of far-flung hopes, the dreamer of improbable dreams. She believes in people and that sometimes, very rarely, impossible things just happen and we call them miracles.";
print(txt);
print("\n");
x=txt.split();
print("There is ",len(x)," words in this sentence");
print(x);
print("\n");
words=[];
appear=[];

for i in x:
    if i not in words:
        words.append(i);
        appear.append(1);
    else:
        appear[words.index(i)]+=1;


print(words);
print("\n");
print(appear);
print("\n");

#why bother this way. Attempt with dict type.

json = {}

for i in x:
    if  i in json:
        json[i] += 1
    else:
        json[i] = 1

print(json);

def circleRadious(rad):
    if type(rad) not in [int,float]:
        raise TypeError("Error: This is type error ");

    if rad < 0:
        raise ValueError("Error: Radius was negative");

    return math.pi*rad**2


testData=[1,2,0];
    
for i in testData:
    print(circleRadious(i));
    print("\n");

def delta(x,y,z):
    if x == None or y == None  or z == None:
        raise ValueError("Value cannot be NULL")    

    if type(x) not in [int,float] or type(y) not in [int,float] or type(z) not in [int,float]:
        raise TypeError("Value can only be float and int? X was  " + str(type(x))+" Y was " + str(type(y))+" and Z was "+str(type(z)));
    
    if x<0 or y<0 or z<0:
        raise ValueError("Plz no negativo for delta testivo")
    


    return (y*y)-(4*x*z)


testData=[(2,2,2),(4,1,2),(1,10,1),(3,0.2,1)]

for i in testData:
    x = i[0]
    y = i[1]
    z = i[2]

    print(x,y,z)
    print(delta(x,y,z))

