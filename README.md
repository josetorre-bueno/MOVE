Merged Dataset 

- Datasets Merged So Far: Business_Sites.csv, Adult_Residential_Facilities.csv, City_Owned_Lands.csv, Elder_Care_Facilities.csv, Healthcare_Facilities.csv, 
Places.csv

- Merged Dataset Columns:
    - Name (Site business name)
    - SiteDescription (Type or use of site)
    - Administrator (Person or entity that owns or administrates site)
    - Licensee (Similar to administrator; specific to Adult_Residential_Facilities.csv and Elder_Care_Facilities.csv)
    - StreetAddress (Site address)
    - City (Site city)
    - State (Site state; all sites in California)
    - Zip (Site zip code)
    - County (Site county; all sites in San Diego County)
    - Email (Site email address; missing for all sites)
    - PhoneNumber (Site phone number; available only for Adult_Residential_Facilities.csv and Elder_Care_Facilities.csv)



### Subset Test Dataset (San Diego Nonprofits + IRS)

To validate EIN-based matching before adding to the full pipeline, I created a smaller San Diego-only nonprofit subset.

### Source Files
- propublica_SD_located_nonprofits.csv (ProPublica API results, San Diego located)
- irs_eo_san_diego.csv (IRS EO San Diego extract)

### Merge Logic
- Outer merge on EIN
- _merge indicator kept to track match status: left_only, both, right_only

### Output
- San_Diego_Non_Profits_EIN.csv