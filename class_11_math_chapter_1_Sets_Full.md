# Chapter 1: Sets

## 1.1 Introduction to Sets

### 1.1.1 Definition of a Set

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1hK4cZ12LphmuL1a_EofNo2fDEXi7v64i" alt="Venn Diagram Representing Sets" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.1:</b> Venn diagram illustrating sets and their relationships</i></figcaption>
</figure>

**Introduction:**  
In mathematics, a **set** is a fundamental concept representing a well-defined collection of distinct objects considered as a whole. Understanding sets is crucial as they form the foundation for many branches of mathematics, including algebra, calculus, and probability.

**Formal Definition:**  

A **set** is a collection of well-defined and distinct objects, called **elements** or **members** of the set. Sets are usually denoted by uppercase letters such as $ A $, $ B $, $ C $, and elements by lowercase letters such as $ a $, $ b $, $ c $.

If $ a $ is an element of set $ A $, it is denoted by  
$$
a \in A,
$$  
and if $ a $ is not an element of $ A $, it is denoted as  
$$
a \notin A.
$$

**Representation of Sets:**  

1. **Roster or Tabular Form:** Lists all the elements explicitly.  
   $$
   A = \{1, 2, 3, 4\}
   $$  
   Here, the set $ A $ contains the elements $ 1, 2, 3, $ and $ 4 $.

2. **Set-Builder Form:** Describes properties that characterize the elements of the set.  
   $$
   B = \{x : x \text{ is a natural number less than } 5 \}
   $$  
   This denotes the set of all natural numbers $ x $ such that $ x < 5 $, i.e., $ B = \{1, 2, 3, 4\} $.

**Geometric Meaning:**  

Geometrically, sets can be visualized using **Venn diagrams**, where each set is represented as a closed curve in a plane, and the elements of the set are points inside the curve. For example, a circle representing set $ A $ encloses all its elements as points inside it, and other points outside belong to the universal set $ U $ but not to $ A $.

---

### 1.1.2 Significance and Applications in Mathematics

**Introduction:**  

Sets are the building blocks in mathematics. They help structure various mathematical objects and form the language of modern mathematics. From defining numbers to describing complex spaces, the concept of sets enables us to systematically study collections of objects.

**Applications:**  

- **Functions and Relations:** Defined as sets of ordered pairs.  
- **Probability:** Events are represented as sets of outcomes.  
- **Algebra:** Groups, rings, and fields are sets with algebraic operations.  
- **Calculus:** Domains and ranges of functions are sets.  
- **Logic:** Truth values and propositions often correspond to sets in Boolean algebra.

Because sets can describe any collection of objects (numbers, points, symbols), they are universally applicable.

---

**Theorem 1: Uniqueness of a Set by Its Elements**

**Statement:** Two sets are equal if and only if they have exactly the same elements.

**Formally:**  
$$
A = B \iff (\forall x)(x \in A \iff x \in B).
$$

**Proof:**  

- **Step 1:** Suppose $ A = B $. Then by definition, every element of $ A $ is in $ B $ and vice versa. Hence,  
  $$
  \forall x, \quad x \in A \implies x \in B \quad \text{and} \quad x \in B \implies x \in A.
  $$

- **Step 2:** Conversely, assume  
  $$
  \forall x, \quad x \in A \iff x \in B.
  $$  
  This means every element of $ A $ is in $ B $ and every element of $ B $ is in $ A $. Therefore,  
  $$
  A = B.
  $$

Thus, the sets $ A $ and $ B $ are identical if and only if they contain the same elements.

---

**Important Types of Sets:**

- **Empty or Null Set:** The set with no elements, denoted by  
  $$
  \emptyset = \{\}.
  $$
- **Finite Set:** Has a limited number of elements, e.g., $ C = \{a, b, c\} $.  
- **Infinite Set:** Has infinitely many elements, e.g.,  
  $$
  N = \{1, 2, 3, \ldots\},
  $$
  the set of natural numbers.  
- **Universal Set:** Contains all elements under consideration, typically denoted as $ U $.

---

**Formulas & Working Rule for Set Operations:**

- **Union:**  
  $$
  A \cup B = \{x : x \in A \text{ or } x \in B\}
  $$
- **Intersection:**  
  $$
  A \cap B = \{x : x \in A \text{ and } x \in B\}
  $$
- **Difference:**  
  $$
  A - B = \{x : x \in A \text{ and } x \notin B\}
  $$
- **Subset:**  
  $$
  A \subseteq B \iff \forall x (x \in A \implies x \in B).
  $$

**Working Rule (Algorithm) to Solve Set Problems:**

1. **Step 1:** Identify all the sets involved and their elements or properties.  
2. **Step 2:** Determine the required operation (union, intersection, difference, subset test).  
3. **Step 3:** Apply the definition rigorously to list or describe elements of the resulting set.  
4. **Step 4:** Use Venn diagrams for visualization to check your results.  
5. **Step 5:** Verify if special cases apply, e.g., empty sets or universal sets.  
6. **Step 6:** Conclude by writing the final set explicitly or using set-builder notation.

---

### 1.1.3 Graded Solved Examples

**Example 1 (Concept Building):**  
Let $ A = \{1, 2, 3\} $ and $ B = \{2, 3, 4, 5\} $. Find $ A \cup B $, $ A \cap B $, and $ A - B $.

**Solution:**  
**Step 1:** List sets explicitly.  
$$
A = \{1, 2, 3\}, \quad B = \{2, 3, 4, 5\}
$$

**Step 2:** Compute union:  
$$
A \cup B = \{1, 2, 3, 4, 5\}
$$

**Step 3:** Compute intersection:  
$$
A \cap B = \{2, 3\}
$$

**Step 4:** Compute difference:  
$$
A - B = \{1\}
$$

---

**Example 2 (Competency Based):**  
If $ U = \{1, 2, 3, \ldots, 10\} $ is the universal set, $ A = \{2, 4, 6, 8, 10\} $, and $ B = \{1, 2, 3, 4, 5\} $, find $ (A \cup B)^c $ (complement of union).

**Solution:**  
**Step 1:** Calculate union $ A \cup B $:  
$$
A \cup B = \{1, 2, 3, 4, 5, 6, 8, 10\}
$$

**Step 2:** The complement $ (A \cup B)^c $ with respect to $ U $ contains elements in $ U $ but not in $ A \cup B $:  
$$
(A \cup B)^c = U - (A \cup B) = \{7, 9\}
$$

---

**Example 3 (HOTS):**  
Given  
$$
A = \{x : x \text{ is an integer and } 1 \leq x \leq 10\}
$$
and  
$$
B = \{x : x \text{ is an even integer}\},
$$
find $ A \cap B^c $ (elements in $ A $ but not in $ B $) and justify your answer.

**Solution:**  
**Step 1:** Write sets explicitly:  
$$
A = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}
$$

$$
B = \{\ldots, -4, -2, 0, 2, 4, 6, 8, 10, \ldots \} \quad \text{(even integers)}
$$

**Step 2:** Restrict $ B $ to elements in $ A $ (since only those are relevant):  
$$
B \cap A = \{2, 4, 6, 8, 10\}
$$

**Step 3:** Compute complement of $ B $ with respect to $ A $:  
$$
B^c = U - B
$$

Within $ A $, the complement $ B^c $ is the set of odd integers from 1 to 10:  
$$
B^c = \{1, 3, 5, 7, 9\}
$$

**Step 4:** Therefore,  
$$
A \cap B^c = \{1, 3, 5, 7, 9\}
$$

**Justification:** This is the set of all elements in $ A $ that are not even, precisely the odd integers from 1 to 10.

---

**Remarks:**  
Sets provide a powerful method for organizing elements and understanding their relationships. Mastery of sets lays the groundwork for advanced mathematical reasoning and problem-solving. Practice with a variety of problems to internalize operations and visualization techniques.

---

## 1.2 Representation of Sets

### 1.2.1 Roster or Tabular Form

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1ynLqmMJ7XF-ie1Q9pBCNpVbltObjB7vI" alt="Diagram illustrating roster and set-builder forms of sets" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.2:</b> Illustration of Roster form of sets</i></figcaption>
</figure>

**Introduction:**  

One of the simplest ways to represent a set is by listing all its elements explicitly. This method is called the **roster form** or **tabular form** of a set. It is straightforward and intuitive, especially useful for sets with a limited number of elements.

**Formal Definition:**  

In **roster form**, a set $ A $ is represented as a list of its elements enclosed in curly braces:  
$$
A = \{ a_1, a_2, a_3, \ldots, a_n \}
$$
where each $ a_i $ is an element of the set, and all elements are listed without repetition.

**Geometric Meaning:**  

Visually, the set $ A $ can be pictured as a collection of discrete points on a diagram or number line corresponding to the listed elements.

---

### 1.2.2 Set-Builder Form

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/12LrA1gjcPorhLKpyCFTWvCBjI_DMxrIN" alt="Diagram illustrating roster and set-builder forms of sets" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.3:</b> Illustration of Set-builder form of sets</i></figcaption>
</figure>

**Introduction:**  

