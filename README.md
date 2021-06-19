# Python-Manga-Downloader
A python script that takes a Mangadex manga link and the chapters you want to download, and downloads and saves them as pdf. 

**How to run**

You need to have the following installed on your computer:

1) Python 3
2) Beautiful Soup python library 
3) Requests python library
4) Pillow python library
5) os python module


**How to use**

- The fist line of input asks for a link to the a Mangadex webpage of a manga e.g. https://mangadex.tv/manga/af918141
- The second line of input asks from which chapter do you want to download from e.g. 1
- The third line of input asks till which chapter do you want to download e.g. 10
- The fourth line line asks you what you would like to name the pdf file e.g. SBR-1-to-10

**How it works**

The programs loops in the given chapters range, download all the images from each of the given chapers. Then the images are combined into a pdf of the given name, then alll the excess downloaded images are deleted, and all that remains is the pdf which can be found in the folder of the same name.
