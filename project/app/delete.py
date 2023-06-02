
def smart_inv(func):
    def inner(x):
        if x==0:
            return "unacceptable Num"
        return func(x)
    return inner





@smart_inv
def inverse(a):
    return 1/a;


print(inverse(2))
print(inverse(0))


x = {"a":23,"b":1, "c":3, "d":0}

mylid = [3,5,11,4,0,1,22,34]

mylid.pop()

print({k:v for k,v in sorted(x.items(), key = lambda i:i[1], reverse=True)})

# y = sorted(x, key = lambda i.items():i[1])
print(x.items())
print(mylid)

