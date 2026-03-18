# Merged dataset format - Name, SiteDescription, Administrator, Licensee,
# StreetAddress, City, State, Zip, County, Email, PhoneNumber

# import pandas
import pandas as pd

# turn CSV datasets into pandas dataframes

# From Adult_Residential_Facilities.csv
# Extracting relevant colums
cols_to_use_1 = ["FacilityName", "FacilityType", "FacilityAdministrator", 
               "Licensee", "FacilityAddress", "FacilityCity", "FacilityState", 
               "FacilityZip", "CountyName" , "FacilityEmail", 
               "FacilityTelephoneNumber"]
# Converting csv file into pandas dataframe
df1 = pd.read_csv("data/Adult_Residential_Facilities.csv", 
                  usecols = cols_to_use_1)[cols_to_use_1]
# Rename dataset-specific column names to merged column names
df1 = df1.rename(columns={"FacilityName" : "Name", 
                    "FacilityType" : "SiteDescription",
                    "FacilityAdministrator" : "Administrator", 
                    "FacilityAddress" : "StreetAddress",
                    "FacilityCity" : "City", "FacilityState" : "State", 
                    "FacilityZip" : "Zip", "CountyName" : "County", 
                    "FacilityEmail" : "Email", 
                    "FacilityTelephoneNumber" : "PhoneNumber"})

# From Business_Sites.csv
cols_to_use_2 = ["OWNNAM1", "OWNNAM2", "OWNNAM3", "BUSTYPE", "CAREOF", 
                "SITE_ADDRESS", "LOCCIT"]
df2 = pd.read_csv("data/Business_Sites.csv", usecols = cols_to_use_2)[cols_to_use_2]
df2["OWNNAM2"] = df2["OWNNAM2"].fillna('')
df2["OWNNAM3"] = df2["OWNNAM3"].fillna('')
df2["Name"] = df2["OWNNAM1"] + " " + df2["OWNNAM2"] + " " + df2["OWNNAM3"]
df2 = df2.drop(columns = ["OWNNAM1", "OWNNAM2", "OWNNAM3"])
df2 = df2.rename(columns={"BUSTYPE" : "SiteDescription",
                    "CAREOF" : "Administrator", 
                    "SITE_ADDRESS" : "StreetAddress",
                    "LOCCIT" : "City"})
# Insert missing columns
df2.insert(3, "Licensee", pd.Series(dtype = 'str'))
df2.insert(6, "State", pd.Series('str'))
df2["State"] = "CA"
df2.insert(7, "Zip", pd.Series(dtype = 'float'))
df2.insert(8, "County", pd.Series('str'))
df2["County"] = "SAN DIEGO"
df2.insert(9, "Email", pd.Series(dtype = 'str'))
df2.insert(10, "PhoneNumber", pd.Series(dtype = 'str'))

# From City_Owned_Lands.csv
cols_to_use_3 = ["common_nm", "desg_use", "managing_dept", "location", 
               "cmty_plan"]
df3 = pd.read_csv("data/City_Owned_Lands.csv", 
                  usecols = cols_to_use_3)[cols_to_use_3]
df3 = df3.rename(columns={"common_nm" : "Name", "desg_use" : "SiteDescription",
                    "managing_dept" : "Administrator", 
                    "location" : "StreetAddress",
                    "cmty_plan" : "City"})
df3.insert(3, "Licensee", pd.Series(dtype = 'str'))
df3.insert(6, "State", pd.Series(dtype = 'str'))
df3.insert(7, "Zip", pd.Series(dtype = 'int'))
df3.insert(8, "County", pd.Series(dtype = 'int'))
df3.insert(9, "Email", pd.Series(dtype = 'str'))
df3.insert(10, "PhoneNumber", pd.Series(dtype = 'str'))

# From Elder_Care_Facilities.csv
cols_to_use_4 = ["FacilityName", "FacilityType", "FacilityAdministrator", 
               "Licensee", "FacilityAddress", "FacilityCity", "FacilityState", 
               "FacilityZip", "CountyName" , "FacilityEmail", 
               "FacilityTelephoneNumber"]
df4 = pd.read_csv("data/Elder_Care_Facilities.csv", 
                  usecols = cols_to_use_4)[cols_to_use_4]
df4 = df4.rename(columns={"FacilityName" : "Name", 
                    "FacilityType" : "SiteDescription",
                    "FacilityAdministrator" : "Administrator", 
                    "FacilityAddress" : "StreetAddress",
                    "FacilityCity" : "City", "FacilityState" : "State", 
                    "FacilityZip" : "Zip", "CountyName" : "County", 
                    "FacilityEmail" : "Email", 
                    "FacilityTelephoneNumber" : "PhoneNumber"})

# From Healthcare_Facilities.csv
cols_to_use_5 = ["FACILITY_NAME", "FACILITY_LEVEL_DESC", "DBA_ADDRESS1", 
               "DBA_CITY", "DBA_ZIP_CODE", "COUNTY_NAME"]
df5 = pd.read_csv("data/Healthcare_Facilities.csv", 
                  usecols = cols_to_use_5)[cols_to_use_5]
df5 = df5.rename(columns={"FACILITY_NAME" : "Name", 
                    "FACILITY_LEVEL_DESC" : "SiteDescription",
                    "DBA_ADDRESS1" : "StreetAddress",
                    "DBA_CITY" : "City", "DBA_ZIP_CODE" : "Zip", 
                    "COUNTY_NAME" : "County"})
df5.insert(2, "Administrator", pd.Series(dtype = 'str'))
df5.insert(3, "Licensee", pd.Series(dtype = 'str'))
df5.insert(6, "State", pd.Series(dtype = 'str'))
df5.insert(9, "Email", pd.Series(dtype = 'str'))
df5.insert(10, "PhoneNumber", pd.Series(dtype = 'str'))

# From Places.csv
cols_to_use_6 = ["NAME", "TYPE", "ADDR", "CITYNM", "Zipcode"]
df6 = pd.read_csv("data/Places.csv", 
                  usecols = cols_to_use_6)[cols_to_use_6]
df6 = df6.rename(columns={"NAME" : "Name", 
                    "TYPE" : "SiteDescription",
                    "ADDR" : "StreetAddress",
                    "CITYNM" : "City", "Zipcode" : "Zip"})
df6.insert(2, "Administrator", pd.Series(dtype = 'str'))
df6.insert(3, "Licensee", pd.Series(dtype = 'str'))
df6.insert(6, "State", pd.Series(dtype = 'str'))
df6["State"] = "CA"
df6.insert(8, "County", pd.Series(dtype = 'str'))
df6["County"] = "SAN DIEGO"
df6.insert(9, "Email", pd.Series(dtype = 'str'))
df6.insert(10, "PhoneNumber", pd.Series(dtype = 'str'))

# merge dataframes
df = pd.concat([df1, df2, df3, df4, df5, df6])
# export dataframes to csv as final merged dataset
df.to_csv("merged/Merged_Dataset.csv", index = False)