def find_D_Curve(coins: [], AMP: int):
    n = len(coins)
    pow_n, sum_coins, mul_coins = n**n, sum(coins), 1
    for x in coins:
        mul_coins *= x 

    def f(x):
        res = x**(n+1) - pow_n*mul_coins*(pow_n*AMP - 1)*x - pow_n*pow_n*AMP*mul_coins*sum_coins
        return res
    
    def dfdx(x):
        res = (n+1)*x**n - pow_n*mul_coins*(pow_n*AMP - 1)
        return res

    max_iter = 20 
    tol = 1E-15  # Tolerance
    x0 = 1 # init guess
    for x in coins:
        x0 = x0 * sum_coins / (x * n) 
    xi_1 = x0
    for i in range(max_iter):
        
        xi = xi_1-f(xi_1)/dfdx(xi_1)  
        if abs(xi - xi_1) < tol:
            break
        xi_1 = xi
        
    return xi

def find_D_Wombat(coins: [], liability: [], AMP: int)):
    res = 0
    for i in range(len(coins)):
        res += coins[i] - AMP*liability[i]/coins[i]

    return res