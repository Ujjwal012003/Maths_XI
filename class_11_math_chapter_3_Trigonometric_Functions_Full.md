# Chapter 3: Trigonometric_Functions

## 3.1 Introduction to Angles

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Diagram showing an angle formed by two rays with a vertex" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.1.1:</b> An angle formed by two rays sharing a common vertex</i></figcaption>
</figure>

**Introduction:**

Angles form one of the fundamental concepts in geometry and trigonometry. Intuitively, an angle represents the amount of rotation or turning between two lines or rays with a common starting point, called the vertex. Understanding angles is essential for analyzing shapes, slopes of lines, and circular motion.

### 3.1.1 Definition of Angles

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Two rays forming an angle with vertex labeled O" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.1.2:</b> Definition of angle with parts labeled</i></figcaption>
</figure>

**Definition:**  
An **angle** is defined as the figure formed by two rays (called the sides of the angle) sharing a common endpoint called the **vertex**. The two rays are named the **initial side** and the **terminal side** (or arm) of the angle.

**Geometric Meaning:**  
Geometrically, an angle measures the amount of rotation from the initial side to the terminal side about the vertex. On the Cartesian plane, if the initial side lies along the positive x-axis, then the angle corresponds to the rotation measured from this axis to the terminal side.

**Types of Angles:**

- **Acute angle:** An angle less than $90^\circ$.
- **Right angle:** Exactly $90^\circ$.
- **Obtuse angle:** Greater than $90^\circ$ but less than $180^\circ$.
- **Straight angle:** Exactly $180^\circ$.
- **Reflex angle:** Greater than $180^\circ$ but less than $360^\circ$.

---

### 3.1.2 Measurement of Angles in Degrees and Radians

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Circle showing angle in degrees and radians" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.1.3:</b> Representation of angles measured in degrees and radians on a unit circle</i></figcaption>
</figure>

**Angle Measurement:**

Angles can be measured in two common units:

- **Degrees** ($^\circ$): The full rotation around a point is divided into 360 equal parts, making $1^\circ = \frac{1}{360}$ of a full rotation.
- **Radians** ($\text{rad}$): Based on the radius of the circle, one radian is the angle subtended at the center of a circle by an arc equal in length to the radius of the circle.

The **degree** is common in everyday use, while the **radian** is fundamental in mathematical and scientific contexts.

**Relationship Between Degrees and Radians:**

The entire circumference of a circle corresponds to an angle of $360^\circ$ or $2\pi$ radians. Thus:

$$
360^\circ = 2\pi \text{ radians}
$$

From this, it follows that:

$$
1^\circ = \frac{\pi}{180} \text{ radians} \quad \text{and} \quad 1 \text{ radian} = \frac{180}{\pi}^\circ.
$$

---

### 3.1.3 Conversion between Degrees and Radians

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Arrows showing conversion between degrees and radians" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.1.4:</b> Conversion between degrees and radians</i></figcaption>
</figure>

**Formulae for Conversion:**

$$
\text{Angle in radians} = \text{Angle in degrees} \times \frac{\pi}{180}
$$

$$
\text{Angle in degrees} = \text{Angle in radians} \times \frac{180}{\pi}
$$

**Working Rule (Algorithm) for Conversion:**

1. **To convert degrees to radians:**  
   - Step 1: Take the given angle in degrees.  
   - Step 2: Multiply the angle by $\frac{\pi}{180}$.  
   - Step 3: Simplify the expression (approximate if necessary using $\pi \approx 3.1416$) to get the angle in radians.

2. **To convert radians to degrees:**  
   - Step 1: Take the given angle in radians.  
   - Step 2: Multiply the angle by $\frac{180}{\pi}$.  
   - Step 3: Simplify or approximate to obtain the angle in degrees.

---

**Theorem (Relationship Between Degrees and Radians):**  
**For any angle, its measure in radians and degrees satisfy:**

$$
\text{radians} = \frac{\pi}{180} \times \text{degrees} \quad \text{and} \quad \text{degrees} = \frac{180}{\pi} \times \text{radians}.
$$

**Proof:**

- Consider a circle of radius $r$.  
- The length of the full circumference $C = 2\pi r$.  
- One full rotation corresponds to $360^\circ$ or the entire circumference.

**Step 1:** By definition of radian measure, the angle $\theta$ in radians subtends an arc length $s = r \theta.$  
**Step 2:** For the entire circle, when the arc length $s = 2 \pi r$, the angle corresponds to $2 \pi$ radians.  
**Step 3:** Since this rotation equals $360^\circ$, we equate:

$$
360^\circ = 2 \pi \text{ radians}.
$$

**Step 4:** Divide both sides by 360:

$$
1^\circ = \frac{2 \pi}{360} = \frac{\pi}{180} \text{ radians}.
$$

**Step 5:** Similarly, dividing $360^\circ = 2 \pi$ radians by $2 \pi$:

$$
1 \text{ radian} = \frac{360^\circ}{2 \pi} = \frac{180^\circ}{\pi}.
$$

Thus, the conversion formulas hold.

---

### Formulas Summary:

$$
\boxed{
\begin{aligned}
1^\circ &= \frac{\pi}{180} \text{ radians}, \\
1 \text{ radian} &= \frac{180}{\pi}^\circ, \\
\text{Angle in radians} &= \text{Angle in degrees} \times \frac{\pi}{180}, \\
\text{Angle in degrees} &= \text{Angle in radians} \times \frac{180}{\pi}.
\end{aligned}
}
$$

---

### Graded Solved Examples

---

**Example 1 (Concept Building):**  
Convert $45^\circ$ into radians.

**Solution:**

- Step 1: Given angle $= 45^\circ.$  
- Step 2: Use conversion formula:  
$$
\text{radians} = 45 \times \frac{\pi}{180} = \frac{\pi}{4}.
$$
- Step 3: Thus, $45^\circ = \frac{\pi}{4}$ radians.

---

**Example 2 (Competency Based):**  
An angle measures $\frac{3\pi}{2}$ radians. Convert this angle to degrees.

**Solution:**

- Step 1: Given angle $= \frac{3\pi}{2}$ radians.  
- Step 2: Use conversion formula:  
$$
\text{degrees} = \frac{3\pi}{2} \times \frac{180}{\pi} = \frac{3 \times 180}{2} = 270^\circ.
$$
- Step 3: The angle is $270^\circ$.

---

**Example 3 (HOTS):**  
A wheel rotates through an angle of $500^\circ$. Find the equivalent radian measure and additionally, express the result in terms of $\pi$.

**Solution:**

- Step 1: Given angle $= 500^\circ.$  
- Step 2: Convert degrees to radians:  

$$
500 \times \frac{\pi}{180} = \frac{500 \pi}{180} = \frac{50 \pi}{18} = \frac{25 \pi}{9}.
$$

- Step 3: Simplify the fraction as done above.  
- Step 4: Thus, the angle in radians is $\frac{25\pi}{9}$.

- Step 5: For approximate decimal value, use $\pi \approx 3.1416$:

$$
\frac{25 \times 3.1416}{9} \approx 8.7266 \text{ radians}.
$$

---

This completes the foundational introduction to angles including their definition, measurement units, and how to convert between degrees and radians. Understanding these concepts paves the way for deeper study in trigonometric functions and their applications.

---

## 3.2 Definition of Trigonometric Functions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Unit circle showing sine, cosine, and tangent with labeled points on the circumference" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.2.1:</b> Unit circle representation of sine, cosine, and tangent functions</i></figcaption>
</figure>

**Introduction:**

Trigonometric functions describe relationships between the angles and sides of triangles, and their extensions to real numbers help us analyze periodic phenomena. In this section, we rigorously define sine, cosine, tangent, their reciprocal functions, and relate them through identities with geometric visualization primarily using the unit circle.

### 3.2.1 Sine, Cosine and Tangent Ratios

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Right triangle labeling opposite, adjacent and hypotenuse" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.2.2:</b> Right triangle illustrating sine, cosine, and tangent ratios</i></figcaption>
</figure>

**Definitions:**

Consider a right-angled triangle with an acute angle $ \theta $. Let **opposite** be the side opposite the angle $ \theta $, **adjacent** be the side adjacent to $ \theta $ (but not the hypotenuse), and **hypotenuse** be the longest side.

- **Sine function:**
$$
\sin \theta = \frac{\text{Opposite side}}{\text{Hypotenuse}}
$$
- **Cosine function:**
$$
\cos \theta = \frac{\text{Adjacent side}}{\text{Hypotenuse}}
$$
- **Tangent function:**
$$
\tan \theta = \frac{\text{Opposite side}}{\text{Adjacent side}} = \frac{\sin \theta}{\cos \theta}
$$

**Geometric Interpretation:**

On the **unit circle** (circle centered at the origin with radius 1), the angle $ \theta $ is measured from the positive x-axis to a point $ P(x, y) $ on the circle's circumference. Then:

- $ \cos \theta = x $, the x-coordinate of $ P $,
- $ \sin \theta = y $, the y-coordinate of $ P $,
- $ \tan \theta = \frac{y}{x} $ (defined only for $ x \neq 0 $).

---

### 3.2.2 Reciprocal Functions: Cosecant, Secant, Cotangent

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Table of reciprocal trigonometric functions" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.2.3:</b> Reciprocal trigonometric functions</i></figcaption>
</figure>

**Definitions:**

- **Cosecant (csc):** Reciprocal of sine,
$$
\csc \theta = \frac{1}{\sin \theta} = \frac{\text{Hypotenuse}}{\text{Opposite side}}.
$$
- **Secant (sec):** Reciprocal of cosine,
$$
\sec \theta = \frac{1}{\cos \theta} = \frac{\text{Hypotenuse}}{\text{Adjacent side}}.
$$
- **Cotangent (cot):** Reciprocal of tangent,
$$
\cot \theta = \frac{1}{\tan \theta} = \frac{\cos \theta}{\sin \theta} = \frac{\text{Adjacent side}}{\text{Opposite side}}.
$$