When a set contains many elements or infinitely many elements, listing each element becomes impractical. Instead, such sets are often represented using **set-builder notation**, which defines the set by a property that all its elements share.

**Formal Definition:**  

A set $ B $ can be represented as:  
$$
B = \{ x : P(x) \}
$$
which reads as "set of all $ x $ such that property $ P(x) $ holds", where $ P(x) $ is a logical condition describing the elements of $ B $.

**Geometric Meaning:**  

Set-builder notation defines sets as regions or collections in space where elements satisfy the defining condition. For example, on the number line, the set of all real numbers greater than 2 can be represented as:  
$$
\{ x : x > 2 \}
$$
which corresponds to the ray starting at 2 and extending to infinity.

---

**Bold Text: Theorem 1: Uniqueness of Set Representation**

**Statement:**  

A set is completely determined by its elements, regardless of the form of representation.

Formally:  
$$
\text{If } A = \{ x : P(x) \} \text{ and } A = \{ a_1, a_2, \ldots, a_n \} \quad \Rightarrow \quad \text{every } a_i \text{ satisfies } P(x) \text{ and no others do.}
$$

**Proof:**  

- **Step 1:** Given $ A $ defined by property $ P(x) $, every element in $ A $ must satisfy $ P(x) $ by definition.

- **Step 2:** If set $ A $, represented by roster form $ \{ a_1, a_2, \ldots, a_n \} $, contains only elements satisfying $ P(x) $, there can be no element outside this list in the set.

- **Step 3:** As both sets have the same elements, they are equal by the axiom of extensionality for sets.  

Hence, the representation of sets via roster or set-builder forms uniquely defines the same set if and only if the elements match.

**Working Rule (Algorithm):**  

1. **Step 1:** Identify whether elements can be easily listed (finite sets) or whether a defining property is more suitable (infinite or large sets).  
2. **Step 2:** For finite sets, write the elements separated by commas inside curly braces (Roster form).  
3. **Step 3:** For sets characterized by a property:  
   - Choose a variable (usually $ x $) to represent elements.  
   - Write $ x : $ or $ x \mid $ meaning "such that".  
   - State the property $ P(x) $ defining the set.  
4. **Step 4:** Convert between forms when necessary:  
   - To move from roster to set-builder, identify a property all elements satisfy.  
   - To move from set-builder to roster, list all elements satisfying $ P(x) $ if the set is finite.  
5. **Step 5:** Use Venn diagrams or number lines to visualize sets aiding in understanding.

---

### 1.2.3 Graded Solved Examples

**Example 1 (Concept Building):**  
Represent the set of vowels in English alphabet in roster form and set-builder form.

**Solution:**  

**Step 1:** List vowels explicitly.  
$$
V = \{ a, e, i, o, u \}
$$

**Step 2:** Express using a property.  
$$
V = \{ x : x \text{ is a vowel in English alphabet} \}
$$

---

**Example 2 (Competency Based):**  
Write the set of even natural numbers less than 20 in roster and set-builder forms.

**Solution:**  

**Step 1:** List even natural numbers less than 20 (from 2 to 18):  
$$
E = \{ 2, 4, 6, 8, 10, 12, 14, 16, 18 \}
$$

**Step 2:** Write in set-builder form:  
$$
E = \{ x : x \text{ is a natural number}, x \text{ is even and } x < 20 \}
$$

---

**Example 3 (HOTS):**  
Represent the set of integers $ x $ such that $ -3 \leq x < 3 $ in both forms.

**Solution:**  

**Step 1:** List elements satisfying $ -3 \leq x < 3 $ with $ x $ integer:  
$$
S = \{ -3, -2, -1, 0, 1, 2 \}
$$

**Step 2:** Write the set-builder form:  
$$
S = \{ x : x \in \mathbb{Z}, -3 \leq x < 3 \}
$$

---

**Remarks:**  

Mastering both roster and set-builder representations of sets improves clarity in mathematical communication and problem-solving ability. When dealing with infinite or large sets, set-builder notation is especially valuable to avoid lengthy listings. Conversely, finite well-defined sets are easier to grasp with the roster form.

Understanding these representations is a cornerstone for learning more advanced set operations, functions, and relations.

---

## 1.3 The Empty Set

### 1.3.1 Definition and Notation

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1l3WHutGr2bISEfSbLTYbEHQclj05ggWC" alt="Geometric Representation of Empty Set in a Universal Set" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.4:</b> Geometric representation of the empty set as a subset of a universal set</i></figcaption>
</figure>

**Introduction:**  

Among the most fundamental concepts in set theory is the **empty set**, a set that contains no elements. Despite having no members, the empty set plays a vital role in the structure of mathematics.

**Formal Definition:**  

A set which contains **no elements** is called an **empty set** or **null set**. It is denoted by the symbol  
$$
\emptyset
$$
or by a pair of braces with nothing inside:  
$$
\{\}
$$

For any set $ A $, the statement $ x \in \emptyset $ is always false, reflecting that no element belongs to the empty set.

**Geometric Meaning:**  

Within the universal set $ U $, the empty set can be illustrated as a blank area with no points inside. On a Venn diagram, it is represented by an empty space or absence of any shaded region inside the universal set.

---

### 1.3.2 Properties of Empty Set

**Bold Text: Property 1: Uniqueness of the Empty Set**

**Statement:**  

There exists exactly one empty set.

**Proof:**  

- **Step 1:** Suppose there are two empty sets, say $\emptyset_1$ and $\emptyset_2$.  
- **Step 2:** Since by definition, neither set contains any elements,  
  $$
  \forall x,\, x \notin \emptyset_1 \quad \text{and} \quad x \notin \emptyset_2.
  $$
- **Step 3:** Thus, both sets contain exactly the same elements (none).  
- **Step 4:** By the axiom of extensionality in set theory, two sets with exactly the same elements are equal.  

Therefore,  
$$
\emptyset_1 = \emptyset_2,
$$
implying uniqueness.

---

**Bold Text: Property 2: The Empty Set is a Subset of Every Set**

**Statement:**  

For any set $ A $,  
$$
\emptyset \subseteq A.
$$

**Proof:**  

- **Step 1:** By definition, $ B \subseteq A $ means every element of $ B $ is in $ A $.  
- **Step 2:** But the empty set has no elements.  
- **Step 3:** As there is no element in $\emptyset$ to contradict the condition, the subset condition holds vacuously.  

Hence, the empty set is a subset of every set.

---

**Bold Text: Property 3: Intersection of any Set with Empty Set is Empty**

**Statement:**  

For any set $ A $,  
$$
A \cap \emptyset = \emptyset.
$$

**Proof:**  

- **Step 1:** An element $ x $ belongs to $ A \cap \emptyset $ only if $ x \in A $ and $ x \in \emptyset $.  
- **Step 2:** But no element is in $\emptyset$.  
- **Step 3:** Therefore, no element can belong to $ A \cap \emptyset $, so  
  $$
  A \cap \emptyset = \emptyset.
  $$

---

**Bold Text: Property 4: Union of any Set with Empty Set is the Set Itself**

**Statement:**  

For any set $ A $,  
$$
A \cup \emptyset = A.
$$

**Proof:**  

- **Step 1:** An element $ x $ belongs to $ A \cup \emptyset $ if $ x \in A $ or $ x \in \emptyset $.  
- **Step 2:** Since no element belongs to $\emptyset$, this means  
  $$
  x \in A \cup \emptyset \iff x \in A.
  $$
- **Step 3:** Hence,  
  $$
  A \cup \emptyset = A.
  $$

---

### 1.3.3 Role in Set Theory

The empty set is indispensable in mathematics and set theory for the following reasons:

- **Identity Element in Union:** It acts as the identity element for the union operation, meaning adding $\emptyset$ to any set does not change it.  
- **Absorbing Element in Intersection:** It absorbs every other set under intersection, resulting in $\emptyset$.  
- **Base Case for Definitions:** In recursive definitions, the empty set is the base case, e.g., for sequences of sets.  
- **Functions and Relations:** It represents the domain or range when no inputs or outputs exist.  
- **Cardinality:** The size or cardinality of $\emptyset$ is zero, denoted as  
  $$
  |\emptyset| = 0.
  $$
- **Foundation of Mathematical Logic:** The empty set underpins concepts in logic, including vacuous truth in proofs and statements.

---

**Formulas and Working Rule**

- **Notation:**  
  $$
  \emptyset = \{\}
  $$

- **Subset property:**  
  $$
  \emptyset \subseteq A, \quad \forall A
  $$

- **Intersection:**  
  $$
  A \cap \emptyset = \emptyset
  $$

- **Union:**  
  $$
  A \cup \emptyset = A
  $$

**Working Rule (Algorithm) to Approach Empty Set Problems:**  

1. **Step 1:** Identify if the question involves sets containing zero elements.  
2. **Step 2:** Use the fact that $\emptyset$ has no elements to evaluate subset, union, and intersection statements.  
3. **Step 3:** Apply vacuous truth for subset problems involving $\emptyset$.  
4. **Step 4:** Utilize the unique properties of union and intersection with $\emptyset$ to simplify expressions.  
5. **Step 5:** When needed, represent empty sets graphically as blank spaces within the universal set for visual understanding.  
6. **Step 6:** Confirm the cardinality of the empty set as zero when counting elements or comparing sizes.

