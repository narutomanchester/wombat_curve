from find_D import find_D_Curve
BASE_FEE = 1

def curve_add_liq(amount_coins_0: [], add_liq_coins: [], AMP: int, D0: float):
    n = len(amount_coins_0)
    amount_coins_1 : [] = amount_coins_0

    for i in range(n):
        if add_liq_coins[i] > 0:
            amount_coins_1[i] = amount_coins_1[i] + add_liq_coins[i]
    
    D1 = find_D_Curve(amount_coins_1, AMP)

    amount_coins_2 : [] = amount_coins_1 
    # recalculate
    for i in range(n):
        amount_coins_2[i] -= abs((D1 * amount_coins_1[i] / D0) * BASE_FEE - amount_coins_1[i])
    
    D2 = find_D_Curve(amount_coins_2, AMP)

    return amount_coins_2, D2

