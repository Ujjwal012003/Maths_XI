# Chapter 2: Relations_and_Functions

## 2.1 Introduction to Relations

### 2.1.1 Definition of Relations and Geometric Interpretation

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1dEnLX09dY3XkfFt1YrEHXwf9RVrFETJL" alt="Sets A and B with ordered pairs showing relation R" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.1:</b> Relation as subset of Cartesian product A × B</i></figcaption>
</figure>

Relations are fundamental in mathematics for establishing connections between elements of one set with elements of another or the same set. These connections help model a variety of mathematical and real-world situations, from linking students to their grades to pairing cities with temperatures. Understanding relations prepares the foundation for the study of functions and mappings.

**Definition:**  
Given two non-empty sets $A$ and $B$, the **Cartesian product** $A \times B$ is the set of all ordered pairs $(a, b)$ where $a \in A$ and $b \in B$. Formally,  
$$
A \times B = \{(a, b) \mid a \in A, b \in B\}.
$$  
A **relation** $R$ from set $A$ to set $B$ is any subset of $A \times B$:  
$$
R \subseteq A \times B.
$$  
Each element of $R$ is an ordered pair $(a,b)$ indicating that $a$ is related to $b$ by the relation $R$.

**Geometric Meaning:**  
Consider $A$ and $B$ as sets of numbers on the x-axis and y-axis respectively. Every ordered pair $(a,b) \in R$ can be represented as a point on the Cartesian plane at coordinate $(a, b)$. Thus, a relation corresponds to a set of points in the plane. This geometric representation helps visualize how elements of one set correspond to elements of another.

---

### 2.1.2 Ordered Pairs and Their Notation

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1boPD2Jg6qBRUNGH8YGbYYbGSybouiQRH" alt="Notation of ordered pairs and difference with unordered pairs" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.2:</b> Representation and notation of ordered pairs</i></figcaption>
</figure>

**Ordered Pair:**  
An **ordered pair** $(a, b)$ is a pair of elements where the order matters. It means $(a, b)$ is different from $(b, a)$ unless $a = b$. The first element $a$ is called the **first coordinate**, and the second element $b$ is called the **second coordinate**.

**Notation:**  
Parentheses are used with a comma separating the two elements:  
$$
(a, b).
$$  
This notation is fundamental because it allows us to distinguish relations and functions where order conveys meaning, for example, input-output pairs in functions.

---

### 2.1.3 Representation of Relations

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1hEO92PhFBA1_L5jM3LWfcfSxG7OriwXd" alt="Various ways to represent relations: set of ordered pairs, arrow diagram, Cartesian product" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.3:</b> Different representations of the relation between sets A and B</i></figcaption>
</figure>

Relations between sets can be represented in various ways to facilitate understanding and analysis:

**1. Set of Ordered Pairs**  
A relation $R$ is defined explicitly as a collection of ordered pairs:  
$$
R = \{(a_1, b_1), (a_2, b_2), \ldots, (a_n, b_n)\}.
$$  
This is a direct and complete description of the relation.

**2. Arrow Diagram**  
We place elements of set $A$ and set $B$ as points (nodes) on two parallel lines and draw arrows from elements in $A$ to elements in $B$ to indicate relation pairs. This visually represents how elements correspond without enumerating pairs explicitly.

**3. Cartesian Product Visualization**  
Since $R \subseteq A \times B$, it can be visualized on the Cartesian plane by plotting all the points $(a,b)$ corresponding to pairs in $R$. This is especially useful when $A$ and $B$ are numerical sets.

---

**Theorem 1 (Relation is a Subset of Cartesian Product):**  
$$
\boxed{
\text{Every relation } R \text{ from } A \text{ to } B \text{ is a subset of } A \times B.
}
$$

**Proof:**  
**Step 1:** By definition, an ordered pair $(a,b)$ belongs to the Cartesian product $A \times B$ if and only if $a \in A$ and $b \in B$.  
**Step 2:** A relation $R$ from $A$ to $B$ is defined as a collection of such ordered pairs where each pair shows a connection between an element of $A$ and an element of $B$.  
**Step 3:** Since every element of $R$ is an ordered pair $(a,b)$ with $a \in A$ and $b \in B$, it follows that $R \subseteq A \times B$.  
Hence proved.

---

### 2.1.4 Formulas Related to Relations

$$
\begin{aligned}
&A \times B = \{(a,b) \mid a \in A, b \in B\}, \\
&|A \times B| = |A| \cdot |B| \quad \text{(Cardinality of Cartesian product)}, \\
&R \subseteq A \times B \quad \text{(Relation as subset)}, \\
&\text{Domain of } R = \{a \in A \mid (a,b) \in R \text{ for some } b \in B\}, \\
&\text{Range of } R = \{b \in B \mid (a,b) \in R \text{ for some } a \in A\}.
\end{aligned}
$$

---

**Working Rule (Algorithm) to Analyze Relations**

1. **Identify sets**: Determine sets $A$ and $B$ involved in the relation.  
2. **Find Cartesian product**: List or identify all ordered pairs in $A \times B$.  
3. **Determine relation pairs**: Identify which ordered pairs are included in relation $R$.  
4. **Use representation**:  
    - Write out the set of ordered pairs explicitly.  
    - Or draw the arrow diagram mapping elements from $A$ to $B$.  
    - Or plot points on the Cartesian plane for $A \times B$ and highlight points belonging to $R$.  
5. **Analyze relation properties** (if needed): Check if each element in domain corresponds to one or more elements in range, etc.

---

### 2.1.5 Graded Solved Examples

**Example 1 (Basic):**  
Let $A = \{1, 2\}$ and $B = \{3, 4\}$. Define relation $R = \{(1, 3), (2, 4)\}$. Represent $R$ using:  
(a) Set of ordered pairs  
(b) Arrow diagram  
(c) Cartesian plane plot

**Solution:**  
**Step 1:** Write ordered pairs directly:  
$$
R = \{(1,3), (2,4)\}.
$$  
**Step 2:** Draw two parallel lists for sets $A$ and $B$, then draw arrows:  
- From 1 in $A$ to 3 in $B$  
- From 2 in $A$ to 4 in $B$  
**Step 3:** On Cartesian plane, plot points $(1, 3)$ and $(2, 4)$.  
This visually confirms the relation.

---

**Example 2 (Competency Based):**  
Given $A = \{1, 2, 3\}$, $B = \{a, b\}$, and relation  
$$
R = \{(1,a), (3,a), (3,b)\}
$$  
Find:  
(a) Domain of $R$  
(b) Range of $R$  
(c) Whether $R$ is a function from $A$ to $B$

**Solution:**  
**Step 1:** Domain = all first elements of ordered pairs:  
$$
\text{Domain} = \{1, 3\}.
$$  
**Step 2:** Range = all second elements of ordered pairs:  
$$
\text{Range} = \{a, b\}.
$$  
**Step 3:** Checking if $R$ is a function:  
For $R$ to be a function, each element of $A$ should relate to exactly one element of $B$. Here, element 3 relates to both $a$ and $b$.  
So, $R$ is **not** a function.

---

**Example 3 (HOTS):**  
Let $A = \{1, 2, 3\}$, $B = \{4, 5, 6\}$, and relation $R$ be defined as:  
$$
(a,b) \in R \text{ if and only if } a + b = 7.
$$  
Represent $R$ as a set of ordered pairs and plot on Cartesian plane.

**Solution:**  
**Step 1:** Calculate all pairs $(a,b)$ with $a \in A$, $b \in B$, summing to 7:  
- $1 + 6 = 7$ $\Rightarrow (1,6) \in R$  
- $2 + 5 = 7$ $\Rightarrow (2,5) \in R$  
- $3 + 4 = 7$ $\Rightarrow (3,4) \in R$  
**Step 2:** So,  
$$
R = \{(1,6), (2,5), (3,4)\}.
$$  
**Step 3:** Plot these points on Cartesian plane: points $(1,6)$, $(2,5)$, $(3,4)$ lie on the line $x + y = 7$.  
This shows a relation defined by a linear equation.

---

This completes the detailed study of the introduction to relations including their definition, ordered pairs, and different methods of representation. Understanding these concepts builds the foundation for exploring functions and other mathematical structures based on relations.

---

## 2.2 Types of Relations

### 2.2.1 Reflexive Relations

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/118yoo9VcvvTNVJNbzJqfh6zykU5UcmOZ" alt="Reflexive relation represented by diagonal on Cartesian plane" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.4:</b>Reflexive Relation </i></figcaption>
</figure>

**Definition:**  
A relation $R$ on a set $A$ is called **reflexive** if every element of $A$ is related to itself. Formally,  
$$
\forall a \in A, \quad (a,a) \in R.
$$

**Geometric Meaning:**  
On the Cartesian plane representing $A \times A$, reflexivity means that all points lying on the diagonal line $y = x$ must be included in the relation. These are points where the first and second coordinates are equal, indicating elements are related to themselves.

---

**Bold Text Theorem 1:**  
$$
\boxed{
R \text{ is reflexive } \iff \forall a \in A, (a,a) \in R.
}
$$

**Bold Text Proof:**  
**Step 1:** Assume $R$ is reflexive. By definition, each element $a \in A$ must satisfy $(a,a) \in R$.  
**Step 2:** Conversely, if $(a,a) \in R$ for all $a \in A$, then by definition $R$ is reflexive.  
Thus, the two statements are equivalent.

**Example (Reflexive Relation):**

Let $ A = \{1,2,3\} $ and define relation  
$$
R = \{(1,1),(2,2),(3,3),(1,2)\}.
$$

Check whether $R$ is reflexive.

**Solution:**

For reflexivity, we must verify that:

$$
(a,a) \in R \quad \text{for all } a \in A.
$$

We check:

- $(1,1) \in R$ ✔
- $(2,2) \in R$ ✔
- $(3,3) \in R$ ✔

Since every element is related to itself,  
$$
R \text{ is reflexive.}
$$

---

### 2.2.2 Symmetric Relations

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1Km0SUW0V1yhVTcBmXUP-MSUwq--rQXI-" alt="Symmetric relation with points reflected about line y=x" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.5:</b> Symmetric Relation </i></figcaption>
</figure>

