examples = r'''Input to model:
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
3. Rubric: ===#Essential Information (0.0 points - 5.0 points): The essay includes all the necessary information required to solve the problem.
#Physics Concepts (0.0 points - 5.0 points): The essay demonstrates the ability to select appropriate physics concepts and principles to use.
#Specific Application (0.0 points to 5.0 points):	The essay applies physics to the specific conditions in the problem.
#Mathematical Procedures (0.0 points - 5.0 points): The essay follows appropriate mathematical rules and procedures during the solution execution.
#Logical Progression (0.0 points - 5.0 points):	The essay progresses logically, is coherent, focused toward a goal, and consistent.
#Overall Score (0.0 points - 25.0 points): The overall quality of the essay scored on the dimensions ===
4. Examples: ---<examples>---

Assessment:

Model output:
# Essential Information (1.5 points):
The student provided a substantial amount of necessary information to solve the problem. They mentioned using the conservation of momentum and energy principles to find the final velocity. However, the student could have provided a clearer step-by-step approach that explicitly stated how the variables m, M, and h are related to the speed after the collision V. Also, momentum is extaneous as it is not needed since the initial conditions do not give enough information to use conservation of momentum to find the speed after the collision V.

# Physics Concepts (1.0 points):
The student chose inappropriate physics concepts for the problem. The student failed to mention if the collision between the bullet and the block was elastic or inelastic, and in either event which quantities are conserved. 

# Specific Application (1.0 points):
The student incorrectly applies the conservation of momentum and energy to the problem. The problem asks about the speed (V) of the block with the bullet emdedded in it after the collision without giving the initial speed of the bullet. Therefore, there is not enough information to apply conservation of momentum to find the speed V. Instead the student should set the kinetic energy immediately after the collision equal to the final gravtiational potential energy and use that relationship to solve for V.

# Mathematical Procedures (0.5 points):
The response describes a mathematical approach, but details of the algebraic manipulations or formulas are not provided and it is faulty since the initial speed of the bullet is not given. Some description of the process would be beneficial.

# Logical Progression (0.5 points):
The student doesn't lay out logical steps linking premises to a conclusion.

# Overall Score (4.5 points):
The overall response demonstrates a lack of understanding of the necessary physics concepts and an ability to apply them to the problem. 

Total Score: 4.5/25 points

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
2. Student Written Response: ***The collision is inelastic so energy is not conserved during the collision, but momentum is. After the collision, the bullet and block are a single object with m + M, where m is the mass of the bullet and M is the mass of the block. The block is suspended by a rope that is attached to a fix support, which means that the block is free to swing. After the collision, mechanical energy is conserved so the initial kinetic energy is equal to the final potential energy.

KE_i = Ug_f where KE_i is the initial kinetic energy and Uf_f is the final potential energy. Kinetic energy is defined as rac{1}{2}m*v^{2} where m is the mass of the object and v is the speed of the object. Gravitational potential energy is defined as mgh where m is the mass of the object, g is the acceleration due to gravity, and h is the height of the object above a reference point where Ug is defined to be zero.
rac{1}{2}(m+M)*V^{2} = (m+M)*g*h
cancelling (m+M)
rac{1}{2}*V^{2} = g*h
multiply through by 2
V^{2} = 2*g*h
taking the square root,
V=\sqrt(2*g*h)***
3. Rubric: ===#Essential Information (0.0 points - 5.0 points): The essay includes all the necessary information required to solve the problem.
#Physics Concepts (0.0 points - 5.0 points): The essay demonstrates the ability to select appropriate physics concepts and principles to use.
#Specific Application (0.0 points to 5.0 points):	The essay applies physics to the specific conditions in the problem.
#Mathematical Procedures (0.0 points - 5.0 points): The essay follows appropriate mathematical rules and procedures during the solution execution.
#Logical Progression (0.0 points - 5.0 points):	The essay progresses logically, is coherent, focused toward a goal, and consistent.
#Overall Score (0.0 points - 25.0 points): The overall quality of the essay scored on the dimensions ===
4. Examples: ---None---

Assessment:

Model output:
Assessment:

# Essential Information (5.0 points): The student included most of the necessary information required to solve the problem. They correctly identified the collision as inelastic and stated that the total mechanical energy is not conserved during the collision. They also stated mechanical energy conservation post-collision.

# Physics Concepts (5.0 points): The student demonstrated the ability to select appropriate physics concepts—inelastic collision, conservation of momentum, and mechanical energy conservation.

# Specific Application (4.0 points): The essay applies physics to the specific conditions of the problem but fails to mention momentum conversation during the collision. The student explictly states that mechanical energy is conserved post collision, which is the key to correctly solving this problem. Using this, the student proceeds to the correct solution.

# Mathematical Procedures (5.0 points): The student correctly uses mathematics to equate kinetic energy and potential energy. 

# Logical Progression (5.0 points): The essay has a logical progression, starting with the type of collision, identifying the conservation laws at play, and solving for the final velocity.

# Overall Score (24.0 points): The overall quality of the essay indicates an understanding of the physics concepts, but with a significant error in the mathematical procedure, leading to an incorrect final expression for \(V\).

Total Score: 24.0/25 points
'''

