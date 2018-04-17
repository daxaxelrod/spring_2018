Fixed income
Swaps

3-20-18

present value of all the fixed payments should be the same as all the variable interest received

def Fixed rate f
def notional n
def variable rate v

f(n) + f(n) + f(n) = v(n) + v(n) + v(n)
note that you have to discount all the values
    f(n) / (1+r)^year

then add the a new term
    add the notional to the payments to make the left side look like a fixed coupon bond
    n / (1 + r)^year
   
the right side looks like a floater. Floaters are always traded at par at the coupon reset date

so we have the pv of fixed rate bond = notional

f + f + f + 1/(1+r)^years = 1 #just got rid of notional

f[1/(1+r) + 1/(1+r)**2 ...] = 1 - 1/(1 + r)**years

f = 1 - 1/(1 + r)**years / f[1/(1+r) + 1/(1+r)**2 ...]

aside
    def Bi = discount factor = 1/(1+r_sub_i)**i

f = 1 - Bn / Sumation(B0(hj))