**Definition:**  
A relation $R$ on set $A$ is **symmetric** if whenever an element $a$ is related to $b$, then $b$ is also related to $a$. Formally,  
$$
\forall a,b \in A, \quad (a,b) \in R \implies (b,a) \in R.
$$

**Geometric Meaning:**  
On the Cartesian plane, symmetry means if the point $(a,b)$ is in $R$, then its reflection $(b,a)$ about the diagonal line $y = x$ is also in $R$. Thus, the set of points in the relation is symmetric about this line.

---

**Bold Text Theorem 2:**  
$$
\boxed{
R \text{ is symmetric } \iff (a,b) \in R \implies (b,a) \in R \quad \forall a,b \in A.
}
$$

**Bold Text Proof:**  
**Step 1:** Suppose $R$ is symmetric. Then by definition, presence of $(a,b)$ in $R$ guarantees $(b,a) \in R$.  
**Step 2:** Conversely, if for every pair $(a,b) \in R$, the pair $(b,a)$ also belongs to $R$, then $R$ satisfies the property of symmetry.  
Hence, the two statements are logically equivalent.

**Example (Symmetric Relation):**

Let $ A = \{1,2,3\} $ and define relation  
$$
R = \{(1,2),(2,1),(2,3),(3,2)\}.
$$

Check whether $R$ is symmetric.

**Solution:**

For symmetry, if $(a,b) \in R$, then $(b,a)$ must also belong to $R$.

We check:

- $(1,2) \in R$ and $(2,1) \in R$ ✔
- $(2,3) \in R$ and $(3,2) \in R$ ✔

Since every ordered pair has its reverse in $R$,

$$
R \text{ is symmetric.}
$$

---

### 2.2.3 Transitive Relations

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1WqeIYK6Q5N_5vhU2-v-zpKj-6inJ8-9v" alt="Transitive relation with chain of connections" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.6:</b> Transitive Relation</i></figcaption>
</figure>

**Definition:**  
A relation $R$ on set $A$ is **transitive** if whenever $a$ is related to $b$, and $b$ is related to $c$, then $a$ is related to $c$. Formally,  
$$
\forall a,b,c \in A, \quad (a,b) \in R \text{ and } (b,c) \in R \implies (a,c) \in R.
$$

**Geometric Meaning:**  
This reflects connection chains on the Cartesian plane or in arrow diagrams: if an arrow leads from $a$ to $b$, and from $b$ to $c$, then there must be a direct arrow from $a$ to $c$.

---

**Bold Text Theorem 3:**  
$$
\boxed{
R \text{ is transitive } \iff (a,b) \in R \text{ and } (b,c) \in R \implies (a,c) \in R \quad \forall a,b,c \in A.
}
$$

**Bold Text Proof:**  
**Step 1:** Suppose $R$ is transitive. Then by definition the relation must include $(a,c)$ whenever $(a,b)$ and $(b,c)$ are in $R$.  
**Step 2:** Conversely, if the condition above holds true for all triples in $A$, then $R$ satisfies transitivity.   
Hence, the equivalence is established.

**Example (Transitive Relation):**

Let $ A = \{1,2,3\} $ and define relation  
$$
R = \{(1,2),(2,3),(1,3)\}.
$$

Check whether $R$ is transitive.

**Solution:**

For transitivity, whenever:

$$
(a,b) \in R \text{ and } (b,c) \in R,
$$

then $(a,c)$ must also belong to $R$.

Here:

- $(1,2) \in R$
- $(2,3) \in R$

So for transitivity, $(1,3)$ must belong to $R$.

Since $(1,3) \in R$ ✔

Thus,

$$
R \text{ is transitive.}
$$

---

### 2.2.4 Equivalence Relations (Brief Introduction)

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Equivalence relation combining reflexive, symmetric, and transitive properties" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.7:</b> Equivalence relation characterized by reflexivity, symmetry, and transitivity</i></figcaption>
</figure>

**Definition:**  
A relation $R$ on a set $A$ is an **equivalence relation** if it is simultaneously reflexive, symmetric, and transitive.

Equivalence relations are foundational as they partition sets into equivalence classes where elements related to each other form subsets with special properties.

**Example (Equivalence Relation):**

Let $ A = \{1,2,3\} $ and define relation  
$$
R = \{(1,1),(2,2),(3,3)\}.
$$

Check whether $R$ is an equivalence relation.

**Solution:**

**Reflexive:**  
Each element is related to itself ✔

**Symmetric:**  
All pairs are of the form $(a,a)$, so symmetry holds ✔

**Transitive:**  
If $(a,a)$ and $(a,a)$ are in $R$, then $(a,a)$ is in $R$ ✔

Thus, $R$ satisfies all three properties.

Therefore,

$$
R \text{ is an equivalence relation.}
$$

---

### 2.2.5 Equivalence Classes and Partition of a Set

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/15YW5D9KQ6eVd4ywiBSi_RKoYGi_GWoLX" alt="Equivalence classes forming partitions of a set" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;">
<i><b>Figure 2.8:</b> An equivalence relation partitions a set into disjoint equivalence classes</i>
</figcaption>
</figure>

**Definition: Equivalence Class**

Let $ R $ be an equivalence relation on a set $ A $.  
For any element $ a \in A $, the **equivalence class** of $ a $, denoted by

$$
[a] = \{ x \in A \mid (x,a) \in R \},
$$

is the set of all elements of $ A $ that are related to $ a $ under $ R $.

---

**Important Properties**

If $ R $ is an equivalence relation on $ A $, then:

1. Every element of $ A $ belongs to exactly one equivalence class.
2. Two equivalence classes are either:
   - identical, or  
   - disjoint.
3. The collection of all equivalence classes forms a **partition** of $ A $.

---

**Theorem: Equivalence Relation Induces a Partition**

$$
\boxed{
\text{Every equivalence relation on a set } A \text{ partitions } A.
}
$$

**Proof (Outline):**

**Step 1:** Since $ R $ is reflexive, every $ a \in A $ satisfies  
$$
(a,a) \in R,
$$
so $ a \in [a] $. Hence, every element belongs to some equivalence class.

**Step 2:** Suppose two equivalence classes $ [a] $ and $ [b] $ have a common element $ x $.  
Then:
$$
(x,a) \in R \quad \text{and} \quad (x,b) \in R.
$$

Using symmetry and transitivity, we conclude:
$$
(a,b) \in R.
$$

Thus,
$$
[a] = [b].
$$

So equivalence classes are either identical or disjoint.

Hence, the equivalence classes form a partition of $ A $.

---

### Example

Let $ A = \{1,2,3,4\} $ and define relation:

$$
R = \{(a,b) : a \equiv b \pmod{2} \}.
$$

This relation groups numbers according to parity.

Equivalence classes:

$$
[1] = \{1,3\}
$$

$$
[2] = \{2,4\}
$$

These two classes partition the set $ A $ into:

$$
\{\{1,3\}, \{2,4\}\}
$$

Each element belongs to exactly one class.

---

### Key Conclusion

Equivalence relations divide a set into meaningful categories where elements inside each class are considered equivalent under the given relation.


### Formulas Summary for Relations on Set $A$:

$$
\begin{aligned}
&\text{Reflexive:} && \forall a \in A, (a,a) \in R, \\
&\text{Symmetric:} && (a,b) \in R \implies (b,a) \in R, \\
&\text{Transitive:} && (a,b) \in R \text{ and } (b,c) \in R \implies (a,c) \in R, \\
&\text{Equivalence Relation:} && R \text{ is reflexive, symmetric, and transitive}.
\end{aligned}
$$

---

### Working Rule (Algorithm) to Identify Relation Types

1. **Given:** A relation $R$ on set $A$.  
2. **Check Reflexivity:** Verify for each $a \in A$ if $(a,a) \in R$. If yes for all, $R$ is reflexive.  
3. **Check Symmetry:** For each $(a,b) \in R$, check if $(b,a) \in R$. If true for all, $R$ is symmetric.  
4. **Check Transitivity:** For all $(a,b), (b,c) \in R$, verify $(a,c) \in R$. If yes for all, $R$ is transitive.  
5. **Equivalence:** If all above three hold, then $R$ is an equivalence relation.  

---



### Graded Solved Examples

**Example 1 (Concept Building):**  
Let $A = \{1, 2, 3\}$ and  
$$
R = \{(1,1), (2,2), (3,3), (1,2), (2,1)\}.
$$  
Determine whether $R$ is reflexive, symmetric, and transitive.

**Solution:**  
**Step 1:** Reflexivity - Check if $(a,a) \in R$ for $a=1,2,3$. All three pairs $(1,1), (2,2), (3,3)$ are present. So, $R$ is reflexive.  
**Step 2:** Symmetry - Check pairs:  
- $(1,2) \in R$ and $(2,1) \in R$; condition holds.  
- No other off-diagonal pairs exist. So, $R$ is symmetric.  
**Step 3:** Transitivity - Check combinations:  
- $(1,2)$ and $(2,1)$ are in $R$, is $(1,1)$ present? Yes.  
- All other necessary chains also satisfy transitivity.  
**Conclusion:** $R$ is reflexive, symmetric, and transitive; therefore, an equivalence relation.

---

**Example 2 (Competency):**  
Let $A = \{a,b,c\}$ and  
$$
R = \{(a,a), (b,b), (c,c), (a,b), (b,a), (a,c)\}.
$$  
Is $R$ symmetric and transitive?

**Solution:**  
**Step 1:** Symmetry - $(a,b) \in R$ and $(b,a) \in R$, so symmetric holds for these pairs.  
However, $(a,c) \in R$ but $(c,a) \notin R$, so $R$ is **not symmetric**.  
**Step 2:** Transitivity - Consider pairs:  
- $(a,b)$, $(b,a)$ included; $(a,a)$ present as well.  
- No counterexamples found for transitivity involving $c$.  
Thus, $R$ is transitive for the existing pairs.  
**Conclusion:** $R$ is transitive but not symmetric.

---

**Example 3 (HOTS):**  
Consider $A = \{1,2,3\}$ and relation  
$$
R = \{(x,y) : x \leq y\}.
$$  
Check whether $R$ is reflexive, symmetric, transitive, and if it is an equivalence relation.

