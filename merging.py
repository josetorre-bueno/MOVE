

''' Merged dataset format - Name, SiteDescription, Administrator, Licensee,
    StreetAddress, City, State, Zip, County, Email, TelephoneNumber
'''

# import pandas
import pandas as pd

# turn CSV datasets into pandas dataframes

cols_to_use_1 = ["FacilityName", "FacilityType", "FacilityAdministrator", 
               "Licensee", "FacilityAddress", "FacilityCity", "FacilityState", 
               "FacilityZip", "CountyName" , "FacilityEmail", 
               "FacilityTelephoneNumber"]
df1 = pd.read_csv("Adult_Residential_Facilities.csv", 
                  usecols = cols_to_use_1)[cols_to_use_1]
df1 = df1.rename(columns={"FacilityName" : "Name", 
                    "FacilityType" : "SiteDescription",
                    "FacilityAdministrator" : "Administrator", 
                    "FacilityAddress" : "Address",
                    "FacilityCity" : "City", "FacilityState" : "State", 
                    "FacilityZip" : "Zip", "CountyName" : "County", 
                    "FacilityEmail" : "Email", 
                    "FacilityTelephoneNumber" : "TelephoneNumber"})

cols_to_use_3 = ["common_nm", "desg_use", "managing_dept", "location", 
               "cmty_plan"]
df3 = pd.read_csv("City_Owned_Lands.csv", 
                  usecols = cols_to_use_3)[cols_to_use_3]
df3 = df3.rename(columns={"common_nm" : "Name", "desg_use" : "SiteDescription",
                    "managing_dept" : "Administrator", "location" : "Address",
                    "cmty_plan" : "City"})
df3.insert(3, "Licensee", pd.Series(dtype = 'str'))
df3.insert(6, "State", pd.Series(dtype = 'str'))
df3.insert(7, "Zip", pd.Series(dtype = 'int'))
df3.insert(8, "County", pd.Series(dtype = 'int'))
df3.insert(9, "Email", pd.Series(dtype = 'str'))
df3.insert(10, "TelephoneNumber", pd.Series(dtype = 'str'))

cols_to_use_4 = ["FacilityName", "FacilityType", "FacilityAdministrator", 
               "Licensee", "FacilityAddress", "FacilityCity", "FacilityState", 
               "FacilityZip", "CountyName" , "FacilityEmail", 
               "FacilityTelephoneNumber"]
df4 = pd.read_csv("Elder_Care_Facilities.csv", 
                  usecols = cols_to_use_4)[cols_to_use_4]
df4 = df4.rename(columns={"FacilityName" : "Name", 
                    "FacilityType" : "SiteDescription",
                    "FacilityAdministrator" : "Administrator", 
                    "FacilityAddress" : "Address",
                    "FacilityCity" : "City", "FacilityState" : "State", 
                    "FacilityZip" : "Zip", "CountyName" : "County", 
                    "FacilityEmail" : "Email", 
                    "FacilityTelephoneNumber" : "TelephoneNumber"})

cols_to_use_5 = ["FACILITY_NAME", "FACILITY_LEVEL_DESC", "DBA_ADDRESS1", 
               "DBA_CITY", "DBA_ZIP_CODE", "COUNTY_NAME"]
df5 = pd.read_csv("Healthcare_Facilities.csv", 
                  usecols = cols_to_use_5)[cols_to_use_5]
df5 = df5.rename(columns={"FACILITY_NAME" : "Name", 
                    "FACILITY_LEVEL_DESC" : "SiteDescription",
                    "DBA_ADDRESS1" : "Address",
                    "DBA_CITY" : "City", "DBA_ZIP_CODE" : "Zip", 
                    "COUNTY_NAME" : "County"})
df5.insert(2, "Administrator", pd.Series(dtype = 'str'))
df5.insert(3, "Licensee", pd.Series(dtype = 'str'))
df5.insert(6, "State", pd.Series(dtype = 'str'))
df5.insert(9, "Email", pd.Series(dtype = 'str'))
df5.insert(10, "TelephoneNumber", pd.Series(dtype = 'str'))

df = pd.concat([df1, df3, df4, df5])
df.to_csv("Merged_Dataset.csv", index = False)