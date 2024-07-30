import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
import seaborn
#using try and error we will find no. of trials for which probability of getting atleast one head is greater than 0.9

#Number of trials required
n=[2,3,4,5,6]#our inputs for no. of trials
y=[1,1,1,1,1]#5-d array
z=[1,1,1,1,1]
#Probability of getting head and tail
p = q=1/2
n0=n[0] #= input("Enter your first guess for no. of trials for which probability of getting atleast one head is greater than 0.9\n")
y[0]=1-binom.cdf(1,n0,p)+binom.pmf(1,n0,p)

print("Probability for getting atleast 1 head for first guess")
print (y[0],"\n")           # P(X > =1)

n1=n[1] #= input("Enter your second guess for no. of trials for which probability of getting atleast one head is greater than 0.9\n")
y[1]=1-binom.cdf(1,n1,p)+binom.pmf(1,n1,p)
print("Probability for getting atleast one head for second guess")
print (y[1],"\n")           # P(X > =1)
n2=n[2] #= input("Enter your third guess for no. of trials for which probability of getting atleast one head is greater than 0.9\n")
y[2]=1-binom.cdf(1,n2,p)+binom.pmf(1,n2,p)
print("Probability for getting atleast 1 head for third guess")
print (y[2],"\n")           # P(X > =1)
n3=n[3] #= input("Enter your fourth guess for no. of trials for which probability of getting atleast one head is greater than 0.9\n")
y[3]=1-binom.cdf(1,n3,p)+binom.pmf(1,n3,p)
print("Probability for getting atleast 1 head for fourth guess")
print (y[3],"\n")           # P(X > =1)
n4=n[4] #= input("Enter your fifth guess for no. of trials for which probability of getting atleast one head is greater than 0.9\n")
y[4]=1-binom.cdf(1,n4,p)+binom.pmf(1,n4,p)
print("Probability for getting atleast 1 head for fifth guess")
print (y[4],"\n")           # P(X > =1)
for i in range(5):
#Generating sample date using Bernoulli r.v.
  prob=[1,1,1,1,1]
  
#Simulating the probability using  the binomial random variable
  data_binom = binom.rvs(n[i],p,size=(1,5)) #Simulating the event of jumping 10 hurdles
  err_ind = np.nonzero(data_binom>=1) #checking probability condition
  err_n = np.size(err_ind) #computing the probability
  prob[i]=err_n/n[i]
  ploti=plt.figure(i)
  plt.plot(data_binom,prob[i])
  

  #print(data_binom)

  #print(data_bern_mat)
  #print(data_binom)
  #data_bern = bernoulli.rvs(size=n[i],p1)
  #ploti=plt.figure(i)
  #plt.plot(data_binom,y[i])
  #data=binom.rvs(n=n[i],p=0.5,loc=0,size=(1,5))
  ''''ax=seaborn.histplot(data_binom,
                kde=True,
                color='pink')
  ax.set(xlabel='Binomial',ylabel='Frequency')
  ploti=plt.figure(i)
  plt.plot(data,y[i])''''
  
plot6 =plt.figure(6) plt.plot(n,y,linestyle='--',marker='*',color='b')
plt.title("number of trials versus bernaulii probability graph for
getting at least  d")
plt.xlabel("$n$")
plt.ylabel("$P_X(x)$")
plt.xlim([2,6]) plt.ylim([0.7,1]) print("from the graph ,we can easily
see that for no. of trails greater than or equal to 4 ,the probability
of getting atleast one head is greater than 0.9") plt.show()


