import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
#using try and error we will find no. of trials for which probability of getting atleast one head is greater than 0.9

#Number of trials required
n=[2,3,4,5,6]#our inputs for no. of trials
y=[1,1,1,1,1]#5-d array
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
plt.plot(n,y,linestyle='--',marker='*',color='b')
plt.title("$number\ of \trials \versus\ bernaulii\ probability \getting\ atleast\ one \head$\n")
plt.xlabel("$n$")
plt.ylabel("$P_X(x)$")
plt.xlim([2,6])
plt.ylim([0.7,1])
print("from the graph ,we can easily see that for no. of trails greater than or equal to 4 ,the probability of getting atleast one head is greater than 0.9")
plt.show()
''''
#y=binom.cdf(k, n, p)
#Mean 
mu = p

#Variance and # sigma is standard deviation
sigma = np.sqrt(p*(1-p))

#Using the Gaussian approximation for the binomial pdf
print(1/(sigma*np.sqrt(n))*(norm.pdf((k-n*mu)/(sigma*np.sqrt(n)))+norm.pdf((k-1-n*mu)/(sigma*np.sqrt(n)))))


#Simulating the probability using  the binomial random variable
data_binom = binom.rvs(n,p,size=simlen) #Simulating the event of jumping 10 hurdles
err_ind = np.nonzero(data_binom <=k) #checking probability condition
err_n = np.size(err_ind) #computing the probability
print(err_n/simlen)
#print(data_binom)


#Simulating the probability using  the bernoulli random variable
data_bern_mat = bernoulli.rvs(p,size=(n,simlen))
data_binom=np.sum(data_bern_mat, axis=0)
#print(data_bern_mat)
#print(data_binom)
err_ind = np.nonzero(data_binom <=k) #checking probability condition
err_n = np.size(err_ind) #computing the probability
print(err_n/simlen)
'''
