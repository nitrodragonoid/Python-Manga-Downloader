import requests
from bs4 import BeautifulSoup
import os
from PIL import Image

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


# Enter url of manga you want to download like this:
manga = 'https://mangadex.tv/manga/manga-nc952011'

# Enter Starting and ending chapter like this:
start = 1
end = 271
mangaName = 'kaguya sama'

current = os.getcwd()

for num in range(start,end+1):
    img_list = []
    img_names = []

    folder = mangaName+"-"+"Chap"+"-"+str(num)
    try:
        os.mkdir(os.path.join(os.getcwd(),folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(),folder))

    c = 'https://mangadex.tv/chapter/'+manga.split("/")[-1]+'/chapter-'+str(num)
    print(c)
    downloader(c,img_list,img_names)

    #Compiling the images into a pdf
    # img_list[0].save(num+'.pdf', "PDF" ,resolution=100.0, save_all=True, append_images=img_list)    

    img_list[0].save(str(num)+'.pdf', "PDF" ,resolution=100.0, save_all=True, append_images=img_list)    

    #Deleting the extra files
    for j in img_names:
        os.remove(j)
    os.chdir(current)

print("Done")
