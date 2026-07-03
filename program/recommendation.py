from match_score import match_score
def recommend_companies(candidate):
    company_scores=match_score(candidate)
    company_scores.sort(key=lambda x: x[2], reverse=True)
    print("\n========== TOP 7 RECOMMENDED COMPANIES ==========\n")
    num_recommendations = min(7, len(company_scores))
    for i in range(num_recommendations):
        print(i + 1, ".", company_scores[i][0])
        print("Role :", company_scores[i][1])
        print("Match Score :", company_scores[i][2], "/100")
        print("Difficulty :", company_scores[i][3])
        print("Missing Skills :", company_scores[i][4])
        print()
    return company_scores