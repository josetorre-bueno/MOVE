
from requests_html import AsyncHTMLSession
from bs4 import BeautifulSoup
import asyncio
import re
import html
import requests

async def main(): 

    facebook = open('facebook.txt', 'a')
    x = open('x.txt', 'a')
    instagram = open('instagram.txt', 'a')
    bsky = open('bsky.txt', 'a')
    threads = open('threads.txt', 'a')
    linkedin = open('linkedin.txt', 'a')
    emails_1 = open('emails_1.txt', 'a')

    # Any list of websites
    with open('websites.txt', 'r') as file:

        for line in file:

            print(line)
            
            try:

                if line.strip() == 'NaN': 
                    facebook.write('NaN')
                    facebook.write('\n')
                    x.write('NaN')
                    x.write('\n')
                    instagram.write('NaN')
                    instagram.write('\n')
                    bsky.write('NaN')
                    bsky.write('\n')
                    threads.write('NaN')
                    threads.write('\n')
                    linkedin.write('NaN')
                    linkedin.write('\n')
                    emails_1.write('NaN')
                    emails_1.write('\n')
                    continue

                fcount = 0
                xcount = 0
                icount = 0
                bcount = 0
                tcount = 0
                lcount = 0
                ecount = 0
                
                session = AsyncHTMLSession()
                page = await session.get(line.strip())
                await page.html.arender(sleep=3, timeout=5)
                soup = BeautifulSoup(page.html.raw_html, 'html.parser')

                for link in soup.find_all('a'):
                    
                    str = link.get('href')
                    if str: 

                        if (str.find('https://www.facebook.com') != -1 
                            and str.find('sharer') == -1 and fcount == 0):
                            facebook.write(str)
                            facebook.write('\n')
                            fcount = 1
                        if str.find('x.com') != -1 and xcount == 0:
                            x.write(str)
                            x.write('\n')
                            xcount = 1
                        if (str.find('www.instagram.com') != -1 and str.find('www.google.com') == -1
                            and icount == 0):
                            instagram.write(str)
                            instagram.write('\n')
                            icount = 1
                        if str.find('bsky.app') != -1 and bcount == 0:
                            bsky.write(str)
                            bsky.write('\n')
                            bcount = 1
                        if str.find('www.threads.com') != -1 and tcount == 0:
                            threads.write(str)
                            threads.write('\n')
                            tcount = 1
                        if (str.find('www.linkedin.com') != -1 and 
                            str.find('shareArticle?') == -1 and lcount == 0):
                            linkedin.write(str)
                            linkedin.write('\n')
                            lcount = 1
                        if str.find('mailto:') != -1:
                            emails_1.write(str.replace('mailto:', '') + ', ')
                            ecount = 1

                if fcount == 0:
                    facebook.write('NaN')
                    facebook.write('\n')
                if xcount == 0:
                    x.write('NaN')
                    x.write('\n')
                if icount == 0:
                    instagram.write('NaN')
                    instagram.write('\n')
                if bcount == 0:
                    bsky.write('NaN')
                    bsky.write('\n')
                if tcount == 0:
                    threads.write('NaN')
                    threads.write('\n')
                if lcount == 0:
                    linkedin.write('NaN')
                    linkedin.write('\n')
                if ecount == 0:
                    emails_1.write('NaN')
                    emails_1.write('\n')
                else:
                    emails_1.write('\n')

            except:

                facebook.write('NaN')
                facebook.write('\n')
                x.write('NaN')
                x.write('\n')
                instagram.write('NaN')
                instagram.write('\n')
                bsky.write('NaN')
                bsky.write('\n')
                threads.write('NaN')
                threads.write('\n')
                linkedin.write('NaN')
                linkedin.write('\n')
                emails_1.write('NaN')
                emails_1.write('\n')
                continue
                
            await session.close()

    facebook.close()
    x.close()
    instagram.close()
    bsky.close()
    threads.close()
    linkedin.close()
    emails_1.close()

asyncio.run(main())
