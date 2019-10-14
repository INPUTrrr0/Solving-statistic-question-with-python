# Solving-statistic-question-with-python
Solving statistic question with python:
Question: 
Randomly choose 168 normally distributed points, split them randomly into 7 groups. Will the standard deviation of the mean of thse 7 groups be the same as the standard deviation of the 168 points? 

Code: 
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

Result:
this is std of 168 data points
0.09334234225821018
these are the means
0.04104938514873088
0.020026540193549148
0.01949887110008378
0.009356056097206652
0.013587698683270378
0.011217622519253017
0.006418658499924722
this is the std of the means
0.010747679187556059