ten_proba = 5/6
rest = 1-ten_proba
rest_proba = 1 - ten_proba
for i in range(10):
    rest = rest_proba * rest
    ten_proba += rest
    print(ten_proba)