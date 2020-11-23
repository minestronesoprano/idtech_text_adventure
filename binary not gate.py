code = """0001101011101011101"""

code_useable = [int(i) for i in str(code)]

print(code_useable)

for x in range(0, len(code_useable)):
    if code_useable[x] == 0:
        code_useable[x] = 1
    else:
        code_useable[x] = 0

code = "".join(str(a) for a in code_useable)
print(code)

"""
not gates reverse the signal of the thing behind - one gate and one changed
or gates work if one or the other of two indicators is on, and the output will be on if one is
and gates - both must be on
Xor gates - one, the other, or none must be on
    make a not gate for a and b, and an or gate for A' and B'"""