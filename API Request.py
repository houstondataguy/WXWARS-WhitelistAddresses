import requests
import math
import pandas as pd

account = 'rpuxwHsnZzAd9GiX1kdkgmxgxmGEiH8bmS'

url = f"https://api.xrpscan.com/api/v1/account/{account}/trustlines2"

response = requests.get(url)

if response.status_code  == 200:
    trustlines_data = response.json()

    # List to store holder accounts and their rounded positive balances
    data = []

    # Iterate over each trustline in the response
    for trustline in trustlines_data['lines']:
        balance = float(trustline['balance'])

        # Only include accounts where balance is non-zero
        if balance != 0:
            # Round the balance down and convert to positive
            rounded_balance = math.floor(abs(balance))

            # Store account and the processed balance
            data.append({
                'Holder Account': trustline['account'],
                'WXWARS Balance': rounded_balance
            })

    # Convert to pandas DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    csv_file = 'wxwars_holders.csv'
    df.to_csv(csv_file, index=False)

    print(f"CSV file '{csv_file}' has been created.")
else:
    print(f"Failed to retrieve trustlines. Status code: {response.status_code}")

