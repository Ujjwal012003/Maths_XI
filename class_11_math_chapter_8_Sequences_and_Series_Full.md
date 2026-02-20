# Chapter 8: Sequences_and_Series

## 8.1 Introduction to Sequences and Series

### 8.1.1 Definition of Sequences

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1x9NvJpISk1qUWEPWYCLCoU54-8yoFTR3" alt="Graph of sequence points with n vs a_n" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 8.1:</b> Each term of the sequence represented as a point at $(n,a_n)$</i></figcaption>
</figure>

**Introduction:**

Sequences and series form the foundation for understanding progressions of numbers and their summations. They appear naturally in various mathematical problems and real-life applications such as finance, computer science, and physics. This section introduces the basic concepts and sets a framework for the subsequent detailed study.

**Definition:**  
A **sequence** is an ordered list of numbers written in a definite order. More formally, a sequence is a function

$$
a: \mathbb{N} \to \mathbb{R},
$$

where to each natural number $ n $, it assigns a real number $ a_n $. The value $ a_n $ is called the **$ n^{th} $ term** of the sequence. The sequence can be denoted by

$$
\{a_n\} = \{a_1, a_2, a_3, \ldots\}.
$$

Each $ n $ belongs to the domain of natural numbers indicating the position of the term.

**Geometric Interpretation:**  
On the Cartesian plane, the sequence $ \{a_n\} $ can be represented as the set of points $ (n, a_n) $ where the $ x $-coordinate is the natural number index and the $ y $-coordinate is the value of the $ n^{th} $ term. Since $ n $ takes only integer values, the graph consists of isolated points aligned at integer $ x $-coordinates.

For example, for a geometric sequence with first term $ a $ and common ratio $ r $,

$$
a_n = a r^{n-1}, \quad n=1, 2, 3, \ldots,
$$

the points plotted reveal exponential growth or decay depending on $ r $.

### 8.1.2 Definition of Series

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1zlBG4VBVkRpSVWzuFnsOd1DdCN9-HxwV" alt="Summation notation over sequence terms" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 8.2:</b> Sum of sequence terms visualized as areas or cumulative sums</i></figcaption>
</figure>

**Definition:**  
A **series** is the sum of the terms of a sequence. Given a sequence $ \{a_n\} $, the **series** formed by it is

$$
S_n = a_1 + a_2 + a_3 + \cdots + a_n = \sum_{k=1}^n a_k,
$$

where $ S_n $ is called the **partial sum** of the series. If the limit of $ S_n $ as $ n \to \infty $ exists,

$$
S = \lim_{n \to \infty} S_n,
$$

then the series **converges** and the limit $ S $ is called the sum of the infinite series.

**Geometric Interpretation:**  
If we visualize the terms $ a_n $ as discrete quantities (for example, rectangles of height $ a_n $ and width 1 along the $ n $-axis), the series $ S_n $ represents the cumulative area formed by these rectangles from $ n=1 $ up to $ n $. Graphically, this shows how the sum grows as more terms are added.

### 8.1.3 Importance and Applications of Sequences and Series

**Importance:**

1. **Mathematics and Calculus:** Sequences help understand limits, which are fundamental for defining derivatives and integrals.
2. **Finance:** Calculation of interests, annuities, and financial growth frequently rely on series and their sums.
3. **Computer Science:** Algorithms often use sequences and series to compute sums and analyze complexity.
4. **Physics:** Many phenomena such as oscillations, wave motion, and quantum mechanics utilize series expansions for solutions.
5. **Engineering:** Signal processing and control theory involve infinite series to model system behaviors.

---

**Theorem 1:**  
**Existence of Partial Sums of a Sequence**

*For any sequence $ \{a_n\} $, the sequence of its partial sums $ \{S_n\} $, where*

$$
S_n = \sum_{k=1}^n a_k,
$$

*always exists.*

**Proof:**

1. The sequence $ \{a_n\} $ is given, so each term $ a_n $ exists as a real number.
2. Define $ S_1 = a_1 $; trivially, $ S_1 $ exists as the sum of one term.
3. Assume $ S_{n-1} $ exists for some $ n \geq 2 $.
4. Then 

   $$
   S_n = S_{n-1} + a_n,
   $$

   which is the sum of two existing real numbers, and hence $ S_n $ exists in $ \mathbb{R} $.
5. By the Principle of Mathematical Induction, $ S_n $ exists for all natural numbers $ n $.

This guarantees that the partial sums $ S_n $ can always be formed for any finite $ n $.

---

**Formulas & Working Rule for Sequences and Series**

**Formulas:**

1. $ n^{th} $ term of a sequence:  
   $$
   a_n
   $$

2. Sum of first $ n $ terms of a series:  
   $$
   S_n = \sum_{k=1}^n a_k
   $$

3. For arithmetic sequence:  
   $$
   a_n = a_1 + (n-1)d
   $$
   $$
   S_n = \frac{n}{2} \left( 2a_1 + (n-1)d \right)
   $$

4. For geometric sequence:  
   $$
   a_n = a_1 r^{n-1}
   $$
   $$
   S_n = a_1 \frac{1 - r^n}{1 - r}, \quad r \neq 1
   $$

---

**Working Rule to Solve Sequence and Series Problems**

1. **Identify the sequence type:** Determine if it is arithmetic, geometric, or another type.
2. **Find the general term $ a_n $:** Use the given pattern or formula.
3. **Calculate necessary terms:** Find particular terms if needed to understand the sequence progression.
4. **Form the series sum $ S_n $:** Apply the relevant sum formula or explicitly sum terms.
5. **Check conditions:** Verify restrictions such as $ r \neq 1 $ when using the geometric sum formula.
6. **Interpret results:** Analyze convergence in infinite series or compute exact sums for finite series.

---

### 8.1.4 Graded Solved Examples

**Example 1 (Concept Building):**

*Find the 5th term of the arithmetic sequence where the first term $ a_1=3 $ and common difference $ d=4 $.*

**Solution:**

Step 1: Identify the formula for the $ n^{th} $ term of an arithmetic progression (AP):  
$$
a_n = a_1 + (n - 1)d
$$

Step 2: Substitute values $ n = 5 $, $ a_1 = 3 $, $ d = 4 $:  
$$
a_5 = 3 + (5 - 1) \times 4 = 3 + 16 = 19
$$

**Answer:** The 5th term is 19.

---

**Example 2 (Competency Based):**

*Determine the sum of the first 6 terms of the geometric sequence with $ a_1 = 2 $ and common ratio $ r = 3 $.*

**Solution:**

Step 1: Use the formula for the sum of the first $ n $ terms of a geometric progression (GP):  
$$
S_n = a_1 \frac{1 - r^n}{1 - r}
$$

Step 2: Substitute $ a_1 = 2 $, $ r = 3 $, and $ n = 6 $:  
$$
S_6 = 2 \frac{1 - 3^6}{1 - 3} = 2 \frac{1 - 729}{1 - 3} = 2 \frac{-728}{-2} = 2 \times 364 = 728
$$

**Answer:** The sum of the first 6 terms is 728.

---

**Example 3 (HOTS):**

