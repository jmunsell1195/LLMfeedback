from Agent.examples import examples_ball_pend_zero

physics = r'''In this problem a bullet of mass m collides with a block of mass M, M > m. The collision is inelastic which means that
momentum of the block + bullet system is conserved but the total mechanical energy of the block + bullet is not because some 
heat is lost to the surroundings. The initial speed of the bullet is not known so conservation of momentum is not applicable, and 
neith is conservation of energy applied between the initial kinetic energy of the bullet and any of the later stages of the problem.
Once the bullet is at rest with respect to the block, that is after the collision, mechanical 
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

essential_physics = '''I this problem 
'''


def prompt_template(problem_statement: str, student_essay: str, rubric: str, physics: str = physics, examples: str = examples_ball_pend_zero) -> str:
  prompt = f'''A student has been asked to solve a physics problem, which is shown under the heading marked Problem Statement. 
The problem statement is delimited by triple backticks (```). The student is asked to produce a written response outlining
their strategy for solving the problem. The student written solution is shown in the section with heading Student Written Response, 
and is delimited by triple asterisks (***). Please assess the student's reasoning using the rubric shown in the section with heading
marked Rubric. The rubric is shown delimited by triple equals signs (===). You will also see an explanation of the physics of the problem 
in the section marked Physics, the physical explanation of the situation is shown delimited by triple ampersands (@@@) This section
is not shown to the student and shouldn't be referenced directly. Finally, you must provide a score (1.0 points - 3.0 points) and your 
comments in the section marked Assessment!!! Some examples of how student writing should be assessed are shown in the section with 
marked Examples, the examples are delimited by triple hyphens (---). 
1. Problem Statement : ```{problem_statement}```
2. Student Written Response: ***{student_essay}***
3. Rubric: ==={rubric}===
4. Solution: @@@{physics}@@@
4. Examples: ---{examples}---

Assessment:'''
  return prompt

def prompt_template_latest(problem_statement: str, student_essay: str, rubric: str, examples: str = examples_ball_pend_zero) -> str:
  prompt = f'''A student has been asked to solve a physics problem, which is shown under the heading marked Problem Statement.
The actual problem statement is delimited by triple backticks (```). The student is asked to produce a written response outlining
their strategy for solving the problem. The student written solution is shown in the section with heading Student Written Response,
and is delimited by triple asterisks (***). Please assess the student's reasoning using the rubric shown in the section with heading
marked Rubric. The rubric is shown delimited by triple equals signs (===). The essential physics of the problem is laid out in section 5 
marked Physics and shown delimited in triple at-symbols (@@@) Finally, you must provide a overall score (1.0 - 3.0) total points and
your comments in the section marked Assessment!!! Some examples of how student writing should be assessed are shown in the section
marked Examples, the examples are delimited by triple hyphens (---)

1. Problem Statement : ```{problem_statement}```
2. Student Written Response: ***{student_essay}***
3. Rubric: ==={rubric}===
4. Examples: ---{examples}---
5. Physics: @@@{physics}@@@

BEFORE returning your response, ask yourself does my response take into account that conservation of momentum is NOT a valid solution strategy since the initial speed of the bullet is not given?
BEFORE returning your response, ask yourself did I score the student's response based on the criteria of the rubric?
Please return your response as a bootstrap formatted HTML table with class="table table-hover dark"
Please show the students original writing with areas that are incorrect or incomplete marked in red (HTML)
Please assess the student response STEP-BY-STEP using the rubric and referencing section 5. Physics
THE INITIAL SPEED OF THE BULLET IS UNKNOWN. ANY SOLUTION OR REASONING THAT REFERENCE IT IS AS A KNOWN QUANTITY IS INCORRECT
DO NOT REFERENCE THE PHYSICS SHOWN IN SECTION 5 IN YOUR RESPONSE. DO NOT GIVE AWAY THE FINAL ANSWER
Assessment:'''
  return prompt

def repeated_attempt_template(history: str, new_attempt: str) -> str:
  template = f'''The student submitted an essay, you previously assessed the essay and provided scores and comments. The student
  used your feedback. The conversation history between you and the student is shown in the section marked Conversation History,
  and the conversation is delimited by triple quotation marks ("""). The students new attempt, incorporating your feedback is shown
  in the section with heading New Attempt, and the students new essay is shown delimited by triple ampersands (&&&).

  6. Conversation History: """{history}"""
  7. New Attempt: &&&{new_attempt}&&&

  Does the student's new attempt solve the issues you raise with their previous attempts? Please score the new attempt using the same
  rubric as the previous attempts using the rubric in section 3.
  Please return your response as a bootstrap formatted HTML table with class="table table-hover dark"
  Assessment:'''
  return template
