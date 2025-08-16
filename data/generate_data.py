# file: generate_data.py
import pandas as pd
import random
import numpy as np
import os # <-- Import the os module

# --- Configuration ---
NUM_JOBS = 100
OUTPUT_FILE = 'data/jobs_india.csv'

# --- Data Pools ---
COMPANIES = {
    "Tata Consultancy Services": "TCS", "Infosys": "INFY", "Wipro": "WIPRO", "HCL Technologies": "HCL",
    "Tech Mahindra": "TECHM", "LTI Mindtree": "LTIM", "Mphasis": "MPHAS", "Persistent Systems": "PERS",
    "Cognizant": "COG", "Capgemini": "CAPG", "Accenture": "ACCN", "IBM": "IBM",
    "Amazon": "AMZN", "Microsoft": "MSFT", "Google": "GOOG", "Flipkart": "FLPK", "Walmart": "WMT",
    "Oracle": "ORCL", "SAP": "SAP", "Salesforce": "CRM", "Adobe": "ADBE", "Intuit": "INTU",
    "Zoho Corporation": "ZOHO", "Freshworks": "FRSH", "Paytm": "PAYTM", "PhonePe": "PHPE", "Razorpay": "RAZR",
    "Swiggy": "SWGY", "Zomato": "ZOMT", "Ola Cabs": "OLA", "CRED": "CRED", "Zerodha": "ZERODHA"
}

LOCATIONS = ["Bengaluru", "Hyderabad", "Pune", "Chennai", "Delhi NCR", "Mumbai", "Kolkata", "Ahmedabad"]

ROLES = {
    "Software Engineer": {
        "skills": ["Java", "Python", "C++", "Data Structures", "Algorithms"],
        "salary_base": 800000
    },
    "Frontend Developer": {
        "skills": ["React", "JavaScript", "HTML", "CSS", "TypeScript", "Next.js"],
        "salary_base": 700000
    },
    "Backend Developer": {
        "skills": ["Java", "Spring Boot", "Python", "Django", "Node.js", "SQL", "Microservices"],
        "salary_base": 900000
    },
    "Full Stack Developer": {
        "skills": ["React", "Node.js", "Express", "MongoDB", "SQL", "JavaScript"],
        "salary_base": 1000000
    },
    "DevOps Engineer": {
        "skills": ["AWS", "Docker", "Kubernetes", "CI/CD", "Terraform", "Jenkins"],
        "salary_base": 1100000
    },
    "Data Scientist": {
        "skills": ["Python", "Machine Learning", "TensorFlow", "PyTorch", "SQL", "Scikit-learn"],
        "salary_base": 1400000
    },
    "Machine Learning Engineer": {
        "skills": ["Python", "TensorFlow", "PyTorch", "C++", "Machine Learning", "NLP"],
        "salary_base": 1500000
    },
    "QA Engineer": {
        "skills": ["Selenium", "Java", "Python", "JMeter", "API Testing", "Automation"],
        "salary_base": 600000
    },
    "Cloud Engineer": {
        "skills": ["AWS", "Azure", "GCP", "Terraform", "Kubernetes"],
        "salary_base": 1200000
    },
    "Android Developer": {
        "skills": ["Kotlin", "Java", "Android SDK", "MVVM", "Jetpack Compose"],
        "salary_base": 800000
    }
}

LEVELS = {
    "Junior": {"exp": "0-2 years", "salary_multiplier": 0.7},
    "Mid-Level": {"exp": "3-5 years", "salary_multiplier": 1.2},
    "Senior": {"exp": "5-8 years", "salary_multiplier": 2.0},
    "Lead": {"exp": "8-12 years", "salary_multiplier": 2.8},
    "Principal": {"exp": "12+ years", "salary_multiplier": 4.0}
}

INDUSTRIES = ["IT Services & Consulting", "FinTech", "E-commerce", "SaaS", "Healthcare IT", "EdTech", "Cloud Computing", "Gaming", "Logistics"]
COMPANY_SIZES = ["51-200 Employees", "201-500 Employees", "501-1000 Employees", "1001-5000 Employees", "5001-10000 Employees", "10000+ Employees"]
VALUES = ["Innovation", "Work-Life Balance", "Customer Centricity", "Teamwork", "Integrity", "Continuous Learning", "Ownership", "Data-Driven Decisions"]

# --- Generation Logic ---
def generate_jobs():
    jobs_list = []
    company_counters = {abbr: 0 for abbr in COMPANIES.values()}

    for i in range(NUM_JOBS):
        company_name, company_abbr = random.choice(list(COMPANIES.items()))
        
        job_id = f"{company_abbr}-{company_counters[company_abbr]}"
        company_counters[company_abbr] += 1
        
        role_name, role_info = random.choice(list(ROLES.items()))
        level_name, level_info = random.choice(list(LEVELS.items()))
        title = f"{level_name} {role_name}"
        
        base_salary = role_info['salary_base']
        salary = base_salary * level_info['salary_multiplier'] * random.uniform(0.9, 1.1)
        salary_min = int(salary)
        salary_max = int(salary_min * random.uniform(1.4, 1.8))
        salary_range = f"[{salary_min}, {salary_max}]"
        
        num_skills = random.randint(3, 5)
        skills = ";".join(random.sample(role_info['skills'], min(num_skills, len(role_info['skills']))))

        location = random.choice(LOCATIONS)
        industry = random.choice(INDUSTRIES)
        company_size = random.choice(COMPANY_SIZES)
        num_values = random.randint(1, 3)
        promoted_values = ";".join(random.sample(VALUES, num_values))
        
        jobs_list.append({
            "job_id": job_id,
            "title": title,
            "company": company_name,
            "location": location,
            "salary_range": salary_range,
            "employment_type": "Full-Time",
            "company_size": company_size,
            "industry": industry,
            "required_skills": skills,
            "values_promoted": promoted_values,
            "experience_required": level_info['exp'],
            "role_level": level_name
        })
        
    return pd.DataFrame(jobs_list)

if __name__ == "__main__":
    print(f"Generating {NUM_JOBS} job listings...")
    
    # --- *** THE FIX IS HERE *** ---
    # Get the directory name from the output file path
    output_dir = os.path.dirname(OUTPUT_FILE)
    
    # Create the directory if it doesn't exist
    if not os.path.exists(output_dir):
        print(f"Creating directory: {output_dir}")
        os.makedirs(output_dir)
    # --- *** END OF FIX *** ---

    jobs_df = generate_jobs()
    jobs_df.to_csv(OUTPUT_FILE, index=False)
    print(f"Successfully created '{OUTPUT_FILE}' with {len(jobs_df)} jobs.")