*A sequence is defined by $ a_n = \frac{1}{n(n+1)} $. Find the sum of the first $ n $ terms.*

**Solution:**

Step 1: Express the general term as partial fractions:  
$$
\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}
$$

Step 2: Write the sum:  
$$
S_n = \sum_{k=1}^n \left( \frac{1}{k} - \frac{1}{k+1} \right)
$$

Step 3: Expand the terms:  
$$
S_n = \left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \cdots + \left(\frac{1}{n} - \frac{1}{n+1}\right)
$$

Step 4: Notice telescoping cancellation:  
All intermediate terms cancel out, leaving  
$$
S_n = 1 - \frac{1}{n+1} = \frac{n}{n+1}
$$

**Answer:** Sum of the first $ n $ terms is $ \frac{n}{n+1} $.

---

This comprehensive introduction to sequences and series prepares students for further exploration of special sequences, convergence tests, and applications in various fields.

---

## 8.2 Sequences

### 8.2.1 General Term of a Sequence

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1_Vga7t03b0Qm9fEI5gRmTvwv3m-vwc2O" alt="Exponential growth in geometric sequences" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 8.3:</b> Geometric sequence points showing exponential growth or decay</i></figcaption>
</figure>

**Definition:**  
The **general term** or **$ n^{th} $ term** of a sequence is a formula that allows calculating the value of any term in the sequence based on its position $ n $. It is denoted as $ a_n $.

For a **geometric sequence**, defined by a first term $ a $ and common ratio $ r $, the general term is:

$$
a_n = a \cdot r^{n-1}, \quad n = 1, 2, 3, \ldots
$$

**Geometric Interpretation:**  
Each term corresponds to a point $ (n, a_n) $ on the Cartesian plane. The sequence can be visualized as isolated points aligned with integer $ x $-values. For geometric sequences:

- If $ |r| > 1 $, the terms increase exponentially, showing points rising steeply.
- If $ 0 < |r| < 1 $, the points decrease approaching zero.
- If $ r < 0 $, the sequence alternates in sign, creating points above and below the axis.

---

### 8.2.2 Types of Sequences

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1suxBxPSgGqqVMh7rAtmMNZ1FE2BGeGoH" alt="Visual comparison of arithmetic and geometric sequences" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 8.4:</b> Comparison of arithmetic (linear) and geometric (exponential) sequences graphically</i></figcaption>
</figure>

**1. Arithmetic Sequence (AP):**

A sequence where the difference between consecutive terms is constant. The general term is

$$
a_n = a_1 + (n-1)d,
$$

where $ a_1 $ is the first term and $ d $ is the common difference.

**Proof of property:**  
Difference between consecutive terms:

$$
a_{n+1} - a_n = [a_1 + n d] - [a_1 + (n-1) d] = d.
$$

Thus, the difference $ d $ is constant.

---

**2. Geometric Sequence (GP):**

A sequence where the ratio of consecutive terms is constant. The general term is

$$
a_n = a_1 \cdot r^{n-1},
$$

where $ a_1 $ is the first term and $ r $ is the common ratio.

**Proof of property:**  
Ratio between consecutive terms:

$$
\frac{a_{n+1}}{a_n} = \frac{a_1 r^{n}}{a_1 r^{n-1}} = r.
$$

Hence, the ratio $ r $ is constant.

---

**3. Fibonacci Sequence:**

Defined recursively by

$$
F_1 = 1, \quad F_2 = 1, \quad F_n = F_{n-1} + F_{n-2}, \quad n > 2.
$$

Each term is the sum of the two preceding terms.

---

### 8.2.3 Finite and Infinite Sequences

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/19GqbTjvcts2TjuRiIOImnpjwJJAwMHqR" alt="Finite versus infinite sequence illustrations" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 8.5:</b> Illustration contrasting finite and infinite sequences</i></figcaption>
</figure>

**Finite Sequence:**  
A sequence with a limited number of terms. For example,

$$
\{a_n\} = \{1, 3, 5, 7\}
$$

contains 4 terms only and terminates.

**Proof:**  
The sequence is explicitly defined for $ n = 1, 2, 3, 4 $ and no terms exist for $ n > 4 $, confirming finiteness.

---

**Infinite Sequence:**  
A sequence which continues indefinitely without end.

Example:

$$
a_n = n, \quad n = 1, 2, 3, \ldots,
$$

with terms $ 1, 2, 3, 4, \ldots $.

**Proof:**  
For every natural number $ n $, a corresponding term $ a_n $ exists, hence the sequence never terminates.

---

**Formulas & Working Rule:**

**Formulas:**

1. Arithmetic sequence general term:

$$
a_n = a_1 + (n-1)d
$$

2. Geometric sequence general term:

$$**
a_n = a_1 r^{n-1}
$$

3. Fibonacci sequence recursive definition:

$$
F_n = F_{n-1} + F_{n-2}
$$

4. Notation for finite sequences:

$$
\{a_1, a_2, \ldots, a_n\}
$$

5. Notation for infinite sequences:

$$
\{a_n\}_{n=1}^\infty
$$

---

**Working Rule (Algorithm) for problems involving sequences:**

1. **Identify the type** of sequence (arithmetic, geometric, recursive, or others).

2. **Find the general term** using given data or sequence properties.

3. **Check sequence length: finite or infinite** based on domain of definition.

4. **Calculate specific terms or sums** where required, applying formulas or recursive relations.

5. **Verify special cases:** for example, division by zero or out-of-domain indices.

---

### 8.2.4 Graded Solved Examples

**Example 1 (Concept Building):**  
Find the 7th term of the arithmetic sequence where $ a_1 = 5 $ and $ d = 3 $.

**Solution:**

Step 1: Use the formula for the general term:

$$
a_n = a_1 + (n-1)d.
$$

Step 2: Substitute $ n = 7 $, $ a_1 = 5 $, and $ d = 3 $:

$$
a_7 = 5 + (7 - 1) \times 3 = 5 + 18 = 23.
$$

**Answer:** The 7th term is 23.

---

**Example 2 (Competency Based):**  
Find the 5th term of the geometric sequence with $ a_1 = 2 $ and $ r = 4 $.

**Solution:**

Step 1: Use the formula for the general term:

$$
a_n = a_1 r^{n-1}.
$$

Step 2: Substitute $ n = 5 $, $ a_1 = 2 $, and $ r = 4 $:

$$
a_5 = 2 \times 4^{4} = 2 \times 256 = 512.
$$

**Answer:** The 5th term is 512.

---

**Example 3 (HOTS):**  
Given the Fibonacci sequence defined by $ F_1 = 1 $, $ F_2 = 1 $, and $ F_n = F_{n-1} + F_{n-2} $, find $ F_6 $.

**Solution:**

Step 1: Calculate the terms iteratively:

$$
\begin{aligned}
F_3 &= F_2 + F_1 = 1 + 1 = 2, \\
F_4 &= F_3 + F_2 = 2 + 1 = 3, \\
F_5 &= F_4 + F_3 = 3 + 2 = 5, \\
F_6 &= F_5 + F_4 = 5 + 3 = 8.
\end{aligned}
$$

