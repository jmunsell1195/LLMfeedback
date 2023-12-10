# doktor_rubric = '''#Essential Information (0.0 point - 5.0 points): Does the essay includes all the necessary information required to solve the problem?
# #Physics Concepts (0.0 points - 5.0 points): Does the essay demonstrate the ability to select appropriate physics concepts and principles to use?
# #Specific Application (0.0 points - 5.0 points): Does the essay apply physics to the specific conditions in the problem?
# #Mathematical Procedures (0.0 points - 5.0 points): Does the essay follow appropriate mathematical rules and procedures during the solution execution?
# #Logical Progression (0.0 points - 25.0 points): Does the essay progresses logically? is it coherent, focused toward a goal, and consistent?'''

# winter_rubric = '''Use the following rubric to grade the essay:
# Student mentions any two of the following: - (2 points)
# -initial kinetic energy and final potential energy
# -conservation of energy
# -solving for v.

# Student mentions 1 of the following: - (1 point)
# -initial kinetic energy and final potential energy
# -conservation of energy
# -solving for v.

# Otherwise student should be given - (0 points)
# '''

doktor_rubric = '''#Essential Information (0.0 points - 5.0 points): The essay includes all the necessary information required to solve the problem.
#Physics Concepts (0.0 points - 5.0 points): The essay demonstrates the ability to select appropriate physics concepts and principles to use.
#Specific Application (0.0 points to 5.0 points):	The essay applies physics to the specific conditions in the problem.
#Mathematical Procedures (0.0 points - 5.0 points): The essay follows appropriate mathematical rules and procedures during the solution execution.
#Logical Progression (0.0 points - 5.0 points):	The essay progresses logically, is coherent, focused toward a goal, and consistent.
#Overall Score (0.0 points - 25.0 points): The overall quality of the essay scored on the dimensions '''

rubric = doktor_rubric.split("#")[1:]
rubric_dict = dict(zip([row.split(":")[0].split("(")[0] for row in rubric],[row.split(":")[1].strip() for row in rubric]))