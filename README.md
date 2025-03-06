# email_domain_tracking Analysis Project

## Overview
This Python-based tool efficiently analyzes email domains from a provided CSV file. It extracts domains, segregates them between business and personal categories, and calculates the occurrence and percentage of each domain type. This tool is essential for organizations looking to understand email traffic sources and enhance email management strategies.

## Features
- **Domain Extraction:** Extracts the domain from each email address in the input CSV file.
- **Domain Categorization:** Identifies and filters personal email domains, focusing analysis on business-related email traffic.
- **Count and Percentage Calculation:** Calculates the frequency of each domain and the percentage it represents of the total email count.
- **Output Files:** Generates multiple CSV files that list business and personal email domains, their counts, and percentages.

## How to Use
1. **Prepare Your Data:** Ensure your CSV file contains a column named `email` with the email addresses. Save this file as `emails.csv`.
2. **Run the Script:** Execute the main script to analyze the email domains. The script will output CSV files with detailed domain data.
3. **Review Results:** Check the generated CSV files for a breakdown of email domain occurrences and their categorization.

## Output
The tool generates the following files:
- `business_email_analysis.csv` - Lists business email domains along with their counts and percentages.
- `personal_email_analysis.csv` - Lists personal email domains along with their counts and percentages.
- `business_emails_list.csv` - Contains all emails classified as business emails with their respective domains.
- `personal_emails_list.csv` - Contains all emails classified as personal emails with their respective domains.

## Requirements
- Python 3
- Pandas library

Install Pandas using pip:
```bash
pip install pandas
```

## Contribution
Contributions to this project are welcome. You can contribute by improving the code efficiency, adding features, or refining the domain categorization logic. Fork this repository, make your changes, and submit a pull request.

## License
This project is open-sourced under the MIT license.

---

Feel free to adjust the content to better fit your project's specifics or let me know if you need additional sections or specific details included!