---

### 1.3.4 Graded Solved Examples

**Example 1 (Concept Building):**  
Is the empty set a subset of the set $ A = \{3, 5, 7\} $?

**Solution:**  

**Step 1:** Recall that the empty set has no elements.

**Step 2:** To be a subset, every element of $\emptyset$ must be in $ A $.

**Step 3:** Since there are no elements in the empty set, there is no element to violate the condition.

**Conclusion:**  
$$
\emptyset \subseteq A.
$$

---

**Example 2 (Competency Based):**  
Find $ B \cap \emptyset $ where $ B = \{ x : x \text{ is a prime number less than } 10 \} $.

**Solution:**  

**Step 1:** The set $ B = \{ 2, 3, 5, 7 \} $.

**Step 2:** Intersection with the empty set involves finding elements common to both.

**Step 3:** Since no element is in $\emptyset$,  
$$
B \cap \emptyset = \emptyset.
$$

---

**Example 3 (HOTS):**  
Given $ U = \{1, 2, 3, 4, 5\} $ is the universal set, and $ A = \emptyset $, show that  
$$
A \subseteq B
$$
for every subset $ B $ of $ U $.

**Solution:**  

**Step 1:** Recall the definition of subset: $ A \subseteq B $ means every element of $ A $ belongs to $ B $.

**Step 2:** Since $ A $ is empty with no elements, there is no element to contradict the subset condition.

**Step 3:** Therefore, $\emptyset$ is a subset of every set $ B $ derived from $ U $.

---

**Remarks:**  

The empty set, though devoid of elements, is a foundational cornerstone of set theory and mathematics. Absorbing its properties and applying them correctly are essential for mastering more advanced topics. Always remember the vacuous truth principle when handling subsets involving the empty set.

---

## 1.4 Finite and Infinite Sets

### 1.4.1 Definition of Finite Sets

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1jOObT1De7xZ0TLVN-DgQi3K83C_M2Pj_" alt="Geometric Representation of Empty Set in a Universal Set" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.5:</b> Illustration of Finite Sets</i></figcaption>
</figure>

**Introduction:**  

Some sets contain a *countable* number of elements. These are called **finite sets**. Think of these as sets where you can list and count all their elements explicitly.

**Formal Definition:**  

A set $ A $ is said to be **finite** if the number of distinct elements in $ A $ is some non-negative integer $ n $. That is, the elements of $ A $ can be counted as  
$$
A = \{a_1, a_2, \ldots, a_n\}
$$
where $ n \geq 0 $. The number $ n $ is called the **cardinality** of $ A $, denoted by $ |A| = n $.

When $ n = 0 $, $ A $ is the **empty set**.

**Geometric Meaning:**  

Geometrically, in a finite set, the elements can be represented as isolated points in a space, such as points on a number line, with a limited number of points.

---

### 1.4.2 Definition of Infinite Sets

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/13HkOl2xjZTdWa4lLtlwL39FlHT79OuK7" alt="Geometric Representation of Empty Set in a Universal Set" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.6:</b> Illustration of Infinite Sets</i></figcaption>
</figure>

**Introduction:**  

Conversely, some sets have elements that never end; you cannot exhaustively list all their elements. Such sets are called **infinite sets**.

**Formal Definition:**  

A set $ B $ is called **infinite** if it is not finite; that is, it has infinitely many elements and its cardinality cannot be expressed as a finite integer. Formally, $ B $ is infinite if there exists a proper subset $ C \subset B $ such that $ C $ can be placed in one-to-one correspondence (bijection) with $ B $ itself.

**Geometric Meaning:**  

Geometrically, infinite sets can be thought of as a continuum of points, such as all points on a line segment or the entire number line extending infinitely in both directions.

---

**Bold Text: Theorem 1: Characterization of Infinite Sets via Proper Subsets**

**Statement:**  

A set $ S $ is infinite if and only if there exists a proper subset $ T \subset S $ such that $ S $ and $ T $ are in one-to-one correspondence.

**Proof:**  

- **Step 1:** Suppose $ S $ is infinite. Then it can be shown using the pigeonhole principle (or Cantor’s argument) that $ S $ has a proper subset $ T \subset S $ and a bijection $ f: S \to T $.

- **Step 2:** Conversely, if there exists a proper subset $ T \subset S $ such that $ S \cong T $ (bijection), then $ S $ cannot be finite because no finite set can be put into a bijection with its proper subset.

- **Step 3:** Hence, this property characterizes infinite sets.

---

### 1.4.3 Examples and Classification

**Examples of Finite Sets:**

1. $ A = \{1, 2, 3, 4\} $ with $ |A| = 4 $  
2. $ B = \{x : x \text{ is a vowel in English alphabet}\} = \{a, e, i, o, u\} $, $ |B| = 5 $  
3. The empty set $ \emptyset $, with $ |\emptyset| = 0 $

**Examples of Infinite Sets:**

1. $ \mathbb{N} = \{1, 2, 3, \ldots\} $, the set of natural numbers; clearly infinite.  
2. $ \mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\} $, the set of all integers; infinite as it extends in both directions.  
3. $ \mathbb{R} = \text{set of all real numbers} $, an uncountably infinite set.

---

**Formulas & Working Rule:**

- **Cardinality of finite set:**  
  $$
  |A| = n, \quad n \in \mathbb{N}_0
  $$

- **Definition of infinite set:**  
  $$
  \exists\, T \subset S, \quad T \neq S, \quad \text{and a bijection } f: S \to T.
  $$

**Working Rule (Algorithm) to Identify Finite/Infinite Sets and Solve Problems:**  

1. **Step 1:** Identify whether set elements can be explicitly listed (finite candidates).  
2. **Step 2:** Check if the number of elements is countable or uncountable.  
3. **Step 3:** For infinite candidate sets, verify if there is a proper subset with a bijection to the original set.  
4. **Step 4:** Use cardinality to classify finite sets by counting elements.  
5. **Step 5:** Use infinite set properties to solve problems, such as comparing infinite cardinalities or constructing bijections.

---

### 1.4.4 Graded Solved Examples

**Example 1 (Concept Building):**  
Is the set $ A = \{2, 4, 6, 8, 10\} $ finite or infinite?

**Solution:**  

**Step 1:** Explicitly count elements in $ A $.  
$$
A = \{2,4,6,8,10\} \implies |A| = 5
$$

**Step 2:** Since the cardinality is finite, $ A $ is a finite set.

---

**Example 2 (Competency Based):**  
Is the set $ B = \{x : x \text{ is an even natural number}\} $ finite or infinite?

**Solution:**  

**Step 1:** List first elements:  
$$
2, 4, 6, 8, \ldots
$$

**Step 2:** The sequence continues indefinitely with no end.

**Step 3:** Establish a bijection with natural numbers $ \mathbb{N} $, e.g., $ f(n) = 2n $.

**Step 4:** Because this is a bijection to a proper subset, $ B $ is infinite.

---

**Example 3 (HOTS):**  
Prove that the set of all multiples of 3, $ M = \{3, 6, 9, 12, \ldots\} $, is infinite by using the bijection method.

**Solution:**  

**Step 1:** Define the function $ f: \mathbb{N} \to M $ by $ f(n) = 3n $.

**Step 2:** Show $ f $ is one-to-one:  
If $ f(m) = f(n) $, then $ 3m = 3n \implies m = n $.

**Step 3:** Show $ f $ is onto:  
For any $ y \in M $, $ y = 3k $ for some $ k \in \mathbb{N} $, so $ y = f(k) $.

**Step 4:** Therefore, $ f $ is bijection, implying $ M $ is infinite as $ \mathbb{N} $ is infinite.

---

**Remarks:**  

Understanding the nature of finite and infinite sets, and the notion of cardinality, is crucial for more advanced studies in mathematics. Recognizing when a set is infinite by demonstrating bijections with proper subsets is a powerful tool. Practice constructing such correspondences for various infinite sets to master the concept.

---

## 1.5 Equal Sets

### 1.5.1 Conditions for Equality of Sets

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/11SSG1qXkJyMeY_5MaXeFPnJllgwNT0GK" alt="Venn Diagram Illustrating Equal Sets" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.7:</b> Venn diagram showing two equal sets with identical elements</i></figcaption>
</figure>

**Introduction:**  

In set theory, equality of sets is a foundational concept that states two sets are equal if they contain exactly the same elements. The order of elements or repetition does not matter.

**Formal Definition:**  

Two sets $ A $ and $ B $ are said to be **equal**, denoted $ A = B $, if every element of $ A $ is also an element of $ B $ and every element of $ B $ is also an element of $ A $. Formally,  
$$
A = B \iff \forall x \, (x \in A \iff x \in B).
$$
This means for **every** element $ x $, belonging to $ A $ is exactly equivalent to belonging to $ B $.

---

**Geometric Meaning:**  

In a Venn diagram, equal sets correspond to two circles overlapping perfectly such that every element inside one circle is also inside the other, indicating complete equality.

