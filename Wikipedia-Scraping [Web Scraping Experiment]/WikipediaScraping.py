# Script By : Vishwesh Deore [ https://github.com/VishweshDeore ]

# Experiments : Wikipedia-Scraping [Web Scraping Experiment]
# [ https://github.com/VishweshDeore/Experiments ]

# Objective : 
# Take User Input(Topic Name) > 
# Fetch data for the topic from wikipedia using web scraping techniques > 
# Save the data in local storage with the topic name as file name

#  #########################################  # 

# Script :
#%%

# Step 1. Importing Packages and Libraries Required

import requests
from bs4 import BeautifulSoup
import urllib.request
from inscriptis import get_text

# Install inscritptis from anaconda prompt : pip install inscriptis
# Inscriptis used from github project of (github id : weblyzard , https://github.com/weblyzard/inscriptis)

#%%

# Step 2. Take User Input and Store it in a Variable

topic=input("Please Enter The Topic Name : ")

#%%

# Step 3. Compiling Page URL and storing it in a variable

url = ("https://en.wikipedia.org/wiki/"+topic)
 
#%%

# Step 4. Fetching the Web Page and Extracting Text Data by Using Inscriptis

#%%

# Step 4.1 Fetching the Web Raw Data 

html = urllib.request.urlopen(url).read().decode('utf-8')

#%%

# Step 4.2. Extracting the Text Information From the Raw Data

text = get_text(html)

#%%

# Step 4.3. Printing the Information to the Console
 
print(text)

#%%

# Step 4.4. Saving the Content to a Text File With the Same Name as the Topic 

a=open(r"G:\SearchResults\\"+topic+".txt",'w')
a.writelines(text)
a.close()

# ############ #
#%%

# Step 5. Fetching the Web Page and Extracting Text Data by Using BeautifulSoup

#%%

# Step 5.1. Creating the Object to Hold to Page Source Content

page=requests.get(url)

#%%

# Step 5.2. Creating an Object to Store the Page Source in Proper HTML Format

soup= BeautifulSoup(page.content,'html.parser') 

#%%

# Step 5.3 Storing Page Source Belonging to a Particular ID Tag on the Page

bodyContent=soup.find(id="bodyContent")

#%%

# Step 5.4 Extracting Textual Information From the Content

text = bodyContent.get_text()

#%%

# Step 5.4. Printing the Information to the Console

print(text)

#%%

# Step 5.5. Saving the Content to a Text File With the Same Name as the Topic 

a=open(r"G:\SearchResults\\"+topic+".txt",'w')
a.writelines(text)
a.close()

#%%
#  #########################################  # 







