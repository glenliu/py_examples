from __future__ import print_function
import math
a=[2.0,3.0,4.0,5.0]
#n1n2.n3*n4=xxx.x
result=[]
for n1 in a:
    for n2 in a:
        for n3 in a:
            for n4 in a:
                re=(10*n1+n2+n3/10)*n4
                # print str(int(n1))+str(int(n2))+ \
                #             '.'+str(int(n3))+'*'+str(int(n4))+'='+str(re)
                redigits = [r for r in str(re) if r != '.']
                B_flag = False
                for d in redigits:
                    if float(d) not in a:
                        B_flag=True
                        break
                if B_flag is True:
                    continue
                else:
                    B_flag=False
                print ("got it!")
                print
                '{0}{1}.{2}*{3}={4}'.format(str(int(n1)), str(int(n2)), str(int(n3)), str(int(n4)), str(re))
                result.append([n1,n2,n3,n4, re])
print (result)
