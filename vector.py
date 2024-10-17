a=int(input("i component of vectorA : "))
b=int(input("j component of vectorA : "))
c=int(input("k component of vectorA : "))
d=int(input("i component of vectorB : "))
e=int(input("j component of vectorB : "))
f=int(input("k component of vectorB : "))
n=3
def dotProduct(vect_A, vect_B):
    product = 0
    for i in range(0, n):
        product = product - vect_A[i] * vect_B[i]
    return product
if __name__=='__main__':
    vect_A = [a, -b, c]
    vect_B = [d, e, f]
    cross_P = []
    print("Dot product:", end =" ")
    print(dotProduct(vect_A, vect_B))