**Answer:** $ F_6 = 8 $.

---

This comprehensive overview equips students with foundational knowledge of sequences, empowering them to recognize sequence types, determine terms, and understand the subtle difference between finite and infinite sequences.

---

## 8.3 Arithmetic Progression (AP)

### 8.3.1 Definition of Arithmetic Progression

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1FBeUoU9H-sIzA7OuxkEP066EsxB-lyB8" alt="Visual representation of equal spacing between terms in AP" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 8.6:</b> Terms of an AP spaced equally on a number line</i></figcaption>
</figure>

**Introduction:**

An arithmetic progression (AP) is one of the most important and frequently used types of sequences in mathematics. It represents a linear pattern where each term after the first is obtained by adding a fixed number called the common difference. This concept is widely applied in various fields such as finance for calculating interests, in physics for velocity increments, and in computer science for algorithm analysis.

**Definition:**  
An **arithmetic progression (AP)** is a sequence of numbers in which the difference between any two consecutive terms is a constant, called the **common difference** and denoted by $ d $.

If $ a_1 $ is the first term of the AP, then the sequence is:

$$
a_1, \quad a_1 + d, \quad a_1 + 2d, \quad a_1 + 3d, \quad \ldots
$$

The **common difference** $ d $ is defined as:

$$
d = a_2 - a_1 = a_3 - a_2 = \ldots
$$

**Geometric Interpretation:**  
On the real number line or coordinate plane, if we plot the term number $ n $ on the x-axis and the term value $ a_n $ on the y-axis, the points lie on a straight line with slope $ d $. This shows that terms of an AP increase (or decrease if $ d < 0 $) linearly.

---

### 8.3.2 Nth Term Formula

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1Y4OV-Ps4qwmZ0B2qLC5zVg4UHA_dEClq" alt="Graph showing linearity of nth term expression in AP" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 8.7:</b> Linear relationship between term index and term value showing the nth term formula</i></figcaption>
</figure>

**Theorem:**  
The $ n^{th} $ term $ a_n $ of an arithmetic progression with first term $ a_1 $ and common difference $ d $ is given by:

$$
\boxed{
a_n = a_1 + (n-1)d
}
$$

**Proof:**

Step 1: The first term is $ a_1 $.

Step 2: The second term is $ a_2 = a_1 + d $.

Step 3: The third term is 

$$
a_3 = a_2 + d = a_1 + 2d.
$$

Step 4: Following this pattern, the $ n^{th} $ term is obtained by adding $ d $ repeatedly $ n-1 $ times:

$$
a_n = a_1 + (n-1)d.
$$

This formula allows direct computation of any term in the sequence without finding the preceding terms.

---

### 8.3.3 Sum of First $ n $ Terms

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1HjKRgnnk2oE-_gjwg5ONsMAzS1Wh1NxQ" alt="Summation of terms in AP" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 8.8:</b> Visual interpretation of sum of first $ n $ terms of an AP</i></figcaption>
</figure>

**Theorem:**  
The sum $ S_n $ of the first $ n $ terms of an arithmetic progression is:

$$
\boxed{
S_n = \frac{n}{2} (a_1 + a_n) = \frac{n}{2} [2a_1 + (n-1)d].
}
$$

**Proof:**

Step 1: Consider the sum of the first $ n $ terms:

$$
S_n = a_1 + a_2 + a_3 + \cdots + a_n.
$$

Step 2: Write $ S_n $ in reverse order:

$$
S_n = a_n + a_{n-1} + a_{n-2} + \cdots + a_1.
$$

Step 3: Add the two sums term-wise:

$$
2 S_n = (a_1 + a_n) + (a_2 + a_{n-1}) + \cdots + (a_n + a_1).
$$

Each pair sums to $ a_1 + a_n $, and there are $ n $ such pairs, so

$$
2 S_n = n (a_1 + a_n).
$$

Step 4: Divide both sides by 2:

$$
S_n = \frac{n}{2}(a_1 + a_n).
$$

Step 5: Substitute $ a_n = a_1 + (n-1)d $ into the expression to get:

$$
S_n = \frac{n}{2} [2a_1 + (n-1)d].
$$

---

### 8.3.4 Common Difference

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1ZOsr2vgh83XUms2CCKWaDm063P64AFPF" alt="Difference between consecutive terms" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 8.9:</b> Illustrating the common difference between consecutive terms of an AP</i></figcaption>
</figure>

**Definition:**  
The **common difference** $ d $ is the constant amount added to each term to get the next term in the sequence:

$$
d = a_{k+1} - a_k, \quad k=1, 2, 3, \ldots
$$

**Examples:**

- For the sequence $ 2, 4, 6, 8, \ldots $,  

$$
d = 4 - 2 = 2.
$$

- For the sequence $ 10, 7, 4, 1, \ldots $,

$$
d = 7 - 10 = -3.
$$

---

### 8.3.5 Working Rule (Algorithm) for AP Problems

1. Identify the first term $ a_1 $ and the common difference $ d $.

2. Use the $ n^{th} $ term formula:

$$
a_n = a_1 + (n-1)d
$$

to find any term.

3. To find the sum of the first $ n $ terms, use:

$$
S_n = \frac{n}{2} (a_1 + a_n) \quad \text{or} \quad S_n = \frac{n}{2} [2a_1 + (n-1)d].
$$

4. For unknowns in $ a_1 $, $ d $, or $ n $, set up equations using given terms or sums.

5. Always check if the problem involves finite or infinite terms (AP is finite by definition).

---

### 8.3.6Graded Solved Examples

**Example 1 (Concept Building):**  
Find the 8th term of the AP: $ 5, 8, 11, \ldots $.

**Solution:**  
Step 1: Identify $ a_1 = 5 $, $ d = 8 - 5 = 3 $.  
Step 2: Use $ a_n = a_1 + (n-1)d $.  
Step 3: Compute 

$$
a_8 = 5 + (8-1) \times 3 = 5 + 21 = 26.
$$

**Answer:** $ a_8 = 26 $.

---

**Example 2 (Competency Based):**  
Find the sum of the first 12 terms of the AP: $ 3, 7, 11, \ldots $.

**Solution:**  
Step 1: $ a_1 = 3 $, $ d = 7 - 3 = 4 $.  
Step 2: Find 

$$
a_{12} = 3 + (12-1) \times 4 = 3 + 44 = 47.
$$

Step 3: Calculate sum:

$$
S_{12} = \frac{12}{2} \times (3 + 47) = 6 \times 50 = 300.
$$

**Answer:** $ S_{12} = 300 $.

---

**Example 3 (HOTS):**  
The sum of the first $ n $ terms of an AP is $ S_n = 3n^2 + 5n $. Find the first term and common difference.

**Solution:**  
Step 1: Recall the sum formula:

$$
S_n = \frac{n}{2} [2a_1 + (n-1)d].
$$

Step 2: Find the first term $ a_1 = S_1 $:

$$
a_1 = S_1 = 3(1)^2 + 5(1) = 3 + 5 = 8.
$$

Step 3: The $ n^{th} $ term is $ a_n = S_n - S_{n-1} $. Calculate the second term:

$$
a_2 = S_2 - S_1 = [3(2)^2 + 5(2)] - 8 = (12 + 10) - 8 = 22 - 8 = 14.
$$

Step 4: Calculate the common difference:

$$
d = a_2 - a_1 = 14 - 8 = 6.
$$

**Answer:** First term $ a_1 = 8 $, common difference $ d = 6 $.

---

This section provides a comprehensive understanding of the arithmetic progression with rigorous proofs and practical problem-solving strategies to master the topic effectively.

---

## 8.4 Special Series

# 8.4.1 Sum of First n Natural Numbers

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1zN77LgSdyOUXY4nMh6jKKiMmJ2IFlbGw" alt="Special series of natural numbers squares and cubes" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;">
<i><b>Figure 8.10:</b> Growth patterns of natural numbers</i>
</figcaption>
</figure>

Special series arise frequently in mathematics, physics, statistics, and competitive examinations. These formulas help compute large sums efficiently without adding terms individually.

Consider the series:

$$
1 + 2 + 3 + \cdots + n
$$

**Theorem**

$$
\boxed{
\sum_{k=1}^{n} k = \frac{n(n+1)}{2}
}
$$

---

**Proof (Using AP Method)**

The series:

$$
1, 2, 3, \ldots, n
$$

is an Arithmetic Progression with:

- First term: $a_1 = 1$
- Last term: $a_n = n$
- Number of terms: $n$

Using AP sum formula:

$$
S_n = \frac{n}{2}(a_1 + a_n)
$$

Substitute values:

$$
S_n = \frac{n}{2}(1 + n)
$$

$$
S_n = \frac{n(n+1)}{2}
$$

Hence proved.

---

### 8.4.2 Sum of Squares of First n Natural Numbers

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1p502nY_RISNF7v6p9Afa2tnM_F0SQ2xy" alt="Special series of natural numbers squares and cubes" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;">
<i><b>Figure 8.11:</b> Sum of squares of first n natural numbers</i>
</figcaption>
</figure>

Consider:

$$
1^2 + 2^2 + 3^2 + \cdots + n^2
$$

**Theorem**

$$
\boxed{
\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}
}
$$

---

**Proof (Outline by Mathematical Induction)**

Let

$$
S_n = 1^2 + 2^2 + \cdots + n^2
$$

Assume formula holds for $n$.

Then for $n+1$:

$$
S_{n+1} = S_n + (n+1)^2
$$

Substitute assumed formula and simplify.

After algebraic simplification, we obtain:

$$
S_{n+1} = \frac{(n+1)(n+2)(2n+3)}{6}
$$

Hence formula holds for all $n$ by induction.

---

### 8.4.3 Sum of Cubes of First n Natural Numbers

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1dtA2_gZr6wbDG0embxoz2kmnJDlmPdBG" alt="Special series of natural numbers squares and cubes" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;">
<i><b>Figure 8.12:</b> Sum of cubes of first n natural numbers</i>
</figcaption>
</figure>

Consider:

$$
1^3 + 2^3 + 3^3 + \cdots + n^3
$$

**Theorem**

$$
\boxed{
\sum_{k=1}^{n} k^3 =
\left( \frac{n(n+1)}{2} \right)^2
}
$$

This remarkable identity states:

> Sum of cubes = Square of sum of first n natural numbers

---

**Proof (Using Known Result)**

We know:

$$
1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}
$$

Squaring both sides:

$$
\left(1 + 2 + \cdots + n\right)^2
=
\left(\frac{n(n+1)}{2}\right)^2
$$

Expanding LHS and simplifying leads to:

$$
1^3 + 2^3 + \cdots + n^3
=
\left(\frac{n(n+1)}{2}\right)^2
$$

Hence proved.

---

### 8.4.4 Applications of Special Series

**1. Finding Large Sums Quickly**

Example:

Find:

$$
1 + 2 + 3 + \cdots + 100
$$

Solution:

$$
S = \frac{100 \times 101}{2} = 5050
$$

---

**2. Sum of Squares Application**

Find:

$$
1^2 + 2^2 + \cdots + 10^2
$$

$$
S = \frac{10 \times 11 \times 21}{6} = 385
$$

---

**3. Sum of Cubes Application**

Find:

$$
1^3 + 2^3 + \cdots + 5^3
$$

$$
S = \left( \frac{5 \times 6}{2} \right)^2
= 15^2 = 225
$$

---

**4. Real-Life Applications**

- Physics: distance traveled under uniform acceleration.
- Statistics: variance calculations.
- Algorithm analysis in computer science.
- Financial growth modeling.

---

### 8.4.5 Working Rule (Algorithm)

1. Identify pattern (natural numbers, squares, cubes).
2. Select correct formula.
3. Substitute value of $n$.
4. Simplify carefully.
5. Avoid manual summation for large $n$.

---

This completes the study of important special series required for Class 11 Sequences and Series.

## 8.5 Arithmetic Mean

### 8.5.1 Definition of Arithmetic Mean

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1qN9J-7qz5wux9sdg1P4l3N0Oeh6hzPtU" alt="Arithmetic mean between two numbers on number line" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;">
<i><b>Figure 8.13:</b> Arithmetic Mean represented as the midpoint between two numbers on the number line</i>
</figcaption>
</figure>

The **Arithmetic Mean (AM)** between two real numbers $a$ and $b$ is defined as the number obtained by dividing their sum by 2.

$$
\boxed{
AM = \frac{a + b}{2}
}
$$

Thus, if $A$ is the arithmetic mean between $a$ and $b$, then:

$$
A = \frac{a + b}{2}
$$

Geometrically, the arithmetic mean represents the midpoint between $a$ and $b$ on the number line.

---

**Arithmetic Mean Between Two Numbers**

Let $a$ and $b$ be two numbers.  
Suppose $A$ is inserted between them such that $a, A, b$ form an Arithmetic Progression (AP).

Since in an AP the middle term is the average of the first and third terms:

$$
A = \frac{a + b}{2}
$$

**Derivation:**

If $a, A, b$ are in AP, then the common difference is the same:

$$
A - a = b - A
$$

Solving:

$$
2A = a + b
$$

$$
A = \frac{a + b}{2}
$$

Hence proved.

---

### 8.5.2 Insertion of k Arithmetic Means

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1D0vvmfbnJxH5E02gjHoVn8PbzeWLEyD-" alt="Arithmetic mean between two numbers on number line" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;">
<i><b>Figure 8.14:</b> Insertion of k Arithmetic Means between two numbers</i>
</figcaption>
</figure>

   Suppose we want to insert $k$ arithmetic means between two numbers $a$ and $b$.

   Then the sequence becomes:

   $$
   a, A_1, A_2, \ldots, A_k, b
   $$

   This forms an AP containing:

   $$
   (k + 2) \text{ terms}
   $$

   **Step 1:** Determine total number of terms

   Total terms:

   $$
   n = k + 2
   $$

   **Step 2:** Use AP nth term formula

   In AP:

   $$
   a_n = a + (n-1)d
   $$

   Here, the last term is $b$, so:

   $$
   b = a + (k+1)d
   $$

   **Step 3:** Solve for common difference

   $$
   d = \frac{b - a}{k+1}
   $$

   **Step 4:** Find inserted means

   The arithmetic means are:

   $$
   A_1 = a + d
   $$

   $$
   A_2 = a + 2d
   $$

   $$
   \vdots
   $$

   $$
   A_k = a + kd
   $$

   Thus, the inserted arithmetic means are:

   $$
   A_r = a + r \cdot \frac{b-a}{k+1}, \quad r = 1,2,\ldots,k
   $$

   ---