**Domain Note:**  
Each reciprocal function is undefined where the corresponding primary function is zero, leading to domain restrictions.

---

### 3.2.3 Relationships Between Trigonometric Functions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Trigonometric identity relationships diagram" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.2.4:</b> Fundamental identities relating trigonometric functions</i></figcaption>
</figure>

**Fundamental Theorems (Boxed):**

1. **Pythagorean Identity**
$$
\sin^2 \theta + \cos^2 \theta = 1
$$

2. **Tangent-Secant Relationship**
$$
\tan^2 \theta + 1 = \sec^2 \theta
$$

3. **Cotangent-Cosecant Relationship**
$$
1 + \cot^2 \theta = \csc^2 \theta
$$

**Step-by-Step Proof of Pythagorean Identity:**

- Step 1: Consider a point $ P $ on the unit circle with coordinates $ (x, y) = (\cos \theta, \sin \theta) $.  
- Step 2: By definition of the unit circle, 
$$
x^2 + y^2 = 1.
$$  
- Step 3: Substitute $ x = \cos \theta $ and $ y = \sin \theta $ to obtain
$$
\cos^2 \theta + \sin^2 \theta = 1.
$$  
- Step 4: Hence proved.

**Note:** The other identities follow by dividing the Pythagorean identity by suitable powers of $ \sin \theta $ or $ \cos \theta $:

- Dividing by $ \cos^2 \theta $ (where $ \cos \theta \neq 0 $):
$$
\frac{\sin^2 \theta}{\cos^2 \theta} + \frac{\cos^2 \theta}{\cos^2 \theta} = \frac{1}{\cos^2 \theta} \implies \tan^2 \theta + 1 = \sec^2 \theta.
$$

- Dividing by $ \sin^2 \theta $ (where $ \sin \theta \neq 0 $):
$$
\frac{\sin^2 \theta}{\sin^2 \theta} + \frac{\cos^2 \theta}{\sin^2 \theta} = \frac{1}{\sin^2 \theta} \implies 1 + \cot^2 \theta = \csc^2 \theta.
$$

---

### 3.2.4 Unit Circle Representation

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Unit circle showing trigonometric values in four quadrants" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.2.5:</b> Unit circle showing sine and cosine in all quadrants</i></figcaption>
</figure>

**Geometric Interpretation:**

- The unit circle allows measuring angles from $0$ to $2\pi$ radians (or 0° to 360°).
- Sine values correspond to the y-coordinates; cosine to x-coordinates for any angle $ \theta $.
- Quadrants and sign conventions:
  - Quadrant I: $ \sin \theta > 0 $, $ \cos \theta > 0 $,
  - Quadrant II: $ \sin \theta > 0 $, $ \cos \theta < 0 $,
  - Quadrant III: $ \sin \theta < 0 $, $ \cos \theta < 0 $,
  - Quadrant IV: $ \sin \theta < 0 $, $ \cos \theta > 0 $.

---

### Formulas Summary

$$
\boxed{
\begin{aligned}
& \sin \theta = \frac{\text{Opposite}}{\text{Hypotenuse}}, \quad \cos \theta = \frac{\text{Adjacent}}{\text{Hypotenuse}}, \quad \tan \theta = \frac{\sin \theta}{\cos \theta}, \\
& \csc \theta = \frac{1}{\sin \theta}, \quad \sec \theta = \frac{1}{\cos \theta}, \quad \cot \theta = \frac{1}{\tan \theta}, \\
& \sin^2 \theta + \cos^2 \theta = 1, \quad 1 + \tan^2 \theta = \sec^2 \theta, \quad 1 + \cot^2 \theta = \csc^2 \theta.
\end{aligned}
}
$$

---

### Working Rule (Algorithm) for Trigonometric Problems

1. **Identify the angle $ \theta $** and the triangle or coordinate setup.  
2. **For right triangles:** Use definitions of sine, cosine, and tangent to express ratios of relevant sides.  
3. **For unit circle problems:** Identify $ \cos \theta $ and $ \sin \theta $ as x and y coordinates of the point on the unit circle.  
4. **Use reciprocal definitions** for cosecant, secant, cotangent when required.  
5. **Apply appropriate identities** (Pythagorean or ratio identities) to simplify or connect functions.  
6. **Check the quadrant** of the angle to determine the sign of the functions.  
7. **Substitute known values/angles** and simplify for numeric or algebraic answers.

---

### Graded Solved Examples

---

**Example 1 (Concept Building):**  
If in a right-angled triangle, the length of the side opposite to angle $ \theta $ is 3 units and the hypotenuse is 5 units, find $ \sin \theta $, $ \cos \theta $, and $ \tan \theta $.

**Solution:**

- Step 1: Given $ \text{Opposite} = 3 $, $ \text{Hypotenuse} = 5 $.  
- Step 2: Find adjacent side by Pythagoras’ theorem:  
$$
\text{Adjacent} = \sqrt{5^2 - 3^2} = \sqrt{25 - 9} = \sqrt{16} = 4.
$$
- Step 3: Calculate $ \sin \theta $:
$$
\sin \theta = \frac{3}{5} = 0.6.
$$
- Step 4: Calculate $ \cos \theta $:
$$
\cos \theta = \frac{4}{5} = 0.8.
$$
- Step 5: Calculate $ \tan \theta $:
$$
\tan \theta = \frac{3}{4} = 0.75.
$$

---

**Example 2 (Competency Based):**  
Prove that $ \tan^2 \theta + 1 = \sec^2 \theta $.

**Solution:**

- Step 1: Start with Pythagorean identity:
$$
\sin^2 \theta + \cos^2 \theta = 1.
$$
- Step 2: Divide both sides by $ \cos^2 \theta $ (assuming $ \cos \theta \neq 0 $):
$$
\frac{\sin^2 \theta}{\cos^2 \theta} + \frac{\cos^2 \theta}{\cos^2 \theta} = \frac{1}{\cos^2 \theta}.
$$
- Step 3: Simplify each term:
$$
\tan^2 \theta + 1 = \sec^2 \theta.
$$
- Step 4: Hence proved.

---

**Example 3 (HOTS):**  
If $ \sin \theta = \frac{3}{5} $ and $ \theta $ lies in the second quadrant, find $ \sec \theta $ and $ \tan \theta $.

**Solution:**

- Step 1: Given $ \sin \theta = \frac{3}{5} $ and $ \theta $ in the second quadrant, so $ \cos \theta < 0 $.  
- Step 2: Use the Pythagorean identity to find $ \cos \theta $:
$$
\cos^2 \theta = 1 - \sin^2 \theta = 1 - \left(\frac{3}{5}\right)^2 = 1 - \frac{9}{25} = \frac{16}{25}.
$$
- Step 3: Since $ \theta $ is in the second quadrant, $ \cos \theta = -\frac{4}{5} $.  
- Step 4: Calculate $ \sec \theta $:
$$
\sec \theta = \frac{1}{\cos \theta} = \frac{1}{-\frac{4}{5}} = -\frac{5}{4}.
$$
- Step 5: Calculate $ \tan \theta $:
$$
\tan \theta = \frac{\sin \theta}{\cos \theta} = \frac{\frac{3}{5}}{-\frac{4}{5}} = -\frac{3}{4}.
$$

---

This concludes the detailed study of the definitions, properties, and relationships of trigonometric functions, providing a strong foundation for further applications in Class 11 Mathematics.

---

## 3.3 Values of Trigonometric Functions at Standard Angles

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Unit circle highlighting standard angles and their sine, cosine values" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.3.1:</b> Unit circle marking standard angles 0°, 30°, 45°, 60°, 90° and corresponding sine, cosine values</i></figcaption>
</figure>

**Introduction:**

The trigonometric functions sine, cosine, and tangent take special values at certain standard angles which form the foundation for solving many mathematical problems. These angles—0°, 30°, 45°, 60°, and 90°—have exact trigonometric values expressible using simple fractions and square roots. Mastery of these values enables understanding of the behavior of trigonometric functions and facilitates computations in trigonometry.

---

### 3.3.1 Exact Values of Sine, Cosine and Tangent at Standard Angles

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Right triangles illustrating 30-60-90 and 45-45-90 triangle" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.3.2:</b> Special right triangles used to derive values of sine, cosine for 30°, 45°, 60°</i></figcaption>
</figure>

**Exact Values Table:**

| Angle (Degrees) | $ \sin \theta $            | $ \cos \theta $            | $ \tan \theta $                         |
|-----------------|------------------------------|------------------------------|-------------------------------------------|
| 0°              | 0                            | 1                            | 0                                         |
| 30°             | $ \frac{1}{2} $            | $ \frac{\sqrt{3}}{2} $     | $ \frac{1}{\sqrt{3}} $ or $ \frac{\sqrt{3}}{3} $ |
| 45°             | $ \frac{\sqrt{2}}{2} $     | $ \frac{\sqrt{2}}{2} $     | 1                                         |
| 60°             | $ \frac{\sqrt{3}}{2} $     | $ \frac{1}{2} $            | $ \sqrt{3} $                             |
| 90°             | 1                            | 0                            | Undefined                                 |

---

**Proofs of Exact Values:**

1. **Values at 0° and 90°:**

On the unit circle of radius 1:

- At angle $0^\circ$, the point on the circumference is $(1, 0)$, so
  $$
  \sin 0^\circ = 0, \quad \cos 0^\circ = 1.
  $$
  Tangent is $\frac{0}{1} = 0$.

- At angle $90^\circ$, the point on the circumference is $(0, 1)$, so
  $$
  \sin 90^\circ = 1, \quad \cos 90^\circ = 0.
  $$
  Tangent is undefined as division by zero occurs.

