import pandas as pd
import requests


api_key = 'UURI49ZijBsQgi7tmF4mbFkhHODMVNvtGQSNAGLsrlMIhsnckbcMYGdQLVqem8yd'

# input_file_path = r"C:\Users\TavishNoel\Downloads\input2.xlsx"
input_file_path = r"input.xlsx"
df = pd.read_excel(input_file_path, sheet_name='Sheet1')
print(df)

def get_zip_codes_in_radius(api_key, center_zip, radius_miles=25):
    print(api_key,center_zip,radius_miles)
    base_url = f"https://www.zipcodeapi.com/rest/{api_key}/radius.json/{center_zip}/{radius_miles}/mile"
    url = base_url.format(api_key, center_zip, radius_miles, 'mi')
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        Zip_list = []
        for i in data['zip_codes']:
            ###Zip_list.append(i['zip_code'])
            Zip_list.append(i['zip_code'])
            
        return Zip_list
    else:
        print(f"Error: {response.status_code}")
        return []


df['Output Zip Codes'] = df['Zip codes'].apply(lambda zip_code: get_zip_codes_in_radius(api_key, zip_code))

# output_file_path = r"C:\Users\TavishNoel\Downloads\output2.xlsx" 
output_file_path = r"output2.xlsx" 
df.to_excel(output_file_path, index=False)

# Read input Excel file
#input_file_path = r"C:\Users\TavishNoel\Downloads\input2.xlsx"
#df = pd.read_excel(input_file_path, sheet_name='Sheet1')