**Geometric Interpretation**

When arithmetic means are inserted between two numbers, the interval between $a$ and $b$ is divided into $(k+1)$ equal parts. Each inserted mean lies at equal distances, confirming the linear structure of AP.

---

### 8.5.3 Working Rule (Algorithm)

1. Identify first number $a$ and last number $b$.
2. Determine number of arithmetic means $k$ to insert.
3. Compute common difference:

   $$
   d = \frac{b-a}{k+1}
   $$

4. Generate means using:

   $$
   A_r = a + rd
   $$

5. Verify that the last term equals $b$.

---

### 8.5.4 Graded Solved Examples

**Example 1 (Concept Building)**

Find the arithmetic mean between 6 and 14.

**Solution:**

$$
AM = \frac{6 + 14}{2} = \frac{20}{2} = 10
$$

**Answer:** $10$

---

**Example 2 (Competency Based)**

Insert 3 arithmetic means between 2 and 14.

**Solution:**

Step 1: $a = 2$, $b = 14$, $k = 3$

Step 2: Compute common difference:

$$
d = \frac{14 - 2}{3+1} = \frac{12}{4} = 3
$$

Step 3: Insert means:

$$
A_1 = 2 + 3 = 5
$$

$$
A_2 = 2 + 6 = 8
$$

$$
A_3 = 2 + 9 = 11
$$

Thus sequence becomes:

$$
2, 5, 8, 11, 14
$$

---

**Example 3 (HOTS)**

Insert 5 arithmetic means between 4 and 34.

**Solution:**

Step 1: $a = 4$, $b = 34$, $k = 5$

Step 2:

$$
d = \frac{34 - 4}{6} = \frac{30}{6} = 5
$$

Step 3: Insert means:

$$
9, 14, 19, 24, 29
$$

Final AP:

$$
4, 9, 14, 19, 24, 29, 34
$$

---

This completes the formal study of Arithmetic Mean as a direct application of Arithmetic Progression.


## 8.6 Geometric Progression (GP)

### 8.6.1 Definition of Geometric Progression

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1L95S-eY3z8d7I434bKBBTyUG9dohNXB_" alt="Exponential growth of geometric sequence" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 8.15:</b> Terms of a GP grow exponentially with common ratio r</i></figcaption>
</figure>

**Introduction:**

A geometric progression (GP) is a sequence of numbers where each term is found by multiplying the previous one by a fixed factor called the common ratio. This multiplicative structure leads to exponential growth or decay, making it vital in modeling natural phenomena such as population growth, radioactive decay, and financial compounding.

**Definition:**  
A **Geometric Progression (GP)** is a sequence $ \{a_n\} $ of numbers where each term after the first is obtained by multiplying the preceding term by a constant called the **common ratio** $ r $. If the first term is $ a $, the sequence is:

$$
a, \quad ar, \quad ar^2, \quad ar^3, \quad \ldots, \quad ar^{n-1}.
$$

Here, $ n $ is a natural number representing the term's position.

**Geometric Interpretation:**  
The terms of a geometric progression, when represented graphically with term index $ n $ on the x-axis and term value $ a_n $ on the y-axis, form points on an exponential curve. For $ |r| > 1 $, the terms increase exponentially; for $ 0 < |r| < 1 $, they decrease approaching zero. Negative values of $ r $ cause the terms to oscillate in sign, producing alternating points above and below the x-axis.

---

### 8.6.2 Nth Term Formula

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1YiBNyozYFcE0XxmAt0vZLHEEz8VvQDVk" alt="Formula for nth term in GP" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 8.16:</b> Calculation of nth term in GP using first term and common ratio</i></figcaption>
</figure>

**Theorem:**

The $ n^{th} $ term of a geometric progression with first term $ a $ and common ratio $ r $ is:

$$
\boxed{
a_n = a \cdot r^{n-1}.
}
$$

**Proof:**

Step 1: The first term is $ a_1 = a $.

Step 2: The second term is obtained by multiplying the first term by $ r $:

$$
a_2 = a \cdot r.
$$

Step 3: The third term is:

$$
a_3 = a_2 \cdot r = a \cdot r \cdot r = a \cdot r^2.
$$

Step 4: Similarly, the $ n^{th} $ term involves multiplying the first term by $ r $ exactly $ n-1 $ times:

$$
a_n = a \cdot r^{n-1}.
$$

This confirms the formula for the $ n^{th} $ term.

---

### 8.6.3 Sum of First $ n $ Terms

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1L0yNDzzH_UKoJRAtaklT62PuHGN4GlnX" alt="Sum of first n terms in GP" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 8.17:</b> Summation of first n terms of GP explained and formula derived</i></figcaption>
</figure>

**Theorem:**

The sum of the first $ n $ terms of a geometric progression with first term $ a $ and common ratio $ r \neq 1 $ is:

$$
\boxed{
S_n = a \frac{1 - r^{n}}{1 - r}.
}
$$

**Proof:**

Step 1: Write the sum $ S_n $ explicitly:

$$
S_n = a + ar + ar^2 + \cdots + ar^{n-1}.
$$

Step 2: Multiply both sides by $ r $:

$$
r S_n = ar + ar^2 + \cdots + ar^{n-1} + ar^n.
$$

Step 3: Subtract these two equations term-wise:

$$
S_n - r S_n = a - ar^{n}.
$$

Step 4: Factor the left-hand side and right-hand side:

$$
S_n (1 - r) = a (1 - r^{n}).
$$

Step 5: Provided $ r \neq 1 $, solve for $ S_n $:

$$
S_n = a \frac{1 - r^{n}}{1 - r}.
$$

---

### 8.6.4 Product of $ n $ Terms

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1GjNEN1PO3XsAi3hPQgfQ9UZ6ALAq1MnC" alt="Product of n terms of a GP" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 8.18:</b> Product of first n terms of a GP explained</i></figcaption>
</figure>

**Theorem:**

The product $ P_n $ of the first $ n $ terms of a geometric progression is:

$$
\boxed{
P_n = a^n \cdot r^{\frac{n(n-1)}{2}}.
}
$$

**Proof:**

Step 1: Express the product as:

$$
P_n = a \times ar \times ar^2 \times \cdots \times ar^{n-1}.
$$

Step 2: Factor out powers:

$$
P_n = a^{n} \times r^{0 + 1 + 2 + \cdots + (n-1)}.
$$

Step 3: Sum the exponents of $ r $, which is the sum of an arithmetic series:

$$
0 + 1 + 2 + \cdots + (n-1) = \frac{n(n-1)}{2}.
$$

