# Define the scores for each factor in the OWASP methodology
# Factors for Estimating Likelihood
threat_agent_factors = {
    'skill_level': 6,    # Network and programming skills
    'motive': 9,         # High reward
    'opportunity': 4,    # Special access to resources
    'size': 6            # Authenticated users
}

vulnerability_factors = {
    'ease_of_discovery': 9,  # Well known to insiders
    'ease_of_exploit': 5,    # Exploiting known vulnerabilities
    'awareness': 9,          # Well-known vulnerability
    'intrusion_detection': 3 # Some level of monitoring
}

# Factors for Estimating Impact
technical_impact_factors = {
    'loss_of_confidentiality': 7, # Extensive critical data disclosure
    'loss_of_integrity': 7,        # Extensive seriously corrupt data
    'loss_of_availability': 7,     # Extensive primary services interruption
    'loss_of_accountability': 1    # Might be fully traceable
}

business_impact_factors = {
    'financial_damage': 7,        # Significant effect on annual profit
    'reputation_damage': 9,       # Potential brand damage
    'non_compliance': 7,          # High profile violation
    'privacy_violation': 7        # Disclosure of thousands of people's information
}

# Calculate the average score for each category
def calculate_average(scores):
    return sum(scores.values()) / len(scores)

# Calculate the overall likelihood and impact
overall_likelihood = calculate_average({**threat_agent_factors, **vulnerability_factors})
overall_technical_impact = calculate_average(technical_impact_factors)
overall_business_impact = calculate_average(business_impact_factors)

print("Overall Likelihood: ", overall_likelihood) 
print("Overall Technical Impact:" , overall_technical_impact)
print("Overall Business Impact:", overall_business_impact)