---

### 1.5.2 Theorems & Proofs

**Bold Text: Theorem 1 (Characterization of Equal Sets):**  
$$
A = B \iff A \subseteq B \text{ and } B \subseteq A.
$$

**Proof:**  

- **Step 1:** Assume $ A = B $. By definition, every element in $ A $ is in $ B $, so $ A \subseteq B $. Similarly, every element in $ B $ is in $ A $, so $ B \subseteq A $.

- **Step 2:** Conversely, assume $ A \subseteq B $ and $ B \subseteq A $.

- **Step 3:** If every element of $ A $ is in $ B $ and every element of $ B $ is in $ A $, then both sets have exactly the same elements.

- **Step 4:** Therefore, $ A = B $.

---

### 1.5.3 Formulas & Working Rule

- **Equality condition:**  
  $$
  A = B \iff (A \subseteq B) \land (B \subseteq A)
  $$

**Working Rule (Algorithm) to Prove Equality of Sets:**  

1. **Step 1:** To show $ A = B $, first prove $ A \subseteq B $:  
   Take an arbitrary element $ x \in A $. Show that $ x \in B $.

2. **Step 2:** Next, prove $ B \subseteq A $:  
   Take an arbitrary element $ y \in B $. Show that $ y \in A $.

3. **Step 3:** From these two subset relations, conclude $ A = B $.

---

### 1.5.4 Graded Solved Examples

**Example 1 (Concept Building):**  
Prove that $ A = \{1, 2, 3\} $ and $ B = \{3, 2, 1\} $ are equal.

**Solution:**  

- **Step 1:** Take $ x \in A $. Since $ A = \{1, 2, 3\} $, $ x $ is either 1, 2, or 3. All these are in $ B $.  
  
- **Step 2:** Take $ y \in B $. Since $ B = \{3, 2, 1\} $, $ y $ is either 3, 2, or 1. All these are in $ A $.  

- **Step 3:** Since $ A \subseteq B $ and $ B \subseteq A $, by the theorem, $ A = B $.

---

**Example 2 (Competency Based):**  
Let $ C = \{x : x \text{ is a prime number less than } 10\} $ and $ D = \{2, 3, 5, 7\} $. Prove $ C = D $.

**Solution:**  

- **Step 1:** Suppose $ x \in C $. By definition, $ x $ is a prime less than 10, so $ x \in \{2, 3, 5, 7\} = D $. Hence $ C \subseteq D $.

- **Step 2:** Take $ y \in D $. By $ D $'s construction, $ y $ is a prime less than 10, so $ y \in C $. Hence $ D \subseteq C $.

- **Step 3:** Therefore, $ C = D $.

---

**Example 3 (HOTS):**  
Let $ A = \{x : x^2 = 1\} $ and $ B = \{-1, 1\} $. Prove $ A = B $.

**Solution:**  

- **Step 1:** If $ x \in A $, then $ x^2 = 1 $, which implies $ x = 1 $ or $ x = -1 $. So $ x \in B $, thus $ A \subseteq B $.

- **Step 2:** If $ y \in B $, then $ y = -1 $ or $ y = 1 $. Thus $ y^2 = 1 $, so $ y \in A $, hence $ B \subseteq A $.

- **Step 3:** Thus, $ A = B $.

---

**Remarks:**  

Equality of sets is the fundamental equivalence relation in set theory, allowing us to identify when two sets represent the same collection of objects. Mastery of subset proofs is essential for rigorous problem-solving and further study in mathematics.

---

## 1.6 Subsets

### 1.6.1 Definition of Subsets

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1JjyYrgk-Zttf3o09zgcURsX2zQcp-mgr" alt="Venn Diagram Showing Relations of Subsets" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.8:</b> Visual representation of subsets </i></figcaption>
</figure>

**Introduction:**  

In set theory, the concept of a **subset** allows us to understand how one set can be contained within another. This helps organize sets in a hierarchy based on their elements.

**Formal Definition:**  

A set $ A $ is called a **subset** of a set $ B $, denoted by  
$$
A \subseteq B,
$$
if every element of $ A $ is also an element of $ B $. Formally,  
$$
A \subseteq B \iff \forall x \, (x \in A \implies x \in B).
$$

---

**Geometric Meaning:**  

Geometrically, we can illustrate $ A \subseteq B $ with a Venn diagram where all points representing elements of $ A $ lie inside the circle representing the set $ B $.

---

### 1.6.2 Proper and Improper Subsets

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/14YsUx8b--ZhCLXf1txsRiOXm0UT62q45" alt="Venn Diagram Showing Relations of Subsets" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.9:</b> Visual representation of subsets including proper and improper subsets</i></figcaption>
</figure>

**Proper Subset:**  

A set $ A $ is a **proper subset** of a set $ B $, denoted by  
$$
A \subset B,
$$
if $ A \subseteq B $ but $ A \neq B $. This means all elements of $ A $ are in $ B $, but $ B $ contains at least one element not in $ A $.

**Improper Subset:**  

If $ A = B $, then $ A $ is an **improper subset** of $ B $.

---

### 1.6.3 Empty Set as a Subset

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/19gZykW0Ay16DI5qAx5lJK3dKoo6jeQwV" alt="Venn Diagram Showing Relations of Subsets" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.10:</b> Visual representation of empty set as a subset of every set</i></figcaption>
</figure>

The **empty set**, denoted by $ \emptyset $, is a subset of every set. This is because there is no element in the empty set that violates the subset condition.

Formally,  
$$
\emptyset \subseteq A,
$$
for any set $ A $.

---

**Theorems & Proofs**

**Theorem 1:** The empty set is a subset of every set.

**Proof:**  

- **Step 1:** By definition, $ \emptyset $ contains no elements.  
- **Step 2:** To be a subset, every element of $ \emptyset $ must also be in $ A $.  
- **Step 3:** Since there are no elements in $ \emptyset $, the condition holds vacuously.  
- **Step 4:** Therefore,  
  $$
  \emptyset \subseteq A.
  $$

---

**Formulas & Working Rule**

- Subset condition:  
  $$
  A \subseteq B \iff \forall x (x \in A \implies x \in B)
  $$
- Proper subset condition:  
  $$
  A \subset B \iff (A \subseteq B) \land (A \neq B)
  $$

**Working Rule (Algorithm) to Check Subsets:**  

1. **Step 1:** For each element of $ A $, verify whether it is also in $ B $.  
2. **Step 2:** If all elements of $ A $ are in $ B $, conclude $ A \subseteq B $.  
3. **Step 3:** To check for proper subset, also verify $ A \neq B $.  
4. **Step 4:** To find the power set, list all subsets of $ A $, including $ \emptyset $ and $ A $ itself.

---

### 1.6.4 Graded Solved Examples

**Example 1 (Concept Building):**  
Verify if $ A = \{1, 2\} $ is a subset of $ B = \{1, 2, 3\} $.

**Solution:**  

- **Step 1:** Elements of $ A $ are 1 and 2.  
- **Step 2:** Both 1 and 2 are in $ B $.  

Thus,  
$$
A \subseteq B.
$$

---

**Example 2 (Competency Based):**  
Is $ A = \{1, 3\} $ a proper subset of $ B = \{1, 2, 3\} $?

**Solution:**  

- **Step 1:** Check if $ A \subseteq B $: Yes, both 1 and 3 are in $ B $.  
- **Step 2:** Compare $ A $ and $ B $: $ A \neq B $.  

Hence,  
$$
A \subset B.
$$

---

**Example 3 (HOTS):**  
Find the power set of $ C = \{x, y, z\} $ and state its cardinality.

**Solution:**  

- **Step 1:** List all subsets:  
  $$
  \emptyset, \{x\}, \{y\}, \{z\}, \{x,y\}, \{y,z\}, \{x,z\}, \{x,y,z\}
  $$
- **Step 2:** There are 8 subsets.

Thus,  
$$
P(C) = \{\emptyset, \{x\}, \{y\}, \{z\}, \{x,y\}, \{y,z\}, \{x,z\}, \{x,y,z\}\}, \quad |P(C)|=8.
$$

---

**Remarks:**  

Understanding subsets, including proper and improper ones, and the concept of power sets, is essential for grasping more complex mathematical structures and operations in set theory. Recognize the empty set’s pivotal role and how power sets expand the universe of subsets for a given set.

---

## 1.7 Power Set

### 1.7.1 Definition and Examples

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1OLT0I-98OdNr04WDKUOCp8UzdmpKMM7x" alt="Illustration of power set with subsets" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.11:</b> Visualization of the power set of a set with three elements</i></figcaption>
</figure>

**Introduction:**  

The **power set** extends the idea of subsets by collecting all possible subsets of a set—including the empty set and the set itself—into a new set. It is a fundamental concept in set theory and combinatorics.

**Formal Definition:**  

For any set $ S $, its **power set** $ P(S) $ is defined as the set of all subsets of $ S $:  
$$
P(S) = \{ A : A \subseteq S \}.
$$

**Examples:**

1. For $ S = \{a\} $,  
   $$
   P(S) = \{\emptyset, \{a\}\}.
   $$

