examples = '''Examples (Same ```Problem Statement``` and ```Rubric```):

```Student Essay``` : - change in momentum is 0 so pf and pi are equal\n- plug in variables for both and solve for the velocity of the block\n- m + mb should be used for mass of block\n- apply energy principle\n- cancel out things that appear on both sides\n- solve for velocity of block

```Response Template``` : 
<table class="table table-striped">
  <thead>
    <tr>
      <th>Category</th>
      <th>Score</th>
      <th>Comments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Essential Information</td>
      <td>2.0</td>
      <td>The essay mentions some components necessary to solve the problem but lacks a clear statement of the conservation of momentum and energy, as well as initial conditions for both blocks.</td>
    </tr>
    <tr>
      <td>Physics Concepts</td>
      <td>2.0</td>
      <td>The essay refers to the energy principle and conservation of momentum implicitly but fails to explicitly state and justify the use of these principles.</td>
    </tr>
    <tr>
      <td>Specific Application</td>
      <td>2.0</td>
      <td>The application of the physics to the specific conditions is hinted at, but not laid out with enough detail or clarity.</td>
    </tr>
    <tr>
      <td>Mathematical Procedures</td>
      <td>1.0</td>
      <td>The mathematical procedure is not properly explained or shown, and the essay suggests a method of cancellation without any equations or expressions to demonstrate this.</td>
    </tr>
    <tr>
      <td>Logical Progression</td>
      <td>2.0</td>
      <td>The essay has a basic structure but lacks a coherent step-by-step explanation that clearly shows the progression from start to finish.</td>
    </tr>
    <tr>
      <th>Overall Score</th>
      <td>9.0</td>
      <td>The essay attempts to solve the problem but is not thorough or explicit in its approach, missing detailed explanations and clear physics and mathematical applications.</td>
    </tr>
  </tbody>
</table>

```Student Essay``` : Because immediately after the collision of the bullet and the block all energy is \nkinetic, because at the moment the block reaches its max height all energy is \npotential, and finally because total energy is constant in the system, I was able \nto equate the kinetic energy after the collision with the potential energy at the \nmax height and was able to use that to solve for V in the kinetic equation.

<table class="table table-bordered">
  <thead>
    <tr>
      <th scope="col">Category</th>
      <th scope="col">Points Awarded</th>
      <th scope="col">Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Essential Information</td>
        <td>2.0</td>
        <td>The essay attempts to relate kinetic and potential energy, but it is missing essential information regarding momentum conservation and elastic collision equations which are key to solving the problem stated.</td>
    </tr>
    <tr>
      <td>Physics Concepts</td>
        <td>1.0</td>
        <td>The student incorrectly applied the concept of conservation of energy to an elastic collision without considering momentum conservation. An elastic collision problem requires both kinetic energy and momentum conservation.</td>
    </tr>
    <tr>
      <td>Specific Application</td>
      <td>1.0</td>
      <td>The specific application of physics to this problem is incorrect. While energy conservation is mentioned, the student does not apply the correct conservation laws for an elastic collision.</td>
    </tr>
    <tr>
      <td>Mathematical Procedures</td>
      <td>1.0</td>
      <td>No mathematical procedures were laid out in the essay. The student mentions solving for velocity using kinetic and potential energy, which is not mathematically correct for this problem.</td>
    </tr>
    <tr>
      <td>Logical Progression</td>
      <td>2.0</td>
      <td>The essay exhibits a logical flow in thought from collision to energy transformation, but the logical sequence does not address the problem statement correctly.</td>
    </tr>
    <tr>
      <th scope="row">Overall Score</th>
      <td>7.0</td>
      <td>The essay has attempted to apply Physics concepts but has done so incorrectly for the given problem. There is a logical flow, albeit incorrect, and the essay lacks the necessary mathematical procedures and correct concept application.</td>
    </tr>
  </tbody>
</table>'''