**Solution:**  
**Step 1:** Reflexive: For all $a$, $a \leq a$ holds true, so $R$ is reflexive.  
**Step 2:** Symmetric: Does $x \leq y$ imply $y \leq x$? No, unless $x = y$, so $R$ is not symmetric.  
**Step 3:** Transitive: If $x \leq y$ and $y \leq z$, then $x \leq z$, so $R$ is transitive.  
**Step 4:** Equivalence relation requires all three properties; since $R$ is not symmetric, it is **not** an equivalence relation.

---

This section establishes the fundamental properties of relations and prepares students to recognize these traits clearly in problems related to set theory and functions.

---

## 2.3 Cartesian Product of Sets

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Cartesian product visualized as grid points on coordinate plane" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.3.0:</b> Visualization of Cartesian product as points on a Cartesian plane</i></figcaption>
</figure>

The Cartesian product of sets is a foundational concept in set theory and mathematics at large that lays the groundwork for relations and functions. It pairs every element of one set with every element of another to form ordered pairs, giving us a structured way to combine sets.

### 2.3.1 Definition and Representation

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Definition and examples of Cartesian product" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.3.1:</b> Example of Cartesian product of sets $A=\{1,2\}$ and $B=\{x,y\}$</i></figcaption>
</figure>

**Definition:**  
If $A$ and $B$ are two non-empty sets, then the **Cartesian product** $A \times B$ is defined as the set of all ordered pairs $(a,b)$, where $a \in A$ and $b \in B$. Symbolically,  
$$
A \times B = \{(a,b) \mid a \in A, b \in B \}.
$$

**Representation:**  
- If $A = \{1, 2\}$ and $B = \{x, y\}$, then  
$$
A \times B = \{(1,x), (1,y), (2,x), (2,y)\}.
$$  
- Each ordered pair corresponds to one point in the Cartesian plane with $a$ as the x-coordinate and $b$ as the y-coordinate.

**Geometric Meaning:**  
Visualizing $A \times B$ on the Cartesian plane places all points $(a,b)$ with $a \in A$ on the x-axis and $b \in B$ on the y-axis as discrete points, forming a grid or lattice of points.

---

### 2.3.2 Properties of Cartesian Products

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Properties of Cartesian products" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.3.2:</b> Demonstration of Cartesian product properties including cardinality and empty set</i></figcaption>
</figure>

The following properties hold for any sets $A, B, C$:

1. **Non-commutativity:**  
$$
A \times B \neq B \times A,
$$  
because $(a,b)$ is generally different from $(b,a)$.

2. **Associativity (up to isomorphism):**  
$$
(A \times B) \times C \cong A \times (B \times C),
$$  
meaning the sets are “structurally the same” when regrouped.

3. **Empty set property:**  
$$
A \times \emptyset = \emptyset \quad \text{and} \quad \emptyset \times A = \emptyset,
$$  
because no ordered pairs can be formed with an empty set.

4. **Cardinality:**  
If $|A| = m$ and $|B| = n$, then  
$$
|A \times B| = m \times n,
$$  
because each element in $A$ pairs with every element in $B$.

---

**Bold Text Theorem 1:**  
$$
\boxed{
|A \times B| = |A| \times |B|
}
$$

**Bold Text Proof:**  
**Step 1:** Suppose $|A| = m$ and $|B| = n$.  
**Step 2:** Every element $a \in A$ pairs with all $n$ elements in $B$, forming $n$ ordered pairs.  
**Step 3:** Since there are $m$ elements in $A$, total pairs formed are $m \times n$.  
Hence, the cardinality of $A \times B$ is $m \cdot n$.

---

### 2.3.3 Relationship Between Elements of Cartesian Products

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Relationship between elements in Cartesian products" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.3.3:</b> Relationship between domain (set A) and range (set B) elements in ordered pairs</i></figcaption>
</figure>

In the ordered pair $(a,b) \in A \times B$:
- The first component $a$ is an element of the **domain** set $A$.
- The second component $b$ is an element of the **range** set $B$.

These pairs form the basis for defining relations and functions, where elements of $A$ are related or mapped to elements of $B$.

---

### Formulas Summary:

$$
\begin{aligned}
&A \times B = \{ (a,b) \mid a \in A, b \in B \}, \\
&|A \times B| = |A| \times |B|, \\
&A \times \emptyset = \emptyset, \\
&A \times B \neq B \times A, \\
&(A \times B) \times C \cong A \times (B \times C).
\end{aligned}
$$

---

### Working Rule (Algorithm) to Find Cartesian Product:

1. **Step 1:** Identify elements in set $A$ and set $B$.  
2. **Step 2:** Form ordered pairs with every element $a \in A$ paired with every element $b \in B$.  
3. **Step 3:** Write out the set of these ordered pairs explicitly as $A \times B$.  
4. **Step 4:** Calculate the cardinality by multiplying $|A|$ and $|B|$.  
5. **Step 5:** Visualize the Cartesian product in coordinate form if sets are numerical.  

---

### Graded Solved Examples

**Example 1 (Concept Building):**  
Find $ A \times B $ where $ A = \{1, 3\} $ and $ B = \{x, y\} $.

**Solution:**  
**Step 1:** List elements of $A$ and $B$.  
**Step 2:** Form ordered pairs:  
$$
(1,x), (1,y), (3,x), (3,y).
$$  
**Step 3:** Thus,  
$$
A \times B = \{(1,x), (1,y), (3,x), (3,y)\}.
$$

---

**Example 2 (Competency Based):**  
If $|A| = 5$ and $|B| = 4$, find the number of elements in $ A \times B $. What is $ B \times A $? Are $A \times B$ and $B \times A$ equal?

**Solution:**  
**Step 1:** Calculate cardinality:  
$$
|A \times B| = 5 \times 4 = 20.
$$  
**Step 2:** $B \times A$ also has $4 \times 5 = 20$ elements, but  
**Step 3:** $A \times B \neq B \times A$ because ordered pairs differ in order.

---

**Example 3 (HOTS):**  
Given $ A = \{1, 2\} $, $ B = \{3, 4\} $, and $ C = \{5, 6\} $, compare $(A \times B) \times C$ and $A \times (B \times C)$.

**Solution:**  
**Step 1:** Elements of $A \times B$ are:  
$$
(1,3), (1,4), (2,3), (2,4).
$$  
**Step 2:** $(A \times B) \times C$ contains ordered pairs like  
$$
((1,3),5), ((1,3),6), \ldots
$$  
**Step 3:** Elements of $B \times C$:  
$$
(3,5), (3,6), (4,5), (4,6).
$$  
**Step 4:** $A \times (B \times C)$ contains  
$$
(1,(3,5)), (1,(3,6)), \ldots
$$  
**Step 5:** Although the elements differ in nested pairing, there is a one-to-one correspondence between these sets, so  
$$
(A \times B) \times C \cong A \times (B \times C),
$$  
showing associativity in Cartesian products.

---

This comprehensive understanding of Cartesian products, their properties, and representation prepares students for later concepts like relations, functions, and further algebraic structures.

---

## 2.4 Introduction to Functions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Illustration of function as a special relation mapping elements from domain to range" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.4.0:</b> A function mapping elements from the domain set $A$ to the range set $B$</i></figcaption>
</figure>

Functions form one of the central pillars of mathematics, representing precise and unique correspondences between elements of sets. They appear in almost every branch of mathematics and science because they describe how one quantity depends on another.

### 2.4.1 Definition of a Function as a Special Relation

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Graphical representation of function with unique output for each input" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.4.1:</b> The function property ensures each input in domain corresponds to a unique output in range</i></figcaption>
</figure>

**Definition:**  
A **function** $ f $ from a set $ A $ to a set $ B $ is a special relation such that every element in $ A $ (called the **domain**) is related to **exactly one** element in $ B $ (called the **codomain**). Formally,  
$$
f: A \rightarrow B
$$  
with  
$$
\forall a \in A, \exists ! \, b \in B \quad \text{such that} \quad (a, b) \in f,
$$  
where "$\exists !$" means "there exists exactly one".

**Geometric Meaning:**  
On the Cartesian coordinate plane, a function corresponds to a set of points such that each x-coordinate (input) corresponds to exactly one y-coordinate (output). Graphically, this is tested by the **vertical line test**: any vertical line crosses the graph of the function at most once, indicating uniqueness of output for each input.

---

### 2.4.2 Function Notation and Examples

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Examples of function notations and mappings" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.4.2:</b> Examples of function notation and mappings between elements</i></figcaption>
</figure>

**Function Notation:**  
- $ f $ denotes a function from $ A $ to $ B $.  
- $ f(x) $ denotes the output of $ f $ corresponding to input $ x \in A $.  
- The notation $ f : x \mapsto f(x) $ explicitly states the mapping.

**Examples:**  
1. **Linear function:**  
   $$
   f(x) = 2x + 3,
   $$  
   For every $ x $, there is a unique output $ f(x) $. For example, $ f(1) = 5 $.

2. **Quadratic function:**  
   $$
   g(x) = x^2,
   $$  
   For every $ x \in \mathbb{R} $, $ g(x) $ is uniquely determined. For instance, $ g(-2) = 4 $.

3. **Piecewise function:**  
   $$
   h(x) = \begin{cases}
   x + 2 & \text{if } x < 0, \\
   x - 1 & \text{if } x \geq 0.
   \end{cases}
   $$  
   Each $ x $ maps to exactly one value depending on the interval it lies in.

---

### 2.4.3 Uniqueness of Function Output Theorem

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Uniqueness theorem ensuring single output for each input" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.4.3:</b> Illustration of uniqueness of output for each input in function $ f $</i></figcaption>
</figure>

**Theorem:**  
$$
\boxed{
\text{For each } x \in A, \quad \exists \text{ a unique } y \in B \text{ such that } f(x) = y.
}
$$

**Proof:**  
**Step 1:** Suppose for some $ x_0 \in A $, there are two outputs $ y_1 = f(x_0) $ and $ y_2 = f(x_0) $.  
**Step 2:** By the definition of a function, each input corresponds to exactly one output, so this implies $ y_1 = y_2 $.  
**Step 3:** Hence, the output is unique for every input $ x $.

This confirms the fundamental nature of functions—the one-to-one association between input and output.

---

### Formulas & Working Rule (Algorithm) for Functions

