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
root.title("Price Compare")
root.iconbitmap('./icons/eCom.ico')
#------------------------------------------

#----------------Logo and text display---------------------------------------
SearchLogo = ImageTk.PhotoImage(Image.open("./images/e-commerce.jpg"))
LabelSearchLogo = Label(image=SearchLogo)
myLabel0 = Label(root, text="Search on different e-commerce sites here:")
#----------------------------------------------------------------------------"""

#--------Input Field-------------
SearchBar = Entry(root, width=50, borderwidth=1, font=('Helvetica',15))
#--------------------------------

#---------Position in the grid--------
LabelSearchLogo.grid(column=1, row=0, columnspan=4)
myLabel0.grid(column=1, row=1, columnspan=4)
myLabel0.config(font=("Courier", 20))
SearchBar.grid(column=1, row=2, columnspan=4)
#-------------------------------------

#-------------------------------------------------------Button function-------------------------------------------------------------
def onClick():
    searchItem = SearchBar.get()
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    headers = {"user-agent" : USER_AGENT}
    #---------------------------------------------------Snapdeal-search--------------------------------------------------------------
    url1 = "https://www.snapdeal.com/search?keyword="+searchItem
    resp1 = requests.get(url1, headers=headers)
    if resp1.status_code == 200:
        soup1 = BeautifulSoup(resp1.content, "html.parser")
    anchor1 = soup1.find('a', class_='dp-widget-link noUdLine')
    if anchor1:
        link1 = anchor1.get('href')
    snapdealName = soup1.find('p', class_='product-title')
    snapdealFeatures = soup1.find('div', class_='product-discount')
    snapdealpercent = soup1.find('div', class_='filled-stars').get('style')[6:-3]
    snapdealRating = float(snapdealpercent)/20
    snapdealPrice = soup1.find('div', class_='product-price-row clearfix').find('span')
    #---------------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------Amazon-search--------------------------------------------------------------
    url2 = "https://www.amazon.in/s?k="+searchItem
    resp2 = requests.get(url2, headers=headers)
    if resp2.status_code == 200:
        soup2 = BeautifulSoup(resp2.content, "html.parser")
    anchor2 = soup2.find('a', class_='a-link-normal a-text-normal')
    if anchor2:
        link2 = "https://www.amazon.in"+anchor2.get('href')
    amazonName = anchor2.find('span').get_text()
    amazonFeatures = soup2.find('div', class_='a-row a-size-base a-color-secondary')
    amazonRating = soup2.find('span', class_='a-icon-alt')
    amazonPrice = soup2.find('span', class_='a-offscreen')
    #---------------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------Shopclues-search--------------------------------------------------------------
    url3 = "https://www.shopclues.com/search?q="+searchItem
    resp3 = requests.get(url3, headers=headers)
    if resp3.status_code == 200:
        soup3 = BeautifulSoup(resp3.content, "html.parser")
    anchor3 = soup3.find('div', class_='row').find('a')
    if anchor3:
        link3 = "https://www.shopclues.com"+anchor3.get('href')
    shopcluesName = soup3.find('div', class_='row').find('h2')
    shopcluesFeatures = soup3.find('span', class_='prd_discount')
    rawRating = soup3.find('span', class_='star')
    if rawRating:
        shopcluesRating = (float(rawRating.find('span').get('style')[6:-2]))/14
    else:
        shopcluesRating = "unavailable"
    shopcluesPrice = soup3.find('span', class_='p_price')
    #---------------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------Flipkart-search--------------------------------------------------------------
    searchItem = SearchBar.get()
    url4 = "https://www.flipkart.com/search?q="+searchItem
    resp4 = requests.get(url4, headers=headers)
    if resp4.status_code == 200:
        soup4 = BeautifulSoup(resp4.content, "html.parser")
    link4 = "https://www.flipkart.com"+soup4.find('a', target='_blank').get('href')
    response = requests.get(link4, headers=headers)
    if response.status_code == 200:
        linkSoup = BeautifulSoup(response.content, "html.parser")
    Name = linkSoup.find('h1').get_text()
    Price = linkSoup.find('div', class_='_1vC4OE _3qQ9m1').get_text()
    Rating = linkSoup.find('div', class_='hGSR34').get_text()
    if linkSoup.find('div', class_='VGWI6T'):
        Offer = linkSoup.find('div', class_='VGWI6T').get_text()
    else:
        Offer = " - "
    #---------------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------Snapdeal-display------------------------------------------------------------------------
    SnapName = Label(root, text=snapdealName.get_text(), wraplength=400, justify='left',)
    SnapOffer = Label(root, text=snapdealFeatures.get_text().replace('\n', ''))
    SnapRating = Label(root, text="Rating : "+str(snapdealRating))
    SnapPrice = Label(root, text="Price : "+snapdealPrice.get_text())
    SnapName.config(font=('helvetica',10,'bold'))
    SnapName.grid(column=1, row=4, columnspan=2)
    SnapOffer.grid(column=1, row=5)
    SnapRating.grid(column=1, row=6)
    SnapPrice.grid(column=1, row=7)
    def openLink1():
        webbrowser.open(link1)
    linkButton1 = Button(root, text="View product", command=openLink1, bg='green', fg='white')
    linkButton1.grid(column=1, row=9)
    #---------------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------Amazon-display-----------------------------------------------------------------------
    amaName = Label(root, text=amazonName, wraplength=400, justify='left')
    amaOffer = Label(root, text=amazonFeatures.get_text().replace('\n', ''), wraplength=100, justify='left')
    amaRating = Label(root, text="Rating : "+amazonRating.get_text(), wraplength=100, justify='left')
    amaPrice = Label(root, text="Price : "+amazonPrice.get_text())
    amaName.config(font=('helvetica',10,'bold'))
    amaName.grid(column=3, row=4, columnspan=2)
    amaOffer.grid(column=3, row=5)
    amaRating.grid(column=3, row=6)
    amaPrice.grid(column=3, row=7)
    def openLink2():
        webbrowser.open(link2)
    linkButton2 = Button(root, text="View product", command=openLink2, bg='green', fg='white')
    linkButton2.grid(column=3, row=9)
    #---------------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------Shopclues-display-----------------------------------------------------------------------
    shopName = Label(root, text=shopcluesName.get_text(), wraplength=400, justify='left')
    shopOffer = Label(root, text=shopcluesFeatures.get_text().replace('\n', ''))
    shopRating = Label(root, text="Rating : "+str(shopcluesRating))
    shopPrice = Label(root, text="Price : "+shopcluesPrice.get_text().replace(' ', ''))
    shopName.config(font=('helvetica',10,'bold'))
    shopName.grid(column=1, row=10, columnspan=2)
    shopOffer.grid(column=1, row=11)
    shopRating.grid(column=1, row=12)
    shopPrice.grid(column=1, row=13)
    def openLink3():
        webbrowser.open(link3)
    linkButton3 = Button(root, text="View product", command=openLink3, bg='green', fg='white')
    linkButton3.grid(column=1, row=14)
    #---------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------Flipkart-display------------------------------------------------------------------------------
    nameLabel = Label(root, text=Name, wraplength=400, justify='left')
    priceLabel = Label(root, text="Price : "+Price)
    ratingLabel = Label(root, text="Rating : "+Rating)
    offerLabel = Label(root, text=Offer)
    nameLabel.config(font=('helvetica',10,'bold'))
    nameLabel.grid(column=3, row=10, columnspan=2)
    offerLabel.grid(column=3, row=11)
    priceLabel.grid(column=3, row=12)
    ratingLabel.grid(column=3, row=13)
    def openLink4():
        webbrowser.open(link4)
    linkButton4 = Button(root, text="View product", command=openLink4, bg='green', fg='white')
    linkButton4.grid(column=3, row=14)
    #----------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------Snapdeal-image------------------------------------------------------------------------------
    Img_url = soup1.find('img', class_='product-image')
    if Img_url:
        print(Img_url.get('src'))
        u = urlopen(Img_url.get('src'))
        raw_data = u.read()
        u.close()
        im = Image.open(BytesIO(raw_data))
        zoom = 0.5
        pixels_x, pixels_y = tuple([int(zoom * x)  for x in im.size])
        im = im.resize((pixels_x, pixels_y), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(im)
        imglabelSnap = Label(image=photo)
        imglabelSnap.image = photo
        imglabelSnap.grid(column=2, row=5, rowspan=3)
    else:
        imglabelSnap = Label(root, text="No Image Available")
        imglabelSnap.grid(column=2, row=5, rowspan=3)
    #----------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------Amazon-image------------------------------------------------------------------------------
    Img_url = soup2.find('img', class_='s-image')
    if Img_url:
        print(Img_url.get('src'))
        u = urlopen(Img_url.get('src'))
        raw_data = u.read()
        u.close()
        im = Image.open(BytesIO(raw_data))
        zoom = 0.5
        pixels_x, pixels_y = tuple([int(zoom * x)  for x in im.size])
        im = im.resize((pixels_x, pixels_y), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(im)
        imglabelAmazon = Label(image=photo)
        imglabelAmazon.image = photo
        imglabelAmazon.grid(column=4, row=5, rowspan=3)
    else:
        imglabelAmazon = Label(root, text="No Image Available")
        imglabelAmazon.grid(column=4, row=5, rowspan=3)
    #----------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------Shopclues-image------------------------------------------------------------------------------
    Img_url = soup3.find('div', class_='img_section').find('img')
    if Img_url:
        print(Img_url.get('src'))
        u = urlopen(Img_url.get('src'))
        raw_data = u.read()
        u.close()
        im = Image.open(BytesIO(raw_data))
        zoom = 0.5
        pixels_x, pixels_y = tuple([int(zoom * x)  for x in im.size])
        im = im.resize((pixels_x, pixels_y), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(im)
        imglabelShop = Label(image=photo)
        imglabelShop.image = photo
        imglabelShop.grid(column=2, row=11, rowspan=3)
    else:
        imglabelShop = Label(root, text="No Image Available")
        imglabelShop.grid(column=2, row=11, rowspan=3)
    #----------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------Flipkart-image------------------------------------------------------------------------------
    Img_url = linkSoup.find('div', class_='_2_AcLJ')
    if Img_url:
        print(Img_url.get('style')[21:].strip(')'))
        u = urlopen(Img_url.get('style')[21:].strip(')'))
        raw_data = u.read()
        u.close()
        im = Image.open(BytesIO(raw_data))
        photo = ImageTk.PhotoImage(im)
        imglabel = Label(image=photo)
        imglabel.image = photo
        imglabel.grid(column=4, row=11, rowspan=3)
    else:
        imglabel = Label(root, text="No Image Available")
        imglabel.grid(column=4, row=11, rowspan=3)
    #----------------------------------------------------------------------------------------------------------------------------------
    exitButton = Button(root, text="Exit", command=root.quit, padx=20, bg='#333', fg='white')
    exitButton.grid(column=1, row=15, columnspan=4, pady=10)
    def Labeldel():
        SnapName.grid_forget()
        SnapOffer.grid_forget()
        SnapRating.grid_forget()
        SnapPrice.grid_forget()
        imglabelSnap.grid_forget()
        amaName.grid_forget()
        amaOffer.grid_forget()
        amaRating.grid_forget()
        amaPrice.grid_forget()
        imglabelAmazon.grid_forget()
        shopName.grid_forget()
        shopOffer.grid_forget()
        shopRating.grid_forget()
        shopPrice.grid_forget()
        imglabelShop.grid_forget()
        nameLabel.grid_forget()
        offerLabel.grid_forget()
        priceLabel.grid_forget()
        ratingLabel.grid_forget()
        imglabel.grid_forget()
        onClick()
    #MyButton.grid_forget()
    MyButton = Button(root, text="Compare",  command=Labeldel, bg='#333', fg='white')
    MyButton.config(font=(15))
    MyButton.grid(column=1, row=3, columnspan=4, pady=10)
    #---------------------------------------------------------------------------------------------------------------------------------

#-----------------------Search button------------------------------
MyButton = Button(root, text="Compare",  command=onClick, bg='#333', fg='white')
MyButton.config(font=(15))
MyButton.grid(column=1, row=3, columnspan=4, pady=10)
#------------------------------------------------------------------

root.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------------