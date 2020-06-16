import requests
from bs4 import BeautifulSoup
from tkinter import *
import webbrowser
from PIL import ImageTk, Image
from urllib.request import urlopen
from io import BytesIO

#---------------------------------GUI---------------------------------------------------------------------------------------------
root = Tk()
#-----------------Title bar----------------
root.title("Google Search Result")
root.iconbitmap('./icons/google-logo.ico')
#------------------------------------------

#----------------Logo and text display---------------------------------------
SearchLogo = ImageTk.PhotoImage(Image.open("./images/Flipkart_logo.png"))
LabelSearchLogo = Label(image=SearchLogo)
myLabel0 = Label(root, text="Search on flipkart here:")
myLabel0.config(font=("Courier", 40))
#----------------------------------------------------------------------------

#--------Input Field-------------
SearchBar = Entry(root, width=50)
#--------------------------------

#---------Position in the grid--------
LabelSearchLogo.grid(column=1, row=0, columnspan=32)
myLabel0.grid(column=1, row=1, columnspan=32)
SearchBar.grid(column=1, row=2, columnspan=32)
#-------------------------------------

#-------------------------------------------------------Button function-------------------------------------------------------------
def onClick():
    #---------------------------------------------------Scraped-search--------------------------------------------------------------
    searchItem = SearchBar.get()
    url = "https://www.flipkart.com/search?q="+searchItem
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    headers = {"user-agent" : USER_AGENT}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
    link = "https://www.flipkart.com"+soup.find('a', target='_blank').get('href')
    response = requests.get(link, headers=headers)
    if resp.status_code == 200:
        linkSoup = BeautifulSoup(response.content, "html.parser")
    Name = linkSoup.find('h1').get_text()
    Price = linkSoup.find('div', class_='_1vC4OE _3qQ9m1').get_text()
    Rating = linkSoup.find('div', class_='hGSR34').get_text()
    if linkSoup.find('div', class_='VGWI6T'):
        Offer = linkSoup.find('div', class_='VGWI6T').get_text()
    else:
        Offer = " - "
    #---------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------display-results------------------------------------------------------------------------------
    nameLabel = Label(root, text=Name, wraplength=400, justify='left')
    priceLabel = Label(root, text="Price : "+Price)
    ratingLabel = Label(root, text="Rating : "+Rating)
    offerLabel = Label(root, text="Offer : "+Offer)
    nameLabel.config(font=(12))
    offerLabel.config(font=(12))
    priceLabel.config(font=(12))
    ratingLabel.config(font=(12))
    nameLabel.grid(column=16, row=5)
    offerLabel.grid(column=16, row=6)
    priceLabel.grid(column=16, row=7)
    ratingLabel.grid(column=16, row=8)
    #----------------------------------------------------------------------------------------------------------------------------------
    def openLink():
        webbrowser.open(link)
    linkButton = Button(root, text="Visit page", command=openLink, bg='green', fg='white')
    linkButton.config(font=(14))
    linkButton.grid(column=16, row=10)
    MyButton.grid_forget()
    exitButton = Button(root, text="Exit", command=root.quit, padx=20, bg='#333', fg='white')
    exitButton.config(font=(14))
    exitButton.grid(column=16, row=11)
    #------------------------------------------------------image----------------------------------------------------------------------
    Img_url = linkSoup.find('div', class_='_2_AcLJ').get('style')[21:].strip(')')
    print(Img_url)
    u = urlopen(Img_url)
    raw_data = u.read()
    u.close()
    im = Image.open(BytesIO(raw_data))
    photo = ImageTk.PhotoImage(im)
    imglabel = Label(image=photo)
    imglabel.image = photo
    imglabel.grid(column=17, row=6, rowspan=3)
    #---------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------

#-----------------------Search button------------------------------
MyButton = Button(root, text="Search", command=onClick, bg='#333', fg='white')
MyButton.config(font=(15))
MyButton.grid(column=1, row=3, columnspan=32)
#------------------------------------------------------------------

root.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------------"""