$$
\begin{aligned}
&f: A \rightarrow B, \\
&f(x) = \text{output corresponding to input } x \in A, \\
&\text{Uniqueness: } \forall x \in A,\; \exists! \, y \in B \text{ such that } f(x) = y.
\end{aligned}
$$

**Working Rule to Check or Define a Function:**

1. Step 1: Identify the domain $ A $ and codomain $ B $.  
2. Step 2: For each input $ x \in A $, check if there is an output $ f(x) \in B $.  
3. Step 3: Verify that for no input $ x $ are there multiple outputs (uniqueness).  
4. Step 4: Express the function with notation $ f(x) $ or mapping $ f: x \mapsto f(x) $.  
5. Step 5: Optionally graph the function and apply the vertical line test to validate uniqueness visually.

---

### Graded Solved Examples

**Example 1 (Concept Building):**  
Let $ f(x) = 3x + 1 $, for $ x \in \mathbb{R} $. Find $ f(2) $.

**Solution:**  
**Step 1:** Substitute $ x = 2 $ into $ f(x) $:  
$$
f(2) = 3(2) + 1 = 6 + 1 = 7.
$$  
**Step 2:** Thus, $ f(2) = 7 $.

---

**Example 2 (Competency Based):**  
Check whether the relation $ R = \{(1,2), (2,3), (2,4)\} $ from set $ A = \{1,2\} $ to $ B = \{2,3,4\} $ is a function.

**Solution:**  
**Step 1:** For input 1, output is 2 (unique).  
**Step 2:** For input 2, outputs are 3 and 4 (not unique).  
**Step 3:** Since $ 2 $ maps to two different outputs, $ R $ is **not** a function.

---

**Example 3 (HOTS):**  
Define a function $ f: \mathbb{R} \rightarrow \mathbb{R} $ by  
$$
f(x) = \begin{cases}
x^2 & \text{if } x \geq 0, \\
- x & \text{if } x < 0.
\end{cases}
$$  
Find $ f(-3) $, determine if $ f $ is a function and justify.

**Solution:**  
**Step 1:** For $ x = -3 < 0 $,  
$$
f(-3) = - (-3) = 3.
$$  
**Step 2:** Each input produces exactly one output (piecewise definition is unambiguous).  
**Step 3:** Hence, $ f $ is a function.

---

This section lays the foundation of functions as precise, structured mappings with clear input-output uniqueness—a vital step for comprehension of further functions and their properties.

---

## 2.5 Domain, Codomain and Range

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Visual explanation of domain, codomain and range with mappings" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.5.0:</b> Illustration of domain, codomain and range in function mapping</i></figcaption>
</figure>

Functions represent connections between elements of sets. To fully understand a function, it is essential to distinguish its **domain**, **codomain**, and **range**. These concepts play a key role in the study of functions and their behavior.

### 2.5.1 Definition of Domain and Codomain

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Domain and codomain depiction as sets and mapping arrows" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.5.1:</b> The domain is the set of all inputs; the codomain contains all possible outputs</i></figcaption>
</figure>

**Domain:**  
The **domain** of a function $ f: A \to B $ is the set of all input values $ x \in A $ for which the function is defined. Formally, it is the set of all **first components** of the ordered pairs in the function:  
$$
\text{Domain}(f) = \{ x \in A : f(x) \text{ is defined} \}.
$$

**Codomain:**  
The **codomain** of a function $ f: A \to B $ is the set $ B $, consisting of all potential outputs (values into which elements of the domain are mapped). The codomain is fixed by the definition of the function, even if not all values in $ B $ are actually achieved by $ f $.

---

### 2.5.2 Definition and Calculation of Range

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Range depicts the actual set of outputs produced by the function" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.5.2:</b> Range is the set of actual outputs generated by the function</i></figcaption>
</figure>

**Range:**   
The **range** of $ f $ is the set of all actual output values generated by applying $ f $ to every element of the domain. It is a subset of the codomain and can be expressed as:  
$$
\text{Range}(f) = \{ y \in B : y = f(x) \text{ for some } x \in A \}.
$$

**Calculation of Range:**  
To find the range, evaluate the function $ f(x) $ for all $ x \in \text{Domain}(f) $, and collect the unique values.

---

**Bold Text Theorem 1:**  
$$
\boxed{
\text{Range}(f) \subseteq \text{Codomain}(f)
}
$$

**Bold Text Proof:**  
**Step 1:** By definition, every output $ y $ of $ f $ for some input $ x \in A $ belongs to the codomain $ B $, so $ y \in B $.  
**Step 2:** The range consists precisely of those $ y $ which are attained by the function from inputs in the domain.  
**Step 3:** Therefore, the range is always a subset of the codomain.

---

### 2.5.3 Examples to Determine Domain, Codomain and Range

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Worked examples for finding domain, codomain and range" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.5.3:</b> Examples illustrating how to compute domain, codomain, and range</i></figcaption>
</figure>

---

**Example 1:**  
Consider the function  
$$
f(x) = \sqrt{x}.
$$  
- **Step 1 (Domain):** $ f(x) $ is defined only when $ x \geq 0 $, so domain is  
$$
\{ x : x \geq 0 \}.
$$  
- **Step 2 (Codomain):** Commonly taken as all non-negative real numbers,  
$$
\{ y : y \geq 0 \}.
$$  
- **Step 3 (Range):** Since $ f(x) $ produces outputs only $ \geq 0 $, range is equal to codomain,  
$$
\{ y : y \geq 0 \}.
$$

---

**Example 2:**  
Let  
$$
g(x) = \frac{1}{x}.
$$  
- **Step 1 (Domain):** Defined for all real numbers except $ 0 $, so domain is  
$$
\{ x : x \in \mathbb{R}, x \neq 0 \}.
$$  
- **Step 2 (Codomain):** Real numbers $ \mathbb{R} $ can be assumed.  
- **Step 3 (Range):** Since $ g(x) \neq 0 $, the range is  
$$
\{ y : y \in \mathbb{R}, y \neq 0 \}.
$$

---

**Example 3 (HOTS – Corrected):**  
Function  
$$
h(x) = \frac{x^2 - 1}{x - 1}.
$$

**Step 1 (Domain):**  
The function is undefined at $ x = 1 $.  
So domain is:

$$
\{ x \in \mathbb{R} : x \neq 1 \}.
$$

**Step 2 (Simplify Expression):**

$$
h(x) = \frac{(x-1)(x+1)}{x-1} = x+1, \quad x \neq 1.
$$

**Step 3 (Range):**

Since $ x \neq 1 $, the expression $ x+1 $ cannot take the value:

$$
1 + 1 = 2.
$$

Therefore, the range is:

$$
\mathbb{R} \setminus \{2\}.
$$

Thus, although $ h(x) $ simplifies algebraically to $ x+1 $, the restriction in the domain removes the output value $ 2 $ from the range.


### Working Rule (Algorithm) to Find Domain, Codomain and Range

1. **Step 1:** Identify the function $ f: A \to B $ and check any restrictions on $ x $ for which $ f(x) $ is defined to determine the domain.  
2. **Step 2:** State the codomain set $ B $ as given or by context.  
3. **Step 3:** Calculate the range by evaluating $ f(x) $ for all $ x \in \text{Domain}(f) $.  
4. **Step 4:** Simplify expression(s) if needed to find all possible output values.  
5. **Step 5:** Express range as a subset of codomain.

---

### Formulas and Key Points

$$
\begin{aligned}
&\text{Domain}(f) = \{x : f(x) \text{ is defined} \}, \\
&\text{Codomain}(f) = \text{Target set of outputs}, \\
&\text{Range}(f) = \{ f(x) : x \in \text{Domain}(f) \} \subseteq \text{Codomain}(f).
\end{aligned}
$$

---

This section's comprehensive explanation and examples ensure students develop a clear understanding of domain, codomain, and range, which are fundamental concepts in the study of functions.

---

## 2.6 Types of Functions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Different types of functions: injective, surjective, bijective" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.6.0:</b> Visualizing injective, surjective, and bijective functions on mappings</i></figcaption>
</figure>

Functions describe relationships between sets with various characteristics such as uniqueness, coverage, and invertibility. Understanding different types of functions is essential, especially one-one (injective), onto (surjective), bijective functions, and special real-valued functions.

---

### 2.6.1 One-One (Injective) Functions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Injective function with unique output for each input" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.6.1:</b> Injective function showing distinct inputs mapping to distinct outputs</i></figcaption>
</figure>

**Definition:**  
A function $ f: A \to B $ is **injective** (one-one) if different inputs in $ A $ map to different outputs in $ B $. Formally,  
$$
f(a_1) = f(a_2) \implies a_1 = a_2 \quad \forall a_1, a_2 \in A.
$$

**Geometric Interpretation:**  
No horizontal line intersects the graph of the function more than once.

**Example:**  
$ f(x) = 2x $ is injective because different $ x $-values produce different $ f(x) $ values.

---

### 2.6.2 Onto (Surjective) Functions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Surjective function where every output in codomain has a pre-image" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.6.2:</b> Surjective function with full coverage on codomain</i></figcaption>
</figure>

**Definition:**  
A function $ f: A \to B $ is **surjective** (onto) if every element $ b \in B $ has at least one $ a \in A $ with $ f(a) = b $.  
Mathematically,  
$$
\forall b \in B, \exists a \in A : f(a) = b.
$$

**Geometric Interpretation:**  
The function covers the entire codomain.

**Example:**  
$ f(x) = x^3 $ maps all real numbers onto $ \mathbb{R} $, making it surjective.

---

### 2.6.3 Bijective Functions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Bijective function showing one-to-one and onto correspondence" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.6.3:</b> Bijective function mapping each element uniquely and covering codomain fully</i></figcaption>
</figure>

**Definition:**  
A function $ f: A \to B $ is **bijective** if it is both injective and surjective. It establishes a perfect pairing between $ A $ and $ B $.

**Properties:**  
- Has an inverse function $ f^{-1} $.  
- Maps elements of $ A $ uniquely onto elements of $ B $.

**Example:**  
$ f(x) = x + 2 $, for $ x \in \mathbb{R} $, is bijective.

---

