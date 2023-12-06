doktor_rubric = '''#Essential Information (0 - 5 points): The essay includes all the necessary information required to solve the problem.
#Physics Concepts (0 - 5 points): The essay demonstrates the ability to select appropriate physics concepts and principles to use.
#Specific Application (0 - 5 points): The essay applies physics to the specific conditions in the problem.
#Mathematical Procedures (0 - 5 points): The essay follows appropriate mathematical rules and procedures during the solution execution.
#Logical Progression (0 - 5 points): The essay progresses logically, is coherent, focused toward a goal, and consistent.'''

winter_rubric = '''Use the following rubric to grade the essay:
Student mentions any two of the following: - (2 points)
-initial kinetic energy and final potential energy
-conservation of energy
-solving for v.

Student mentions 1 of the following: - (1 point)
-initial kinetic energy and final potential energy
-conservation of energy
-solving for v.

Otherwise student should be given - (0 points)
'''

rubric = doktor_rubric.split("#")[1:]
rubric_dict = dict(zip([row.split(":")[0].split("(")[0] for row in rubric],[row.split(":")[1].strip() for row in rubric]))