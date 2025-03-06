import pandas as pd

# Load the CSV file
df = pd.read_csv('emails.csv')

# List of personal email domains to filter out
personal_emails = [
    "yahoo.com", "ymail.com", "yahoo.es", "yahoo.fr", "yahoo.co.uk", "yahoo.com.mx", "yahoo.com.ar", "yahoo.com.br",
    "gmail.com", "googlemail.com",
    "aol.com",
    "hotmail.com", "hotmail.it",
    "att.net",
    "bellsouth.net",
    "icloud.com",
    "me.com",
    "mac.com",
    "live.com",
    "msn.com",
    "outlook.com", "outlook.fr",
    "rocketmail.com",
    "mail.com",
    "comcast.net",
    "sbcglobal.net", "sbcglobai.net",
    "epix.net",
    "verizon.net",
    "charter.net",
    "netzero.net",
    "aim.com",
    "cs.com",
    "juno.com",
    "rock.com",
    "earthlink.net",
    "centurytel.net",
    "flash.net",
    "peoplepc.com",
    "cableone.net",
    "roadrunner.com",
    "cox.net",
    "gmx.net",
    "telus.net",
    "myway.com",
    "popchick.com",
    "hellokitty.com",
    "mail2hell.com",
    "proton.me"
]

# Extract the domain from email addresses
df['domain'] = df['email'].apply(lambda x: x.split('@')[-1])

# Separate dataframes for business and personal emails
df_personal = df[df['domain'].isin(personal_emails)]
df_business = df[~df['domain'].isin(personal_emails)]

# Count occurrences of each domain in business and personal emails
business_counts = df_business['domain'].value_counts().reset_index()
business_counts.columns = ['domain', 'business_count']
personal_counts = df_personal['domain'].value_counts().reset_index()
personal_counts.columns = ['domain', 'personal_count']

# Calculate the percentage of each domain
total_business_count = business_counts['business_count'].sum()
business_counts['business_percentage'] = (business_counts['business_count'] / total_business_count) * 100

total_personal_count = personal_counts['personal_count'].sum()
personal_counts['personal_percentage'] = (personal_counts['personal_count'] / total_personal_count) * 100

# Create columns listing out emails
df_business['business_emails'] = df_business['email']
df_personal['personal_emails'] = df_personal['email']

# Save the results to new CSV files
business_counts.to_csv('business_email_analysis.csv', index=False)
personal_counts.to_csv('personal_email_analysis.csv', index=False)

df_business[['email', 'domain', 'business_emails']].to_csv('business_emails_list.csv', index=False)
df_personal[['email', 'domain', 'personal_emails']].to_csv('personal_emails_list.csv', index=False)

