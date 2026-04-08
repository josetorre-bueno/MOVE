
import pandas as pd 
import numpy as np
import requests
import zipfile
import io
import re
import os
import pyzstd
import struct
import zlib
import inflate64
from pathlib import Path
import xml.etree.ElementTree as ET
import pandas as pd

# this currently uses the San Diego Nonporfits EIN dataset to find matches in the index you can change this 
# to whatever dataset you need just make sure that it has EINs
df= pd.read_csv('EIN_approach/data/San_Diego_Non_Profits_EIN.csv')

# You need to download this index at https://www.irs.gov/charities-non-profits/form-990-series-downloads 
# Also currently this is scrapes for the 2025 forms you can change this to whatever year you like
index=pd.read_csv('data/index_2025.csv')

xml_merged= pd.merge(df,index,on='EIN',how='inner')

files_needed=xml_merged['XML_BATCH_ID'].unique()


output_dir = "XML"
os.makedirs(output_dir, exist_ok=True)

# actual xml extraction 
def read_zip_entry(zf, filename):
    """Read any zip entry by reading raw bytes and decompressing manually."""
    zinfo = zf.getinfo(filename)

    zf.fp.seek(zinfo.header_offset)
    fheader = zf.fp.read(30)
    fname_len = struct.unpack_from('<H', fheader, 26)[0]
    extra_len = struct.unpack_from('<H', fheader, 28)[0]
    zf.fp.seek(zinfo.header_offset + 30 + fname_len + extra_len)
    raw = zf.fp.read(zinfo.compress_size)

    if zinfo.compress_type == 0:    
        return raw
    elif zinfo.compress_type == 8: 
        return zlib.decompress(raw, -15)
    elif zinfo.compress_type == 9:  
        inflater = inflate64.Inflater()
        return inflater.inflate(raw)
    elif zinfo.compress_type == 93: 
        return pyzstd.decompress(raw)
    else:
        raise NotImplementedError(f"Unsupported compression type: {zinfo.compress_type}")


for name in files_needed:
    r = requests.get(f"https://apps.irs.gov/pub/epostcard/990/xml/2025/{name}.zip")
    z = zipfile.ZipFile(io.BytesIO(r.content))
    ein_needed = set(str(int(e)).zfill(9)for e in xml_merged[xml_merged['XML_BATCH_ID'] == name]['EIN'].unique())

    for file in z.namelist():
        xml_bytes = read_zip_entry(z, file)
        xml = xml_bytes.decode("utf-8", errors="ignore")

        match = re.search(r"<EIN>(\d{9})</EIN>", xml)
        if match:
            ein = match.group(1)

            if ein in ein_needed:
                filename = file.split("/")[-1]
                save_path = os.path.join(output_dir, filename)

                with open(save_path, "wb") as f:
                    f.write(xml_bytes)


folder = Path("XML")
data = []

#Parses each xml file to get the data fields that you want
for file in folder.iterdir():
    tree = ET.parse(file)
    root = tree.getroot()