Step 4: Substitute the sum into the expression:

$$
P_n = a^{n} \cdot r^{\frac{n(n-1)}{2}}.
$$

---

### 8.6.5 Formulas & Working Rule

**Formulas:**

$$
a_n = a r^{n-1}
$$

$$
S_n = a \frac{1 - r^{n}}{1 - r}, \quad r \neq 1
$$

$$
P_n = a^{n} \cdot r^{\frac{n(n-1)}{2}}
$$

---

**Working Rule (Algorithm) to Solve GP Problems:**

1. Identify the first term $ a $ and common ratio $ r $.

2. Use the $ n^{th} $ term formula $ a_n = a r^{n-1} $ to find any required term.

3. For summing the first $ n $ terms, apply

$$
S_n = a \frac{1 - r^{n}}{1 - r}.
$$

4. To calculate the product of first $ n $ terms, use

$$
P_n = a^{n} \cdot r^{\frac{n(n-1)}{2}}.
$$

5. Always verify the value of $ r $ (ensure $ r \neq 1 $ in sum formula) and check the domain of the problem.

---

### 8.6.6 Graded Solved Examples

**Example 1 (Concept Building):**

Find the 6th term of the geometric progression: $ 2, 6, 18, \ldots $.

**Solution:**

Step 1: Identify $ a = 2 $, $ r = \frac{6}{2} = 3 $.

Step 2: Use formula:

$$
a_6 = 2 \times 3^{6-1} = 2 \times 3^5 = 2 \times 243 = 486.
$$

**Answer:** $ 486 $

---

**Example 2 (Competency Based):**

Find the sum of the first 5 terms of the geometric progression: $ 5, 15, 45, \ldots $.

**Solution:**

Step 1: $ a = 5 $, $ r = 3 $, $ n = 5 $.

Step 2: Sum formula:

$$
S_5 = 5 \frac{1 - 3^5}{1 - 3} = 5 \times \frac{1 - 243}{1 - 3} = 5 \times \frac{-242}{-2} = 5 \times 121 = 605.
$$

**Answer:** $ 605 $

---

**Example 3 (HOTS):**

If the product of the first 4 terms of a geometric progression is 256 and the second term is 4, find the first term and the common ratio.

**Solution:**

Step 1: Let first term be $ a $ and common ratio $ r $.

Step 2: Product of first 4 terms:

$$
P_4 = a^4 \cdot r^{\frac{4 \times 3}{2}} = a^4 \cdot r^6 = 256.
$$

Step 3: The second term is:

$$
a r = 4.
$$

Step 4: Solve for $ a = \frac{4}{r} $ and substitute into product formula:

$$
\left(\frac{4}{r}\right)^4 \times r^6 = \frac{4^4}{r^4} \times r^6 = 4^4 \times r^{2} = 256 \times r^2 = 256.
$$

Step 5: Simplify:

$$
256 r^2 = 256 \implies r^2 = 1 \implies r = \pm 1.
$$

Step 6: If $ r = 1 $, then from step 3:

$$
a = \frac{4}{1} = 4.
$$

Since $ r = -1 $ can also be a solution:

$$
a = \frac{4}{-1} = -4.
$$

**Answer:** First term $ a = 4 $ or $ -4 $, common ratio $ r = 1 $ or $ -1 $.

---

This detailed exposition on geometric progression covers essential formulas, proofs, and typical examples, serving as a comprehensive guide for mastering the topic.

---

## 8.7 Geometric Mean

### 8.7.1 Definition of Geometric Mean

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1oH32RhZ8U4qC-LLhGaXdXlFRVvUjPFMT" alt="Geometric mean between two numbers on number line" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;">
<i><b>Figure 8.19:</b> Geometric Mean between two positive numbers forming a geometric progression</i>
</figcaption>
</figure>

The **Geometric Mean (GM)** between two positive real numbers $a$ and $b$ is defined as the positive number obtained by taking the square root of their product.

$$
\boxed{
GM = \sqrt{ab}
}
$$

Thus, if $G$ is the geometric mean between $a$ and $b$, then:

$$
G = \sqrt{ab}
$$

The geometric mean is defined only for **positive numbers** in the real number system.

---

**Geometric Mean Between Two Numbers**

Let $a$ and $b$ be two positive numbers.  
Suppose $G$ is inserted between them such that $a, G, b$ form a Geometric Progression (GP).

Since in a GP the square of the middle term equals the product of the extreme terms:

$$
G^2 = ab
$$

Taking positive square root:

$$
G = \sqrt{ab}
$$

---

**Derivation:**

If $a, G, b$ are in GP, then the common ratio is same:

$$
\frac{G}{a} = \frac{b}{G}
$$

Cross multiplying:

$$
G^2 = ab
$$

Taking square root:

$$
G = \sqrt{ab}
$$

Hence proved.

---

### 8.7.2 Insertion of k Geometric Means

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1EDNfSkeGD4T7pWwmpJPyQFUWOl_YUIlr" alt="Geometric mean between two numbers on number line" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;">
<i><b>Figure 8.20:</b> Insertion of k Geometric Means between two positive numbers</i>
</figcaption>
</figure>

Suppose we want to insert $k$ geometric means between two positive numbers $a$ and $b$.

Then the sequence becomes:

$$
a, G_1, G_2, \ldots, G_k, b
$$

This forms a GP containing:

$$
n = k + 2 \text{ terms}
$$

---

**Step 1: Use nth term formula of GP**

In a GP:

$$
a_n = a r^{n-1}
$$

Since the last term is $b$, we get:

$$
b = a r^{k+1}
$$

---

**Step 2: Solve for common ratio**

$$
r^{k+1} = \frac{b}{a}
$$

$$
r = \left( \frac{b}{a} \right)^{\frac{1}{k+1}}
$$

---

**Step 3: Determine inserted geometric means**

The geometric means are:

$$
G_1 = ar
$$

$$
G_2 = ar^2
$$

$$
\vdots
$$

$$
G_k = ar^k
$$

Thus, in general:

$$
G_r = a \left( \frac{b}{a} \right)^{\frac{r}{k+1}}, \quad r = 1,2,\ldots,k
$$

**Geometric Interpretation**

When geometric means are inserted between two numbers, the ratio between consecutive terms remains constant. The numbers increase (or decrease) multiplicatively rather than additively, forming an exponential pattern.

---

### 8.7.3 Working Rule (Algorithm)

1. Identify first term $a$ and last term $b$.
2. Determine number of geometric means $k$.
3. Compute common ratio:

   $$
   r = \left( \frac{b}{a} \right)^{\frac{1}{k+1}}
   $$

4. Generate means using:

   $$
   G_r = ar^r
   $$

5. Verify that final term equals $b$.

---

### 8.7.4 Graded Solved Examples

**Example 1 (Concept Building):**

Find the geometric mean between 4 and 9.

**Solution:**

$$
GM = \sqrt{4 \times 9} = \sqrt{36} = 6
$$

**Answer:** $6$

---

**Example 2 (Competency Based):**

Insert 2 geometric means between 3 and 81.

**Solution:**

Step 1: $a = 3$, $b = 81$, $k = 2$

