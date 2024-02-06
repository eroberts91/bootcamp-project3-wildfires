import pandas as pd


file_path = 'Fires3.csv'

df = pd.read_csv(file_path)

#Name, Year, Cause, Size, Lat/long,State
selected_columns = ['FIRE_NAME', 'FIRE_YEAR', 'NWCG_GENERAL_CAUSE', 'FIRE_SIZE', 'LATITUDE', 'LONGITUDE', 'STATE']
cleaned_df = df[selected_columns]


cleaned_file_path = 'cleaned_Fires.csv'
cleaned_df.to_csv(cleaned_file_path, index=False)


cleaned_df.head() 


cleaned_df['CAUSE'] = cleaned_df['CAUSE'].copy()

#Match justin's abbrv
cleaned_df['CAUSE'].replace({
    'Debris and open burning': 'Debris Burning', 
    'Missing data/not specified/undetermined': 'Undetermined', 
    'Recreation and ceremony': 'Recreation',
    'Equipment and vehicle use': 'Equipment use',
    'Arson/incendiarism': 'Arson',
    'Railroad operations and maintenance': 'Railroad',
    'Misuse of fire by a minor': 'Children',
    'Firearms and explosives use': 'Firearms',
    'Power generation/transmission/distribution': 'Electricity supply'
}, inplace=True)


print(cleaned_df.head())

cleaned_df['CAUSE'].replace({
    'Debris and open burning': 'Debris Burning',
    'Missing data/not specified/undetermined': 'Undetermined',
    'Recreation and ceremony': 'Recreation',
    'Equipment and vehicle use': 'Equipment use',
    'Arson/incendiarism': 'Arson',
    'Railroad operations and maintenance': 'Railroad',
    'Misuse of fire by a minor': 'Children',
    'Firearms and explosives use': 'Firearms',
    'Power generation/transmission/distribution': 'Electricity supply'
}, inplace=True)

#check to see if it actually overwrote after, change to engine = python?
cleaned_df.to_csv('cleaned_Fires.csv', index=False)

#check again 
cleaned_df.head()

