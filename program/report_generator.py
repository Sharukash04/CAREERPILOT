def generate_report(candidate, recommendations):

    print("\n========================================")
    print("         CAREERPILOT REPORT")
    print("========================================")

    print("\nCandidate Name :", candidate.name)
    print("Phone Number   :", candidate.phone_number)
    print("Age            :", candidate.age)
    print("Email          :", candidate.email)
    print("Degree         :", candidate.degree)
    print("Department     :", candidate.department)
    print("College Name   :", candidate.college)
    print("CGPA           :", candidate.cgpa)
    print("Skills         :", ", ".join(candidate.skills))
    print("Experience     :", candidate.work_experience)   
    print("Internship     :", candidate.internships)   
    print("Projects       :", candidate.projects)
    print("Preferred Role :", candidate.preferred_role)

    print("\n========== TOP 7 RECOMMENDED COMPANIES ==========\n")

    top = recommendations[:7]
    for i, rec in enumerate(top):
        print(i+1,".",rec[0])
        print("Role :",rec[1])
        print("Match Score :",rec[2],"/100")
        print("Difficulty :",rec[3])
        print("Missing Skills :",rec[4])
        print()

    if top:
        print(f"Company with the Maximum Match Score: {top[0][0]} ({top[0][2]}/100)\n")

    print("Career Roadmap Generated Successfully")

