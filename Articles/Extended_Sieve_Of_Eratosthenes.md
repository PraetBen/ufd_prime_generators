# Extending the Sieve of Eratosthenes to Polynomials (for the first time?)

In this article, the logic and method behind the sieve of Eratosthenes is extended to polynomials of the form f(x)=x²+x+C. For some special C values, like 41, the sieve filters out all composites, ending up only with prime numbers. It is something I have been working on in my free time and hopefully, you will find it as interesting as I do.

To the best of my (limited mathematical) knowledge, nobody applied the sieve of Eratosthenes on polynomials before and sieving is currently only done on the regular list of integers. In this article, I show when and how it is possible to extend the sieve to certain polynomials. For most other polynomials, this sieving process does not seem to work. Let’s find out why!

## A personal note
I’m not a mathematician. My notation and terminology are probably off. What you will read here is based on my own experimental findings and patterns I discovered while ‘playing around’ with prime numbers quite a long time ago. In short, I discovered multiple new ways to generate prime numbers by using polynomials that are related to Unique Factorization Domains. I give no proof as I don’t know how to do such a thing. The best I could do was to try and intuitively explain the patterns that I have discovered.

I did not find anything similar in literature, which makes my work new and original, I guess. Maybe it is not actually new, as it is quite hard to understand math without much background. But maybe someone who reads this knows?

I hope this has any use to or might inspire someone. Or to put it in the words of Grant Sanderson (also known as 3blue1brown): “Some of the most useful math you’ll ever find, has its origins in someone who is just looking for a good story.”

## Sieve of Eratosthenes
The Sieve of Eratosthenes is one of the most intuitive methods to generate the complete list of prime numbers. To sieve the list of integers, you go through each number one by one, starting with 2. Then all multiples of that number (4, 6, 8, …) are crossed out as composite and will be ignored in the rest of the sieve. Then, all multiples of 3 are crossed off, after which the multiples of 5 are treated and so on, up until a certain cut-off value (100 in the example below). After the sieving is done, the remaining numbers are the prime numbers. This process is illustrated in the figure below.

![](images/Extended_Sieve_Of_Eratosthenes/image001.jpg?raw=true)

## Sieving Euler’s prime generating polynomial
To some of you, the following polynomial might ring a bell:

![](images/Extended_Sieve_Of_Eratosthenes/image002.jpg?raw=true)

This function is known as a prime generating polynomial and was discovered by Euler, who, already back in the 1700’s, noticed that this was quite a special function - when inserting integers starting from 0 all the way up to 40, all resulting numbers are prime.

The values of this function are listed below in the table, for -25 <= x < 150. The black values of x indicate that f(x) is a prime number, whereas the red ones indicate composites.

![](images/Extended_Sieve_Of_Eratosthenes/image003.jpg?raw=true)

The question now is: How can you find and cross out all the composites (in red)? Note, for example, the position of the first composites, namely at 40, 41, 44, 49, 56, 65 and 76. There are exactly 0, 2, 4, 6 and 10 primes between those. However, this pattern fails at 81, where an ‘unexpected’ composite shows up. It turns out there will be two steps necessary to find all the composites, and the first will use of the discovered pattern.

There is a python notebook which can be opened in the browser to follow the article in interactive way.

Run it here: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PraetBen/ufd_prime_generators/master?filepath=2FExtended_Sieve_Of_Eratosthenes%2Finteractive_article.ipynb)


## Step 1: Finding the first composites
Look at the table below, which lists a couple of the first values of x, f(x) and the sum of those two. You can observe that this last column corresponds exactly to the composites found earlier! That gives us our first element for the sieve. To start the sieving process, you can start at x = -1 because of symmetry. A first list of composites can then be found by filling in x+f(x) for each x.


| x  | f(x) | x+f(x) |
|----|------|--------|
| -1 | 41   | 40     |
| 0  | 41   | 41     |
| 1  | 43   | 44     |
| 2  | 47   | 49     |
| 3  | 53   | 56     |
| 4  | 61   | 65     |
| 5  | 71   | 76     |
| 6  | 83   | 89     |


