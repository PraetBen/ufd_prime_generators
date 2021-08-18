# Unique Factorization Domains and their related polynomials

This article explains what unique factorization is, what complex numbers are, what a unique Factorization Domain (UFD) is and polynomials related to it. This is important as it allows to understand when and how prime numbers can be generated from those polynomials using various methods, among which
* Extended Trial division
* Extended Sieve of Eratosthenes

## Fundamental Theorem of Arithmetic
This theorem says that any number n, can be written as a combination of prime numbers AND that it can only be done in a single unique way. The latter condition is particularly important to us. 

![Fundamental theorem of Arithmetic](Visualisations/images/Fundamental_Theorem_Of_Arithmetic.png?raw=true)

![Fundamental theorem of Arithmetic](Visualisations/images/image002.png?raw=true)
<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/4ac54202ebef1a4f49064fbc409600c290910b49" width="200" height="30">
While working with regular integers (in ℤ), unique factorization holds. As such, it may be difficult to see when or how this would not be valid anymore. It is only when going to complex numbers and other domains, that unique factorization can stop working.

## Domain ℤ[i]
ℤ[i] consists of all numbers that are of the form a+bi, with a and b in ℤ.
 
 ![Set Of Complex Integers](Visualisations/images/Set_Of_Complex_Integers.png?raw=true)

These types of numbers are called Gaussian integers. The length, or norm “N()”, of between the point and the origin is its absolute value. Visually, these numbers can be plotted on a two-dimensional plane, like classical vectors. The point (3, 2) corresponds to 3+2i. 

 ![Norm Of Complex Integers](Visualisations/images/Norm_Of_Complex_Integers.png?raw=true)

 ![Complex Numbers Visualized](Visualisations/images/Complex_Numbers_Visualized.png?raw=true)

The number 13, which is a prime in ℤ, can be factored into two smaller gaussian integers and is reducible in ℤ[i]. As such, 13 is thus not a prime in ℤ[i], which is in strong contrast to its primality in ℤ. 

 ![13 factorized](Visualisations/images/13_factorized.png?raw=true)
 
  ![Norm Of Complex Integers](Visualisations/images/image011.png?raw=true)
  
  ![Norm Of Complex Integers](Visualisations/images/image012.png?raw=true); ![Norm Of Complex Integers](Visualisations/images/image043.png?raw=true)

## Polynomials related to UFDs

There are a few polynomials that can be derived, each corresponding to a Heegner Number and thus related to the Unique Factorization Domain. For example, for Z[i], multiplying (x+yi) with its conjugate (x-yi), results in the ‘real’ polynomial x²+y². This is the same as its norm. 

 ![xyi_x2y2](Visualisations/images/xyi_x2y2.png?raw=true)

In general, the following functions can be derived from the Heegner Numbers. As mentioned before, a transformation is necessary to make the mathematics work out, for those numbers that are 3 modulo 4 (which means: the numbers that have a remainder of 3, when you divide them by 4).  For the Heegner numbers, all are 3 modulo for except for 1 and 2. Therefore, we prefer to work with a generalized α.


 ![xyi_x2y2](Visualisations/images/image024.png?raw=true)
 
 ![xyi_x2y2](Visualisations/images/image025.png?raw=true)