examples_ball_pend_zero = r'''Input to model:
A student has been asked to solve a physics problem, which is shown under the heading marked Problem Statement. 
The actual problem statement is delimited by triple backticks (```). The student is asked to produce a written response outlining
their strategy for solving the problem. The student written solution is shown in the section with heading Student Written Response, 
and is delimited by triple asterisks (***). Please assess the student's reasoning using the rubric shown in the section with heading
marked Rubric. The rubric is shown delimited by triple equals signs (===). Finally, you must provide a score out of 25 total points and 
your comments in the section marked Assessment!!! Some examples of how student writing should be assessed are shown in the section with
marked Examples, the examples are delimited by triple hyphens (---)
  the heading marked Rubric. 
1. Problem Statement : ```In words, describe the general strategy that you could use to to answer the following question : A bullet of mass m is fired horizontally into a block of mass M that is suspended vertically by a string attached to a fixed support. The block with the embedded bullet rises to a height h. What is the speed, V of the block, with the bullet embedded in it, immediately after the collision, in terms of the variables provided in the problem?```
2. Student Written Response: ***I used a system of the bullet, block, and Earth to setup change in momentum to 
be 0, then set final and initial momentum equal to each other. I then solved for 
the final velocity in terms of the masses and initial velocity of the bullet. 
Using the energy principle, I found the velocity of the bullet initially in 
terms of what we have and plugged that into the original equation.***
3. Rubric: ===#Essential Information (1.0 points - 3.0 points): The essay includes all the necessary information required to solve the problem.
#Physics Concepts (1.0 points - 3.0 points): The essay demonstrates the ability to select appropriate physics concepts and principles to use.
#Specific Application (1.0 points to 3.0 points):	The essay applies physics to the specific conditions in the problem.
#Mathematical Procedures (1.0 points - 3.0 points): The essay follows appropriate mathematical rules and procedures during the solution execution.
#Logical Progression (1.0 points - 3.0 points):	The essay progresses logically, is coherent, focused toward a goal, and consistent.
#Overall Score (1.0 points - 3.0 points): The overall quality of the essay scored on the dimensions ===
4. Examples: ---<examples>---

Assessment:

Model output:
# Essential Information (1.25 points):
The student provided a substantial amount of necessary information to solve the problem. They mentioned using the conservation of momentum and energy principles to find the final velocity. However, the student could have provided a clearer step-by-step approach that explicitly stated how the variables m, M, and h are related to the speed after the collision V. Also, momentum is extaneous as it is not needed since the initial conditions do not give enough information to use conservation of momentum to find the speed after the collision V.

# Physics Concepts (1.25 points):
The student chose inappropriate physics concepts for the problem. The student failed to mention if the collision between the bullet and the block was elastic or inelastic, and in either event which quantities are conserved. 

# Specific Application (1.0 points):
The student incorrectly applies the conservation of momentum and energy to the problem. The problem asks about the speed (V) of the block with the bullet emdedded in it after the collision without giving the initial speed of the bullet. Therefore, there is not enough information to apply conservation of momentum to find the speed V. Instead the student should set the kinetic energy immediately after the collision equal to the final gravtiational potential energy and use that relationship to solve for V.

# Mathematical Procedures (1.0 points):
The response describes a mathematical approach, but details of the algebraic manipulations or formulas are not provided and it is faulty since the initial speed of the bullet is not given. Some description of the process would be beneficial.

# Logical Progression (1.0 points):
The student doesn't lay out logical steps linking premises to a conclusion.

# Overall Score (1.75 points):
The overall response demonstrates a lack of understanding of the necessary physics concepts and an ability to apply them to the problem. 

Total Score: 2.0/3.0 points

Input to model:
A student has been asked to solve a physics problem, which is shown under the heading marked Problem Statement. 
The actual problem statement is delimited by triple backticks (```). The student is asked to produce a written response outlining
their strategy for solving the problem. The student written solution is shown in the section with heading Student Written Response, 
and is delimited by triple asterisks (***). Please assess the student's reasoning using the rubric shown in the section with heading
marked Rubric. The rubric is shown delimited by triple equals signs (===). Finally, you must provide a score out of 25 total points and 
your comments in the section marked Assessment!!! Some examples of how student writing should be assessed are shown in the section with
marked Examples, the examples are delimited by triple hyphens (---)
  the heading marked Rubric. 
1. Problem Statement : ```In words, describe the general strategy that you could use to to answer the following question : A bullet of mass m is fired horizontally into a block of mass M that is suspended vertically by a string attached to a fixed support. The block with the embedded bullet rises to a height h. What is the speed, V of the block, with the bullet embedded in it, immediately after the collision, in terms of the variables provided in the problem?```
2. Student Written Response: ***The collision is inelastic so energy is not conserved during the collision, but momentum is. After the collision, the bullet and block are a single object with m + M, where m is the mass of the bullet and M is the mass of the block. The block is suspended by a rope that is attached to a fix support, which means that the block is free to swing. After the collision, mechanical energy is conserved so the kinetic energy immediately after the collision (initial kinetic energy) is equal to the potential energy at height h (final).

KE_i = Ug_f where KE_i is the initial kinetic energy and Uf_f is the final potential energy. Kinetic energy is defined as rac{1}{2}m*v^{2} where m is the mass of the object and v is the speed of the object. Gravitational potential energy is defined as mgh where m is the mass of the object, g is the acceleration due to gravity, and h is the height of the object above a reference point where Ug is defined to be zero.
rac{1}{2}(m+M)*V^{2} = (m+M)*g*h
cancelling (m+M)
rac{1}{2}*V^{2} = g*h
multiply through by 2
V^{2} = 2*g*h
taking the square root,
V=\sqrt(2*g*h)***
3. Rubric: ===#Essential Information (1.0 points - 3.0 points): The essay includes all the necessary information required to solve the problem.
#Physics Concepts (1.0 points - 3.0 points): The essay demonstrates the ability to select appropriate physics concepts and principles to use.
#Specific Application (1.0 points to 3.0 points):	The essay applies physics to the specific conditions in the problem.
#Mathematical Procedures (1.0 points - 3.0 points): The essay follows appropriate mathematical rules and procedures during the solution execution.
#Logical Progression (1.0 points - 3.0 points):	The essay progresses logically, is coherent, focused toward a goal, and consistent.
#Overall Score (1.0 points - 3.0 points): The overall quality of the essay scored on the dimensions ===
4. Examples: ---None---

Assessment:

Model output:
Assessment:

# Essential Information (3.0 points): The student included most of the necessary information required to solve the problem. They correctly identified the collision as inelastic and stated that the total mechanical energy is not conserved during the collision. They also stated mechanical energy conservation post-collision.

# Physics Concepts (3.0 points): The student demonstrated the ability to select appropriate physics concepts—inelastic collision, conservation of momentum, and mechanical energy conservation.

# Specific Application (3.0 points): The essay applies physics to the specific conditions of the problem but fails to mention momentum conversation during the collision. The student explictly states that mechanical energy is conserved post collision, which is the key to correctly solving this problem. Using this, the student proceeds to the correct solution.

# Mathematical Procedures (3.0 points): The student correctly uses mathematics to equate kinetic energy and potential energy. 

# Logical Progression (3.0 points): The essay has a logical progression, starting with the type of collision, identifying the conservation laws at play, and solving for the final velocity.

# Overall Score (3.0 points): The overall quality of the essay indicates an understanding of the physics concepts, the strategy let to a correct final expression for \(V\).

Total Score: 3.0/3.0 points
'''