Like the regular sieve of Eratosthenes, all ‘multiples’ can be crossed out as well. For example, for x=-1, you can also cross out all the multiples of 41 minus 1 (-1+41k) This results in 40, 81 and 122 and so on.

Then, just as in the regular sieve of Eratosthenes, go to the next number (namely x = 0) and continue to do the same process for each x till the end. Below the results for the first x-values where now all the multiples are also given in the last column, which corresponds to x + kf(x). I invite you to try it for yourself and find the composite generated by x = 5 and verify that this pattern indeed holds up.


| x  | f(x) | x+kf(x) |
|----|------|--------|
| -1 | 41   | 40, 81, 122     |
| 0  | 41   | 41, 82, 123     |
| 1  | 43   | 44, 87, 130     |
| 2  | 47   | 49, 96, 143     |
| 3  | 53   | 56, 109     |
| 4  | 61   | 65, 126     |
| 5  | Try   | yourself!     |

## Step 2: Finding the remaining composites

After completing these steps for all x values, you can find and cross the first series of composites out. The found composites are crossed out and highlighted in light grey colour in the figure below. As you can see, there still are some composites that were not found by the sieve. In other words, the sieving is not complete. For example, the composite at x=84 or at x=91 have not been found yet.

![](images/Extended_Sieve_Of_Eratosthenes/image004.jpg?raw=true)


It turns out that, we can use the composites that were crossed out before to find those missing composites. Let’s look now at the first composites that were found by the sieve:


![](images/Extended_Sieve_Of_Eratosthenes/image005.jpg?raw=true)

![](images/Extended_Sieve_Of_Eratosthenes/image006.jpg?raw=true)

![](images/Extended_Sieve_Of_Eratosthenes/image007.jpg?raw=true)

![](images/Extended_Sieve_Of_Eratosthenes/image008.jpg?raw=true)

![](images/Extended_Sieve_Of_Eratosthenes/image009.jpg?raw=true)

Two observations can be made from this:

First, we can see that the resulting f(x) of the composite can always be divided by the original f(x) that was used earlier to find this composite. These numbers are indicated in bold. For example, through x=1, we found the composite at x=44 which is divisible by f(1) = 43.

Second, there is another divisor present. Using the same example, we see that f(44) happens to be divisible by 47. Now, this information can be used to find all the remaining composites! Summing this new divisor, 47 (also called q in this article) up with the x-value of the composite 44, results in the position of a new composite, namely at x = 91.

Also here all the ‘multiples’ can be crossed out. For example, all the values at 44+47k. The table below illustrates this for the first composites found. Try this for the last composite in the table to verify that this indeed works and to really understand what is going on!

Each composite found and crossed out, generates another new set of composites by their respective newly found divisor. For example, the composite at the position x = 44 + 2 * 47 = 138 must be divisible by 47, and its other divisor ‘q’ will generate composites at the position 138 + kq. Try this to verify that this indeed works.

 | x  | q (new divisor) | x+kq |
|----|------|--------|
| 40 | 41   | 81, 122     |
| 41 | 43   | 84, 127     |
| 44  | 47   | 91, 138     |
| 49 | 53   | 102     |
| 56 | 61   | 117     |
| 65  | Try   | yourself!     |


By applying these steps to each composite that has been found, the sieve ends up with only prime numbers remaining. In other words, the sieve crosses all the composites out! This is the crucial step in making the sieve work.

## Programming the sieve
The process above can be implemented to program a sieve. Below, a pseudo code is given to make you understand the logic behind it. As the sieve only goes up to a certain cut-off value, only the ‘relevant’ composites should be considered, namely those under the cut-off value.

For each x do the following:
   * Find the composites by x + kf(x) for each k and add them to be “treated”
   * While there are untreated composites, treat them one at a time, by;
        * crossing them out
        * finding the new composites (generated by the new divisor)
        * add those new ones to be treated
        
There are many ways of implementing this: numerically, symbolically, or even by using matrices. The numerical implementation is the easiest to understand and is therefore provided. 