2. For $ S = \{a, b\} $,  
   $$
   P(S) = \{\emptyset, \{a\}, \{b\}, \{a, b\}\}.
   $$

3. For $ S = \{1, 2, 3\} $,  
   $$
   P(S) = \{\emptyset, \{1\}, \{2\}, \{3\}, \{1, 2\}, \{1, 3\}, \{2, 3\}, \{1, 2, 3\}\}.
   $$

---

**Number of Subsets of a Set**

If a set $ S $ has $ n $ elements, the **number of subsets** of $ S $, equivalently the size of the power set, is:  
$$
|P(S)| = 2^n.
$$

This formula counts every possible subset combination, including the empty subset and $ S $ itself.

---

### 1.7.2 Relation to Cardinality

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1PIr8KsI91DsAXzrg9vAr_Ly_8MXq7u73" alt="Relation of Cardinality of Sets and Power Sets" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.12:</b> Relation of Cardinality of Sets and Power Sets</i></figcaption>
</figure>

**Cardinality of Sets and Power Sets:**  

Let $ |S| = n $ be the cardinality of set $ S $. Then:  
- The cardinality of the power set of $ S $ is $ |P(S)| = 2^n $.  
- This means the power set grows exponentially with the size of the original set.

**Geometric Meaning:**  

Visualizing power sets helps understand the increasing complexity of subsets as the size of the original set grows. Each element independently either is or is not part of a subset, creating $ 2^n $ combinations, akin to binary choices.

---

**Theorem 1: Cardinality of Power Set**

**Statement:**  

If a set $ S $ has $ n $ elements, the power set $ P(S) $ contains $ 2^n $ subsets.

**Proof:**  

- **Step 1:** Each element of $ S $ can either be included or excluded from a subset.  
- **Step 2:** Since each element has 2 choices, and there are $ n $ elements, total number of subsets is:  
  $$
  2 \times 2 \times \cdots \times 2 = 2^n.
  $$
- **Step 3:** Hence, the power set contains $ 2^n $ subsets.

---

**Formulas & Working Rule**

- **Power set:**  
  $$
  P(S) = \{A : A \subseteq S\}
  $$
- **Number of subsets (cardinality of $ P(S) $):**  
  $$
  |P(S)| = 2^{|S|}
  $$

**Working Rule (Algorithm) to Find Power Set:**  

1. **Step 1:** Identify all elements of the set $ S $.  
2. **Step 2:** List all subsets starting from empty set $ \emptyset $ to full set $ S $.  
3. **Step 3:** For each subset, determine all combinations of elements.  
4. **Step 4:** Count total subsets to verify it matches $ 2^n $.  
5. **Step 5:** Write the power set explicitly, ensuring all subsets are included.

---

### 1.7.3 Graded Solved Examples

**Example 1 (Concept Building):**  
Find the power set of $ S = \{a\} $.

**Solution:**  

- Subsets: $ \emptyset, \{a\} $  
- Therefore,  
  $$
  P(S) = \{\emptyset, \{a\}\}.
  $$
- Number of subsets $ = 2^1 = 2 $.

---

**Example 2 (Competency Based):**  
Find the power set of $ S = \{a, b\} $.

**Solution:**  

- Subsets: $ \emptyset, \{a\}, \{b\}, \{a, b\} $  
- Therefore,  
  $$
  P(S) = \{\emptyset, \{a\}, \{b\}, \{a, b\}\}.
  $$
- Number of subsets $ = 2^2 = 4 $.

---

**Example 3 (HOTS):**  
If $ S = \{1, 2, 3\} $, list the power set $ P(S) $ and count its number of subsets.

**Solution:**  

- Subsets:  
  $$
  \emptyset, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, \{1,2,3\}.
  $$

- The power set is:  
  $$
  P(S) = \{\emptyset, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, \{1,2,3\}\}.
  $$

- Number of subsets $ = 2^3 = 8 $.

---

**Remarks:**  

The concept of power sets is crucial as it reveals the combinatorial nature of sets and their subsets. Understanding power sets also leads to enhanced understanding of functions, relations, and counting principles, all pivotal topics in mathematics.

---

## 1.8 Universal Set

### 1.8.1 Definition and Usage

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1ltE2ek_efiu4UOf6ta98m49hqoFUtvFO" alt="Venn diagram showing universal set and subsets" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.13:</b> Venn diagram illustrating the universal set with subsets and complements</i></figcaption>
</figure>

**Introduction:**  

In set theory, the **universal set** serves as the complete universe under consideration for a given discussion. It contains all the elements relevant to the problem or context.

**Formal Definition:**  

The **universal set** $ U $ is the set that includes all possible elements under consideration. Every other set discussed in that context is a **subset** of $ U $. It is usually fixed for a particular discussion or problem.

---

**Geometric Meaning**

On a Venn diagram, the universal set is represented by a rectangle or enclosing boundary. All subsets lie inside this boundary.

---

**Relationship with Other Sets**

**Subsets:**  

For any subset $ A $ of the universal set $ U $,  
$$
A \subseteq U.
$$

**Complement of a Set:**  

The **complement** of a set $ A $, denoted by $ A' $ or $ A^c $, consists of all elements of $ U $ that are not in $ A $:  
$$
A' = U - A = \{x : x \in U \text{ and } x \notin A\}.
$$

---

### 1.8.2 Theorems & Proofs

**Bold Text: Theorem 1:** For any subset $ A $ of universal set $ U $,  
$$
A \cup A' = U \quad \text{and} \quad A \cap A' = \emptyset.
$$

**Proof:**  

- **Step 1:** Every element $ x \in U $ is either in $ A $ or not in $ A $.  
- **Step 2:** If $ x \in A $, then $ x \in A \cup A' $.  
- **Step 3:** If $ x \notin A $, then $ x \in A' $, hence $ x \in A \cup A' $.  
- **Step 4:** Thus, $ A \cup A' = U $.

- **Step 5:** By definition, no element is in both $ A $ and $ A' $.  
- **Step 6:** So, $ A \cap A' = \emptyset $.

---

**Formulas & Working Rule**

- **Complement of a set:**  
  $$
  A' = U - A
  $$

- **Union with complement:**  
  $$
  A \cup A' = U
  $$

- **Intersection with complement:**  
  $$
  A \cap A' = \emptyset
  $$

**Working Rule (Algorithm) to Solve Problems Involving Universal Set and Complements:**  

1. **Step 1:** Identify the universal set $ U $ relevant to the problem.  
2. **Step 2:** For a given subset $ A $, find elements in $ A $ and $ U \setminus A $ (complement).  
3. **Step 3:** Use properties of union and intersection with complements to simplify expressions.  
4. **Step 4:** Verify results with Venn diagrams when possible.  
5. **Step 5:** Apply formulas for probabilities or set operations involving complements.

---

### 1.8.3 Graded Solved Examples

**Example 1 (Concept Building):**  
Let $ U = \{1, 2, 3, 4, 5\} $, and $ A = \{2, 4\} $. Find the complement $ A' $.

**Solution:**  

- **Step 1:**  
  $$
  A' = U - A = \{1, 3, 5\}.
  $$

---

**Example 2 (Competency Based):**  
If $ U = \{1,2,3,4,5,6,7,8,9,10\} $, and $ B = \{1,3,5,7,9\} $, find $ B \cup B' $ and $ B \cap B' $.

**Solution:**  

- **Step 1:**  
  $$
  B' = U - B = \{2,4,6,8,10\}.
  $$
- **Step 2:**  
  $$
  B \cup B' = U
  $$
- **Step 3:**  
  $$
  B \cap B' = \emptyset
  $$

---