### 2.6.4 Real-Valued Functions and Special Types

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Graphs of special real-valued functions" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.6.4:</b> Examples of rational, modulus, signum, and greatest integer functions</i></figcaption>
</figure>

**Real-Valued Functions:**  
Functions from a subset of real numbers to real numbers: $ f: \mathbb{R} \to \mathbb{R} $.

---

**Special Types:**

1. **Rational Functions:**  
Defined as  
$$
f(x) = \frac{p(x)}{q(x)}
$$  
where $ p, q $ are polynomials and $ q(x) \neq 0 $.

2. **Modulus Function:**  
$$
f(x) = |x| = \begin{cases} 
x & x \geq 0, \\
-x & x < 0
\end{cases}
$$  
An even function with a V-shaped graph.

3. **Signum Function:**  
$$
\operatorname{sgn}(x) = \begin{cases} 
1 & x > 0, \\
0 & x = 0, \\
-1 & x < 0
\end{cases}
$$  
Indicates the sign of $ x $.

4. **Greatest Integer Function:**  
$$
f(x) = \lfloor x \rfloor = \text{greatest integer} \leq x.
$$  
Has a step-like graph with discontinuities at integers.

---

### Theorems and Proofs

**Bold Text Theorem 1 (Injective Function Criterion):**  
$$
\boxed{
f \text{ is injective } \iff f(a_1) = f(a_2) \Rightarrow a_1 = a_2.
}
$$

**Bold Text Proof:**  
**Step 1:** Suppose $ f(a_1) = f(a_2) $.  
**Step 2:** If $ f $ is injective, then this equality implies $ a_1 = a_2 $.  
**Step 3:** Conversely, if $ a_1 \neq a_2 $, then $ f(a_1) \neq f(a_2) $, satisfying injectivity.

---

**Bold Text Theorem 2 (Surjective Function Criterion):**  
$$
\boxed{
f \text{ is surjective } \iff \forall b \in B, \exists a \in A : f(a) = b.
}
$$

**Bold Text Proof:**  
**Step 1:** By definition, surjectivity means every $ b $ in codomain is an image of some $ a $ in domain.

---

### Working Rule (Algorithm) to Identify Function Types

1. Step 1: Identify the domain $ A $ and codomain $ B $.  
2. Step 2: To check injectivity, test whether $ f(a_1) = f(a_2) $ implies $ a_1 = a_2 $.  
3. Step 3: To check surjectivity, verify if for every $ b \in B $ there exists $ a \in A $ such that $ f(a) = b $.  
4. Step 4: If both conditions hold, the function is bijective.

---

### Graded Solved Examples

**Example 1 (Basic):**  
Is the function $ f(x) = 2x + 3 $ bijective from $ \mathbb{R} \to \mathbb{R} $?

**Solution:**  
**Step 1:** Check injectivity:  
Assume $ f(a) = f(b) $,  
$$
2a + 3 = 2b + 3 \implies a = b.
$$  
So $ f $ is injective.

**Step 2:** Check surjectivity:  
For any $ y \in \mathbb{R} $, solve $ y = 2x + 3 \implies x = \frac{y - 3}{2} \in \mathbb{R}. $  
Since every $ y $ has a pre-image, $ f $ is surjective.

**Step 3:** Hence, $ f $ is bijective.

---

**Example 2 (Competency):**  
Is $ g(x) = x^2 $ injective or surjective from $ \mathbb{R} \to \mathbb{R} $?

**Solution:**  
**Step 1:** Check injectivity:  
$ g(1) = 1^2 = 1 $, $ g(-1) = (-1)^2 = 1 $, but $ 1 \neq -1 $.  
So $ g $ is not injective.

**Step 2:** Check surjectivity:  
Negative numbers have no square roots in $ \mathbb{R} $, so not every $ y \in \mathbb{R} $ has an $ x $ with $ g(x) = y $.  
So $ g $ is not surjective.

---

**Example 3 (HOTS):**  
Analyze the function $ h(x) = |x| $ on domain $ \mathbb{R} $ and codomain $ \mathbb{R} $.

**Solution:**  
**Step 1:** Check injectivity:  
$ h(1) = 1, h(-1) = 1 $, but $ 1 \neq -1 $, so $ h $ is not injective.

**Step 2:** Check surjectivity:  
For $ y \geq 0 $, $ h(x) = y $ has solutions $ x = y $ or $ x = -y $.  
For $ y < 0 $, no solution. So range is $ [0, \infty) \neq \mathbb{R} $, not surjective.

---

This section equips students with tools to classify, analyze, and understand diverse types of functions, reinforcing core ideas fundamental in higher mathematics.

---

## 2.7 Operations on Functions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Graph showing addition, subtraction, multiplication, division, and composition of functions" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.7.0:</b> Visual representation of operations on functions</i></figcaption>
</figure>

Functions are fundamental mathematical objects, and performing operations on them helps build more complex functions and analyze their behaviors. This section explores operations including addition, subtraction, multiplication, division, and composition, along with crucial properties such as the fact that the composition of functions is itself a function.

---

### 2.7.1 Addition, Subtraction, Multiplication and Division of Functions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Function operations illustrated graphically" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.7.1:</b> Illustrations of addition, subtraction, multiplication, and division of functions</i></figcaption>
</figure>

**Definitions:**

1. **Addition:**  
For two functions $ f $ and $ g $ defined on the same domain, the sum $ (f+g) $ is defined by  
$$
(f+g)(x) = f(x) + g(x).
$$

2. **Subtraction:**  
The difference $ (f-g) $ is defined by  
$$
(f-g)(x) = f(x) - g(x).
$$

3. **Multiplication:**  
The product $ (fg) $ is given by  
$$
(fg)(x) = f(x) \cdot g(x).
$$

4. **Division:**  
Provided $ g(x) \neq 0 $, the quotient $ \left(\frac{f}{g}\right) $ is  
$$
\left(\frac{f}{g}\right)(x) = \frac{f(x)}{g(x)}.
$$

**Geometric Interpretation:**  
These operations combine the outputs of $ f $ and $ g $ pointwise. Graphically, $ (f+g)(x) $ is obtained by adding the y-values of $ f $ and $ g $, etc. Multiplication and division produce transformations with distinct visual characteristics corresponding to product and ratio effects on the functions.

---

### 2.7.2 Composition of Functions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Composition of functions visualized as mapping through intermediate domain" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.7.2:</b> Composition $ (f \circ g)(x) = f(g(x)) $, mapping through intermediate function</i></figcaption>
</figure>

**Definition:**  
Given functions $ g: A \to B $ and $ f: B \to C $, the composition $ (f \circ g): A \to C $ is defined as  
$$
(f \circ g)(x) = f(g(x))
$$  
for all $ x \in A $.

**Geometric Meaning:**  
Composition can be visualized as applying $ g $ first to transform the input $ x $ in $ A $ to $ g(x) $ in $ B $, then applying $ f $ to map $ g(x) $ in $ B $ to $ f(g(x)) $ in $ C $.

---

**Bold Text Theorem:** Composition of Functions is a Function

$$
\boxed{
\text{If } f: B \to C \text{ and } g: A \to B \text{ are functions, then } f \circ g: A \to C \text{ is a function.}
}
$$

**Bold Text Proof:**

**Step 1:** Since $ g $ is a function, for each $ x \in A $, $ g(x) $ is uniquely defined in $ B $.

**Step 2:** Given $ f $ is a function, for each element $ y \in B $, $ f(y) $ is uniquely defined in $ C $.

**Step 3:** Thus, for every $ x \in A $, the value $ f(g(x)) $ is uniquely defined in $ C $.

**Step 4:** This satisfies the definition of a function from $ A $ to $ C $, hence $ f \circ g $ is a function.

---

### Formulas Summary:

$$
\begin{aligned}
&(f + g)(x) = f(x) + g(x), \\
&(f - g)(x) = f(x) - g(x), \\
&(f \cdot g)(x) = f(x) \cdot g(x), \\
&\left(\frac{f}{g}\right)(x) = \frac{f(x)}{g(x)}, \quad g(x) \neq 0, \\
&(f \circ g)(x) = f(g(x)).
\end{aligned}
$$

---

### Working Rule (Algorithm) to Perform Operations and Composition:

1. **Step 1:** Identify the domain common to both functions $ f $ and $ g $.  
2. **Step 2:** For addition, subtraction, multiplication, and division, apply the formulas directly for each $ x $ in the domain (exclude points where denominator is zero for division).  
3. **Step 3:** For composition $ f \circ g $, first compute $ g(x) $ for $ x $, then apply $ f $ to the result $ g(x) $.  
4. **Step 4:** Ensure the output $ g(x) $ lies in the domain of $ f $ to validate $ f(g(x)) $.  
5. **Step 5:** Write the resulting function explicitly, simplifying where possible.

---

### Graded Solved Examples

**Example 1 (Concept Building):**  
Let $ f(x) = x + 2 $ and $ g(x) = 3x $. Find $ (f+g)(x) $ and $ (f \circ g)(x) $.

**Solution:**  
**Step 1:** Add functions:  
$$
(f+g)(x) = (x + 2) + (3x) = 4x + 2.
$$  
**Step 2:** Compose functions:  
$$
(f \circ g)(x) = f(g(x)) = f(3x) = 3x + 2.
$$

---

**Example 2 (Competency Based):**  
Given $ f(x) = x^2 $ and $ g(x) = \sqrt{x} $, find $ \left(\frac{f}{g}\right)(4) $ and $ (g \circ f)(4) $.

**Solution:**  
**Step 1:** Compute $ \left(\frac{f}{g}\right)(4) $:  
$$
\frac{f(4)}{g(4)} = \frac{16}{2} = 8.
$$  
**Step 2:** Compute $ (g \circ f)(4) $:  
$$
g(f(4)) = g(16) = \sqrt{16} = 4.
$$

---

**Example 3 (HOTS):**  
Let $ f(x) = \frac{1}{x} $, $ g(x) = x - 1 $. Find the domain of $ \left(\frac{f}{g}\right)(x) $ and evaluate $ (f \circ g)(2) $.

