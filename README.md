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
- Master_EIN_SD.csv

### EIN + XML Enrichment

After validating nonprofit matching on EIN, I added an IRS XML step to enrich matched nonprofits with organization and leadership contact information.

### XML Sources
- XML/ (IRS filing XMLs)
- data/2025_XML/ (additional IRS filing XMLs)

### XML Output
- EIN_XML_combining.ipynb
- Person-level nonprofit contact table
- Fields include EIN, organization name, website, address, person name, and title

### Key Files
- `Master_EIN_SD.csv`: San Diego nonprofit EIN matching output combining IRS and ProPublica nonprofit information
- `CalNonprofits_Contact_Information.csv`: nonprofit directory contact data including websites, public emails, social links, and phone numbers
- `sd_nonprofit_prospects_irs_enriched.csv`: nonprofit prospect list enriched with IRS organization information such as revenue and assets
- `mission_aligned.csv`: filtered site/entity list used for outreach targeting

### Contact Generation Use Case
- XML enrichment is used to surface nonprofit leadership contacts from IRS 990 filings
- Website domains can be cleaned and paired with `person_name` to generate likely email patterns
- Four main email guesses used:
  - `first@domain.com`
  - `first.last@domain.com`
  - `flast@domain.com`
  - `firstlast@domain.com`
- EIN remains the key field used to connect organization-level tax and registry data back to the contact pipeline

### CA_Nonprofit_Contact_Info
- Nonprofits sourced from the CalNonprofits member directory
- Fields: Name, Organization Type, Street Address, County, Website, Emails (General Contact), Staff/Misc Emails, Contact Form Link, Linkedin, Instagram, Facebook, X, Threads, BlueSky, Phone Number
