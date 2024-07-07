import re
import json

def parse_resume(resume_text):
    resume = {
        "name": "",  
        "education": [],
        "skills": {
            "languages": [],
            "libraries_and_tools": [],
            "analytics": []
        },
        "experience": [],
        "projects": [],
        "achievements": [],
        "publications": []
    }

    
    name_match = re.search(r'(?<=Name:\s).*', resume_text)
    if name_match:
        resume["name"] = name_match.group().strip()

    
    education_matches = re.findall(r'Education\n(.*?)\nSkills', resume_text, re.DOTALL)
    for match in education_matches:
        education_details = match.strip().split('\n')
        degree, university, location, dates, details = education_details
        resume["education"].append({
            "degree": degree.strip(),
            "university": university.strip(),
            "location": location.strip(),
            "dates": dates.strip(),
            "details": details.strip()
        })

    
    skills_matches = re.findall(r'Skills\n(.*?)\nExperience', resume_text, re.DOTALL)
    if skills_matches:
        skills_details = skills_matches[0].strip().split('\n')
        for skill_line in skills_details:
            category, skills = skill_line.split(':')
            resume["skills"][category.lower().replace(" ", "_")] = [skill.strip() for skill in skills.split(',')]

    
    experience_matches = re.findall(r'Experience\n(.*?)\nProjects', resume_text, re.DOTALL)
    for match in experience_matches:
        experience_details = match.strip().split('\n')
        title, company, location, dates, description = experience_details
        resume["experience"].append({
            "title": title.strip(),
            "company": company.strip(),
            "location": location.strip(),
            "dates": dates.strip(),
            "description": description.strip()
        })

    
    projects_matches = re.findall(r'Projects\n(.*?)\nAchievements', resume_text, re.DOTALL)
    for match in projects_matches:
        projects_details = match.strip().split('\n')
        for project_detail in projects_details:
            project_name, project_description = project_detail.split(':')
            resume["projects"].append({
                "name": project_name.strip(),
                "description": project_description.strip()
            })

    
    achievements_matches = re.findall(r'Achievements & Awards\n(.*?)\nPublications', resume_text, re.DOTALL)
    if achievements_matches:
        resume["achievements"] = [achievement.strip() for achievement in achievements_matches[0].strip().split('\n')]


    publications_matches = re.findall(r'Publications\n(.*?)\n$', resume_text, re.DOTALL)
    if publications_matches:
        publications_details = publications_matches[0].strip().split('\n')
        for pub_detail in publications_details:
            publication_title = pub_detail.strip()
            resume["publications"].append({
                "title": publication_title.strip()
            })

    return resume

if __name__ == "__main__":
    resume_text = """
    Name: Abhinav Raja Raizada
    Education
    SRM Institute of Science and Technology, Kattankulathur Chennai, Tamil Nadu
    B.TECH in Computer Science and Engineering, CGPA: 9.24 2021 – 2025
    SKD Academy Lucknow, Uttar Pradesh
    ISC: 87% 2019 – 2021
    La Martiniere College Lucknow, Uttar Pradesh
    ICSE 2007 – 2019
    Skills
    Languages: Python, C/C++, SQL
    Libraries and Tools: NumPy, Pandas, Scikit-learn, OpenCV, NLTK, TensorFlow, PyTorch, Keras, PowerBI, Tableau, Excel, Git, Docker, AWS, Microsoft Azure, Terraform, Ansible, Kubernetes
    Analytics: Supply Chain Operations, BI product development, Customer interaction, Feature mapping, Ad-hoc analysis
    Experience
    Research Intern Sep, 2023 – Apr, 2024
    Samsung R&D Institute, Bangalore, India
    • Led successful implementation of Automatic Read Speech to Conversational Speech Recognition Project with
    Samsung Mentorship Team.
    • Achieved 100% completion mark from mentors. Collaborated with a cross-functional team to integrate NLP models
    into existing frameworks.
    Summer Intern Jun. 2023 – Jul, 2023
    Uttar Pradesh Metro Railway Corporation, Lucknow, Uttar Pradesh
    • Gained hands-on experience in IT department of UPMRC during Summer Internship, enhanced skills in PowerBI &
    SQL through a Data Science Project directing employee complaints.
    • Developed and maintained business reports to support Supply Chain operations. Provided analytical support.
    Artificial Intelligence Researcher Jul, 2023 – Oct, 2023
    Zetpeak, Chennai, India
    • Engaged in an immersive paid online internship, earning Rs. 5000 per month, and collaborating closely with
    experienced professionals. Focused on gaining practical skills and knowledge to upscale academic and professional
    growth in the AI/ML field, conducted ad-hoc analysis to investigate system decisions and metrics impact.
    Projects
    • Instance Segmentation: Developed an instance segmentation model trained on Sentinel-2 imagery. Accurately
    delineates agricultural field boundaries but struggles with crop type prediction. [Link]
    • Disease Detective: Developed Disease Detective, a robust medical diagnosis chatbot using KNN and Decision Trees
    on 1100 data points, providing personalized disease identification, severity assessment, & precautionary advice. [Try It!]
    • Automated Deploying AWS using Gitlab and Terraform: Automated EC2 instance creation in user-defined
    VPC & subnet using AWS, GitLab, Terraform. Included init, plan, user approval, apply, destroy stages with dynamic
    security group config, auto-scaling via CloudWatch. [Try It!]
    Achievements & Awards
    • Corporate Domain Lead: Led the Corporate Domain, formerly Apple Developers Group (ADG), overseeing club
    operations and event management. Coordinated with multiple business teams for BI product development and
    maintenance.
    • Finalists in Smart India Hackathon (Internal Round) and Philips Ideathon.
    Publications
    “Analyzing the Efficacy: A Critical Assessment of a Symptom Analysis and Initial Diagnosis Chatbot for
    Disease Detection”, Technological Innovation towards Digital Transformation Arena (ICSCSP2024 · VOLUME-I),
    Lecture Notes in Networks and Systems (LNNS), Springer, June 2024. [Link]
    """

    # Parse the resume text into JSON format
    parsed_resume = parse_resume(resume_text)
    
    # Print the JSON output
    print(json.dumps(parsed_resume, indent=2))