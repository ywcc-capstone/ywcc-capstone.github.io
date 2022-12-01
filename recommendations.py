"""Generates advanced letters of recommendation for the highest perfoming students.

Usage: 
    List the students and project managers in their respective lists, following 
    the namedtuple syntax. Then, run the command `python3 recommendations.py` to
    generate a recommendation letter.
"""
from collections import namedtuple
import os

Student = namedtuple("Student", ['first_name', 'last_name', 'he_she_they', 'his_her_their'])

adv_students = [
    Student("Max", "Mayfield", "She", "Her"),
    Student("Billy", "Hargrove", "He", "His"),
]

adv_project_managers = [
    Student("Steve", "Harrington", "He", "His"),
    Student("Nancy", "Wheeler", "She", "Her"),
    Student("Mike", "Wheeler", "He", "His"),
]

all_students = adv_students + adv_project_managers

for student in all_students:
    first_name, last_name, he_she_they, his_her_their = student
    adv_template_for_members = (
    f"""
    Please accept this letter as an expression of confidence in {first_name} {last_name}’s outstanding qualities as a student leader. {first_name} was in the capstone program at NJIT in the Fall of 2022. This is a real-world project-based learning experience that aims to provide students with the knowledge, skills, and techniques needed to excel in the technology industry. In this program, students are not only practically trained in network administration/ security, software engineering, requirements management, software architecture, web/database programming, R&D skills, and quality assurance methods but also in leadership, project management, communication, and social and presentation skills. 
    
    {first_name} is ranked in the top 5% of the capstone program performance metrics. {he_she_they} has taken extra responsibilities and demonstrated exceptional performance in technical development and working within a collaborative team alike. It is unusual to find students who have strong skills in software engineering like {first_name}. This student has also excelled in real-world projects and impressed industry stakeholders through the means of presentation and collaboration. 

    {first_name}’s leadership skills went above and beyond what I would expect from any student. {his_her_their} dedication was extraordinary. Project stakeholders were very pleased with the results of their work, team-building skills, and leadership capabilities. This student inspired team members, managed risks and uncertainties, adapted to change, and overcame new challenges. {first_name} was always proactive and very responsive in all project work. {he_she_they} strives for perfection and does not see failure as an option. I also noticed that the student’s research capabilities are excellent. I must say that this student became an exceptional role model for all of their peers in Fall 2022. 

    {first_name} did not only attend all of the required training meetings but many of the optional ones. {his_her_their} willingness to learn was also one of their unique qualifications. Guiding their team with passion and incredible commitment, {first_name} delivered all of the required deliverables outstandingly on time, on budget, and on target. {he_she_they} was able to effortlessly cooperate with the team to present project deliverables very successfully. {he_she_they} was always professional in appearance, impressive in presentation skills, and focused on the quality and content of what was being presented. Our team of expert judges were amazed that they transformed such a challenging project into a success story. I highly recommend {first_name} and am fully confident that this student will excel wherever they may go and add substantial value to any organization they join.

    Should you have any questions or concerns, please feel free to contact me. Thank you 
    """)
    print(adv_template_for_members)
    input("Press enter for next...") 
    os.system("clear")