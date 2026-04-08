from requests_html import AsyncHTMLSession
from bs4 import BeautifulSoup
import asyncio
import re
import html
import requests

async def main(): 

    contact_urls = open('contact_urls.txt', 'w')
    # Any list of websites
    with open('websites.txt', 'r') as file:

        for line in file:

            try:

                if line.strip() == 'nan': 
                    contact_urls.write('NaN')
                    contact_urls.write('\n')
                    continue

                if 'https://' not in line.strip():
                    line = 'https://' + line.strip().lower()
                    print(line)

                ccount = 0
            
                session = AsyncHTMLSession()
                page = await session.get(line.strip())
                await page.html.arender(sleep=3, timeout=5)
                soup = BeautifulSoup(page.html.raw_html, 'html.parser')

                for link in soup.find_all('a'):
                
                    str = link.get('href')
                    if str:
            
                        if str.find('contact') != -1 and ccount == 0:
                            if str.find('https') != -1:
                                contact_urls.write(str)
                                contact_urls.write('\n')
                            else:
                                contact_link = (line.strip() + str).replace('//contact', '/contact')
                                contact_urls.write(contact_link)
                                contact_urls.write('\n')
                            ccount = 1

                if ccount == 0:
                    contact_urls.write('NaN')
                    contact_urls.write('\n')

            except Exception: 
                
                contact_urls.write('NaN')
                contact_urls.write('\n')

            if session:
                await session.close()

    contact_urls.close()

    emails_2 = open('emails_2.txt', 'a')
    forms = open('forms.txt', 'a')
    with open('contact_urls.txt', 'r') as file:

        for line in file:

            print(line)

            try:
            
                if line.strip() == 'NaN': 
                    emails_2.write('NaN')
                    emails_2.write('\n')
                    forms.write('NaN')
                    forms.write('\n')
                    continue

                ecount = 0
                fcount = 0

                session = AsyncHTMLSession()
                page = await session.get(line.strip())
                await page.html.arender(sleep=3, timeout=5)
                soup = BeautifulSoup(page.html.raw_html, 'html.parser')

                my_set = set()
                for link in soup.find_all('a'):
                    str = link.get('href')
                    if str and str.find('mailto:') != -1:
                        email = str.replace('mailto:', '') + ', '
                        if email not in my_set:  
                            emails_2.write(email)
                            my_set.add(email)
                            ecount = 1

                if soup.find('form'):
                    forms.write(line.strip() + ' ')
                    fcount = 1

                if ecount == 0:
                    emails_2.write('NaN')
                    emails_2.write('\n')
                else:
                    emails_2.write('\n')
                if fcount == 0:
                    forms.write('NaN')
                    forms.write('\n')
                else:
                    forms.write('\n')

            except:

                emails_2.write('NaN')
                emails_2.write('\n')
                forms.write('NaN')
                forms.write('\n')

            if session:
                await session.close()

        emails_2.close()
        forms.close()

asyncio.run(main())
