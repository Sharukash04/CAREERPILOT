import openpyxl
workbook = openpyxl.load_workbook("database/companies.xlsx")
sheet = workbook.active

def match_score(candidate):
    company_scores = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        score = 0
        company = row[0] if row[0] is not None else "Unknown"
        role = row[1] if row[1] is not None else "Unknown"
        degree = row[2] if row[2] is not None else ""
        skills = row[3] if row[3] is not None else ""
        cgpa = row[4]
        difficulty = row[6] if len(row) > 6 and row[6] is not None else "Unknown"
        missing_skills = []
        # Degree Match
        if candidate.degree.lower() in degree.lower():
            score += 20
        # CGPA Match
        try:
            db_cgpa = float(cgpa) if cgpa is not None else 0.0
            if candidate.cgpa >= db_cgpa:
                score += 10
        except (ValueError, TypeError):
            pass
        # Skills Match
        company_skills = skills.split(",")
        for skill in company_skills:
            if skill.strip().lower() in [i.lower() for i in candidate.skills]:
                score += 15
            else:
                missing_skills.append(skill.strip())
        # Preferred Job Role Match (Up to 30 points)
        if candidate.preferred_role and (candidate.preferred_role.lower() in role.lower() or role.lower() in candidate.preferred_role.lower()):
            score += 30

        # Work Experience Match (Up to 15 points)
        experience_req = row[5] if len(row) > 5 else None # Work Experience Column
        if experience_req and candidate.work_experience is not None:
            try:
                # E.g. "0-2 Years"=min=0, max=2. "2+ Years"=min=2.
                if "+" in str(experience_req):
                    min_exp=float(str(experience_req).split("+")[0].strip())
                    max_exp=99.0
                elif "-" in str(experience_req):
                    parts=str(experience_req).replace("Years", "").replace("Year", "").split("-")
                    min_exp=float(parts[0].strip())
                    max_exp=float(parts[1].strip())
                else:
                    min_exp=0.0
                    max_exp=99.0

                if min_exp<=candidate.work_experience<=max_exp:
                    score += 15
            except Exception:
                pass

        # Projects and Internships = Up to 25 points total
        if candidate.projects > 0:
            score += min(candidate.projects * 5, 15)
        if candidate.internships > 0:
            score += min(candidate.internships * 5, 10)

        # Cap score at 100
        score = min(score, 100)

        company_scores.append([
            company,
            role,
            score,
            difficulty,
            missing_skills
        ])
    return company_scores