class Person:
    def __init__(self, name, phone_number, age, email):
        self._name = name
        self._phone_number = phone_number
        self._age = age
        self._email = email

    @property
    def name(self):
        return self._name

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def age(self):
        return self._age

    @property
    def email(self):
        return self._email


class Candidate(Person):
    def __init__(self, name, phone_number, age, email, degree, department, college, cgpa, graduation_year, skills, projects, internships, work_experience, preferred_role):
        super().__init__(name, phone_number, age, email)
        self._degree = degree
        self._department = department
        self._college = college
        self._cgpa = cgpa
        self._graduation_year = graduation_year
        self._skills = skills
        self._projects = projects
        self._internships = internships
        self._work_experience = work_experience
        self._preferred_role = preferred_role

    @property
    def degree(self):
        return self._degree

    @property
    def department(self):
        return self._department

    @property
    def college(self):
        return self._college

    @property
    def cgpa(self):
        return self._cgpa

    @property
    def graduation_year(self):
        return self._graduation_year

    @property
    def skills(self):
        return self._skills

    @property
    def projects(self):
        return self._projects

    @property
    def internships(self):
        return self._internships

    @property
    def work_experience(self):
        return self._work_experience

    @property
    def preferred_role(self):
        return self._preferred_role


def get_candidate_details():
    print("\n========== CANDIDATE DETAILS ==========\n")

    name = input("Enter Your Name: ")

    # Phone Number Validation
    while True:
        phone_number = input("Enter Your Phone Number: ")
        if len(phone_number) == 10 and phone_number.isdigit():
            break
        else:
            print("Enter Valid Phone Number")

    # Age Validation
    while True:
        age = int(input("Enter Your Age: "))
        if age >= 18:
            break
        else:
            print("Enter Valid Age")

    # Email Validation
    while True:
        email = input("Enter Your Email: ")
        if "@" in email and "." in email:
            break
        else:
            print("Enter Valid Email")

    print("\n---------- Education Details ----------")

    degree = input("Enter Your Degree (eg: B.E): ")
    department = input("Enter Your Department (eg: COMPUTER SCIENCE AND ENGINEERING): ")
    college = input("Enter Your College Name: ")
    cgpa = float(input("Enter Your CGPA: "))
    graduation_year = int(input("Enter The Graduation Year: "))

    print("\n---------- Skills ----------")

    notvalid = (
        "running", "jogging", "coding", "swimming",
        "cricket", "football", "kabaddi",
        "tabletennis", "badminton", "volleyball"
    )

    while True:
        skills_input = input("Enter The Skills That You Have (comma separated): ")
        skills = [skill.strip().lower() for skill in skills_input.split(",") if skill.strip()]

        # Check if at least one valid skill exists
        if not skills:
            print("Enter Valid Skills")
        elif all(skill in notvalid for skill in skills):
            print("Please Enter Technical Skills Only")
        else:
            break

    print("\n---------- Additional Details ----------")

    projects = int(input("Number of Projects You Have: "))
    internships = int(input("Number of Internships You Have Taken: "))
    work_experience = float(input("Enter Work Experience (in years, 0 if none): "))

    while True:
        preferred_role = input("Preferred Job Role: ")
        if preferred_role.strip() != "":
            break
        else:
            print("Enter Valid Preferred Job Role")

    return Candidate(
        name=name,
        phone_number=phone_number,
        age=age,
        email=email,
        degree=degree,
        department=department,
        college=college,
        cgpa=cgpa,
        graduation_year=graduation_year,
        skills=skills,
        projects=projects,
        internships=internships,
        work_experience=work_experience,
        preferred_role=preferred_role
    )