# Values provided by the user for calculating the average risk rating

# Threat Agent Factors
skill_level = [3, 5]  # Range: some technical skills to advanced computer user
motive = 9  # High reward
opportunity = 7  # Some access or resources required
size = 9  # Large group of attackers

# Vulnerability Factors
ease_of_discovery = 9  # Automated tools available
ease_of_exploit = 5  # Easy
awareness = 9  # Public knowledge
intrusion_detection = [3, 9]  # Range: logged and reviewed to not logged

# Impact Factors
loss_of_confidentiality = 7  # Extensive critical data disclosure
loss_of_integrity = 7  # Extensive seriously corrupt data
loss_of_availability = 5  # Possible interruption to primary services
loss_of_accountability = 7  # Possibly traceable

# Calculating the average for the skill level and intrusion detection as they have a range
avg_skill_level = sum(skill_level) / len(skill_level)
avg_intrusion_detection = sum(intrusion_detection) / len(intrusion_detection)

# List of all values
all_values = [
    avg_skill_level, motive, opportunity, size,
    ease_of_discovery, ease_of_exploit, awareness, avg_intrusion_detection,
    loss_of_confidentiality, loss_of_integrity, loss_of_availability, loss_of_accountability
]

# Calculating the total average
total_average = sum(all_values) / len(all_values)
print("Overall Risk Results:", total_average)
