# Julia

> Source: https://www-math.mit.edu/~stevenj/Julia-cheatsheet.pdf

> Aliases: julialang-programming

$ Basics
    `julialang.org                 {{Julia Documentation}} 
    `juliabox.org                  {{Run Julia online}} 
    `github.com/stevenj/julia-mit  {{Installation and Tutorial}} 
    `ipython notebook              {{Start IJulia browser}} 
    `[Shift]+[Enter]               {{Execute input cell in IJulia}} 

$ Defining/Changing Variables
    `x=3                           {{Define variable x to be 3}} 
    `x=[1,2,3]                     {{Array/"Column"-vector (1,2,3)}} 
    `y=[1 2 3]                     {{ Define a 1x3 row vector (1,2,3)}} 
    `A=[1 2 3 4; 5 6 7 8; 9 10 11 12]
>                                  {{Set A to 3 × 4 matrix with rows 1,2,3,4 etc.}} 
    `x[2]=7                        {{Change x from (1,2,3) to (1,7,3)}} 
    `A[2,1]=0                      {{Change element A(second row, first column) to 0}} 
    `u, v = (15.03, 1.2e-27)       {{Set u=15.03, v=1.2×10^(–27)}} 
    `f(x)=3x                       {{Define a function f(x)}} 
    `x -> 3x                       {{An anonymous function}} 

$ Simple Matrices
    `rand(12), rand(12,4)          {{Random 12-length vector or 12x4 matrix with uniform random numbers in \[0,1)}} 
    `randn(12)                     {{Gaussian random numbers (mean 0, std. dev. 1)}} 
    `eye(5)                        {{5x5 identity matrix I}} 
    `linspace(1.2,4.7,100)         {{100 equally spaced points from 1.2 to 4.7}} 
    `diagm(x)                      {{Matrix whose diagonal is the entries of x}} 

$ Matrices and Vectors
    `x[2:12]                       {{The 2nd to 12th elements of x}} 
    `x[2:end]                      {{The 2nd to the last elements of x}} 
    `A[5,1:3]                      {{Row vector of 1st 3 elements in 5th row of A}} 
    `A[5,:]                        {{Row vector of 5th row of A}} 
    `diag(A)                       {{Vector of diagonals of A}} 

$ Arithmetic of Numbers
    `3*4, 7+4, 2-6, 8/3            {{Mul., Add., Sub., Div. numbers}} 
    `3^7, 3^(8+2im)                {{Compute 3^7 or 3^(8+2i)}} 
    `sqrt(-5+0im)                  {{Representation of square root of -5}} 
    `exp(12)                       {{Compute e^12}} 
    `log(3), log10(100)            {{Natural log (ln), base-10 log (log10)}} 
    `abs(-5), abs(2+3im)           {{Absolute value |–5| or |2+3i|}} 
    `sin(5pi/3)                    {{Value of sin(5π/3)}} 

$ Arithmetic of Vectors and Matrices
    `x * 3, x + 3                  {{Multiply/Add every element of x by 3}} 
    `x + y                         {{Element-wise addition of two vectors x and y}} 
    `A*y, A*B                      {{Product of matrix A and vector y or matrix B (not defined for two vectors)}} 
    `x .* y                        {{Element-wise product of vectors x and y}} 
    `x .^ 3                        {{Every element of x is cubed}} 
    `cos(x), cos(A)                {{Cosine of every element of x or A}} 
    `exp(A), expm(A)               {{Exp of each element of A, matrix exp e^A}} 
    `x′, A′                        {{Conjugate transpose of a vector or matrix}} 
    `x’*y, dot(x,y), sum(conj(x).*y)
>                                  {{Three ways to compute x·y}} 
    `A\\b, inv(A)                  {{Return solution to Ax=b, or the inverse of matrix A}} 
    `λ, V = eig(A)                 {{Eigenvals λ and eigenvectors (columns of V) of A}} 

$ Plotting
    `plot(y), plot(x,y)            {{Plot y vs. 0,1,2,3,... or versus x}} 
    `loglog(x,y), semilogx(x,y), semilogy(x,y)
>                                  {{Log scale plots}} 
    `title(“A title”), xlabel(“xaxis”), ylabel(“foo”)
>                                  {{Set labels}} 
    `legend([“curve 1”, “curve 2”], “northwest”)
>                                  {{Legend at upper-left}} 
    `grid(), axis(“equal”)         {{Add grid lines, use equal x and y scaling}} 
    `title(L”the curve $e^\\sqrt{x}$”)
>                                  {{Title with LaTeX equation}} 
    `savefig(“fig.png”), savefig(“fig.pdf”)
>                                  {{Save PNG or PDF image}} 

