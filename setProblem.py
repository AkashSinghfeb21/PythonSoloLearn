# You are working on a recruitment platform, which should match the available jobs and the candidates based on their skills.

# The skills required for the job, and the candidate's skills are stored in sets.

# Complete the program to output the matched skill.

skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}

n = skills & job_skills

print(", ".join(n))
