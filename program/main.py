from candidate import get_candidate_details
from recommendation import recommend_companies
from report_generator import generate_report

# Get Candidate Details
candidate=get_candidate_details()

# Company Recommendation
recommendations=recommend_companies(candidate)

# Generate Final Report
generate_report(candidate,recommendations)