2. **Values at 30° and 60° (Using 30°-60°-90° Triangle):**

- Consider an equilateral triangle of side length 2.  
- Drop an altitude to split it into two right triangles with angles 30°, 60°, and 90°, with sides:
  - Hypotenuse = 2,
  - Opposite side to 30° = 1,
  - Adjacent side to 30° = $\sqrt{3}$.

Thus,
$$
\sin 30^\circ = \frac{\text{Opposite}}{\text{Hypotenuse}} = \frac{1}{2}, \quad
\cos 30^\circ = \frac{\sqrt{3}}{2}, \quad
\tan 30^\circ = \frac{1}{\sqrt{3}}.
$$
By the complementary angle property,
$$
\sin 60^\circ = \cos 30^\circ = \frac{\sqrt{3}}{2}, \quad
\cos 60^\circ = \sin 30^\circ = \frac{1}{2}, \quad
\tan 60^\circ = \sqrt{3}.
$$

3. **Values at 45° (Using 45°-45°-90° Triangle):**

- Consider an isosceles right triangle with legs 1 and 1, hypotenuse $\sqrt{2}$:
$$
\sin 45^\circ = \cos 45^\circ = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}.
$$
Tangent:
$$
\tan 45^\circ = \frac{\sin 45^\circ}{\cos 45^\circ} = 1.
$$

---

### 3.3.2 Use of the Unit Circle for Value Determination

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Unit circle illustrating standard angles and sine/cosine projection" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.3.3:</b> Unit circle showing coordinates at standard angles used for determining sine and cosine values</i></figcaption>
</figure>

**Geometric Interpretation:**

- The **unit circle** is a circle centered at the origin with radius 1.
- Each point $P(x, y)$ on the unit circle corresponds to an angle $\theta$ made with the positive x-axis.
- The x-coordinate $x$ equals $\cos \theta$.
- The y-coordinate $y$ equals $\sin \theta$.
- Values for standard angles can be read directly from their coordinates on the unit circle.
- Tangent of $\theta$ corresponds to the slope of the line connecting the origin to $P$, or $\frac{y}{x}$ (when defined).

---

### Formulas Summary

$$
\boxed{
\begin{aligned}
& \sin 0^\circ = 0, \quad \cos 0^\circ = 1, \quad \tan 0^\circ = 0, \\
& \sin 30^\circ = \frac{1}{2}, \quad \cos 30^\circ = \frac{\sqrt{3}}{2}, \quad \tan 30^\circ = \frac{1}{\sqrt{3}}, \\
& \sin 45^\circ = \frac{\sqrt{2}}{2}, \quad \cos 45^\circ = \frac{\sqrt{2}}{2}, \quad \tan 45^\circ = 1, \\
& \sin 60^\circ = \frac{\sqrt{3}}{2}, \quad \cos 60^\circ = \frac{1}{2}, \quad \tan 60^\circ = \sqrt{3}, \\
& \sin 90^\circ = 1, \quad \cos 90^\circ = 0, \quad \tan 90^\circ \text{ undefined}.
\end{aligned}
}
$$

---

### Working Rule (Algorithm) for Finding Values at Standard Angles

1. Determine if the angle corresponds to a special triangle (30°-60°-90° or 45°-45°-90°) or a quadrant angle (0°, 90°).  
2. Use the corresponding triangle relationships or the unit circle coordinates:  
   - For 30°, 60°, use side ratios of the equilateral triangle split: $1,\ \sqrt{3},\ 2$.  
   - For 45°, use the isosceles right triangle side ratio: $1,\,1,\,\sqrt{2}$.  
3. Assign sine to the side opposite the angle divided by hypotenuse, cosine to adjacent over hypotenuse, and tangent as their ratio.  
4. For values at 0° and 90°, use simple geometric interpretations on the unit circle.  
5. Recall tangent is undefined where cosine is zero (at 90°).  
6. Use the symmetry of the unit circle for other quadrants if needed.

---

### Graded Solved Examples

---

**Example 1 (Concept Building):**  
Find $\sin 45^\circ$, $\cos 45^\circ$, and $\tan 45^\circ$.

**Solution:**

- Step 1: Consider a 45°-45°-90° right triangle with legs of length 1.  
- Step 2: Calculate the hypotenuse:
$$
\text{Hypotenuse} = \sqrt{1^2 + 1^2} = \sqrt{2}.
$$
- Step 3: Calculate sine:
$$
\sin 45^\circ = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}.
$$
- Step 4: Calculate cosine (equal to sine for this triangle):
$$
\cos 45^\circ = \frac{\sqrt{2}}{2}.
$$
- Step 5: Tangent is the ratio:
$$
\tan 45^\circ = \frac{\sin 45^\circ}{\cos 45^\circ} = 1.
$$

---

**Example 2 (Competency Based):**  
Verify the value of $\tan 30^\circ$ using sine and cosine.

**Solution:**

- Step 1: Recall from the 30°-60°-90° triangle:
$$
\sin 30^\circ = \frac{1}{2}, \quad \cos 30^\circ = \frac{\sqrt{3}}{2}.
$$
- Step 2: Calculate tangent:
$$
\tan 30^\circ = \frac{\sin 30^\circ}{\cos 30^\circ} = \frac{\frac{1}{2}}{\frac{\sqrt{3}}{2}} = \frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}.
$$

---

**Example 3 (HOTS):**  
Using the unit circle, find $\sin 60^\circ$, $\cos 60^\circ$, and $\tan 60^\circ$, and explain why $\tan 90^\circ$ is undefined.

**Solution:**

- Step 1: From equilateral triangle split or unit circle at 60°:
$$
\sin 60^\circ = \frac{\sqrt{3}}{2}, \quad \cos 60^\circ = \frac{1}{2}.
$$
- Step 2: Calculate tangent:
$$
\tan 60^\circ = \frac{\sin 60^\circ}{\cos 60^\circ} = \frac{\frac{\sqrt{3}}{2}}{\frac{1}{2}} = \sqrt{3}.
$$
- Step 3: Address $\tan 90^\circ$:
  - At 90°, the point on the unit circle is $(0,1)$.  
  - Tangent is $\frac{y}{x} = \frac{1}{0}$, which is undefined due to division by zero.  
  - This corresponds to the vertical tangent line to the unit circle at the top point.

---

By mastering these exact values and their geometric interpretations, students build a solid foundation for understanding and applying trigonometric functions throughout their mathematical journey.

---

## 3.4 Graphs of Trigonometric Functions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Graphs of sine, cosine and tangent functions on coordinate axes" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.4.1:</b> Graphs of sine, cosine, and tangent functions</i></figcaption>
</figure>

**Introduction:**

Trigonometric functions describe periodic phenomena and are characterized by distinctive graphs. Studying their graphs reveals essential properties such as periodicity, amplitude, and symmetry. Understanding these properties is crucial for analyzing function behavior and solving trigonometric problems.

---

### 3.4.1 Graph of Sine and Cosine Functions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Graph showing sine and cosine waves with period and amplitude labeled" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.4.2:</b> Graphs of sine and cosine functions showing amplitude and period</i></figcaption>
</figure>

**Definition and Geometric Meaning:**

- The **sine function** $ y = \sin x $ maps an angle $ x $ to the vertical coordinate on the unit circle.
- The **cosine function** $ y = \cos x $ maps an angle $ x $ to the horizontal coordinate on the unit circle.

Both functions produce smooth wave-like graphs oscillating between $-1$ and $1$.

**Key Properties:**

- **Periodicity:** Both sine and cosine functions repeat values every $ 2\pi $ radians, i.e.,  
$$
\sin(x + 2\pi) = \sin x, \quad \cos(x + 2\pi) = \cos x.
$$
- **Amplitude:** The maximum absolute value they attain is 1.  
- **Symmetry:**  
  - Sine is an **odd function**, meaning  
  $$
  \sin(-x) = -\sin x.
  $$
  - Cosine is an **even function**, meaning  
  $$
  \cos(-x) = \cos x.
  $$

---

### 3.4.2 Graph of Tangent and Cotangent Functions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Graph of tangent function with vertical asymptotes" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.4.3:</b> Graph of tangent function showing vertical asymptotes at $ \pm \frac{\pi}{2} $</i></figcaption>
</figure>

**Definition and Geometric Meaning:**

- The **tangent function** $ y = \tan x $ can be seen as the slope of the line from the origin to a point on the unit circle.
- The **cotangent function** $ y = \cot x $ is the reciprocal of tangent.

These functions exhibit vertical asymptotes where cosine or sine are zero, respectively.

**Key Properties:**

- **Periodicity:** Both have period $\pi$, i.e.,  
$$
\tan(x + \pi) = \tan x, \quad \cot(x + \pi) = \cot x.
$$
- **Amplitude:** These values are unbounded.
- **Symmetry:** Both are odd functions:  
$$
\tan(-x) = - \tan x, \quad \cot(-x) = - \cot x.
$$
- **Asymptotes:**  
  - Tangent has vertical asymptotes at $ x = \pm \frac{\pi}{2}, \pm \frac{3\pi}{2}, \ldots $  
  - Cotangent has vertical asymptotes at $ x = 0, \pm \pi, \pm 2\pi, \ldots $

---

### 3.4.3 Graphs of Reciprocal Functions: Secant and Cosecant

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Graph of secant function with asymptotes and peaks" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.4.4:</b> Graph of secant function showing vertical asymptotes and oscillating peaks</i></figcaption>
</figure>

**Definition and Geometric Meaning:**

- **Secant function** $ y = \sec x = \frac{1}{\cos x} $ takes reciprocal values of cosine.
- **Cosecant function** $ y = \csc x = \frac{1}{\sin x} $ takes reciprocal values of sine.

