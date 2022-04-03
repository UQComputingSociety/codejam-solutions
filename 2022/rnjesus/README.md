# RNJesus

## Problem Statement

**Background**

Generating random numbers on a computer is no easy task! In general, there are two different types computers can generate:

1. RNG (Entropy Based Random Number Generator)

2. [PRNG (Pseudo-Random Number Generator)](https://en.wikipedia.org/wiki/Pseudorandom_number_generator)

True randomness is hard to achieve on a computer - logic has to be deterministic, and when you have hard-coded determinism, expected behaviour is introduced to your 'randomness'. As such, true RNG is not achievable with a computer alone, and requires some external source of "entropy". This is generally accomplished through recording some natural source, and using it to generate random values through some digital conversion. Examples of this can include measuring the temperature of an object, recording feedback from a microphone, and more.

Without this source of entropy however, we resort to PRNG. PRNG gives us random number generation, that is also deterministic, i.e., given an input seed, we can reproduce the same sequence of "random" values - this is the reason you are able to enter a seed into Minecraft, and generate the same world each time! This relies on mathematical foundations which produce unpredictable, seemingly 'chaotic' (random) behaviour, such that you can't predict what the `nth` value is, but can always reproduce it given you know the initial conditions.

One way to introduce 'random' behaviour to your data, is to introduce some chaos! A Linear Feedback Shift Register ([LFSR](https://en.wikipedia.org/wiki/Linear-feedback_shift_register)) is one common way often used in computers, however many chaotic functions and processes exist which you can use as a source of deterministic "randomness".

**Your Task**

The [Logistic map](https://en.wikipedia.org/wiki/Logistic_map) is a well known chaotic function, and is what we will use a source of pseudo-randomness in our PRNG. It is a recursive sequence generation, with each iteration given by the function:

![image](https://s3.amazonaws.com/hr-assets/0/1648484871-fb348752ff-logistic.png)

In this context, the `seed` is the initial value of the sequence, `x_0`, and `r` is a pre-defined coefficient which changes properties about the map (see the Wikipedia page, and the constraints below).

The map (with the given `r` coefficient) will produce a pseudo-random value between 0 and 1. Use this to implement a PRNG which uses this map as its source of randomness, and generates `n` pseudo-random values between `min` and `max`. 

## Input Format

Space separated, the seed `x_0` (float), a minimum value `min` (int), a maximum value `max` (int), and `n`, the number of numbers to generate (int)

e.g.

s min max n

## Constraints

0 < x_0 < 1

0 <= min <= 100

min < max <= 1000

0 <= n <= 100

r = 3.7783

## Output Format
n PRNG generated numbers, `r_i`, each on a new line, rounded to 5 decimal places

min <= r_i <= max forall i

## Sample Input

```
0.3795796905420248 33 34 3
```

## Sample Output

```
33.88979
33.37053
33.88124
```
