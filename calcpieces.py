# A stick is 180 cm long. Xiaoming cuts it every 3cm, and every 4 cm. How many pieces will be after the cut?

dao=0
cutlen=[]
pieces=1
for i3 in range(1,180):
    print("length:\t"+str(i3))
    if i3%3==0:
        cutlen.append(i3)
        dao=dao+1
        pieces=pieces+1
        print("length:\t"+str(i3)+"\tdao:\t"+str(dao)+"\tpieces:\t"+str(pieces))

for i4 in range(1,180):
    print("length:\t"+str(i4))
    if i4%4==0 and i4 not in cutlen:
        cutlen.append(i4)
        dao=dao+1
        pieces=pieces+1
        print("length:\t"+str(i4)+"\tdao:\t"+str(dao)+"\tpieces:\t"+str(pieces))

print("final pieces:\t"+str(pieces))