#headings
##vector dot product
###product of vector a and vector b

#styling
** a.b**

#quoting text
> this is a quoted text

# link
(https://1drv.ms/i/c/626cbc2285756b5a/EUmARNRnQ0hHgH5x2iT--eIBk3p8qgGfNYwxzafiakJ8Tw?e=mg1NXA)
# images
![adding image](https://1drv.ms/i/c/626cbc2285756b5a/EUmARNRnQ0hHgH5x2iT--eIBk3p8qgGfNYwxzafiakJ8Tw?e=mg1NXA)

# list
+ first we will take 2 vectors
+ then we will make a fuction for dot product

# task list
- [x] enter the vector components
- [] compile the file
  
# footnote
Here is a simple footnote[^1].
[^1]: this is a footnote.

# alerts
>[!NOTE]
>Key information users need to know to achieve their goal.
> [!TIP]
> practice daily.!!!
>
# Tables 
|Version|Approach|Complexity|Memory Usage|Performance|
|----|----|----|----|----|
|Naive|	Basic for-loop|	𝑂(𝑛)|minimal|moderate|
|Parallelized|	Multithreading|O(n/p)|	Moderate|	High|
SIMD Optimized|	Vectorized operations|O(n/k)|	High	|Very High|

#code
```py
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
```

#mathematical expression
$\mathbf{A} \cdot \mathbf{B} = \sum_{i=1}^{n} a_i \cdot b_i$
