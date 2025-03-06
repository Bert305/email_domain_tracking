import pandas as pd

# Load the CSV file
df = pd.read_csv('emails.csv')

# Function to extract domain from an email address
def extract_domain(email):
    return email.split('@')[-1]

# Apply the function to extract domains
df['domain'] = df['email'].apply(extract_domain)

# Count occurrences of each domain
domain_counts = df['domain'].value_counts().reset_index()
domain_counts.columns = ['domain', 'count']

# Save the domain counts to a CSV file
domain_counts.to_csv('email_domains_count.csv', index=False)

# Optional: save the original dataframe with domains to another CSV
df.to_csv('emails_with_domains.csv', index=False)

print("Domains and their counts have been saved to 'email_domains_count.csv'.")