Their graphs have vertical asymptotes corresponding to zeros of the respective denominators.

**Key Properties:**

- **Periodicity:** Both have period $ 2\pi $,  
$$
\sec(x + 2\pi) = \sec x, \quad \csc(x + 2\pi) = \csc x.
$$
- **Symmetry:**  
  - Secant is an even function:  
  $$
  \sec(-x) = \sec x.
  $$
  - Cosecant is an odd function:  
  $$
  \csc(-x) = -\csc x.
  $$
- **Amplitude:** Neither function has a finite amplitude; their values tend to infinity near asymptotes.

---

### 3.4.4 Periodicity, Amplitude, and Symmetry of Graphs

**Periodicity:**  
- **Sine and Cosine:** Period $ 2\pi $.  
- **Tangent and Cotangent:** Period $ \pi $.  
- **Secant and Cosecant:** Period $ 2\pi $.

**Amplitude:**  
- **Sine and Cosine:** Amplitude is 1 (maximum absolute value).  
- **Tangent, Cotangent, Secant, Cosecant:** No fixed amplitude (values can tend to infinity).

**Symmetry:**  
- **Even Functions:** Cosine and Secant satisfy $ f(-x) = f(x) $.  
- **Odd Functions:** Sine, Tangent, Cotangent, and Cosecant satisfy $ f(-x) = -f(x) $.

---

### 3.4.5 Quadrantal Angles and Their Graphical Significance

**Quadrantal angles** are the multiples of $ \frac{\pi}{2} $ (or 90°), such as $ 0, \frac{\pi}{2}, \pi, \frac{3\pi}{2}, 2\pi $, etc. They correspond to key points on the unit circle.

**Graphical Significance:**

- At quadrantal angles, sine and cosine values are either 0 or $ \pm 1 $.
- Tangent and cotangent functions have vertical asymptotes at some quadrantal angles (e.g., tangent is undefined at $ \pm \frac{\pi}{2} $).
- Secant and cosecant have vertical asymptotes corresponding to the zeros of cosine and sine, respectively, which occur at quadrantal angles.

---

### Formulas Summary

$$
\boxed{
\begin{aligned}
& \text{Period}[\sin x] = \text{Period}[\cos x] = 2\pi, \\
& \text{Period}[\tan x] = \text{Period}[\cot x] = \pi, \\
& \text{Period}[\sec x] = \text{Period}[\csc x] = 2\pi, \\
& \text{Amplitude}[\sin x] = \text{Amplitude}[\cos x] = 1, \\
& \sin(-x) = -\sin x, \quad \cos(-x) = \cos x, \quad \tan(-x) = -\tan x, \\
& \cot(-x) = -\cot x, \quad \sec(-x) = \sec x, \quad \csc(-x) = -\csc x.
\end{aligned}
}
$$

---

### Working Rule (Algorithm) for Sketching Graphs of Trigonometric Functions

1. **Identify the function type** (sine, cosine, tangent, etc.).  
2. **Determine period and amplitude**:  
   - Use the period to know one full cycle length.  
   - Use the amplitude to know maximum and minimum values (if finite).  
3. **Mark key points:**  
   - For sine and cosine, mark maxima, minima, and zeros.  
   - For tangent and cotangent, mark vertical asymptotes and zeros.  
   - For secant and cosecant, locate vertical asymptotes and oscillating peaks.  
4. **Use symmetry:**  
   - Use even/odd nature to plot the graph on negative axes accordingly.  
5. **Plot the curve smoothly between key points** to complete one period.  
6. **Repeat the pattern using periodicity to sketch over the desired $x$-range.**

---

### Graded Solved Examples

---

**Example 1 (Concept Building):**  
Sketch the graph of $ y = \sin x $ for $ x \in [0, 2\pi] $.

**Solution:**

- Step 1: The period is $ 2\pi $ and amplitude is 1.  
- Step 2: Mark key points:  
  - $ x = 0, y = 0 $,  
  - $ x = \frac{\pi}{2}, y = 1 $,  
  - $ x = \pi, y = 0 $,  
  - $ x = \frac{3\pi}{2}, y = -1 $,  
  - $ x = 2\pi, y = 0 $.  
- Step 3: Connect these points smoothly to form one wave cycle.  
- Step 4: Use symmetry and periodicity to extend the graph if needed.

---

**Example 2 (Competency Based):**  
Find the period and amplitude of $ y = 3 \cos 2x $, and sketch the graph for $ x \in [0, \pi] $.

**Solution:**

- Step 1: The amplitude is the coefficient of cosine, which is 3.  
- Step 2: Period $= \frac{2\pi}{2} = \pi$.  
- Step 3: Calculate key points:  
  - At $ x = 0 $, $ y = 3 $.  
  - At $ x = \frac{\pi}{4} $, $ y = 3 \cos \left( 2 \times \frac{\pi}{4} \right) = 3 \cos \frac{\pi}{2} = 0 $.  
  - At $ x = \frac{\pi}{2} $, $ y = 3 \cos \pi = -3 $.  
  - At $ x = \frac{3\pi}{4} $, $ y = 0 $.  
  - At $ x = \pi $, $ y = 3 $.  
- Step 4: Connect these points smoothly to sketch one period.

---

**Example 3 (HOTS):**  
Sketch the graph of $ y = \tan x $ for $ x \in \left( -\frac{\pi}{2}, \frac{\pi}{2} \right) $ and explain the behavior near vertical asymptotes.

**Solution:**

- Step 1: The period of tangent is $ \pi $.  
- Step 2: Vertical asymptotes occur at $ x = \pm \frac{\pi}{2} $.  
- Step 3: At $ x = 0 $, $ y = 0 $.  
- Step 4: As $ x \to \frac{\pi}{2}^- $, $ y \to +\infty $.  
- Step 5: As $ x \to -\frac{\pi}{2}^+ $, $ y \to -\infty $.  
- Step 6: Sketch the curve increasing monotonically from $-\infty$ to $+\infty$ between the asymptotes.

---

Understanding these graphs and their properties will greatly enhance your proficiency in trigonometry and its applications.

---

## 3.5 Fundamental Trigonometric Identities

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Unit circle showing sine and cosine coordinates and Pythagorean relation" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.5.1:</b> Unit circle depicting sine and cosine as coordinates on the circle</i></figcaption>
</figure>

**Introduction:**

Fundamental trigonometric identities are essential tools in mathematics, allowing us to simplify expressions, solve equations, and understand the intrinsic relationships between trigonometric functions. Among these, Pythagorean identities form the cornerstone, connecting sine, cosine, tangent, and their reciprocal functions through foundational relationships.

---

### 3.5.1 Pythagorean Identities

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Right angled triangle demonstrating Pythagorean theorem visualizing sine and cosine" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.5.2:</b> Right triangle illustrating relationship between sine, cosine, and the unit circle radius</i></figcaption>
</figure>

**Definition & Geometric Meaning:**

The fundamental Pythagorean identity is:

$$
\sin^2 x + \cos^2 x = 1.
$$

This identity signifies that for any angle $ x $, the sum of the squares of sine and cosine equals one, echoing the Pythagorean theorem applied to the unit circle where the radius is 1.

---

**Theorem (Pythagorean Identity):**

$$
\boxed{
\sin^2 x + \cos^2 x = 1.
}
$$

---

**Proof using the Unit Circle:**

- Step 1: Consider the unit circle centered at the origin with radius 1. Any point on this circle corresponding to angle $ x $ has coordinates $ (\cos x, \sin x) $.
  
- Step 2: By the definition of the unit circle:

$$
(\cos x)^2 + (\sin x)^2 = 1^2,
$$

which simplifies to

$$
\cos^2 x + \sin^2 x = 1.
$$

Hence, the identity is proved.

---

### 3.5.2 Other Forms of Pythagorean Identities

From the primary identity, dividing by $ \cos^2 x $ (with $ \cos x \neq 0 $) and $ \sin^2 x $ (with $ \sin x \neq 0 $) respectively, we derive:

$$
\tan^2 x + 1 = \sec^2 x,
$$

and

$$
1 + \cot^2 x = \csc^2 x.
$$

These identities relate the tangent and cotangent functions to their reciprocal secant and cosecant functions.

---

**Theorem:**

$$
\boxed{
\begin{aligned}
& \tan^2 x + 1 = \sec^2 x, \\
& 1 + \cot^2 x = \csc^2 x.
\end{aligned}
}
$$

---

**Proof:**

- Step 1: Starting with the fundamental identity:

$$
\sin^2 x + \cos^2 x = 1.
$$

- Step 2: Divide each term by $ \cos^2 x $ (where $ \cos x \neq 0 $):

$$
\frac{\sin^2 x}{\cos^2 x} + \frac{\cos^2 x}{\cos^2 x} = \frac{1}{\cos^2 x} \implies \tan^2 x + 1 = \sec^2 x.
$$

- Step 3: Similarly, dividing by $ \sin^2 x $ (where $ \sin x \neq 0 $):

$$
\frac{\sin^2 x}{\sin^2 x} + \frac{\cos^2 x}{\sin^2 x} = \frac{1}{\sin^2 x} \implies 1 + \cot^2 x = \csc^2 x.
$$

---

### 3.5.3 Applications in Simplification

These identities facilitate the simplification of complicated trigonometric expressions and solving equations.

---

### Formulas Summary

$$
\boxed{
\begin{aligned}
& \sin^2 x + \cos^2 x = 1, \\
& \tan^2 x + 1 = \sec^2 x, \\
& 1 + \cot^2 x = \csc^2 x.
\end{aligned}
}
$$

---

### Working Rule (Algorithm) for Using Pythagorean Identities:

1. **Identify** the trigonometric expression to simplify or equation to solve.  
2. **Check** if terms can be expressed using sine, cosine, tangent, cotangent, secant, or cosecant.  
3. **Apply** the relevant Pythagorean identity to substitute or relate expressions.  
4. **Simplify** the resulting expression or solve the equation accordingly.  
5. **Verify** any constraints due to division by zero or domain restrictions.

---

### Graded Solved Examples

---

**Example 1 (Concept Building):**  
Verify the identity $ \sin^2 45^\circ + \cos^2 45^\circ = 1 $.

**Solution:**

- Step 1: Find sine and cosine of $45^\circ$:
$$
\sin 45^\circ = \frac{\sqrt{2}}{2}, \quad \cos 45^\circ = \frac{\sqrt{2}}{2}.
$$

- Step 2: Calculate left side:
$$
\left(\frac{\sqrt{2}}{2}\right)^2 + \left(\frac{\sqrt{2}}{2}\right)^2 = \frac{2}{4} + \frac{2}{4} = \frac{4}{4} = 1.
$$

- Step 3: Left side equals right side, confirming the identity.

---

**Example 2 (Competency Based):**  
Simplify $ \tan^2 x \cdot \sec^2 x - \tan^2 x $.

**Solution:**

- Step 1: Use the identity $ \tan^2 x + 1 = \sec^2 x $, so substitute:

$$
\tan^2 x \cdot \sec^2 x - \tan^2 x = \tan^2 x (\sec^2 x - 1).
$$

- Step 2: Replace $ \sec^2 x - 1 $ by $ \tan^2 x $:

$$
= \tan^2 x \cdot \tan^2 x = \tan^4 x.
$$

---

**Example 3 (HOTS):**  
Given $ \sin x = \frac{3}{5} $ with $ x $ in the first quadrant, find $ \tan^2 x $ and $ \sec^2 x $.

**Solution:**

- Step 1: Use the fundamental identity:

$$
\cos^2 x = 1 - \sin^2 x = 1 - \left( \frac{3}{5} \right)^2 = 1 - \frac{9}{25} = \frac{16}{25}.
$$

- Step 2: Find $ \cos x $:

$$
\cos x = \sqrt{\frac{16}{25}} = \frac{4}{5} \quad (\text{positive in first quadrant}).
$$

- Step 3: Calculate $ \tan x = \frac{\sin x}{\cos x} = \frac{3/5}{4/5} = \frac{3}{4} $.

Therefore,

$$
\tan^2 x = \left( \frac{3}{4} \right)^2 = \frac{9}{16}.
$$

- Step 4: Use identity $ \sec^2 x = 1 + \tan^2 x $:

$$
\sec^2 x = 1 + \frac{9}{16} = \frac{25}{16}.
$$

---

Understanding and applying these fundamental trigonometric identities empower students to solve complex problems efficiently in mathematics and related fields.

---

## 3.6 Angle Addition and Subtraction Formulas

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Geometric representation of angle addition on unit circle" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.6.1:</b> Geometric representation showing angle addition on the unit circle</i></figcaption>
</figure>

**Introduction:**

The angle addition and subtraction formulas are vital identities in trigonometry that allow us to find the sine, cosine, and tangent of the sum or difference of two angles. These formulas play a significant role in simplifying trigonometric expressions and solving equations involving multiple angles.

---

### 3.6.1 Sine and Cosine Addition and Subtraction Formulas

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Diagram explaining sine and cosine addition formulas with corresponding right triangles" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.6.2:</b> Illustration of sine and cosine addition using triangles and angles</i></figcaption>
</figure>

**Theorems (Boxed):**

$$
\boxed{
\begin{aligned}
\sin(x + y) &= \sin x \cos y + \cos x \sin y, \\
\sin(x - y) &= \sin x \cos y - \cos x \sin y, \\
\cos(x + y) &= \cos x \cos y - \sin x \sin y, \\
\cos(x - y) &= \cos x \cos y + \sin x \sin y.
\end{aligned}
}
$$

---

**Proof of Sine Addition Formula:**

- Step 1: Consider two angles $ x $ and $ y $ on the unit circle and points corresponding to these angles.
- Step 2: Using the coordinates of these points, express $ \sin(x+y) $ in terms of $ \sin x, \cos x, \sin y, \cos y $.
- Step 3: Using trigonometric definitions and algebraic manipulation, derive:
  $$
  \sin(x + y) = \sin x \cos y + \cos x \sin y.
  $$

Similarly, the cosine addition and subtraction formulas are proved using analogous steps exploiting the same geometric setup.

---

### 3.6.2 Tangent Addition and Subtraction Formulas

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Graphical interpretation of tangent addition formula" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.6.3:</b> Construction visualizing tangent addition and subtraction</i></figcaption>
</figure>

**Theorems (Boxed):**

$$
\boxed{
\begin{aligned}
\tan(x + y) &= \frac{\tan x + \tan y}{1 - \tan x \tan y}, \\
\tan(x - y) &= \frac{\tan x - \tan y}{1 + \tan x \tan y}.
\end{aligned}
}
$$

**Proof:**

- Step 1: Express tangent in terms of sine and cosine:
  $$
  \tan(x + y) = \frac{\sin(x + y)}{\cos(x + y)}.
  $$
- Step 2: Substitute sine and cosine addition formulas.
- Step 3: Divide numerator and denominator by $ \cos x \cos y $.
- Step 4: After simplification, obtain the tangent addition formula.

The tangent subtraction formula follows similarly by analogy.

---

### Formulas Summary:

$$
\boxed{
\begin{aligned}
\sin(x \pm y) &= \sin x \cos y \pm \cos x \sin y, \\
\cos(x \pm y) &= \cos x \cos y \mp \sin x \sin y, \\
\tan(x \pm y) &= \frac{\tan x \pm \tan y}{1 \mp \tan x \tan y}.
\end{aligned}
}
$$

---

### Working Rule (Algorithm) for Using Angle Addition and Subtraction Formulas

1. Identify if the problem involves the sum or difference of two angles.  
2. Determine the required trigonometric function (sine, cosine, or tangent).  
3. Express the function using the corresponding addition or subtraction formula.  
4. Substitute known angle values or algebraic expressions.  
5. Simplify the resulting expression algebraically.  
6. Verify domain constraints to avoid division by zero in tangent formulas.

---

### Graded Solved Examples

---

**Example 1 (Concept Building):**  
Calculate $\sin(75^\circ)$ using the sine addition formula.

**Solution:**

- Step 1: Express $75^\circ$ as $30^\circ + 45^\circ$.  
- Step 2: Use formula:
  $$
  \sin(75^\circ) = \sin 30^\circ \cos 45^\circ + \cos 30^\circ \sin 45^\circ.
  $$
- Step 3: Substitute values:  
  $$
  = \frac{1}{2} \times \frac{\sqrt{2}}{2} + \frac{\sqrt{3}}{2} \times \frac{\sqrt{2}}{2} = \frac{\sqrt{2}}{4} + \frac{\sqrt{6}}{4} = \frac{\sqrt{2} + \sqrt{6}}{4}.
  $$

---

**Example 2 (Competency Based):**  
Find $\cos(15^\circ)$ using the cosine subtraction formula.

**Solution:**

- Step 1: Express $15^\circ = 45^\circ - 30^\circ$.  
- Step 2: Use formula:
  $$
  \cos(15^\circ) = \cos 45^\circ \cos 30^\circ + \sin 45^\circ \sin 30^\circ.
  $$
- Step 3: Substitute values:  
  $$
  = \frac{\sqrt{2}}{2} \times \frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2} \times \frac{1}{2} = \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4} = \frac{\sqrt{6} + \sqrt{2}}{4}.
  $$

---

**Example 3 (HOTS):**  
Evaluate $\tan(75^\circ)$ using the tangent addition formula.

**Solution:**

- Step 1: Express $75^\circ = 45^\circ + 30^\circ$.  
- Step 2: Use formula:
  $$
  \tan(75^\circ) = \frac{\tan 45^\circ + \tan 30^\circ}{1 - \tan 45^\circ \tan 30^\circ}.
  $$
- Step 3: Substitute values:
  $$
  = \frac{1 + \frac{1}{\sqrt{3}}}{1 - 1 \times \frac{1}{\sqrt{3}}} = \frac{1 + \frac{1}{\sqrt{3}}}{1 - \frac{1}{\sqrt{3}}}.
  $$
- Step 4: Rationalize:
  $$
  = \frac{\frac{\sqrt{3} + 1}{\sqrt{3}}}{\frac{\sqrt{3} - 1}{\sqrt{3}}} = \frac{\sqrt{3} + 1}{\sqrt{3} - 1}.
  $$

---

Mastering these formulas and their applications will enhance problem-solving capability in trigonometry and its practical applications.

---

## 3.6 Angle Addition and Subtraction Formulas

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Geometric representation of angle addition on unit circle" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.6.1:</b> Geometric representation showing angle addition on the unit circle</i></figcaption>
</figure>

**Introduction:**

The angle addition and subtraction formulas are vital identities in trigonometry that allow us to find the sine, cosine, and tangent of the sum or difference of two angles. These formulas play a significant role in simplifying trigonometric expressions and solving equations involving multiple angles.

---

### 3.6.1 Sine and Cosine Addition and Subtraction Formulas

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Diagram explaining sine and cosine addition formulas with corresponding right triangles" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.6.2:</b> Illustration of sine and cosine addition using triangles and angles</i></figcaption>
</figure>

**Theorems (Boxed):**

$$
\boxed{
\begin{aligned}
\sin(x + y) &= \sin x \cos y + \cos x \sin y, \\
\sin(x - y) &= \sin x \cos y - \cos x \sin y, \\
\cos(x + y) &= \cos x \cos y - \sin x \sin y, \\
\cos(x - y) &= \cos x \cos y + \sin x \sin y.
\end{aligned}
}
$$

---

**Proof of Sine Addition Formula:**

