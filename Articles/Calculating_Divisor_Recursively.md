# Calculating the divisor q in a recursively for the Extended Sieve of Eratosthenes

In the [previous article](Extended_Sieve_Of_Eratosthenes.md), we found that f(x+kq) is divisible by q, for any k ∈ ℤ. By evaluating f(x+kq)/q, another ‘new’ divisor was found, which in turn is used to find more composite numbers. This divisor was obtained by doing an (from a calculation point of view) expensive division operation.
 
![](images/Calculating_Divisor_Recursively/image001.jpg?raw=true) 

However, by a recursive relation that I discovered, this new divisor can be calculated analytically without doing the actual division, through a recursive manner. The following shows how this is done. The notation changes slightly from f(x + kq) to f(x + kᵢqᵢ), which is divisible by qᵢ like usual, as well as by the newly found divisor qᵢ₊₁ ,the ‘new’ divisor.

For this part, the general polynomial function f(x, y) = x² + xy + Cy² is necessary. The extended sieve uses x² + x + C, which is f(x, y) with y = 1. The notation (c, d) will be used, which corresponds to f(c, d).

To make this article easier to understand, a jupyter notebook project is provided which can be opened in the browser. The text below can be a bit hard to grasp, whereas interacting with the code might give a better feel for what is going on.


Run it here: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PraetBen/ufd_prime_generators/master?filepath=Extended_Sieve_Of_Eratosthenes%2Fcalculating_divisor_recursively.ipynb)


## Starting point k₀
Starting the sieve with any k₀, f(k₀) will be divisible by itself and 1. So far, nothing shocking.


![](images/Calculating_Divisor_Recursively/image002.jpg?raw=true) 

Note that q₀ equals 1, so this is already known:

![](images/Calculating_Divisor_Recursively/image003.jpg?raw=true) 

![](images/Calculating_Divisor_Recursively/image004.jpg?raw=true) 


Solving then for c₁ and d₁ is trivial:

![](images/Calculating_Divisor_Recursively/image005.jpg?raw=true) 

![](images/Calculating_Divisor_Recursively/image006.jpg?raw=true) 
 

This way, the first divisor for f(k₀), being f(k₀) itself in fact. This can just be considered as a starting point of the sieve. This notation is used so that it will be easier to see the recursive nature of the next divisor.


## Second ‘series’ of composites k₁
This new divisor q₁ can now be used to create the next series of composites, just as in the regular sieving method. Recall that f(xᵢ + qᵢ) is divisible by qᵢ and another (unknown) composite qᵢ₊₁. This will now be calculated analytically for the next series, where q₁ is already found above. The new divisor q₂ is what we want to obtain.

![](images/Calculating_Divisor_Recursively/image007.jpg?raw=true) 

Solving this equation for c₂ and d₂, by filling in c₁ and d₁ and evaluating the function on the left-hand side, results in:

![](images/Calculating_Divisor_Recursively/image008.jpg?raw=true) 

![](images/Calculating_Divisor_Recursively/image009.jpg?raw=true) 

Resulting in a ‘new’ found divisor q₂. This shows that it is possible to calculate the divisors and all the composites without doing a division! Depending on the ‘path’ that was chosen, namely the kᵢ that were filled in, the corresponding composites and divisors can be found.
 

**Numerical example:**

Considering the example which the original sieving article started with, where the divisors and composites were searched for f(1) and then for k = 2. In fact, this corresponds here to an initial k₀=1 and k₁=2. By using the obtained formula, the divisors 43 and 179 are found, which corresponds to the examples used above.

![](images/Calculating_Divisor_Recursively/image010.jpg?raw=true) 

![](images/Calculating_Divisor_Recursively/image011.jpg?raw=true) 
 
Another way to write this is [k₀, k₁] = [1, 2], indicating the ‘path’ that was followed. This example basically says that f(1+2*43) will be divisible by 179, and that there will be more composites on f(1+2*43+179k) for any k.

## Third ‘series’ of composites k₃

Continuing the same logic, the next “series” of composites, will be of the form:

![](images/Calculating_Divisor_Recursively/image012.jpg?raw=true) 

The term series is used in this context as we can fill in any k₂ and find a whole series of new composites. Solving for c₃ and d₃, the new divisor q₃ can be found. This divisor is based on only the kᵢ used.

![](images/Calculating_Divisor_Recursively/image013.jpg?raw=true) 
 
![](images/Calculating_Divisor_Recursively/image014.jpg?raw=true) 

![](images/Calculating_Divisor_Recursively/image015.jpg?raw=true) 


Rewriting it in terms of the already found divisors, allows us to see the recursive pattern:

![](images/Calculating_Divisor_Recursively/image016.jpg?raw=true) 

![](images/Calculating_Divisor_Recursively/image017.jpg?raw=true) 


**Numerical example:**

Try this for k₂ = 2. The ‘path’ followed then can be written as [1, 1, 2].

## General recursive relation
Generally, there is a recursive relation which allows to find any composite:

 
![](images/Calculating_Divisor_Recursively/image018.jpg?raw=true) 

Where

![](images/Calculating_Divisor_Recursively/image019.jpg?raw=true) 

![](images/Calculating_Divisor_Recursively/image020.jpg?raw=true)

![](images/Calculating_Divisor_Recursively/image021.jpg?raw=true)  


This recursive relation can be used to calculate all the divisors and thus find all the composites without using division. This can be done by going through all the kᵢ and qᵢ. Extending the sieving to a polynomial function, without even using a single division, is something I find a genuinely nice mathematical result.

 

## Sieving by paths

Thinking in terms of ‘paths’, one could go through all the possible paths [k₀, k₁, k₂, …, kᵢ]  to sieve out all the composites. In the provided jupyter notebook, an algorithm has been implemented to find the position of a composite based on this 'path' taken. 

Additionally, if there would be an easy way to ‘find back’ the path of any value k, using this logic, one could determine directly if f(x) is a prime or not, without the need for sieving everything. But it does not seem possible to do such a thing (efficiently).


## Some final thoughts

It is possible to do even more than sieving with this special type of polynomials. For example, also [trial division can be extended](Unique_Factorization_Domains.md)! This makes me wonder, which other methods, now used on regular integers, could we apply on those polynomials to generate or find prime numbers?

See also [my github](https://github.com/PraetBen/ufd_prime_generators/) to stay up to date! 

Ben Praet

21/08/2021