#heights = list(map(int, input().split()))

def is_ranged(heights):
    #for inf in range(1, len(heights)):
        #if heights
    heights_sorted = sorted(heights)
    if (heights==heights_sorted) | (heights == heights_sorted[::-1]):
        return("YES")
    return ("NO")

#print(is_ranged(heights))

assert is_ranged([1,2,3,4])=="YES"
assert is_ranged([7,6,5,5])=="YES"
assert is_ranged([4,4,4,4])=="YES"
assert is_ranged([5,2,3,1])=="NO"

s = list(map(int, "1 2 3 4".split()))
print(s)
assert is_ranged(s)=="YES"