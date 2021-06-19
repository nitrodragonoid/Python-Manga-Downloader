import requests
from bs4 import BeautifulSoup
import os
from PIL import Image

manga = str(input("Enter the Mangadex link to the manga you want to download: "))
start = int(input("From which chapter do you want to download enter a number: "))
end = int(input("To wich chaper d you want to download enter a number: "))
mangaName = str(input("Enter the name you want to save the pdf with: ")) 

img_list = []
img_names = []

folder = mangaName
try:
    os.mkdir(os.path.join(os.getcwd(),folder))
except:
    pass
os.chdir(os.path.join(os.getcwd(),folder))

#Fetching all the images of the manga panels
def downloader(url,img_list,img_names):
    req = requests.get(url)
    sop = BeautifulSoup(req.text, 'html.parser')
    title = str(sop.title.text).split("\n")
    name = title[0]
    chap = title[1]
    images = sop.find_all('img')
   
    pg = -1
    for i in images:
        link = str(i).split()[5].split('"')[1]
        pg += 1
        file = chap+" "+str(pg)+".jpg"
        print('Downloading',file)
        if pg != 0:
            with open(file.replace(":","-").replace(" ","-"),'wb') as f:
                im = requests.get(link)
                f.write(im.content)
            img = Image.open(file.replace(":","-").replace(" ","-"))
            im = img.convert('RGB')
            img_list.append(im)
            img_names.append(str(file.replace(":","-").replace(" ","-")))

for num in range(start, end+1):
    c = 'https://mangadex.tv/chapter/'+manga.split("/")[-1]+'/chapter_'+str(num)
    print(c)
    downloader(c,img_list,img_names)

#Compiling the images into a pdf
img_list[0].save(mangaName+'.pdf', "PDF" ,resolution=100.0, save_all=True, append_images=img_list)    

#Deleting the extra files
for j in img_names:
    os.remove(j)

print("Done")