- Step 1: Consider two angles $ x $ and $ y $ on the unit circle and points corresponding to these angles.
- Step 2: Using coordinates of these points, express $ \sin(x+y) $ in terms of $ \sin x, \cos x, \sin y, \cos y $.
- Step 3: Using trigonometric definitions and algebraic manipulation, derive:
  $$
  \sin(x + y) = \sin x \cos y + \cos x \sin y.
  $$

Similarly, cosine formulas are proved using analogous steps exploiting the same geometric setup.

---

### 3.6.2 Tangent Addition and Subtraction Formulas

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Graphical interpretation of tangent addition formula" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.6.3:</b> Construction visualizing tangent addition and subtraction</i></figcaption>
</figure>

**Theorems (Boxed):**

$$
\boxed{
\begin{aligned}
\tan(x + y) &= \frac{\tan x + \tan y}{1 - \tan x \tan y}, \\
\tan(x - y) &= \frac{\tan x - \tan y}{1 + \tan x \tan y}.
\end{aligned}
}
$$

**Proof:**

- Step 1: Express tangent in terms of sine and cosine:
  $$
  \tan(x + y) = \frac{\sin(x + y)}{\cos(x + y)}.
  $$
- Step 2: Substitute sine and cosine addition formulas.
- Step 3: Divide numerator and denominator by $ \cos x \cos y $.
- Step 4: After simplification, obtain the tangent addition formula.

The tangent subtraction formula follows by analogy.

---

### Formulas Summary:

$$
\boxed{
\begin{aligned}
\sin(x \pm y) &= \sin x \cos y \pm \cos x \sin y, \\
\cos(x \pm y) &= \cos x \cos y \mp \sin x \sin y, \\
\tan(x \pm y) &= \frac{\tan x \pm \tan y}{1 \mp \tan x \tan y}.
\end{aligned}
}
$$

---

### Working Rule (Algorithm) for Using Angle Addition and Subtraction Formulas

1. Identify if the problem is about the sum or difference of two angles.  
2. Determine the required trigonometric function (sine, cosine, tangent).  
3. Express the function using the corresponding addition or subtraction formula.  
4. Substitute known angle values or expressions.  
5. Simplify the expression by performing algebraic operations.  
6. Verify domain constraints to avoid division by zero in tangent formulas.

---

### Graded Solved Examples

---

**Example 1 (Concept Building):**  
Calculate $\sin(75^\circ)$ using the sine addition formula.

**Solution:**

- Step 1: Express $75^\circ$ as $30^\circ + 45^\circ$.  
- Step 2: Use formula:
  $$
  \sin(75^\circ) = \sin 30^\circ \cos 45^\circ + \cos 30^\circ \sin 45^\circ.
  $$  
- Step 3: Substitute values:  
  $$
  = \frac{1}{2} \times \frac{\sqrt{2}}{2} + \frac{\sqrt{3}}{2} \times \frac{\sqrt{2}}{2} = \frac{\sqrt{2}}{4} + \frac{\sqrt{6}}{4} = \frac{\sqrt{2} + \sqrt{6}}{4}.
  $$

---

**Example 2 (Competency Based):**  
Find $\cos(15^\circ)$ using cosine subtraction formula.

**Solution:**

- Step 1: Express $15^\circ = 45^\circ - 30^\circ$.  
- Step 2: Use formula:
  $$
  \cos(15^\circ) = \cos 45^\circ \cos 30^\circ + \sin 45^\circ \sin 30^\circ.
  $$  
- Step 3: Substitute values:  
  $$
  = \frac{\sqrt{2}}{2} \times \frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2} \times \frac{1}{2} = \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4} = \frac{\sqrt{6} + \sqrt{2}}{4}.
  $$

---

**Example 3 (HOTS):**  
Evaluate $\tan(75^\circ)$ using tangent addition formula.

**Solution:**

- Step 1: Express $75^\circ = 45^\circ + 30^\circ$.  
- Step 2: Use formula:
  $$
  \tan(75^\circ) = \frac{\tan 45^\circ + \tan 30^\circ}{1 - \tan 45^\circ \tan 30^\circ}.
  $$  
- Step 3: Substitute values:
  $$
  = \frac{1 + \frac{1}{\sqrt{3}}}{1 - 1 \times \frac{1}{\sqrt{3}}} = \frac{1 + \frac{1}{\sqrt{3}}}{1 - \frac{1}{\sqrt{3}}}.
  $$  
- Step 4: Rationalize:
  $$
  = \frac{\frac{\sqrt{3} + 1}{\sqrt{3}}}{\frac{\sqrt{3} - 1}{\sqrt{3}}} = \frac{\sqrt{3} + 1}{\sqrt{3} - 1}.
  $$

---

Mastering these formulas and their applications will enhance problem-solving capability in trigonometry and its practical applications.

---

## 3.8 Solving Trigonometric Equations

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Graphical illustration showing sine equation solutions and their periodic nature" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.8.1:</b> Graphical depiction of solutions to sine equation indicating periodicity</i></figcaption>
</figure>

**Introduction:**

Solving trigonometric equations is a fundamental aspect of trigonometry, which enables us to find all possible angles satisfying a given trigonometric condition. The equations often have infinitely many solutions due to the periodic nature of trigonometric functions. In this section, we explore methods to solve basic trigonometric equations, utilize trigonometric identities to simplify problems, and express solutions in their general forms.

---

### 3.8.1 Basic Trigonometric Equations

**Definition:**  
A trigonometric equation is an equation that involves trigonometric functions such as sine, cosine, tangent, and their reciprocals. It may generally be expressed as:

$$
f(x) = c,
$$

where $f(x)$ is a trigonometric function and $c$ is a constant.

**Geometric Meaning:**  
On the unit circle, solving such equations corresponds to finding all angles $x$ for which the function equals the given constant, considering the periodicity.

---

### 3.8.2 Use of Identities in Solving Equations

**Theorem (Trigonometric Identities Application):**  
Trigonometric identities allow transformation of complex equations into simpler forms that are easier to solve. This includes Pythagorean identities, angle sum and difference formulas, double angle and half angle formulas.

**Proof (Conceptual):**  
Using identities like

$$
\sin^2 x + \cos^2 x = 1,
$$

or

$$
\sin(x \pm y) = \sin x \cos y \pm \cos x \sin y,
$$

we rewrite equations into equivalents where solutions can be obtained by standard techniques.

---

### 3.8.3 General Solutions for Equations

**General Solution Forms:**  

- For $ \sin x = k $, with $ -1 \leq k \leq 1 $:

$$
\boxed{
x = \arcsin k + 2n\pi, \quad \text{or} \quad x = \pi - \arcsin k + 2n\pi, \quad n \in \mathbb{Z}
}
$$

- For $ \cos x = k $, with $ -1 \leq k \leq 1 $:

$$
\boxed{
x = \pm \arccos k + 2n\pi, \quad n \in \mathbb{Z}
}
$$

- For $ \tan x = k $, with $ k \in \mathbb{R} $:

$$
\boxed{
x = \arctan k + n\pi, \quad n \in \mathbb{Z}
}
$$

---

### Formulas Summary

$$
\boxed{
\begin{aligned}
& \sin x = k \implies x = \arcsin k + 2n\pi \quad \text{or} \quad x = \pi - \arcsin k + 2n\pi, \\
& \cos x = k \implies x = \pm \arccos k + 2n\pi, \\
& \tan x = k \implies x = \arctan k + n\pi.
\end{aligned}
}
$$

---

### Working Rule (Algorithm) for Solving Trigonometric Equations:

1. **Simplify the equation:** Use algebraic manipulation and trigonometric identities to reduce the equation to a basic form involving sine, cosine, or tangent equal to a constant.
2. **Find principal solution(s):** Use inverse trigonometric functions or known special angle values.
3. **Write general solutions:** Add periodic terms $ 2n\pi $ for sine and cosine functions, and $ n\pi $ for tangent, to account for all possible solutions.
4. **Check domain constraints:** Verify that the values satisfy the original domain restrictions and equation.

---

### Graded Solved Examples

---

**Example 1 (Concept Building):**  
Solve $ \sin x = \frac{1}{2} $.

**Solution:**

- Step 1: Principal solutions: $ x = \frac{\pi}{6} $ and $ x = \pi - \frac{\pi}{6} = \frac{5\pi}{6} $.
- Step 2: General solution:

$$
x = \frac{\pi}{6} + 2n\pi \quad \text{or} \quad x = \frac{5\pi}{6} + 2n\pi, \quad n \in \mathbb{Z}.
$$

---

**Example 2 (Competency Based):**  
Solve $ 2 \cos^2 x - 3 \cos x + 1 = 0 $.

**Solution:**

- Step 1: Let $ u = \cos x $, rewrite:

$$
2 u^2 - 3 u + 1 = 0.
$$

- Step 2: Factorize:

$$
(2u - 1)(u - 1) = 0 \implies u = \frac{1}{2} \quad \text{or} \quad u = 1.
$$

- Step 3: Solve for $ x $:

For $ \cos x = \frac{1}{2} $: 

$$
x = \pm \frac{\pi}{3} + 2n\pi.
$$

For $ \cos x = 1 $:

$$
x = 2n\pi.
$$

---

**Example 3 (HOTS):**  
Solve $ \sin 2x = \sqrt{3} \cos x $ for $ x \in [0, 2\pi] $.

**Solution:**

- Step 1: Use double angle formula: $ \sin 2x = 2 \sin x \cos x $.

Rewrite the equation:

$$
2 \sin x \cos x = \sqrt{3} \cos x.
$$

- Step 2: Bring all terms to one side:

$$
2 \sin x \cos x - \sqrt{3} \cos x = 0,
$$

or

$$
\cos x (2 \sin x - \sqrt{3}) = 0.
$$

