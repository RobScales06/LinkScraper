#Created by Rob Scales
#11/29/2020
#LinkScraper
#input a link and a filename to get a csv of all of the http or https links embedded in the website

#necessary libraries: requests, csv, os:
import requests
import csv
import os

print("Input website URL:")
webLink = input()
print("Name of output CSV (blank if none):")
outfile = input() + ".csv"

outfileTxt = ""

url = requests.get(webLink)
htmltext = url.text

with open(outfile, 'w') as csvfile: #open csv for writing
    for i in range(len(htmltext)):
        if(htmltext[i]=='h' and htmltext[i+1]=='t' and htmltext[i+2]=='t' and htmltext[i+3]=='p'):
            j=0
            while(htmltext[j+i] != "\""):
                print(htmltext[j+i], end="")
                outfileTxt += htmltext[j+i]
                j+=1
            outfileTxt +="\n"
            print("\n")
    csvfile.write(outfileTxt) #write links to csv
#finish program

if(outfile == ".csv"): #eliminate file if no name
    os.remove(".csv")
    print("***" + webLink + " processed!***")
else:
    print("***" + webLink + " processed to " + outfile + "!***")