**Solution:**  
**Step 1:** $ f(x) = \frac{1}{x} $ undefined at $ x=0 $, $ g(x) = x-1 $ defined for all real $ x $.  
**Step 2:** For $ \left(\frac{f}{g}\right)(x) = \frac{f(x)}{g(x)} = \frac{\frac{1}{x}}{x-1} = \frac{1}{x(x-1)} $, the domain excludes $ x=0 $ and $ x=1 $.  
**Step 3:** For composition:  
$$
(f \circ g)(2) = f(g(2)) = f(2 - 1) = f(1) = 1.
$$

---

This section clarifies fundamental operations on functions and ensures understanding of function compositions as functions themselves—crucial foundations for advanced mathematical studies.

---

## 2.8 Inverse Functions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Function and its Inverse on Cartesian Plane" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.8.0:</b> A function and its inverse reflected about the line <math>y = x</math></i></figcaption>
</figure>

### 2.8.1 Definition and Existence Conditions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder2" alt="Graph showing function and its inverse" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.8.1:</b> Illustration of the inverse function as reflection of the function about the line <math>y = x</math></i></figcaption>
</figure>

**Intuition:**  
An inverse function reverses the action of the original function. If a function $ f $ takes an element $ x $ and outputs $ y $, then its inverse $ f^{-1} $ takes $ y $ and returns the original $ x $. This "reversal" property works only if $ f $ uniquely pairs every input with a distinct output.

**Formal Definition:**  
Let $ f: A \to B $ be a function. The inverse function of $ f $, denoted by $ f^{-1} $, is a function $ f^{-1}: B \to A $ such that

$$
f(x) = y \iff f^{-1}(y) = x, \quad \forall x \in A, \forall y \in B.
$$

**Geometric Meaning:**  
On the Cartesian plane, the graph of $ f^{-1} $ is the reflection of the graph of $ f $ about the line $ y = x $. This means exchanging the roles of $ x $ and $ y $ coordinates in each point $ (x, y) $ on the graph of $ f $ gives a point $ (y, x) $ on the graph of $ f^{-1} $.

---

### 2.8.2 Theorem: Inverse Function Exists if and only if Function is Bijective

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder3" alt="Bijective function illustration" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.8.2:</b> Representation of injective, surjective, and bijective functions</i></figcaption>
</figure>

**Theorem:**  
$$
\boxed{
\text{A function } f: A \to B \text{ has an inverse function } f^{-1}: B \to A \text{ if and only if } f \text{ is bijective.}
}
$$

That is, $ f $ must be both **injective** (one-to-one) and **surjective** (onto).

**Proof:**

1. **(If part)**: Suppose $ f $ has an inverse $ f^{-1} $.  
   - To show $ f $ is injective:  
     Assume $ f(x_1) = f(x_2) = y $. Applying $ f^{-1} $ to both sides gives  
     $$
     f^{-1}(y) = f^{-1}(f(x_1)) = x_1,
     $$
     and similarly  
     $$
     f^{-1}(y) = f^{-1}(f(x_2)) = x_2.
     $$
     Therefore, $ x_1 = x_2 $, proving injectivity.

   - To show $ f $ is surjective:  
     For any $ y \in B $, since $ f^{-1} $ is defined on $ B $, there exists $ x = f^{-1}(y) \in A $ such that  
     $$
     f(x) = f(f^{-1}(y)) = y.
     $$
     Hence, $ f $ maps some $ x $ to every $ y $ in $ B $, proving surjectivity.

2. **(Only if part)**: Suppose $ f $ is bijective.  
   - Because $ f $ is injective, for every $ y \in B $ there is at most one $ x \in A $ with $ f(x) = y $.  
   - Because $ f $ is surjective, for every $ y \in B $ there is at least one $ x \in A $ with $ f(x) = y $.  
   Combining these, for each $ y \in B $, there exists a unique $ x \in A $ such that $ f(x) = y $. Define the inverse function $ f^{-1} $ by  
   $$
   f^{-1}(y) = x.
   $$
   This creates a well-defined function $ f^{-1}: B \to A $ that is the inverse of $ f $.

Thus, $ f $ is invertible if and only if it is bijective.

---

### 2.8.3 Formulas & Working Rule (Algorithm) to Find an Inverse Function

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder4" alt="Flowchart to find inverse function" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.8.3:</b> Algorithmic steps to find the inverse function</i></figcaption>
</figure>

**Key Formulas:**

If $ y = f(x) $ defines the function, then the inverse function $ x = f^{-1}(y) $ is found by solving the equation:

$$
y = f(x)
$$

for $ x $ in terms of $ y $. After this, rename the variable $ y $ as $ x $ in the expression to write $ f^{-1}(x) $ explicitly.

**Working Rule (Algorithm):**

1. **Step 1:** Write the equation for the function as $ y = f(x) $.  
2. **Step 2:** Interchange $ x $ and $ y $ symbols to reflect the reversal of roles:  
   $$
   x = f(y).
   $$
3. **Step 3:** Solve this new equation for $ y $ in terms of $ x $.  
4. **Step 4:** The resulting expression for $ y $ is $ f^{-1}(x) $.  
5. **Step 5:** Verify the inverse by checking that  
   $$
   f(f^{-1}(x)) = x \quad \text{and} \quad f^{-1}(f(x)) = x.
   $$

**Important Note:**  
Make sure the function is bijective over the domain and codomain; otherwise, the inverse function may not exist or may be defined on a restricted interval.

---

### 2.8.4 Graded Solved Examples

**Example 1 (Concept Building):**  
Find the inverse function of $ f(x) = 2x + 3 $.

**Solution:**

**Step 1:** Write $ y = 2x + 3 $.  
**Step 2:** Interchange $ x $ and $ y $:  
$$
x = 2y + 3.
$$  
**Step 3:** Solve for $ y $:  
$$
2y = x - 3 \implies y = \frac{x - 3}{2}.
$$  
**Step 4:** Hence,  
$$
f^{-1}(x) = \frac{x - 3}{2}.
$$  
**Step 5:** Verification:  
$$
f(f^{-1}(x)) = 2\left(\frac{x - 3}{2}\right) + 3 = x - 3 + 3 = x.
$$

---

**Example 2 (Competency Based):**  
Find the inverse of $ f(x) = \frac{3x - 4}{5} $ and state the domain and codomain of $ f^{-1} $ assuming $ f: \mathbb{R} \to \mathbb{R} $.

**Solution:**

**Step 1:** $ y = \frac{3x - 4}{5} $.  
**Step 2:** Interchange $ x $ and $ y $:  
$$
x = \frac{3y - 4}{5}.
$$  
**Step 3:** Multiply both sides by 5:  
$$
5x = 3y - 4 \implies 3y = 5x + 4 \implies y = \frac{5x + 4}{3}.
$$  
**Step 4:** Thus,  
$$
f^{-1}(x) = \frac{5x + 4}{3}.
$$  
**Domain and Codomain:**  
Since the original function was from $ \mathbb{R} \to \mathbb{R} $, its inverse function is also from $ \mathbb{R} \to \mathbb{R} $.

**Step 5:** Verify:  
$$
f(f^{-1}(x)) = \frac{3 \times \frac{5x + 4}{3} - 4}{5} = \frac{5x + 4 - 4}{5} = \frac{5x}{5} = x.
$$

---

**Example 3 (HOTS):**  
Let $ f(x) = \frac{2x + 1}{x - 3} $ with domain $ x \neq 3 $. Find $ f^{-1}(x) $ and state its domain.

**Solution:**

**Step 1:** Write $ y = \frac{2x + 1}{x - 3} $.  
**Step 2:** Interchange $ x $ and $ y $:  
$$
x = \frac{2y + 1}{y - 3}.
$$  
**Step 3:** Solve for $ y $:

Multiply both sides by $ y - 3 $:  
$$
x(y - 3) = 2y + 1 \implies xy - 3x = 2y + 1.
$$  
Bring all $ y $ terms to one side:  
$$
xy - 2y = 3x + 1 \implies y(x - 2) = 3x + 1.
$$  
Divide by $ x - 2 $ (provided $ x \neq 2 $):  
$$
y = \frac{3x + 1}{x - 2}.
$$  
**Step 4:** Therefore,  
$$
f^{-1}(x) = \frac{3x + 1}{x - 2}.
$$  
**Domain of $ f^{-1} $:**  
$ x \neq 2 $ (denominator cannot be zero).

**Step 5:** Verification:  

Compute $ f(f^{-1}(x)) $:

$$
f\left(\frac{3x + 1}{x - 2}\right) = \frac{2 \times \frac{3x + 1}{x - 2} + 1}{\frac{3x + 1}{x - 2} - 3} = \frac{\frac{2(3x + 1)}{x - 2} + 1}{\frac{3x + 1}{x - 2} - \frac{3(x - 2)}{x - 2}} = \frac{\frac{6x + 2}{x - 2} + 1}{\frac{3x + 1 - 3x + 6}{x - 2}}.
$$

Simplify numerator:  
$$
\frac{6x + 2}{x - 2} + 1 = \frac{6x + 2 + (x - 2)}{x - 2} = \frac{7x}{x - 2}.
$$

Simplify denominator:  
$$
\frac{3x + 1 - 3x + 6}{x - 2} = \frac{7}{x - 2}.
$$

Therefore,

$$
f(f^{-1}(x)) = \frac{\frac{7x}{x - 2}}{\frac{7}{x - 2}} = \frac{7x}{x - 2} \times \frac{x - 2}{7} = x.
$$

Hence verified.

---

**Remark:**  
Always check the domain restrictions to avoid values causing division by zero or outside the bijection range.

---

This completes the comprehensive study of inverse functions for Class 11 Mathematics.

---

## 2.9 Graphs of Functions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Graph of a function on Cartesian plane showing domain and range" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.9.0:</b> Graph of a function illustrating key points on the Cartesian plane</i></figcaption>
</figure>

### 2.9.1 Plotting Functions on Cartesian Plane

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Plotting linear, quadratic and trigonometric functions" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.9.1:</b> Sample graphs of linear, quadratic, and sine functions</i></figcaption>
</figure>

**Intuition:**  
Plotting a function on the Cartesian plane involves drawing the set of all points $(x, y)$ where $ y = f(x) $. This visually demonstrates the relationship between input values and their corresponding outputs, facilitating understanding of the function's behavior.

