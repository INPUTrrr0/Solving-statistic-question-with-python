import numpy
import random
import statistics

mu, sigma = 0, 0.1
x = np.random.normal(mu, sigma, 168)
print ("this is std of 168 data points")
#print (np.mean(x))
print(np.std(x))

#xx = np.ndarray.tolist(x)

l = numpy.array_split(numpy.array(x),7)
means = []
myresults = []
print ("these are the means")
#map(np.mean,l)
for i in l:
    for e in i:
        myresults.append(e)
    x = sum(myresults)/len(myresults)
    print(x)
    means.append(x)
print ("this is the std of the means")
print(np.std(means))
   