physics = r'''In this problem a bullet of mass m collides with a block of mass M, M > m. The collision is inelastic which means that
momentum of the block + bullet system is conserved but the total mechanical energy of the block + bullet is not because some 
heat is lost to the surroundings. Once the bullet is at rest with respect to the block, that is after the collision, mechanical 
energy is conserved again. The problem asks to find the speed V after the collision is over. Normally, you could do this by
using conservation of momentum with the block and the bullet as your system. However, in this problem the inital speed of the bullet
is not given. Therefore conservation of momentum cannot be used to solve for the speed V immediately after the collision. Instead, we use the
fact that mechanical energy is conserved immediately after the collision. Thus, we set the post-collision kinetic energy equal of the composite 
block + bullet object equal to the gravitational potential energy of the block+bullet object when it is has swung to height h above where it started.
putting my mathematical steps in LaTeX:
KE_{i} = GPE+{f} 
Where
-KE_{i} is the post collision kinetic energy of the bullet block system
-GPE_{f} is the gravitational potential energy of the bullet block system when it is at height h above where it started
Kinetic energy is defined as KE = \frac{1}{2}m*v^{2} for an object with mass m moving at speed v.
Graviattion Potential energy is defined as GPE = m*g*h where m is the mass of the object, g is the acceleration due to gravity, 
and h is the height of the object above the reference point where GPE is set equal to zero
Using these definition, the mass of the object is (m+M). V  is the post collision speed of the block+bullet object, g is the acceleration due to gravity
and h is the highest point the block + bullet object swings to.
\frac{1}{2}(m+M)*V^{2} = (m+M)*g*h
dividing both sides by (m+M) [cancelling (m+M)]
\frac{1}{2}V^{2} = g*h
multiplying both sides by 2
V^2 = 2*g*h
taking the square root of both sides
V = \sqrt{2*g*h}
'''


def prompt_template(problem_statement: str, student_essay: str, rubric: str, physics: str = physics, examples: str = examples) -> str:
  prompt = f'''A student has been asked to solve a physics problem, which is shown under the heading marked Problem Statement. 
The problem statement is delimited by triple backticks (```). The student is asked to produce a written response outlining
their strategy for solving the problem. The student written solution is shown in the section with heading Student Written Response, 
and is delimited by triple asterisks (***). Please assess the student's reasoning using the rubric shown in the section with heading
marked Rubric. The rubric is shown delimited by triple equals signs (===). You will also see an explanation of the physics of the problem 
in the section marked Physics, the physical explanation of the situation is shown delimited by triple ampersands (@@@). Finally, you must 
provide a score out of 25 total points and your comments in the section marked Assessment!!! Some examples of how student writing should be
 assessed are shown in the section with marked Examples, the examples are delimited by triple hyphens (---). 
1. Problem Statement : ```{problem_statement}```
2. Student Written Response: ***{student_essay}***
3. Rubric: ==={rubric}===
4. Solution: @@@{physics}@@@
4. Examples: ---{examples}---

Assessment:'''
  return prompt