**Formal Definition:**  
Given a function $ f: A \to B $, the **graph** of $ f $ is the set of ordered pairs  
$$
\{(x, y) \in A \times B : y = f(x)\}
$$
plotted on the Cartesian coordinate plane defined by the $ x $ (horizontal) and $ y $ (vertical) axes.

**Geometric Meaning:**  
By plotting points $(x, f(x))$ on the plane and connecting them smoothly, we create a visual representation of the function’s behavior—intercept points, slope changes, maxima/minima, and other crucial traits become evident.

---

### 2.9.2 Graphical Interpretation of Domain and Range

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Graphical domain and range illustration" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.9.2:</b> Illustration of domain and range on the graph of $ y = x^2 $</i></figcaption>
</figure>

**Intuition:**  
The **domain** of a function corresponds to all possible $ x $-values for which $ f(x) $ is defined, while the **range** corresponds to all possible $ y $-values attained by $ f(x) $.

**Formal Understanding:**  
- **Domain:** Set of all $ x $ values on the horizontal axis for which $ (x, f(x)) $ is on the graph.  
- **Range:** Set of all $ y $ values on the vertical axis appearing as the ordinate of points on the graph.

**Geometric Meaning:**  
Graphically, the domain is visible as the horizontal span of the graph and the range as the vertical span.

**Examples:**

1. For $ f(x) = 2x + 1 $, the graph is a straight line extending infinitely both ways horizontally and vertically.  
   - Domain: $ (-\infty, \infty) $  
   - Range: $ (-\infty, \infty) $

2. For $ f(x) = x^2 $ (a parabola opening upwards), the domain spans all real $ x $, but the range is $ [0, \infty) $ since $ x^2 \geq 0 $.

3. For $ f(x) = \sin x $, domain is all real $ x $, but range is $ [-1, 1] $ as sine oscillates between these values.

---

### 2.9.3 Horizontal Line Test for One-One Functions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Horizontal line test visual illustration for parabola and line" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.9.3:</b> Horizontal Line Test: (left) parabola fails, (right) line passes</i></figcaption>
</figure>

**Theorem:**

$$
\boxed{
\text{A function } f \text{ is one-to-one (injective) if and only if every horizontal line intersects its graph at most once.}
}
$$

**Proof:**

1. Suppose $ f $ is one-to-one. By definition, if $ f(x_1) = f(x_2) $, then $ x_1 = x_2 $. Hence, no horizontal line $ y = k $ can intersect the graph of $ f $ in two distinct points $ (x_1, k) $ and $ (x_2, k) $ with $ x_1 \neq x_2 $. Thus, any horizontal line intersects the graph at most once.

2. Conversely, if no horizontal line cuts the graph more than once, then for any $ y = k $, there is at most one $ x $ such that $ f(x) = k $. This implies injectivity.

**Graphical Explanation:**

- For $ f(x) = x^2 $, the parabola opens upwards. A horizontal line at $ y = 1 $ meets it twice (points $ (-1, 1), (1, 1) $), so $ f $ is not one-to-one.

- For $ f(x) = x $, the line $ y = x $ is strictly increasing; any horizontal line meets it once, so $ f $ is one-to-one.

---

### 2.9.4 Formulas & Working Rule (Algorithm) for Graphing Functions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Graphing functions stepwise" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.9.4:</b> Stepwise method to graph various functions</i></figcaption>
</figure>

**Formulas:**

- $ y = mx + c $ (Linear function)  
- $ y = ax^2 + bx + c $ (Quadratic function)  
- $ y = \sin x $, $ y = \cos x $, $ y = \tan x $ (Trigonometric functions)  
- $ y = \frac{p(x)}{q(x)} $ (Rational functions)

**Working Rule (Algorithm) for Plotting Any Function:**

1. **Step 1:** Identify the type of function and its domain.  
2. **Step 2:** Find key features such as intercepts, vertices, and asymptotes (if any).  
3. **Step 3:** Create a table of values by selecting points of $ x $ and calculating $ f(x) $.  
4. **Step 4:** Plot the resultant points $ (x, f(x)) $ on the Cartesian plane.  
5. **Step 5:** Connect plotted points smoothly or with straight lines based on the function type.  
6. **Step 6:** Analyze the graph for domain and range visually, and apply the horizontal line test if checking injectivity.

---

### 2.9.5 Graded Solved Examples

**Example 1 (Concept Building): Plot $ f(x) = 2x + 1 $**

**Solution:**

- **Step 1:** Identify function type — linear.  
- **Step 2:** Find intercepts:  
  - $ x $-intercept: Set $ 2x + 1 = 0 \Rightarrow x = -\frac{1}{2} $.  
  - $ y $-intercept: $ f(0) = 1 $.  
- **Step 3:** Table of values:  
  $$
  \begin{array}{c|ccc}
  x & -1 & 0 & 1 \\
  \hline
  f(x) & -1 & 1 & 3
  \end{array}
  $$
- **Step 4:** Plot points $ (-1, -1), (0, 1), (1, 3) $.  
- **Step 5:** Connect points with a straight line.  
- **Step 6:** Domain and range are all real numbers.

---

**Example 2 (Competency Based): Plot $ f(x) = x^2 $ and determine domain and range**

**Solution:**

- **Step 1:** Quadratic function, domain $ (-\infty, \infty) $.  
- **Step 2:** Vertex at $ (0, 0) $, opens upwards.  
- **Step 3:** Points:  
  $$
  \begin{array}{c|ccccc}
  x & -2 & -1 & 0 & 1 & 2 \\
  \hline
  f(x) & 4 & 1 & 0 & 1 & 4 \\
  \end{array}
  $$
- **Step 4:** Plot points and draw a smooth curve opening upwards.  
- **Step 5:** Domain is all real numbers; range is $ [0, \infty) $.  
- **Step 6:** Horizontal line test fails; hence, function is not one-to-one.

---

**Example 3 (HOTS): Plot $ f(x) = \frac{1}{x-1} $ and analyze domain, range, and asymptotes**

**Solution:**

- **Step 1:** Rational function; domain excludes $ x = 1 $ because the denominator is zero there.  
- **Step 2:** Vertical asymptote at $ x = 1 $.  
- **Step 3:** Horizontal asymptote: as $ x \to \pm\infty $, $ f(x) \to 0 $.  
- **Step 4:** Table near the domain gap:  
  $$
  \begin{array}{c|cccc}
  x & 0.5 & 0.9 & 1.1 & 1.5 \\
  \hline
  f(x) & -2 & -10 & 10 & 2 \\
  \end{array}
  $$
- **Step 5:** Plot points and sketch graph with branches approaching the asymptotes.  
- **Step 6:** Domain: $ (-\infty, 1) \cup (1, \infty) $; Range: $ (-\infty, 0) \cup (0, \infty) $.

---

This section provides a rigorous, step-by-step understanding and application of plotting functions, interpreting domains and ranges from graphs, checking injectivity via the horizontal line test, and applying these to varied function types.

---

## 2.10 Binary Operations

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Representation of binary operation combining two elements" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.10.0:</b> Binary operation taking two elements from a set and producing another element of the set</i></figcaption>
</figure>

### 2.10.1 Definition of Binary Operations

**Intuition:**  
A binary operation is a rule that takes two elements from a set and combines them to produce another element, usually belonging to the same set. This idea generalizes common operations like addition and multiplication.

**Formal Definition:**  
Let $ A $ be a non-empty set. A **binary operation** on $ A $ is a function  
$$
* : A \times A \to A
$$
which assigns to each ordered pair $ (a, b) \in A \times A $ an element $ a * b $ in $ A $.

Here, $ A \times A $ is the Cartesian product of $ A $ with itself, i.e., the set of all ordered pairs of elements in $ A $.

**Geometric Meaning:**  
If we think of the set $ A $ as points in a plane or any geometric space, then a binary operation takes two points $ (a, b) $ and outputs a point $ c = a * b $ in the same space. This can be visualized as an "operation arrow" from the pair $ (a, b) $ to the element $ c $.

---

### 2.10.2 Examples and Verification on a Set

**Example 1: Addition on Integers**  
Let $ A = \mathbb{Z} $ (the set of all integers). Define $ + $ by  
$$
a + b = \text{sum of } a \text{ and } b.
$$  
Check this is a binary operation on $ \mathbb{Z} $:

- For any $ a, b \in \mathbb{Z} $, the sum $ a + b $ is also an integer.  
- Hence, $ + : \mathbb{Z} \times \mathbb{Z} \to \mathbb{Z} $ satisfies closure and is a binary operation.

---

**Example 2: Operation $ \star $ on set $ A = \{0,1,2\} $**  
Define  
$$
a \star b = (a + b) \bmod 3.
$$  
Check if $ \star $ is a binary operation on $ A $:

- For any $ a, b \in A $, $ (a + b) \bmod 3 \in \{0,1,2\} $ because modular arithmetic output is within this set.  
- Thus, $ \star : A \times A \to A $ is a binary operation.

---

**Example 3: Subtraction on Natural Numbers $ A = \mathbb{N} $**  
Define $ a \bullet b = a - b $. Check if this is a binary operation:

- Although $ a, b \in \mathbb{N} $, $ a - b $ may not be in $ \mathbb{N} $ if $ a < b $. For example, $ 2 - 3 = -1 \notin \mathbb{N} $.  
- Thus, subtraction is not a binary operation on $ \mathbb{N} $ as it is not closed.

---

**Verification Algorithm:**  
To verify a binary operation $*$ on $ A $:

1. **Step 1:** For arbitrary elements $ a, b \in A $, apply the operation $ a * b $.  
2. **Step 2:** Check if the result belongs to set $ A $.  
3. **Step 3:** If true for all pairs $ (a, b) $, then $*$ is a binary operation on $ A $; else, not.

---

### 2.10.3 Binary Operations as Functions from $ A \times A $ to $ A $

To understand binary operations rigorously, it is essential to see them as functions.

**Definition:**  
A binary operation $*$ on a set $ A $ is precisely a function  
$$
* : A \times A \to A,
$$
where $ A \times A $ is the domain (all ordered pairs of elements in $ A $) and $ A $ is the codomain.

That is, the operation takes inputs $ (a,b) $ and produces a single output $ a * b $ in $ A $.