- Step 3: Solve each factor:

- $ \cos x = 0 \implies x = \frac{\pi}{2}, \frac{3\pi}{2}. $  
- $ 2 \sin x - \sqrt{3} = 0 \implies \sin x = \frac{\sqrt{3}}{2} \implies x = \frac{\pi}{3}, \frac{2\pi}{3}. $

---

Mastery over solving trigonometric equations involves understanding how to manipulate expressions, utilize identities, and capture all solutions through general solution formulas.

---

## 3.9 Inverse Trigonometric Functions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Graphs of inverse sine, inverse cosine and inverse tangent functions" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.9.1:</b> Graphs of arcsin(x), arccos(x), and arctan(x) showing domain and range</i></figcaption>
</figure>

**Introduction:**

Inverse trigonometric functions allow us to find the angle corresponding to a given value of a trigonometric function. They provide a way to "undo" the trigonometric function and are extensively used to determine unknown angles when side ratios are known, particularly in triangle problems.

---

### 3.9.1 Definition and Principal Values

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Unit circle highlighting principal value ranges of inverse trigonometric functions" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.9.2:</b> Unit circle illustrating principal value ranges of inverse trigonometric functions</i></figcaption>
</figure>

**Definition:**  
For a trigonometric function $ f $, its inverse $ f^{-1} $ maps values from the range of $ f $ back to angles in its domain. For instance, the inverse sine function, denoted $ \arcsin x $ or $ \sin^{-1} x $, gives the angle whose sine is $ x $.

**Principal Value Branch:**  
Due to the non-one-to-one nature of trigonometric functions, restricted domains are chosen to define inverses uniquely.

| Function         | Symbol         | Principal Domain (for inverse)                             | Range of Inverse             |
|------------------|----------------|------------------------------------------------------------|------------------------------|
| Sine             | $ \arcsin x $  | $\left[- \frac{\pi}{2}, \frac{\pi}{2}\right]$             | $[-1, 1]$                  |
| Cosine           | $ \arccos x $  | $[0, \pi]$                                              | $[-1, 1]$                  |
| Tangent          | $ \arctan x $  | $\left( - \frac{\pi}{2}, \frac{\pi}{2} \right)$           | $ \mathbb{R} $             |
| Cotangent        | $ \arccot x $  | $(0, \pi)$                                              | $ \mathbb{R} $             |
| Secant           | $ \arcsec x $  | $\left[0, \frac{\pi}{2}\right) \cup \left(\frac{\pi}{2}, \pi\right]$ | $ (-\infty, -1] \cup [1, \infty) $ |
| Cosecant         | $ \arccsc x $  | $\left[- \frac{\pi}{2}, 0\right) \cup \left(0, \frac{\pi}{2}\right]$ | $ (-\infty, -1] \cup [1, \infty) $ |

---

### 3.9.2 Properties and Graphs

- **Domain and Range:** Inverse trigonometric functions have restricted domains to ensure their invertibility.  
- **Continuity and Monotonicity:** On each principal domain, these inverse functions are continuous and strictly monotonic.  
- **Symmetry:**  
  - $ \arcsin(-x) = -\arcsin x $ (odd function)  
  - $ \arccos(-x) = \pi - \arccos x $ (neither odd nor even)  
  - $ \arctan(-x) = -\arctan x $ (odd function)  

- **Graphs:**  
  The graphs of inverse functions are reflections of the original trigonometric functions’ graphs about the line $ y = x $, restricted within their principal domains and ranges.

---

### 3.9.3 Applications in Finding Angles

Inverse trigonometric functions are crucial for:

- Calculating angles given side ratios in right triangles:  
  For example, if the lengths of the opposite side and hypotenuse are known,  
  $$
  \theta = \arcsin \left( \frac{\text{opposite}}{\text{hypotenuse}} \right).
  $$

- Solving trigonometric equations where the variable is inside a trigonometric function.

---

### Formulas Summary

$$
\boxed{
\begin{aligned}
& y = \arcsin x \iff x = \sin y, \quad y \in \left[- \frac{\pi}{2}, \frac{\pi}{2} \right], \\
& y = \arccos x \iff x = \cos y, \quad y \in [0, \pi], \\
& y = \arctan x \iff x = \tan y, \quad y \in \left( -\frac{\pi}{2}, \frac{\pi}{2} \right).
\end{aligned}
}
$$

---

### Working Rule (Algorithm) for Using Inverse Trigonometric Functions

1. **Identify the ratio or value** whose corresponding angle needs to be found.  
2. **Select the appropriate inverse function** based on the given trigonometric ratio (sine, cosine, or tangent).  
3. **Check the value lies within the domain** of the inverse function.  
4. **Compute or estimate the inverse function value** (using tables, calculators, or known special angles).  
5. **Interpret the angle within the principal domain** to find the correct solution.  
6. If needed, use symmetry or periodicity properties to find other solutions.

---

### Graded Solved Examples

---

**Example 1 (Concept Building):**  
Find $ \theta = \arcsin \frac{1}{2} $.

**Solution:**

- Step 1: Recognize that $ \sin \frac{\pi}{6} = \frac{1}{2} $.  
- Step 2: Therefore,  
  $$
  \theta = \frac{\pi}{6}.
  $$

---

**Example 2 (Competency Based):**  
Find the value of $ \arccos \left(- \frac{1}{2} \right) $.

**Solution:**

- Step 1: Note that $ \cos \frac{2\pi}{3} = -\frac{1}{2} $.  
- Step 2: Hence,  
  $$
  \arccos \left(- \frac{1}{2}\right) = \frac{2\pi}{3}.
  $$

---

**Example 3 (HOTS):**  
Solve $ \arctan x = \frac{\pi}{4} $.

**Solution:**

- Step 1: From the definition,  
  $$
  x = \tan \frac{\pi}{4} = 1.
  $$

---

This completes the detailed study of inverse trigonometric functions, their definitions, properties, graphs, and applications essential for Class 11 Mathematics.

---

## 3.10 Applications of Trigonometric Functions

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Diagram illustrating height and distance problem with angles and right triangle" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.10.1:</b> Right triangle model representing a height and distance problem</i></figcaption>
</figure>

**Introduction:**

Trigonometric functions play an important role in solving real-world problems involving angles and distances. From calculating heights and distances to modeling periodic phenomena, the applications of trigonometry extend far beyond theory into practical scenarios. This section explores various classic applications, equipping students with the methodology to approach and solve such problems using trigonometric concepts.

---

### 3.10.1 Height and Distance Problems

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Geometric setup of an observer, object height and angle of elevation" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.10.2:</b> Angle of elevation and distance in height and distance problem</i></figcaption>
</figure>

**Definition:**

Height and distance problems involve calculating the height of an object or the distance between two objects using measures of angles of elevation or depression and trigonometric functions.

**Geometric Meaning:**

- The problem is modeled with right triangles where trigonometric ratios such as sine, cosine, and tangent represent the relationships between height, distance, and angles.
- Angles of elevation and depression are angles formed with the horizontal or ground level.

---

**Formulas & Concepts:**

For a right triangle with height $h$, distance $d$, and angle $ \theta $:

- Angle of elevation:

$$
\tan \theta = \frac{h}{d} \implies h = d \tan \theta.
$$

- Angle of depression uses the same relation, considering geometry.

---

**Working Rule (Algorithm):**

1. Identify the given quantities — angle of elevation/depression, distance, or height.
2. Draw a diagram representing the scenario as a right triangle.
3. Choose the correct trigonometric ratio based on known sides/angles.
4. Formulate the equation using sine, cosine, or tangent.
5. Solve for the unknown quantity using algebraic manipulation.

---

**Example:**

A person standing 50 m away from a tower observes an angle of elevation of $ 30^\circ $. Find the height of the tower.

**Solution:**

- Step 1: Let height of tower = $h$, distance $d = 50$ m.
- Step 2: Using tangent relation:

$$
\tan 30^\circ = \frac{h}{50}.
$$

- Step 3: $ \tan 30^\circ = \frac{1}{\sqrt{3}} $, so

$$
h = 50 \times \frac{1}{\sqrt{3}} = \frac{50 \sqrt{3}}{3} \approx 28.87 \text{ m}.
$$

---

### 3.10.2 Inclination and Bearings

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Diagram illustrating bearing and inclination angles in navigation" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.10.3:</b> Representation of bearing and inclination with directions and angles</i></figcaption>
</figure>

**Definition:**

- **Inclination** is the angle made by a line or surface with the horizontal.
- **Bearing** refers to the direction of an object in navigation, measured clockwise from north.

**Geometric Interpretation:**

- Bearings are expressed as angles from the north direction on the compass rose, and trigonometric functions help calculate components of displacement.
- The problem is often modeled in coordinate planes or right triangles.

---

**Working Rule (Algorithm):**

1. Identify the bearing angle given or to be found.
2. Represent the problem on a north-south and east-west coordinate system.
3. Use trigonometric functions to find distances or angles based on bearings.
4. Solve the problem using known ratios and coordinate geometry.

---

**Example:**

A ship sails on a bearing of $ 60^\circ $ for 30 km. Compute the eastward and northward distances covered.

**Solution:**

- Step 1: Let eastward distance = $x$, northward distance = $y$.
- Step 2: From bearing $60^\circ$:

$$
x = 30 \sin 60^\circ = 30 \times \frac{\sqrt{3}}{2} = 15 \sqrt{3} \approx 25.98 \text{ km}.
$$

$$
y = 30 \cos 60^\circ = 30 \times \frac{1}{2} = 15 \text{ km}.
$$

---

### 3.10.3 Modeling Periodic Phenomena

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Graph showing periodic sine wave representing periodic phenomena" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.10.4:</b> Sine wave modeling periodic natural phenomena</i></figcaption>
</figure>

**Definition:**

