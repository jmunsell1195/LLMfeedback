def prompt_template(problem_statement: str, student_essay: str, rubric: str) -> str:
  template = f'''You are given a student essay in the section marked ```Student Essay``` where the student elucidates their approach to solving a problem which is given in the section marked ```Problem```. In particular they are asked to include essential information, cite specific physics concepts, and apply scientific ideas. Also please be mindful of mathematical procedures and logical progression of the essay. Please score the essay according to the rubric shown in the section marked ```Rubric```. THIS IS VERY IMPORTANT PLEASE provide your score and explanation in the section marked ```Score```
```Student Essay```: {student_essay}
```Problem Statement```: {problem_statement}
```Rubric```: {rubric}
```Score```:'''
  return template