Step 2: Find common ratio:

$$
r = \left( \frac{81}{3} \right)^{\frac{1}{3}} = 27^{\frac{1}{3}} = 3
$$

Step 3: Insert means:

$$
G_1 = 3 \times 3 = 9
$$

$$
G_2 = 3 \times 3^2 = 27
$$

Thus sequence becomes:

$$
3, 9, 27, 81
$$

---

**Example 3 (HOTS):**

Insert 3 geometric means between 2 and 162.

**Solution:**

Step 1: $a = 2$, $b = 162$, $k = 3$

Step 2:

$$
r = \left( \frac{162}{2} \right)^{\frac{1}{4}} = 81^{\frac{1}{4}} = 3
$$

Step 3: Insert means:

$$
6, 18, 54
$$

Final GP:

$$
2, 6, 18, 54, 162
$$

---

This completes the formal study of Geometric Mean as a direct application of Geometric Progression.


## 8.8 Relationship Between Arithmetic Mean and Geometric Mean (AM ≥ GM)

### 8.8.1 Statement of AM ≥ GM Inequality

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/17UxjmsaJBL5xJQ3my6bSxOP2cW5ReLzv" alt="Comparison of arithmetic mean and geometric mean" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;">
<i><b>Figure 8.21:</b> Arithmetic Mean is always greater than or equal to Geometric Mean for positive numbers</i>
</figcaption>
</figure>

For any two **positive real numbers** $a$ and $b$,

$$
\boxed{
\frac{a+b}{2} \ge \sqrt{ab}
}
$$

That is,

$$
\text{Arithmetic Mean} \ge \text{Geometric Mean}
$$

---

**Proof of AM ≥ GM**

Let $a$ and $b$ be two positive real numbers.

We know that the square of any real number is always non-negative:

$$
(a - b)^2 \ge 0
$$

Expanding:

$$
a^2 - 2ab + b^2 \ge 0
$$

Rearranging:

$$
a^2 + b^2 \ge 2ab
$$

Add $2ab$ to both sides:

$$
a^2 + 2ab + b^2 \ge 4ab
$$

Recognize left side as a perfect square:

$$
(a + b)^2 \ge 4ab
$$

Taking positive square root on both sides:

$$
a + b \ge 2\sqrt{ab}
$$

Divide both sides by 2:

$$
\frac{a+b}{2} \ge \sqrt{ab}
$$

Hence proved.

---

### 8.8.2 Equality Condition

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1fjT7VFTOSJKpVLBr0TtygwR2Rb1R7Gf3" alt="Geometric interpretation using rectangle and square" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;">
<i><b>Figure 8.22:</b> Equality Condition</i>
</figcaption>
</figure>

Equality holds if and only if:

$$
a = b
$$

Because in the proof:

$$
(a - b)^2 = 0
$$

only when:

$$
a = b
$$

Therefore,

$$
AM = GM \quad \text{if and only if} \quad a = b
$$

---

### 8.8.3 Working Rule (Algorithm)

1. Ensure numbers are positive.
2. Compute Arithmetic Mean:

   $$
   AM = \frac{a+b}{2}
   $$

3. Compute Geometric Mean:

   $$
   GM = \sqrt{ab}
   $$

4. Compare values.
5. Check equality condition ($a=b$).

---

### 8.8.4 Graded Solved Examples

**Example 1 (Concept Building):**

Verify AM ≥ GM for $a = 4$ and $b = 9$.

**Solution:**

Arithmetic Mean:

$$
AM = \frac{4+9}{2} = \frac{13}{2} = 6.5
$$

Geometric Mean:

$$
GM = \sqrt{4 \times 9} = \sqrt{36} = 6
$$

Thus:

$$
6.5 > 6
$$

Hence verified.

---

**Example 2 (Competency Based):**

Find two positive numbers whose sum is 20 and whose product is maximum.

**Solution:**

Let numbers be $x$ and $20-x$.

Using AM ≥ GM:

$$
\frac{x + (20-x)}{2} \ge \sqrt{x(20-x)}
$$

$$
\frac{20}{2} \ge \sqrt{x(20-x)}
$$

$$
10 \ge \sqrt{x(20-x)}
$$

Squaring both sides:

$$
100 \ge x(20-x)
$$

Maximum product occurs when equality holds:

$$
x = 20-x
$$

$$
2x = 20
$$

$$
x = 10
$$

Thus numbers are:

$$
10 \text{ and } 10
$$

Maximum product:

$$
100
$$

---

**Example 3 (HOTS):**

Prove that for positive numbers $a$ and $b$:

$$
a + b \ge 2\sqrt{ab}
$$

**Solution:**

This is equivalent to:

$$
\frac{a+b}{2} \ge \sqrt{ab}
$$

which is already proved above.

Hence:

$$
a + b \ge 2\sqrt{ab}
$$

with equality when $a = b$.

---

This establishes the fundamental inequality relating Arithmetic Mean and Geometric Mean, a powerful tool in algebra and optimization problems.


## 8.9 Infinite Geometric Series

### 8.9.1 Convergence Criteria

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1b5YPz0YiAa9xBI6iTlui8NIyTaFFWxk4" alt="Convergence dependent on common ratio in infinite series" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 8.23:</b> Graphical representation of convergence when common ratio |r| < 1</i></figcaption>
</figure>

**Introduction:**

Infinite geometric series arise in contexts where a term is repeatedly multiplied by a fixed ratio, producing an unending sequence of terms. Remarkably, under certain conditions, the sum of these infinite terms converges to a finite limit, making infinite geometric series crucial in calculus, physics, and economics.

**Definition:**  
An infinite geometric series of the form

$$
S = a + ar + ar^2 + ar^3 + \cdots
$$

converges if and only if the absolute value of the common ratio satisfies:

$$
|r| < 1.
$$

If $ |r| \geq 1 $, the terms do not diminish sufficiently, and the series diverges (the sum grows without bound or oscillates).

### 8.9.2 Sum to Infinity Formula

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1y41kHTjvskGFoYh60viPtW7RZjNd3kiZ" alt="Summation of infinite geometric series convergence" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 8.24:</b> Illustration showing total sum settling to a finite value as terms continue infinitely</i></figcaption>
</figure>

**Theorem:**

If $ |r| < 1 $, the sum of the infinite geometric series is:

$$
\boxed{
S = \frac{a}{1 - r}.
}
$$

**Proof:**

Step 1: Consider the sum of the first $ n $ terms,

$$
S_n = a + ar + ar^2 + \ldots + ar^{n-1} = a \frac{1 - r^n}{1 - r} \quad \text{for } r \neq 1.
$$

Step 2: Taking the limit as $ n \to \infty $,

$$
S = \lim_{n \to \infty} S_n = \lim_{n \to \infty} a \frac{1 - r^n}{1 - r}.
$$

Since $ |r| < 1 $, $ r^n \to 0 $ as $ n \to \infty $,

$$
\Rightarrow S = \frac{a}{1 - r}.
$$

This completes the proof that the infinite sum converges to $ \frac{a}{1 - r} $ under the convergence condition.

---

### 8.9.3 Applications and Examples