Periodic phenomena are natural or physical processes that repeat values over time, modeled effectively by trigonometric functions like sine and cosine.

**Geometric Meaning:**

- The periodicity of sine and cosine graphs represents cycles in phenomena like sound waves, tides, daylight hours, and mechanical vibrations.

---

**Working Rule (Algorithm):**

1. Identify periodic nature and period $T$.
2. Represent the quantity as a function $ y = A \sin (\omega t + \phi) $ or $ y = A \cos (\omega t + \phi) $, where $ \omega = \frac{2\pi}{T} $.
3. Use initial conditions to find amplitude $A$, phase shift $ \phi $.
4. Use the function to predict future behavior or other quantities.

---

**Example:**

A city's daylight hours vary periodically with period 365 days. Suppose the amount of daylight $D$ days after January 1 is modeled by:

$$
D = 12 + 3 \sin \left( \frac{2\pi}{365} t \right).
$$

Find daylight hours 91 days after January 1 (April 1).

**Solution:**

- Step 1:

$$
D = 12 + 3 \sin \left( \frac{2\pi}{365} \times 91 \right).
$$

- Step 2:

Calculate inside sine:

$$
\frac{2\pi}{365} \times 91 = \frac{182\pi}{365} \approx 1.567 \text{ radians}.
$$

- Step 3:

Calculate:

$$
\sin 1.567 \approx 0.9999.
$$

- Step 4:

So,

$$
D \approx 12 + 3 \times 0.9999 = 15 \text{ hours (approximately)}.
$$

---

### 3.10.4 Real World Applications

Trigonometric functions are used extensively in:

- **Navigation and Surveying:** Calculating distances and angles.  
- **Engineering:** Design of mechanical components involving rotations and waves.  
- **Physics:** Analysis of oscillations, waves, and harmonic motion.  
- **Astronomy:** Computing positions and movements of celestial bodies.  

---

### Summary of Key Formulas

$$
\boxed{
\begin{aligned}
& \tan \theta = \frac{\text{Height}}{\text{Distance}}, \\
& x = d \sin \alpha, \quad y = d \cos \alpha \quad \text{(components from bearing)}, \\
& y = A \sin (\omega t + \phi) \quad \text{(periodic phenomena)}.
\end{aligned}
}
$$

---

### Complete Working Rule (Algorithm) for Solving Application Problems

1. Draw a neat diagram representing all given parameters and unknowns.  
2. Identify relevant angles and sides.  
3. Choose and write appropriate trigonometric ratios or models.  
4. Substitute known values and solve for unknowns algebraically.  
5. Interpret the answers in the context of the problem.

---

### Graded Solved Examples

---

**Example 1 (Concept Building):**  
Find the height of a tree if the angle of elevation from a point 20 m away is $ 45^\circ $.

**Solution:**

- Step 1: Use $ \tan \theta = \frac{\text{height}}{\text{distance}} $.

- Step 2:

$$
\tan 45^\circ = \frac{h}{20} \implies 1 = \frac{h}{20} \implies h = 20 \text{ m}.
$$

---

**Example 2 (Competency Based):**  
A ship sails 40 km on a bearing $ 60^\circ $. Find its northward and eastward displacement.

**Solution:**

- Step 1:

$$
\text{Eastward} = 40 \sin 60^\circ = 40 \times \frac{\sqrt{3}}{2} = 20 \sqrt{3}.
$$

- Step 2:

$$
\text{Northward} = 40 \cos 60^\circ = 40 \times \frac{1}{2} = 20.
$$

---

**Example 3 (HOTS):**  
The temperature varies sinusoidally during the day as:

$$
T(t) = 15 + 10 \sin \left( \frac{\pi}{12} t - \frac{\pi}{2} \right),
$$

where $t$ is time in hours after midnight. Find the temperature at 6 AM.

**Solution:**

- Step 1: Substitute $ t = 6 $.

- Step 2:

$$
T(6) = 15 + 10 \sin \left( \frac{\pi}{12} \times 6 - \frac{\pi}{2} \right) = 15 + 10 \sin \left( \frac{\pi}{2} - \frac{\pi}{2} \right) = 15 + 10 \sin 0 = 15.
$$

---

Mastering these applications will deepen the understanding of trigonometric functions and their practical impact.

---

## 3.11 Problem Classification and Solution Techniques

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Classification of trigonometric problem types shown by geometric figures and formula applications" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.11.1:</b> Classification of trigonometric problem types with geometric and formulaic representations</i></figcaption>
</figure>

**Introduction:**

Trigonometric problems come in various forms and require diverse approaches for their solutions. Understanding how to classify these problems and selecting the proper solution technique is central to solving them effectively. This section covers three fundamental solution approaches: direct computation of trigonometric ratios, using identities creatively for simplification, and applying formulas to different problem types.

---

### 3.11.1 Direct Computation of Trigonometric Ratios

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Right triangle with sides labeled, showing sine, cosine, and tangent calculations" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.11.2:</b> Right triangle demonstrating direct computation of sine, cosine, and tangent ratios</i></figcaption>
</figure>

**Definition:**  
Direct computation involves using the primary definitions of sine, cosine, and tangent based on the sides of a right-angled triangle.

- $ \sin \theta = \frac{\text{Opposite side}}{\text{Hypotenuse}} $
- $ \cos \theta = \frac{\text{Adjacent side}}{\text{Hypotenuse}} $
- $ \tan \theta = \frac{\text{Opposite side}}{\text{Adjacent side}} $

**Geometric Interpretation:**  
These ratios directly measure the relationships between sides relative to an angle in a right triangle, providing meaningful geometric insights.

---

### 3.11.2 Using Identities in Problem Solving

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Formula chart showing basic trigonometric identities" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.11.3:</b> Basic trigonometric identities essential for problem solving</i></figcaption>
</figure>

**Theorem (Using Identities):**  
Trigonometric identities such as Pythagorean, addition-subtraction, double angle, and half angle formulas allow complex expressions and equations to be transformed into manageable forms for evaluation or proof.

---

**Proof (Conceptual):**  
By substituting complex expressions with their equivalent identities, many complicated problems reduce to simpler ones involving standard angles or easily computable ratios.

---

### Standard Key Identities Used:

$$
\boxed{
\begin{aligned}
& \sin^2 x + \cos^2 x = 1, \\
& \sin (x \pm y) = \sin x \cos y \pm \cos x \sin y, \\
& \cos (x \pm y) = \cos x \cos y \mp \sin x \sin y, \\
& \tan (x \pm y) = \frac{\tan x \pm \tan y}{1 \mp \tan x \tan y}, \\
& \sin 2x = 2 \sin x \cos x, \quad \cos 2x = \cos^2 x - \sin^2 x,
\end{aligned}
}
$$

and others.

---

### 3.11.3 Application of Formulas in Various Problem Types

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/placeholder" alt="Flow chart showing approach to different trigonometric problem types" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.11.4:</b> Flowchart for selecting formulas based on problem classification</i></figcaption>
</figure>

---

**Working Rule (Algorithm):**

1. **Step 1:** Analyze the problem to identify whether it's asking for basic ratio evaluation, equation solving, or expression simplification.

2. **Step 2:** For direct computation, use the triangle side-based definitions of trigonometric functions.

3. **Step 3:** When expressions involve sums, differences, multiples, or powers of angles, select the appropriate identities or formulas.

4. **Step 4:** Simplify the expression or equation by applying identities, reducing to known values or to simpler equations.

5. **Step 5:** Solve the resulting trigonometric equation if applicable, considering the domain and principal values.

6. **Step 6:** Cross-verify solutions using unit circle values or known trigonometric function properties to ensure validity.

---

### Graded Solved Examples

---

**Example 1 (Concept Building):**  
Calculate $ \sin 75^\circ $ by direct computation using identities.

**Solution:**

- Step 1: Express $ 75^\circ = 45^\circ + 30^\circ $.

- Step 2: Use sine addition formula:

$$
\sin 75^\circ = \sin (45^\circ + 30^\circ) = \sin 45^\circ \cos 30^\circ + \cos 45^\circ \sin 30^\circ.
$$

- Step 3: Substitute known values:

$$
= \frac{\sqrt{2}}{2} \times \frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2} \times \frac{1}{2} = \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4} = \frac{\sqrt{6} + \sqrt{2}}{4}.
$$

---

**Example 2 (Competency Based):**  
Simplify the expression $ \sin^2 x - \cos^2 x $.

**Solution:**

- Step 1: Recognize

$$
\sin^2 x - \cos^2 x = -(\cos^2 x - \sin^2 x).
$$

- Step 2: Use the double angle formula:

$$
\cos 2x = \cos^2 x - \sin^2 x,
$$

so

$$
\sin^2 x - \cos^2 x = -\cos 2x.
$$

---

**Example 3 (HOTS):**  
Prove that

$$
\frac{\sin x + \sin 3x}{\cos x + \cos 3x} = \tan 2x.
$$

**Solution:**

- Step 1: Use sum-to-product formulas:

$$
\sin A + \sin B = 2 \sin \frac{A+B}{2} \cos \frac{A-B}{2},
$$

$$
\cos A + \cos B = 2 \cos \frac{A+B}{2} \cos \frac{A-B}{2}.
$$

- Step 2: Let $ A = 3x, B = x $. Then:

$$
\sin x + \sin 3x = 2 \sin 2x \cos x,
$$

$$
\cos x + \cos 3x = 2 \cos 2x \cos x.
$$

- Step 3: The original expression becomes:

$$
\frac{2 \sin 2x \cos x}{2 \cos 2x \cos x} = \frac{\sin 2x}{\cos 2x} = \tan 2x.
$$

---

By understanding the nature of trigonometric problems and systematically applying the appropriate formulas and definitions, students can tackle a wide variety of problems with confidence and precision.

---