# Modify this portion to get the specifc fields that you want 
    # Preparer Firm

    preparer_firm_ein = root.find(".//{*}PreparerFirmGrp/{*}PreparerFirmEIN")
    preparer_firm_name = root.find(".//{*}PreparerFirmName/{*}BusinessNameLine1Txt")
    preparer_addr = root.find(".//{*}PreparerUSAddress/{*}AddressLine1Txt")
    preparer_city = root.find(".//{*}PreparerUSAddress/{*}CityNm")
    preparer_state = root.find(".//{*}PreparerUSAddress/{*}StateAbbreviationCd")
    preparer_zip = root.find(".//{*}PreparerUSAddress/{*}ZIPCd")

    # Preparer Person
    preparer_person = root.find(".//{*}PreparerPersonGrp/{*}PreparerPersonNm")
    preparer_ptin = root.find(".//{*}PreparerPersonGrp/{*}PTIN")
    preparer_phone = root.find(".//{*}PreparerPersonGrp/{*}PhoneNum")
    preparer_self = root.find(".//{*}PreparerPersonGrp/{*}SelfEmployedInd")

    # Nonprofit (Filer)
    filer_ein = root.find(".//{*}Filer/{*}EIN")
    nonprofit_name = root.find(".//{*}Filer/{*}BusinessName/{*}BusinessNameLine1Txt")
    filer_phone = root.find(".//{*}Filer/{*}PhoneNum")
    filer_addr = root.find(".//{*}Filer/{*}USAddress/{*}AddressLine1Txt")
    filer_city = root.find(".//{*}Filer/{*}USAddress/{*}CityNm")
    filer_state = root.find(".//{*}Filer/{*}USAddress/{*}StateAbbreviationCd")
    filer_zip = root.find(".//{*}Filer/{*}USAddress/{*}ZIPCd")

    # Business Officer
    officer_name = root.find(".//{*}BusinessOfficerGrp/{*}PersonNm")
    officer_title = root.find(".//{*}BusinessOfficerGrp/{*}PersonTitleTxt")
    officer_phone = root.find(".//{*}BusinessOfficerGrp/{*}PhoneNum")
    officer_sig = root.find(".//{*}BusinessOfficerGrp/{*}SignatureDt")
    officer_discuss = root.find(".//{*}BusinessOfficerGrp/{*}DiscussWithPaidPreparerInd")

    # Books in Care Of
    books_name = root.find(".//{*}BooksInCareOfDetail/{*}BusinessName/{*}BusinessNameLine1Txt")
    books_phone = root.find(".//{*}BooksInCareOfDetail/{*}PhoneNum")
    books_addr = root.find(".//{*}BooksInCareOfDetail/{*}USAddress/{*}AddressLine1Txt")
    books_city = root.find(".//{*}BooksInCareOfDetail/{*}USAddress/{*}CityNm")
    books_state = root.find(".//{*}BooksInCareOfDetail/{*}USAddress/{*}StateAbbreviationCd")
    books_zip = root.find(".//{*}BooksInCareOfDetail/{*}USAddress/{*}ZIPCd")

    # Principal Officer
    principal_name = root.find(".//{*}PrincipalOfficerNm")
    principal_addr = root.find(".//{*}IRS990/{*}USAddress/{*}AddressLine1Txt")
    principal_city = root.find(".//{*}IRS990/{*}USAddress/{*}CityNm")
    principal_state = root.find(".//{*}IRS990/{*}USAddress/{*}StateAbbreviationCd")
    principal_zip = root.find(".//{*}IRS990/{*}USAddress/{*}ZIPCd")

    # Board (first entry)
    board_name = root.find(".//{*}Form990PartVIISectionAGrp/{*}PersonNm")
    board_title = root.find(".//{*}Form990PartVIISectionAGrp/{*}TitleTxt")
    board_hours = root.find(".//{*}Form990PartVIISectionAGrp/{*}AverageHoursPerWeekRt")
    board_officer = root.find(".//{*}Form990PartVIISectionAGrp/{*}OfficerInd")


    data.append({
        "preparer_firm_ein": preparer_firm_ein.text if preparer_firm_ein is not None else None,
        "preparer_firm_name": preparer_firm_name.text if preparer_firm_name is not None else None,
        "preparer_addr": preparer_addr.text if preparer_addr is not None else None,
        "preparer_city": preparer_city.text if preparer_city is not None else None,
        "preparer_state": preparer_state.text if preparer_state is not None else None,
        "preparer_zip": preparer_zip.text if preparer_zip is not None else None,

        "preparer_person": preparer_person.text if preparer_person is not None else None,
        "preparer_ptin": preparer_ptin.text if preparer_ptin is not None else None,
        "preparer_phone": preparer_phone.text if preparer_phone is not None else None,
        "preparer_self": preparer_self.text if preparer_self is not None else None,

        "nonprofit_ein": filer_ein.text if filer_ein is not None else None,
        "nonprofit_name": nonprofit_name.text if nonprofit_name is not None else None,
        "nonprofit_phone": filer_phone.text if filer_phone is not None else None,
        "nonprofit_addr": filer_addr.text if filer_addr is not None else None,
        "nonprofit_city": filer_city.text if filer_city is not None else None,
        "nonprofit_state": filer_state.text if filer_state is not None else None,
        "nonprofit_zip": filer_zip.text if filer_zip is not None else None,

        "officer_name": officer_name.text if officer_name is not None else None,
        "officer_title": officer_title.text if officer_title is not None else None,
        "officer_phone": officer_phone.text if officer_phone is not None else None,
        "officer_signature": officer_sig.text if officer_sig is not None else None,
        "officer_discuss": officer_discuss.text if officer_discuss is not None else None,

        "books_name": books_name.text if books_name is not None else None,
        "books_phone": books_phone.text if books_phone is not None else None,
        "books_addr": books_addr.text if books_addr is not None else None,
        "books_city": books_city.text if books_city is not None else None,
        "books_state": books_state.text if books_state is not None else None,
        "books_zip": books_zip.text if books_zip is not None else None,

        "principal_name": principal_name.text if principal_name is not None else None,
        "principal_addr": principal_addr.text if principal_addr is not None else None,
        "principal_city": principal_city.text if principal_city is not None else None,
        "principal_state": principal_state.text if principal_state is not None else None,
        "principal_zip": principal_zip.text if principal_zip is not None else None,

        "board_name": board_name.text if board_name is not None else None,
        "board_title": board_title.text if board_title is not None else None,
        "board_hours": board_hours.text if board_hours is not None else None,
        "board_officer": board_officer.text if board_officer is not None else None,
    })

df = pd.DataFrame(data)

df.to_csv('xml_dataset.csv', index=False)