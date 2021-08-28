
def exp(x,eps):
    t=1
    k=float(1)
    s=float(0)  
    while abs(t)>eps:
        s = s + t
        t = t*(x/k)
        k += 1
    return s

x=float(input())
eps=0.000001
print("sinus de",x,"este",float(exp(x,eps)))