* [The Github repository](https://github.com/PraetBen/ufd_prime_generators/Extended_Sieve/)
* Link to run sieve in browser: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PraetBen/ufd_prime_generators/HEAD?filepath=%2FExtended_Sieve_Of_Eratosthenes%numerical_implementation_demo.ipynb)

## Sieving mechanisms

The process above to cross out polynomials can be explained by first proving a property of polynomials in general. Then, how this property is used to implement the sieving mechanism described above is shown.

### A Property of polynomials
Consider f(x) of the form ax²+bx+c.

For this type of polynomial, the following property holds.

    When f(x)=p*q, in other words when q divides f(x), then q also divides f(x+kq) for any k ∈  ℤ.
    
This can be easily proven by evaluating f(x+kq)

![](images/Extended_Sieve_Of_Eratosthenes/image010.jpg?raw=true)

Expanding  (x+kq)² and then rearranging

![](images/Extended_Sieve_Of_Eratosthenes/image011.jpg?raw=true)

Substituting f(x)=ax²+bx+c and then rearranging

![](images/Extended_Sieve_Of_Eratosthenes/image012.jpg?raw=true)

Substituting back f(x)=pq and then rearranging

![](images/Extended_Sieve_Of_Eratosthenes/image013.jpg?raw=true)

 

Now it is clear that f(x+kq) can be divided by q, for any q that divides f(x). This property is used to explain why the sieving works.

### Using this property for sieving
Recall the process we used to find composites.

In the first step of the sieving, we found that multiples of f(x) summed up with x, namely x+kf(x) generated a first list of composites. This can now be explained by the property above. f(x) can be also written as f(x) = pq, where p = 1 and q = f(x). This is the starting point of the sieving process we found earlier. As it is shown that q divides f(x + kq), we expect to find the composites on x+kq = x +kf(x) which corresponds to our findings.

In the second step of the sieving, we found the ‘remaining composites’ by using the already crossed out composites. This can be now fully explained by the equations above. Each composite and its divisor q generate a new list of composites, and so on. This is because x+kq will always be divisible by q, as proved above.

### Does this also work with other functions?

This article started with the choice of a certain function f(x)=x²+x+41. One could ask if the previous algorithm would still work if one would use 61 instead of 41? After all, 61 is also a prime number, just like 41. When using the sieving process, we only expect composites for x > 60. However, there is already a composite present at x = 1, namely at f(1) = 63, which is divisible by 3. So, it does not work for C = 61 and it will not work for the most other ones. You can try it also yourself on the mybinder link provided earlier (use C=61). There are a lot more other composites that were not sieved out.

The last question that remains is why and when this sieve works. For most polynomials, as demonstrated above, there are more composites than those that can be found by the previous sieving process. This means that the sieving will still cross out some polynomials, but not all of them. In other words, the sieve works for the prime generating function (x²+x+41) discussed above, but not for most other polynomials.

## Why does it work with C being 41 and not 61?

The key to understanding why the sieving works with 41 and not 61 or most other numbers, lies in unique factorization domains. In short, 41 is a special type of number (derived from Heegner Numbers) where unique factorization works, whereas for 61, is not. More specifically Unique factorization holds only for C = 1, 2, 3, 5, 11, 17 and 41. Only for those numbers, the extended sieve works.

See [this article](Unique_Factorization_Domains.md) for a more detailed explanation. Not mandatory but helpful if you haven’t read about complex numbers, UFD and Heegner number and if you want to understand all the details.

The function can be rewritten in the complex domain as

![](images/Extended_Sieve_Of_Eratosthenes/image014.jpg?raw=true)

where


![](images/Extended_Sieve_Of_Eratosthenes/image015.jpg?raw=true)

Below some helpful equations if you want to verify the math.

![](images/Extended_Sieve_Of_Eratosthenes/image016.jpg?raw=true)

### Non-unique factorization
Let’s look at f(x) = x² + x + 61.

This is a function where unique factorization does not hold. Consider x = 5, which is not crossed out by the sieve. Examining f(5) in more detail, it can be observed that:

![](images/Extended_Sieve_Of_Eratosthenes/image017.jpg?raw=true)