**Geometric/Functional Interpretation:**  
This view treats the binary operation as a well-defined mapping from the plane $ A \times A $ (the set of input pairs) to the set $ A $ (outputs). This function perspective guarantees operations are consistent and predictable.

---

### 2.10.4 Theorems and Properties

**Theorem:**  
*If $*$ is a binary operation on a finite set $ A $, then the number of possible distinct binary operations on $ A $ is*  
$$
|A|^{|A|^{2}}.
$$

**Proof:**  

- Since $ A $ has $ n $ elements, $ |A| = n $.  
- The domain $ A \times A $ has $ n^2 $ ordered pairs.  
- Each ordered pair $ (a,b) $ must be mapped to one of $ n $ elements in $ A $.  
- Thus, the total number of functions $ A \times A \to A $ is $ n^{n^2} $.  
- Therefore, there are $ n^{n^{2}} $ binary operations on $ A $.

---

### 2.10.5 Working Rule (Algorithm) for Handling Binary Operations

1. **Step 1:** Identify the set $ A $ and the operation rule $*$.  
2. **Step 2:** Verify closure by checking if $ a * b \in A $ for all pairs $ (a,b) $.  
3. **Step 3:** For any computation, substitute given values into the operation definition.  
4. **Step 4:** For functional description, express $*$ as $*: A \times A \to A$.  
5. **Step 5:** To construct or analyze tables for finite $ A $, list all $ (a,b) $ pairs and their $ a * b $ value to verify the operation's features.

---

### 2.10.6 Graded Solved Examples

**Example 1 (Concept Building):**  
Given $ A = \{0,1\} $, define $ a * b = (a + b) \bmod 2 $. Is $*$ a binary operation on $ A $?

**Solution:**

- **Step 1:** Check pairs:  
  $(0,0): 0+0=0 \mod 2 = 0 \in A$.  
- **Step 2:** $(0,1): 0+1=1 \mod 2 = 1 \in A$.  
- **Step 3:** $(1,0): 1+0=1 \mod 2 = 1 \in A$.  
- **Step 4:** $(1,1): 1+1=2 \mod 2 = 0 \in A$.  
- **Step 5:** All outputs are in $ A $, so $*$ is a binary operation on $ A $.

---

**Example 2 (Competency Based):**  
Let $ A = \{0,1,2\} $. Define $ a \diamond b = (a \times b) \bmod 3 $. Verify closure and compute $ 2 \diamond 2 $.

**Solution:**

- **Step 1:** Closure: For any $ a,b \in A $, $ a \times b \in \{0,1,2,4,\ldots\} $. Modulo 3 brings the result back to $ A $.  
- **Step 2:** Calculate $ 2 \diamond 2 = (2 \times 2) \bmod 3 = 4 \bmod 3 = 1 $.  
- **Step 3:** Since all outcomes are in $ A $, closure holds and $ \diamond $ is a binary operation on $ A $.

---

**Example 3 (HOTS):**  
Let $ A = \{1, -1\} $ and define  
$$
a \star b = ab.
$$  
Is $*$ a binary operation on $ A $? Verify and find $ (-1) \star (-1) $.

**Solution:**

- **Step 1:** Check closure: product of elements of $ A $ is $ \pm 1 $, which remain in $ A $.  
- **Step 2:** $ (-1) \star (-1) = (-1) \times (-1) = 1 \in A $.  
- **Step 3:** Therefore, $*$ is a binary operation on $ A $.

---

This completes the rigorous introduction to binary operations, their definitions as functions, examples to verify closure, and higher-level insights into functional mappings on Cartesian products of sets.

---

## 2.11 Applications and Examples

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Visual representation of function applications and graphs" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 2.11.0:</b> Conceptual visualization of relations, functions, and their graphical interpretations</i></figcaption>
</figure>

### 2.11.1 Determining if a Relation is a Function

**Intuition:**  
A function is a special kind of relation where each input corresponds to exactly one output. Determining whether a given relation is a function involves checking the uniqueness of outputs for each input.

**Formal Definition:**  
A relation $ R $ from a set $ A $ to a set $ B $ is a **function** if for every $ a \in A $, there exists exactly one $ b \in B $ such that $ (a, b) \in R $.

**Geometric Meaning:**  
Graphically, a relation is a function if and only if any vertical line drawn through its graph intersects it at most once. This is known as the **vertical line test**.

---

**Working Rule (Algorithm) to Determine if a Relation is a Function:**

1. **Step 1:** Examine the given set of ordered pairs or the relation's graph.  
2. **Step 2:** For each input (x-coordinate), check if there is more than one output (y-coordinate).  
3. **Step 3:** If every input corresponds to exactly one output, the relation is a function; otherwise, it is not.

---

**Example 1 (Concept Building):**  
Given $ R = \{(1, 4), (2, 5), (3, 6)\} $, is $ R $ a function?

**Solution:**  
- Each input 1, 2, and 3 corresponds to exactly one output 4, 5, and 6 respectively.  
- Therefore, $ R $ is a function.

---

**Example 2 (Competency Based):**  
Given $ S = \{(1, 4), (1, 5), (2, 3)\} $, is $ S $ a function?

**Solution:**  
- Input 1 corresponds to two outputs, 4 and 5.  
- Hence, $ S $ is not a function.

---

### 2.11.2 Domain and Range Problem Solving

**Intuition:**  
The **domain** of a function is the set of all inputs for which the function is defined, while the **range** is the set of all possible outputs.

**Working Rule (Algorithm) to Find Domain and Range:**

1. **Step 1:** Identify restrictions like denominators being zero or square roots of negative numbers.  
2. **Step 2:** Express these restrictions as inequalities or equations to exclude invalid inputs for the domain.  
3. **Step 3:** For the range, analyze the behavior of the function and possible output values, either algebraically or graphically.

---

**Example 3 (Concept Building):**  
Find the domain and range of $ f(x) = \frac{2x+3}{x-4} $.

**Solution:**

- **Domain:** Denominator cannot be zero: $ x \neq 4 $, so  
  $$
  \text{Domain} = (-\infty, 4) \cup (4, \infty).
  $$  
- **Range:** The function can take all real values except possibly some value corresponding to a horizontal asymptote; for this function, all real values are possible.  
  $$
  \text{Range} = (-\infty, \infty).
  $$

---

**Example 4 (Competency Based):**  
Find the domain and range of $ g(x) = \sqrt{x - 1} $.

**Solution:**

- **Domain:** Under the square root must be non-negative:  
  $$
  x - 1 \geq 0 \implies x \geq 1.
  $$  
  So the domain is  
  $$
  [1, \infty).
  $$  
- **Range:** Square root outputs non-negative values, so  
  $$
  [0, \infty).
  $$

---

### 2.11.3 Composition and Inverse Function Problems

**Intuition:**  
Function composition combines two functions by applying one function to the result of another. The inverse function reverses the operation of a function.

**Working Rule (Algorithm) for Composition:**  
1. **Step 1:** Calculate the inner function $ g(x) $.  
2. **Step 2:** Substitute $ g(x) $ into $ f(x) $ to get $ f(g(x)) $.

**Working Rule (Algorithm) for Inverse Functions:**  
1. **Step 1:** Replace $ f(x) $ by $ y $.  
2. **Step 2:** Interchange $ x $ and $ y $.  
3. **Step 3:** Solve for $ y $.  
4. **Step 4:** Write the inverse function as $ f^{-1}(x) = y $.

---

**Example 5 (Concept Building):**  
Given $ f(x) = 2x + 3 $ and $ g(x) = x^2 $, find $ (f \circ g)(2) $.

**Solution:**  
- Calculate $ g(2) = 2^2 = 4 $.  
- Then, $ f(g(2)) = f(4) = 2 \times 4 + 3 = 11 $.  
Hence, $ (f \circ g)(2) = 11 $.

---

**Example 6 (Competency Based):**  
Find the inverse of $ f(x) = 3x - 5 $.

**Solution:**  
- Replace $ f(x) $ with $ y $:  
  $$
  y = 3x - 5.
  $$  
- Swap $ x $ and $ y $:  
  $$
  x = 3y - 5.
  $$  
- Solve for $ y $:  
  $$
  3y = x + 5 \implies y = \frac{x + 5}{3}.
  $$  
- So,  
  $$
  f^{-1}(x) = \frac{x + 5}{3}.
  $$

---

**Example 7 (HOTS):**  
If $ f(x) = 2x + 1 $, compute $ f^{-1}(f(3)) $.

**Solution:**

- Calculate $ f(3) = 2 \times 3 + 1 = 7 $.  
- Find $ f^{-1}(x) $:  
  $$
  y = 2x + 1 \implies x = 2y + 1 \implies y = \frac{x - 1}{2}.
  $$  
- Therefore,  
  $$
  f^{-1}(7) = \frac{7 - 1}{2} = 3.
  $$

---

### 2.11.4 Graphical Interpretation Exercises

**Intuition:**  
Graphical exercises help visualize functions, understand their behavior, and interpret their properties such as intercepts, increasing/decreasing behavior, and domains and ranges.

---

**Example 8 (Concept Building):**  
Graph the linear function $ y = 2x + 3 $.

**Solution:**

- Plot the $ y $-intercept $ (0, 3) $.  
- Use slope $ m = 2 $: from $ (0, 3) $, move up 2 units and right 1 unit to $ (1, 5) $.  
- Draw a line through these points.

---

**Example 9 (Competency Based):**  
Graph the inequality $ 3x + 2y < 6 $.

**Solution:**

- Draw the boundary line $ 3x + 2y = 6 $.  
- Find intercepts: $ (0,3) $, $ (2,0) $.  
- Since inequality is strict ($<$), use a dashed line.  
- Test point $ (0,0) $:  
  $$
  3(0) + 2(0) = 0 < 6,
  $$  
  so shade the region containing $ (0,0) $.

---

**Example 10 (HOTS):**  
Graph $ y = x^2 - 4 $.

**Solution:**

- Vertex at $ (0, -4) $.  
- Plot points $ (1, -3) $, $ (-1, -3) $, $ (2, 0) $, $ (-2, 0) $.  
- Sketch a smooth parabola opening upwards through these points.

---

This section equips students with essential problem-solving approaches in functions, focusing on verifying function properties, exploring domain and range, handling composition and inverse functions, and interpreting graphs.

---