**Applications:**  
Infinite geometric series model phenomena such as:

- Decaying radioactive substances.
- Calculations of repeating decimals.
- Present value computations in finance.
- Signal processing in engineering.

---

**Working Rule (Algorithm) for Infinite Geometric Series Problems**

1. Identify the first term $ a $ and common ratio $ r $.

2. Verify the convergence condition $ |r| < 1 $.

3. If convergent, use the formula:

   $$
   S = \frac{a}{1 - r}.
   $$

4. Interpret the result within the problem context.

5. If $ |r| \geq 1 $, state that the series diverges and no finite sum exists.

---

### 8.9.4 Graded Solved Examples

**Example 1 (Concept Building):**

Find the sum to infinity of the series:

$$
3 + \frac{3}{2} + \frac{3}{4} + \frac{3}{8} + \ldots
$$

**Solution:**

Step 1: Identify $ a = 3 $, $ r = \frac{1}{2} $.

Step 2: Check $ |r| = \frac{1}{2} < 1 $, so series converges.

Step 3: Apply sum formula:

$$
S = \frac{3}{1 - \frac{1}{2}} = \frac{3}{\frac{1}{2}} = 6.
$$

**Answer:** The sum to infinity is $ 6 $.

---

**Example 2 (Competency Based):**

Determine if the series:

$$
5 - \frac{10}{3} + \frac{20}{9} - \frac{40}{27} + \ldots
$$

converges and find its sum if it does.

**Solution:**

Step 1: Identify $ a = 5 $, $ r = -\frac{2}{3} $.

Step 2: $ |r| = \frac{2}{3} < 1 $, so series converges.

Step 3: Use sum formula:

$$
S = \frac{5}{1 - \left(-\frac{2}{3}\right)} = \frac{5}{1 + \frac{2}{3}} = \frac{5}{\frac{5}{3}} = 3.
$$

**Answer:** The series converges and its sum is $ 3 $.

---

**Example 3 (HOTS):**

Find the sum to infinity of the infinite series:

$$
\frac{8}{3} + \frac{4}{3} + \frac{2}{3} + \frac{1}{3} + \ldots
$$

**Solution:**

Step 1: $ a = \frac{8}{3} $, $ r = \frac{1}{2} $.

Step 2: $ |r| = \frac{1}{2} < 1 $, series converges.

Step 3: Sum is:

$$
S = \frac{\frac{8}{3}}{1 - \frac{1}{2}} = \frac{\frac{8}{3}}{\frac{1}{2}} = \frac{8}{3} \times 2 = \frac{16}{3}.
$$

**Answer:** The sum to infinity is $ \frac{16}{3} $.

---

This completes the comprehensive study of infinite geometric series with convergence criteria, summation formula, and problem-solving strategies essential for mastering the topic.

---

## 8.10 Chapter Summary

### 8.10.1 Summary

This chapter introduced the fundamental concepts of **Sequences and Series**, which form an essential part of algebra and serve as a foundation for higher studies in calculus, analysis, finance, engineering, and applied sciences.

We began by understanding that a **sequence** is an ordered list of numbers defined by a specific rule. Formally, a sequence can be viewed as a function:

$$
a : \mathbb{N} \to \mathbb{R},
$$

where each natural number $n$ is associated with a real number $a_n$. The term $a_n$ is called the $n^{th}$ term of the sequence. Sequences may be finite or infinite depending on whether they terminate after a fixed number of terms or continue indefinitely.

A **series**, on the other hand, is the sum of the terms of a sequence. If $\{a_n\}$ is a sequence, then the series formed by it is:

$$
S_n = \sum_{k=1}^{n} a_k.
$$

The concept of partial sums plays a crucial role in understanding convergence and summation behavior.

The chapter then focused on two special and highly important types of sequences:

**Arithmetic Progression (AP)**

An arithmetic progression is a sequence in which the difference between consecutive terms remains constant. This constant difference is called the **common difference** $d$.

If $a_1$ is the first term, then the $n^{th}$ term of an AP is given by:

$$
a_n = a_1 + (n-1)d.
$$

The sum of the first $n$ terms is:

$$
S_n = \frac{n}{2}(a_1 + a_n)
= \frac{n}{2}[2a_1 + (n-1)d].
$$

Applications of AP include modeling uniform growth, linear trends, installment payments, and evenly spaced quantities.

We also studied the concept of **Arithmetic Mean (AM)**. If $A$ is inserted between two numbers $a$ and $b$ such that $a, A, b$ form an AP, then:

$$
A = \frac{a+b}{2}.
$$

Insertion of $k$ arithmetic means divides the interval into equal additive parts.

---

**Special Series**

Three important summation formulas were derived:

1. Sum of first $n$ natural numbers:

$$
\sum_{k=1}^{n} k = \frac{n(n+1)}{2}
$$

2. Sum of squares:

$$
\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}
$$

3. Sum of cubes:

$$
\sum_{k=1}^{n} k^3 =
\left(\frac{n(n+1)}{2}\right)^2
$$

These formulas enable quick computation of large sums and frequently appear in algebra, statistics, and mathematical modeling.

---

**Geometric Progression (GP)**

A geometric progression is a sequence in which each term is obtained by multiplying the previous term by a fixed number called the **common ratio** $r$.

If $a$ is the first term, then:

$$
a_n = a r^{n-1}.
$$

The sum of the first $n$ terms (for $r \ne 1$) is:

$$
S_n = a \frac{1 - r^n}{1 - r}.
$$

GP models exponential growth and decay, making it important in population studies, compound interest, radioactive decay, and financial calculations.

The **Geometric Mean (GM)** between two positive numbers $a$ and $b$ is:

$$
GM = \sqrt{ab}.
$$

If $G$ is inserted between $a$ and $b$ in a GP, then:

$$
G^2 = ab.
$$

Insertion of geometric means divides intervals multiplicatively rather than additively.

---

**Relationship Between AM and GM**

A fundamental inequality studied in this chapter is:

$$
\frac{a+b}{2} \ge \sqrt{ab},
$$

for all positive real numbers $a$ and $b$.

This is known as the **AM ≥ GM inequality**, with equality holding if and only if:

$$
a = b.
$$

This result is extremely important in optimization problems and mathematical inequalities.

---

**Infinite Geometric Series**

An infinite geometric series:

$$
a + ar + ar^2 + ar^3 + \cdots
$$

converges if and only if:

$$
|r| < 1.
$$

In such cases, its sum is:

$$
S = \frac{a}{1 - r}.
$$

This remarkable result shows that infinitely many terms can produce a finite sum under appropriate conditions.

---

**Concluding Remarks**

Throughout the chapter, we developed the ability to:

- Identify types of sequences.
- Derive general term formulas.
- Compute finite and infinite sums.
- Insert arithmetic and geometric means.
- Apply special summation formulas.
- Use inequalities for optimization.

Sequences describe patterns.  
Series measure accumulation.  
Arithmetic progressions model linear growth.  
Geometric progressions model exponential behavior.

These concepts are foundational not only for algebra but also for calculus and real-world problem solving.

This completes the study of Sequences and Series.