This shows us that there are two different ways to factor 91, as both 13 and 7 have nothing to do with (5 + α) and (5 + ᾱ). There is no unique factorization here, as 91 is factored in two very different and unrelated ways.

This demonstrates why composites are present other than those found by the sieving method. This means that the sieve does not work now anymore. On the contrary, no such composites show up for functions where the unique factorization holds, which is why there are only primes left after the sieving.

### Unique factorization
Now, let’s look at f(x) = x² + x + 41

This is a function where unique factorization holds. Consider again x = 5, which is not crossed out by the sieve. Examining f(5) in more detail, it can be observed that:
 
![](images/Extended_Sieve_Of_Eratosthenes/image018.jpg?raw=true)

Both (5 + α) and (5 + ᾱ) are no further factorable, and 71 is a prime number. As unique factorization holds, the fact that 71 can be factorized using the complex domain, it must mean that there is no other possible way to factor it.

Consider then as a final illustration the composite generated by the sieving method:

![](images/Extended_Sieve_Of_Eratosthenes/image019.jpg?raw=true)
 

6847 is divisible by both 167 & 41 and by (82+ α) & (82+ ᾱ) in the complex domain. Given that we are in a Unique Factorization Domain, unique factorization must hold. This means that (82+ α) and (82+ ᾱ) must be further factorable, consisting of the same ‘smallest’ blocks. Indeed, it can be found that:

![](images/Extended_Sieve_Of_Eratosthenes/image020.jpg?raw=true)

![](images/Extended_Sieve_Of_Eratosthenes/image021.jpg?raw=true)

And that

![](images/Extended_Sieve_Of_Eratosthenes/image022.jpg?raw=true)

![](images/Extended_Sieve_Of_Eratosthenes/image023.jpg?raw=true)

This illustrates that both ways of factorizing the number consists in the end of the same ‘smallest’ blocks and shows that the factorization is really unique.

![](images/Extended_Sieve_Of_Eratosthenes/image024.jpg?raw=true)
 

## Generalized Sieve Of Eratosthenes

You probably have already noticed  the similarity with the regular sieve of Eratosthenes. There is an overcomplicated way of looking at this sieving method, so that all the previous is also valid for the ‘regular’ sieve of Eratosthenes. Therefore, the sieving method introduced in this article could also be called the “Generalized Sieve Of Eratosthenes”.

Remember the property that was used for sieving the polynomials, namely 

    When f(x)=p*q, in other words when q divides f(x), then q also divides f(x + kq) for any k ∈  ℤ.

For f(x) = x, which corresponds to the set of all integers, this also works. The only change that needs to be made is that p will always equal 1.
 
Consider

![](images/Extended_Sieve_Of_Eratosthenes/image025.jpg?raw=true)

It can be observed that

![](images/Extended_Sieve_Of_Eratosthenes/image026.jpg?raw=true)

is always divisible by x, for any k. The sieving is done by crossing out all the (x + kx) positions, starting from k = 1. This is indeed the same as saying that all multiples of x are sieved out. It says nothing much, but the similarity with the extended sieve of Eratosthenes is striking, when looking at the ‘regular’ sieve in this manner.

## Some final thoughts
Personally, the question that remains is, if it is new, or if this has any value for mathematics. Please let me know your thoughts on all of this.  

It is possible to do even more than sieving with this special type of polynomials. For example, also [trial division can be extended](Unique_Factorization_Domains.md)! This makes me wonder, which other methods, now used on regular integers, could we apply on those polynomials to find/generate prime numbers?

Some final comments on the Extended Sieve.
* The sieve also works for x²+1 and x²+2 (see implementation + overview article for why)
* For now, the new divisor ‘q’ is calculated by doing the actual division, but in fact, it can be calculated analytically (in a recursive manner) without doing this division. [See more here](Calculating_Divisor_Recursively.md).
* The sieve works with 2x²+29, with some modifications. The working of the sieve is based on Unique Factorization, so maybe other polynomials related to class number 1 could also be working like this.
* The full sieve (using heegner numbers), implemented in python, can be found [here](https://github.com/PraetBen/ufd_prime_generators/Extended_Sieve/numerical_implementation.ipynb).

Ben Praet

21/08/2021