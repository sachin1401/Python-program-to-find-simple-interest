# method-1_____method-1


# Simple interest formula is given by:
# Simple Interest = (P x T x R)/100
# Where,
# P is the principle amount
# T is the time and
# R is the rate

# enter the value of p
P=int(input('Enter the value of P: '))

# enter the value of t
T=int(input('Enter the value of T: '))

# enter the value of r
R=int(input('Enter the value of R: '))

# simple interest formula
SI=(P*T*R)/100;

# now the final output
print(SI)


# method-2_____method-2

# method-2_____method-2

# method-2_____method-2


# secound method create by function method

# here declare three variable 
def si(p,t,r):

# SI formula
    si=(p*t*r)/100
    
    # it is imp to declare return value otherwise you will get "None"
    return si

print("the value of simple interest: ") 

# enter the value of p
p=int(input('Enter the value of principle: '))

# enter the value of t
t=int(input('Enter the value of time: '))

# enter the value of r
r=int(input('Enter the value of rate: '))

# final output
print("value of si :",si(p,t,r))    