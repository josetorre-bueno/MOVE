# import pandas
import pandas as pd

# turn CSV datasets into pandas dataframes
df1 = pd.read_csv("Adult_Residential_Facilities.csv", index_col = False,
    usecols = ["FacilityName", "Licensee", "FacilityAdministrator", 
               "FacilityAddress", "FacilityCity", "FacilityState", 
               "FacilityZip", "CountyName", "FacilityType", "FacilityEmail", 
               "FacilityTelephoneNumber"])

df1 = df1.rename(columns={"FacilityName" : "Name", "FacilityAdministrator" :
                    "Administrator", "FacilityAddress" : "Address",
                    "FacilityCity" : "City", "FacilityState" : "State", 
                    "FacilityZip" : "Zip", "CountyName" : "County", 
                    "FacilityType" : "SiteType", 
                    "FacilityEmail" : "Email", 
                    "FacilityTelephoneNumber" : "TelephoneNumber"})

df3 = pd.read_csv("City_Owned_Lands.csv", index_col = False,
    usecols = ["common_nm", "managing_dept", "location", 
               "cmty_plan", "desg_use"])
df3 = df3.rename(columns={"common_nm" : "Name", "managing_dept" :
                    "Administrator", "location" : "Address",
                    "cmty_plan" : "City", "desg_use" : "SiteType"})
df3.insert(4, "State", pd.Series(dtype = 'str'))
df3.insert(5, "Zip", pd.Series(dtype = 'int'))
df3.insert(7, "Email", pd.Series(dtype = 'str'))
df3.insert(8, "TelephoneNumber", pd.Series(dtype = 'str'))

df4 = pd.read_csv("Elder_Care_Facilities.csv", index_col = False,
    usecols = ["FacilityName", "Licensee", "FacilityAdministrator", 
               "FacilityAddress", "FacilityCity", "FacilityState", 
               "FacilityZip", "CountyName", "FacilityType", "FacilityEmail", 
               "FacilityTelephoneNumber"])
df4 = df4.rename(columns={"FacilityName" : "Name", "FacilityAdministrator" :
                    "Administrator", "FacilityAddress" : "Address",
                    "FacilityCity" : "City", "FacilityState" : "State", 
                    "FacilityZip" : "Zip", "CountyName" : "County", 
                    "FacilityType" : "SiteType", 
                    "FacilityEmail" : "Email", 
                    "FacilityTelephoneNumber" : "TelephoneNumber"})

df5 = pd.read_csv("Healthcare_Facilities.csv", index_col = False,
    usecols = ["FACILITY_NAME", "DBA_ADDRESS1", 
               "DBA_CITY", "DBA_ZIP_CODE", "COUNTY_NAME", 
               "FACILITY_LEVEL_DESC"])
df5 = df5.rename(columns={"FACILITY_NAME" : "Name", "DBA_ADDRESS1" : "Address",
                    "DBA_CITY" : "City", "DBA_ZIP_CODE" : "Zip", 
                    "COUNTY_NAME" : "County",
                    "FACILITY_LEVEL_DESC" : "SiteType"})
df5.insert(1, "Administrator", pd.Series(dtype = 'str'))
df5.insert(6, "State", pd.Series(dtype = 'str'))
df5.insert(7, "Email", pd.Series(dtype = 'str'))
df5.insert(8, "TelephoneNumber", pd.Series(dtype = 'str'))

df = pd.concat([df1, df3, df4, df5])
df.to_csv("Merged_Dataset.csv", index = False)