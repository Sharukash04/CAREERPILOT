def skill_gap(candidate_skills, company_skills):
    m=[]
    for i in company_skills:
        if i.strip() not in candidate_skills:
            m.append(i.strip())
    return m