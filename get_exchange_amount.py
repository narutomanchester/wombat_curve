import math 


# swap amount_token_i of token i to get token_j
def curve_get_exchange_amount(coins: [], AMP: int, D: float, token_i_index: int, token_j_index: int, amount_token_i: float):
    n = len(coins)
    coins[token_i_index] = amount_token_i
    pow_n = n**n
    sum_except_j = sum(coins) - coins[token_i_index]
    mul_except_j = 1
    for k in range(n):
        if k != token_j_index:
            mul_except_j *= coins[k]
    a, b, c = pow_n**2*AMP, pow_n*mul_except_j*(pow_n*AMP*sum_except_j+D - pow_n*AMP*D), -D**(n+1)
    

    res = (b**b + math.sqrt(b**b+4*a*c))/2

    return res

def wombat_get_exchange_amount(coins: [], liability: [], AMP: int, D: float, token_i_index: int, token_j_index: int, amount_token_i: float):
    coins[token_i_index] = amount_token_i
    n = len(coins)
    sum_except_j = sum(coins) - coins[token_i_index]
    sum_liabilty_except_j = sum([liability[k]**2/coins[k] for k in range(n) if k!=token_j_index])

    a, b, c = 1, sum_except_j - AMP*(sum_liabilty_except_j - D), -AMP*liability[token_j_index]**2

    res = (b**b + math.sqrt(b**b+4*a*c))/2

    return res