**Example 3 (HOTS):**  
Given $ U = \{a, b, c, d, e\} $, $ C = \{b, d\} $, find $ (C')' $.

**Solution:**  

- **Step 1:** First find  
  $$
  C' = U - C = \{a, c, e\}.
  $$
- **Step 2:** Then find complement of $ C' $:  
  $$
  (C')' = U - C' = \{b, d\} = C.
  $$

---

**Remarks:**  

The universal set concept and complement operation provide a powerful framework to analyze sets holistically. They are especially useful in probability, logic, and advanced set operations. Mastery of these concepts through practice is essential for students progressing in mathematics.

---

## 1.9 Venn Diagrams

### 1.9.1 Graphical Representation of Sets

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/10xUg5QTYKyIBs0A_SdZpbfs3f9I20K-U" alt="Venn diagram illustrating union, intersection, complement, and difference of sets" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.14:</b> Venn diagram showing the graphical representation of union, intersection, complement, and difference of sets A and B</i></figcaption>
</figure>

**Introduction:**  

Venn diagrams offer a powerful visual way to understand sets and their relationships. By representing sets as circles (or other shapes) within a universal space, these diagrams help visualize operations such as union, intersection, complement, and difference for clearer comprehension.

**Formal Definition:**  

A **Venn diagram** visually represents sets as areas within a universal set. For two sets $ A $ and $ B $, their relationship is depicted by two overlapping circles within a universal rectangle.

**Geometric Meaning:**  

- Each circle represents a set.  
- The overlap region illustrates intersection.  
- The union is the combined areas covered by both circles.  
- The area outside a circle within the rectangle represents the complement.

---

### 1.9.2 Union and Intersection Visualization

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1jSLbzSYPEx2ZT0MxSkuXdxwDpz0ukQQt" alt="Venn diagram illustrating union, intersection, complement, and difference of sets" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.15:</b> Venn diagram showing the graphical representation of union and intersection of sets A and B</i></figcaption>
</figure>

**Union of Sets $ A $ and $ B $:**  

The **union** $ A \cup B $ contains all elements that belong to $ A $, or $ B $, or both.

**Venn Diagram Representation:**  

The union is shown by shading both circles $ A $ and $ B $, including their overlapping part.

**Example:**  

Given $ A = \{1, 2, 3\} $ and $ B = \{3, 4, 5\} $,  
$$
A \cup B = \{1, 2, 3, 4, 5\}.
$$

---

**Intersection of Sets $ A $ and $ B $:**  

The **intersection** $ A \cap B $ contains all elements that belong to both $ A $ and $ B $.

**Venn Diagram Representation:**  

Only the overlapping region of circles $ A $ and $ B $ is shaded.

**Example:**  

With $ A $ and $ B $ as above,  
$$
A \cap B = \{3\}.
$$

---

### 1.9.3 Complement and Difference Representation

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1VK9zg2i2fEN4uCkb-NecxgBH2nwemG85" alt="Venn diagram illustrating union, intersection, complement, and difference of sets" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.16:</b> Venn diagram showing the graphical representation of complement and difference of sets A and B</i></figcaption>
</figure>

**Complement of a Set $ A $:**  

The **complement** $ A' $ consists of all elements in the universal set $ U $ that are **not** in $ A $.

**Venn Diagram Representation:**  

The area outside circle $ A $ but within the rectangle $ U $ is shaded.

**Example:**  

If $ U = \{1, 2, 3, 4, 5, 6\} $ and $ A = \{1, 3, 5\} $,  
$$
A' = \{2, 4, 6\}.
$$

---

**Difference of Sets $ A $ and $ B $:**  

The **difference** $ A - B $ is the set of elements in $ A $ but not in $ B $.

**Venn Diagram Representation:**  

Only the part of circle $ A $ outside the circle $ B $ is shaded.

**Example:**  

With $ A = \{1, 2, 3\} $, $ B = \{3, 4, 5\} $,  
$$
A - B = \{1, 2\}.
$$

---

**Bold Text: Theorems & Proofs**

**Theorem 1:** For any sets $ A $ and $ B $, the following hold:  

- $ A \cup B = B \cup A $ (Commutative Law)  
- $ A \cap B = B \cap A $ (Commutative Law)  
- $ A \cap (B \cup C) = (A \cap B) \cup (A \cap C) $ (Distributive Law)

**Proof Outline for Commutativity:**  

- To prove $ A \cup B = B \cup A $, note $ x \in A \cup B \iff x \in A \text{ or } x \in B $.  
- By the commutativity of "or", $ x \in B \text{ or } x \in A \iff x \in B \cup A $.  
- Hence, $ A \cup B = B \cup A $.

---

### 1.9.4 Formulas & Working Rule

- Union:  
  $$
  A \cup B = \{x : x \in A \text{ or } x \in B\}
  $$
- Intersection:  
  $$
  A \cap B = \{x : x \in A \text{ and } x \in B\}
  $$
- Complement:  
  $$
  A' = \{x : x \in U \text{ and } x \notin A\}
  $$
- Difference:  
  $$
  A - B = \{x : x \in A \text{ and } x \notin B\}
  $$

**Working Rule (Algorithm) to Use Venn Diagrams:**  

1. **Step 1:** Identify all sets involved and determine the universal set $ U $.  
2. **Step 2:** Draw circles representing each set within a rectangular universal set diagram.  
3. **Step 3:** Shade the area corresponding to the required operation (union, intersection, complement, difference).  
4. **Step 4:** Analyze the shaded area to write sets using set-builder or roster notation.  
5. **Step 5:** Validate your answers through logical reasoning or counting elements.

---

### 1.9.5 Graded Solved Examples

**Example 1 (Concept Building):**  
Draw a Venn diagram of sets $ A = \{1, 2, 3\} $ and $ B = \{3, 4, 5\} $. Shade $ A \cup B $.

**Solution:**  

- Shade both circles representing $ A $ and $ B $.  
- Elements in $ A \cup B $ are $ \{1, 2, 3, 4, 5\} $.

---

**Example 2 (Competency Based):**  
With the same sets, shade $ A \cap B $.

**Solution:**  

- Shade the overlapping section of $ A $ and $ B $ representing the element $ 3 $.  
- Thus, $ A \cap B = \{3\} $.

---

**Example 3 (HOTS):**  
If $ U = \{1, 2, 3, 4, 5, 6\} $, $ A = \{1, 2, 3\} $, $ B = \{3, 4, 5\} $, find and depict $ (A \cup B)' $.

**Solution:**  

- $ A \cup B = \{1, 2, 3, 4, 5\} $.  
- The complement $ (A \cup B)' = U - (A \cup B) = \{6\} $.  
- Shade area outside both $ A $ and $ B $ circles, representing the element $ 6 $.

---

**Remarks:**  

Venn diagrams bridge the gap between abstract sets and intuitive understanding. By mastering their construction and interpretation, students can effectively solve complex set problems involving unions, intersections, complements, and differences.

---

## 1.10 Operations on Sets

### 1.10.1 Union of Sets

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1-wPwpzhbFZMInVAJryrxFb9gbMDpB1-x" alt="Venn diagrams illustrating operations on sets" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.17:</b> Union of sets A and B</i></figcaption>
</figure>

**Introduction:**  

The **union** of two sets combines all elements from both sets into one, without repeating any elements.

**Formal Definition:**  

For sets $ A $ and $ B $,  
$$
A \cup B = \{ x : x \in A \text{ or } x \in B \}.
$$

**Geometric Meaning:**  

On a Venn diagram, $ A \cup B $ is represented by the total area covered by circles $ A $ and $ B $, including their overlap.

---

**Properties of Union:**

- **Commutative Law:**  
  $$
  A \cup B = B \cup A.
  $$
- **Associative Law:**  
  $$
  (A \cup B) \cup C = A \cup (B \cup C).
  $$
- **Identity Element:**  
  $$
  A \cup \emptyset = A.
  $$

**Proof of Commutative Law:**  
Assume $ x \in A \cup B $. Then $ x \in A $ or $ x \in B $, so $ x \in B \cup A $. Similarly, the other inclusion holds.

---

### 1.10.2 Intersection of Sets

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1YgDnyukLsMvKfcEG9YprcxAd2NNOw9qB" alt="Venn diagrams illustrating operations on sets" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.18:</b> Intersection of sets A and B</i></figcaption>
</figure>

**Introduction:**  

The **intersection** consists of elements common to both sets.

**Formal Definition:**  

For sets $ A $ and $ B $,  
$$
A \cap B = \{ x : x \in A \text{ and } x \in B \}.
$$

**Geometric Meaning:**  

On a Venn diagram, $ A \cap B $ is the overlap area between $ A $ and $ B $.

---

**Properties of Intersection:**

- **Commutative Law:**  
  $$
  A \cap B = B \cap A.
  $$
- **Associative Law:**  
  $$
  (A \cap B) \cap C = A \cap (B \cap C).
  $$
- **Absorption Law:**  
  $$
  A \cup (A \cap B) = A.
  $$

**Proof of Commutative Law:**  
If $ x \in A \cap B $, then $ x \in A $ and $ x \in B $, so $ x \in B \cap A $. The converse also holds.

---

### 1.10.3 Difference of Sets

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/10vTKz7VBqrfhlM4hB61-X1wCr9sbIPkr" alt="Venn diagrams illustrating operations on sets" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.19:</b> Difference of sets A and B</i></figcaption>
</figure>

**Definition:**  

The difference of two sets $ A $ and $ B $ is the set of elements in $ A $ that are not in $ B $.  
$$
A - B = \{ x : x \in A \text{ and } x \notin B \}.
$$

**Geometric Meaning:**  

This is the portion of $ A $ in the Venn diagram excluding the overlap with $ B $.

---

### 1.10.4 Complement of a Set

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1C8Jf-HABlwpNoMgcUOh4bbOub5anZE_7" alt="Venn diagrams illustrating operations on sets" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.20:</b> Complement of set A</i></figcaption>
</figure>

**Definition:**  

Given the universal set $ U $ containing $ A $, the complement of $ A $ is the set of elements in $ U $ not in $ A $.  
$$
A' = U - A = \{ x : x \in U \text{ and } x \notin A \}.
$$

**Geometric Meaning:**  

The region outside $ A $ in the Venn diagram representing $ U $.

---

### 1.10.5 De Morgan's Laws

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1DTr-UG32KmgfbiEAAcrF-bny39CTT8J-" alt="Venn diagrams illustrating operations on sets" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.21:</b> De Morgan's Laws</i></figcaption>
</figure>

**Theorem:**  

For any subsets $ A, B $ of a universal set $ U $:  
$$
(A \cup B)' = A' \cap B',
$$
$$
(A \cap B)' = A' \cup B'.
$$

**Proof of First Law:**  

- **Step 1:** Let $ x \in (A \cup B)' $, so $ x \notin A \cup B $.  
- **Step 2:** Then $ x \notin A $ and $ x \notin B $.  
- **Step 3:** Hence $ x \in A' $ and $ x \in B' $, so $ x \in A' \cap B' $.  
- **Step 4:** Conversely, if $ x \in A' \cap B' $, then $ x \notin A $ and $ x \notin B $, so $ x \notin A \cup B $.  
- **Step 5:** Therefore, $ (A \cup B)' = A' \cap B' $.

---

**Formulas & Working Rule**

- Union:  
  $$
  A \cup B = \{x : x \in A \text{ or } x \in B\}
  $$
- Intersection:  
  $$
  A \cap B = \{x : x \in A \text{ and } x \in B\}
  $$
- Difference:  
  $$
  A - B = \{x : x \in A \text{ and } x \notin B\}
  $$
- Complement:  
  $$
  A' = U - A
  $$
- De Morgan's laws:  
  $$
  (A \cup B)' = A' \cap B', \quad (A \cap B)' = A' \cup B'
  $$

**Working Rule (Algorithm):**

1. Step 1: Identify the universal set and all given subsets.  
2. Step 2: Apply the set operation definition to find elements satisfying the condition.  
3. Step 3: Use Venn diagrams to visualize complex operations.  
4. Step 4: For complements, ensure knowledge of universal set.  
5. Step 5: Apply De Morgan's laws when simplifying complements of unions or intersections.  
6. Step 6: Check results by analyzing set membership conditions.

---

### 1.10.6 Graded Solved Examples

**Example 1 (Concept Building):**  

Given $ A = \{1, 2, 3\} $, $ B = \{3, 4, 5\} $, find $ A \cup B $.

**Solution:**  
$$
A \cup B = \{1, 2, 3, 4, 5\}.
$$

---

**Example 2 (Competency Based):**  

For the same $ A $ and $ B $, find $ A \cap B $.

**Solution:**  
$$
A \cap B = \{3\}.
$$

---

**Example 3 (HOTS):**  

If $ U = \{1, 2, 3, 4, 5, 6\} $, $ A = \{1, 2, 3\} $, $ B = \{3, 4, 5\} $, find $ (A \cup B)' $.

**Solution:**  
$$
A \cup B = \{1, 2, 3, 4, 5\},
$$
$$
(A \cup B)' = U - (A \cup B) = \{6\}.
$$

---

**Remarks:**  

Understanding set operations and De Morgan's laws forms a cornerstone for higher studies in mathematics and logical reasoning. Careful application of definitions and proofs enhances problem-solving skills.

---

## 1.11 Properties of Set Operations

### 1.11.1 Commutative Laws

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1FxWemTZQi6uDZ35R-xpdkenuHBVkmPEC" alt="Venn Diagrams illustrating properties of set operations" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.22:</b> Commutative laws of set operations</i></figcaption>
</figure>

**Definition:**  

The order of sets in union and intersection operations does not change the result.

- For union:  
  $$
  A \cup B = B \cup A
  $$
- For intersection:  
  $$
  A \cap B = B \cap A
  $$

**Proof:**  

- Let $ x $ be an arbitrary element.  
- If $ x \in A \cup B $, then $ x \in A $ or $ x \in B $, which means $ x \in B \cup A $.  
- Similarly for intersection, $ x \in A \cap B \implies x \in A $ and $ x \in B $, so $ x \in B \cap A $.

---

### 1.11.2 Associative Laws

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1aiVPfCIoUdbMBM2GoD542NWeBteJBQTM" alt="Venn Diagrams illustrating properties of set operations" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.23:</b> Associative laws of set operations</i></figcaption>
</figure>

**Definition:**  

The grouping of sets in union and intersection operations does not change the result.

- For union:  
  $$
  (A \cup B) \cup C = A \cup (B \cup C)
  $$
- For intersection:  
  $$
  (A \cap B) \cap C = A \cap (B \cap C)
  $$

**Proof:**  

- For union, if $ x \in (A \cup B) \cup C $, then $ x \in A $, or $ x \in B $, or $ x \in C $, which is the same as $ x \in A \cup (B \cup C) $.

- The argument is similar for intersection with "and" replacing "or".

---

### 1.11.3 Distributive Laws

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1NM2SqIFHBkoEq_lnlo_6WOzsoZd9K9Ii" alt="Venn Diagrams illustrating properties of set operations" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.24:</b> Distributive laws of set operations</i></figcaption>
</figure>

**Definition:**  

Union distributes over intersection and vice versa.

- Union over intersection:  
  $$
  A \cup (B \cap C) = (A \cup B) \cap (A \cup C)
  $$
- Intersection over union:  
  $$
  A \cap (B \cup C) = (A \cap B) \cup (A \cap C)
  $$

**Proof:**  

- First, show $ A \cup (B \cap C) \subseteq (A \cup B) \cap (A \cup C) $ by considering an element $ x \in A \cup (B \cap C) $ and deducing that $ x $ belongs to both $ A \cup B $ and $ A \cup C $.

- Second, show reverse inclusion by taking $ x \in (A \cup B) \cap (A \cup C) $ and demonstrating $ x \in A \cup (B \cap C) $.

---

### 1.11.4 Identity Laws

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/15i0fV6bY2VBsDixRo8Z2UtG1huBEB1H5" alt="Venn Diagrams illustrating properties of set operations" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.25:</b> Identity laws of set operations</i></figcaption>
</figure>

**Definition:**  

The union or intersection with identity elements leaves a set unchanged.

- Union with empty set:  
  $$
  A \cup \emptyset = A
  $$
- Intersection with universal set $ U $:  
  $$
  A \cap U = A
  $$

**Proof:**  

- Since $ \emptyset $ contains no elements, union with it adds nothing new.

- Universal set contains all elements, so intersection with it retains $ A $.

---

### 1.11.5 Complement Laws

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1DSjG6LzMTnR7rdD3xDlBg--IaE63HLkU" alt="Venn Diagrams illustrating properties of set operations" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.26:</b> Complement laws of set operations</i></figcaption>
</figure>

**Definition:**  

The complement of a set relates to the universal set and the empty set.

- Complement of universal set:  
  $$
  U' = \emptyset
  $$
- Complement of empty set:  
  $$
  \emptyset' = U
  $$

**Proof:**  

- The universal set contains all elements, so nothing exists outside it.

- The empty set has no elements; hence, all elements of $ U $ are outside the empty set.

---

**Formulas & Working Rule:**

- **Commutative Laws:**  
  $$
  A \cup B = B \cup A, \quad A \cap B = B \cap A
  $$
- **Associative Laws:**  
  $$
  (A \cup B) \cup C = A \cup (B \cup C), \quad (A \cap B) \cap C = A \cap (B \cap C)
  $$
- **Distributive Laws:**  
  $$
  A \cup (B \cap C) = (A \cup B) \cap (A \cup C), \quad A \cap (B \cup C) = (A \cap B) \cup (A \cap C)
  $$
- **Identity Laws:**  
  $$
  A \cup \emptyset = A, \quad A \cap U = A
  $$
- **Complement Laws:**  
  $$
  U' = \emptyset, \quad \emptyset' = U
  $$

**Working Rule (Algorithm):**  

1. Step 1: Identify the sets and operations involved.  
2. Step 2: Use the respective law to rewrite or simplify set expressions.  
3. Step 3: Verify results using membership and element logic.  
4. Step 4: For proofs, demonstrate set inclusions both ways.  
5. Step 5: Apply Venn diagrams to visually confirm properties.

---

### 1.11.6 Graded Solved Examples

**Example 1 (Concept Building):**  
Prove $ A \cup B = B \cup A $ for $ A = \{1, 3\} $, $ B = \{2, 3\} $.

**Solution:**  

- Step 1: $ A \cup B = \{1, 2, 3\} $.

- Step 2: $ B \cup A = \{2, 1, 3\} = \{1, 2, 3\} $.

- Step 3: Set equality holds by element comparison.

---

**Example 2 (Competency Based):**  
Prove distributive law $ A \cup (B \cap C) = (A \cup B) \cap (A \cup C) $ for $ A=\{1\}, B=\{1,2\}, C=\{1,3\} $.

**Solution:**  

- Step 1: Compute $ B \cap C = \{1\} $.

- Step 2: Compute $ A \cup (B \cap C) = \{1\} $.

- Step 3: Compute $ (A \cup B) \cap (A \cup C) = \{1,2\} \cap \{1,3\} = \{1\} $.

- Step 4: Both sides equal $ \{1\} $, proving the law.

---

**Example 3 (HOTS):**  
Show that $ (A \cap B)^c = A^c \cup B^c $.

**Solution:**  

- Step 1: Use the definitions of complement, union, and intersection.

- Step 2: Use element-wise reasoning to prove both inclusions.

- Step 3: Conclude equality by mutual subset relations (De Morgan's law).

---

**Remarks:**  

Mastering these properties and their proofs equips students for deeper set theory concepts and mathematical problem-solving. Visual aids paired with rigorous logic enhance comprehension and application.

---

## 1.12 Cardinality of Sets

### 1.12.1 Definition of Cardinality

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1WpPQr8-4JpYQU2CbUnE5PkonbIExKDPx" alt="Venn diagram illustrating cardinality of sets and their operations" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.27:</b> cardinality of sets</i></figcaption>
</figure>

**Introduction:**  

The **cardinality** of a set quantifies the number of elements in that set. It provides a numerical measure of the size of the set, whether finite or infinite.

**Formal Definition:**  

For any set $ A $, the **cardinality** of $ A $, denoted $ |A| $, is defined as the number of distinct elements in $ A $.

- If $ A $ is finite with elements $ a_1, a_2, \ldots, a_n $, then  
  $$
  |A| = n.
  $$

- If $ A $ is infinite, its cardinality is not a finite number (this section focuses on finite sets).

**Geometric Meaning:**  

Cardinality corresponds to the count of points representing elements on the graph or diagram of the set.

---

### 1.12.2 Cardinality of Finite Sets

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1AafOB2pV4CEoXBs6k_8CIJLyunMUs6hV" alt="Venn diagram illustrating cardinality of sets and their operations" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.28:</b> cardinality of finite sets</i></figcaption>
</figure>

A **finite set** is a set with a countable number of elements.

- **Example:**  
  $ A = \{1, 3, 5, 7\} $ has cardinality $ |A| = 4 $.

- The empty set $ \emptyset $ has cardinality zero:  
  $$
  |\emptyset| = 0.
  $$

---

**Formula for Cardinality of Union of Two Sets:**

**Theorem (Cardinality of Union):**  

For any two finite sets $ A $ and $ B $,  
$$
|A \cup B| = |A| + |B| - |A \cap B|.
$$

**Proof:**  

- **Step 1:** Start with the total number of elements in $ A $ and $ B $:  
  $$
  |A| + |B|.
  $$

- **Step 2:** Elements in $ A \cap B $ are counted twice (once in $ |A| $, once in $ |B| $).

- **Step 3:** Subtract $ |A \cap B| $ to correct double counting:  
  $$
  |A \cup B| = |A| + |B| - |A \cap B|.
  $$

---

### 1.12.3 Formula for Cardinality of Difference of Sets

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1AowFjpuzCvk4ial_1qa-p5IgRUNE_9Sv" alt="Venn diagram illustrating cardinality of sets and their operations" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.29:</b> cardinality of difference of sets</i></figcaption>
</figure>

**Theorem (Cardinality of Difference):**  

For finite sets $ A $ and $ B $,  
$$
|A - B| = |A| - |A \cap B|.
$$

**Proof:**  

- **Step 1:** The difference $ A - B $ consists of elements in $ A $ not in $ B $.

- **Step 2:** The elements counted in $ A \cap B $ overlap with $ B $.

- **Step 3:** Removing these gives:  
  $$
  |A - B| = |A| - |A \cap B|.
  $$

---

**Formulas & Working Rule**

- Cardinality of union:  
  $$
  |A \cup B| = |A| + |B| - |A \cap B|
  $$
- Cardinality of difference:  
  $$
  |A - B| = |A| - |A \cap B|
  $$

**Working Rule (Algorithm) to Find Cardinalities:**  

1. **Step 1:** Identify the elements and count elements in $ A $, $ B $, and $ A \cap B $.  
2. **Step 2:** Apply the formula for union or difference, depending on the operation.  
3. **Step 3:** Use Venn diagrams to visualize to avoid double counting.  
4. **Step 4:** Calculate the correct cardinality value.

---

### 1.12.4 Graded Solved Examples

**Example 1 (Concept Building):**  
Find the cardinality of the set $ A = \{1, 2, 3, 4\} $.

**Solution:**  
Since $ A $ has four elements,  
$$
|A| = 4.
$$

---

**Example 2 (Competency Based):**  
For $ A = \{1, 2, 3\} $, $ B = \{3, 4, 5\} $, find $ |A \cup B| $.

**Solution:**  
Calculate:  
- $ |A| = 3 $,  
- $ |B| = 3 $,  
- $ |A \cap B| = |\{3\}| = 1 $.  

Apply formula:  
$$
|A \cup B| = 3 + 3 - 1 = 5.
$$

---

**Example 3 (HOTS):**  
Given $ A = \{a, b, c, d\} $, $ B = \{c, d, e, f\} $, find $ |A - B| $.

**Solution:**  
- $ |A| = 4 $,  
- $ |A \cap B| = |\{c, d\}| = 2 $.  

Applying formula:  
$$
|A - B| = 4 - 2 = 2.
$$

---

**Remarks:**  

Mastering cardinality fundamentals is vital for solving more complex set theory problems, including those involving multiple sets and operations. Understanding and applying counting methods with care prevents errors such as double counting.

---


## 1.13 Chapter Summary

### 1.13.1 Summary

In this chapter, we studied the foundational concept of **Sets**, which forms the language and structural basis of modern mathematics. Sets allow us to organize, classify, and analyze collections of objects systematically. Nearly every advanced topic in mathematics—such as functions, relations, probability, algebra, and calculus—relies on set-theoretic ideas.

We began with the **definition of a set** as a well-defined collection of distinct objects called elements. Sets are usually denoted by capital letters such as $A$, $B$, and $C$, while elements are written in lowercase. The membership of an element in a set is expressed using the symbol:

$$
a \in A
$$

and non-membership by:

$$
a \notin A.
$$

Two main methods of representing sets were introduced:

1. **Roster (Tabular) Form**, where elements are explicitly listed.
2. **Set-Builder Form**, where elements are described using a defining property.

These representations help us describe both finite and infinite collections efficiently.

We then studied important types of sets. The **empty set**, denoted by:

$$
\emptyset,
$$

is the set containing no elements. Despite having no elements, it plays a crucial role in set theory. It is unique and is a subset of every set:

$$
\emptyset \subseteq A.
$$

We also examined **finite sets**, which have a limited number of elements, and **infinite sets**, which contain endlessly many elements. The concept of **cardinality**, denoted by $|A|$, measures the number of elements in a finite set. Infinite sets cannot be counted in a finite manner and exhibit unique structural properties.

The concept of **equality of sets** was established through the principle:

$$
A = B \iff A \subseteq B \text{ and } B \subseteq A.
$$

Two sets are equal if and only if they contain exactly the same elements, regardless of order or repetition.

Next, we studied **subsets**. A set $A$ is a subset of $B$ if every element of $A$ belongs to $B$:

$$
A \subseteq B.
$$

If $A \subseteq B$ but $A \neq B$, then $A$ is called a **proper subset** of $B$. The empty set is a subset of every set, and every set is a subset of itself (improper subset).

An important extension of subsets is the **power set**. The power set of a set $S$, denoted by:

$$
P(S),
$$

is the set of all subsets of $S$. If $|S| = n$, then the number of elements in its power set is:

$$
|P(S)| = 2^n.
$$

This exponential growth reflects the combinatorial richness of subsets.

We then introduced the concept of the **universal set**, denoted by $U$, which contains all elements under consideration in a given context. Every set discussed is assumed to be a subset of the universal set. The **complement** of a set $A$ with respect to $U$ is:

$$
A' = U - A
$$

We established two fundamental complement properties:

$$
A \cup A' = U
$$

$$
A \cap A' = \emptyset.
$$

To visually understand these relationships, we studied **Venn diagrams**, which represent sets as regions within a universal boundary. These diagrams help interpret operations such as union, intersection, difference, and complement graphically.

The four primary operations on sets were studied in detail:

- **Union:**
  $$
  A \cup B = \{x : x \in A \text{ or } x \in B\}
  $$

- **Intersection:**
  $$
  A \cap B = \{x : x \in A \text{ and } x \in B\}
  $$

- **Difference:**
  $$
  A - B = \{x : x \in A \text{ and } x \notin B\}
  $$

- **Complement:**
  $$
  A' = U - A.
  $$

We also studied the **algebra of sets**, including important laws:

- **Commutative Laws**
- **Associative Laws**
- **Distributive Laws**
- **Identity Laws**
- **Absorption Laws**
- **De Morgan’s Laws**

De Morgan’s Laws are especially important:

$$
(A \cup B)' = A' \cap B'
$$

$$
(A \cap B)' = A' \cup B'.
$$

These identities allow simplification of complex set expressions and are widely used in probability and logic.

Throughout the chapter, emphasis was placed on logical reasoning, subset proofs, visualization through diagrams, and step-by-step solution methods. The working rules provided systematic procedures to approach set problems accurately.

In conclusion, the study of sets equips us with a precise language to describe collections and relationships. Concepts such as subsets, power sets, complements, and operations form the foundation for advanced mathematical structures. Mastery of this chapter ensures strong conceptual clarity and prepares students for further topics such as relations, functions, probability, and algebraic structures.

Understanding sets is not merely about memorizing definitions—it is about developing logical thinking and structured problem-solving skills that are essential throughout mathematics.
