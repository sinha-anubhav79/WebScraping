import requests
from bs4 import BeautifulSoup
from tkinter import *
import webbrowser
from PIL import ImageTk, Image

#---------------------------------GUI---------------------------------------------------------------------------------------------
root = Tk()
#-----------------Title bar----------------
root.title("Price Compare")
root.iconbitmap('./icons/google-logo.ico')
#------------------------------------------

#----------------Logo and text display---------------------------------------
SearchLogo = ImageTk.PhotoImage(Image.open("./images/e-commerce.jpg"))
LabelSearchLogo = Label(image=SearchLogo)
myLabel0 = Label(root, text="Search on different e-commerce sites here:")
#----------------------------------------------------------------------------"""

#--------Input Field-------------
SearchBar = Entry(root, width=50)
#--------------------------------

#---------Position in the grid--------
LabelSearchLogo.grid(column=1, row=0, columnspan=2)
myLabel0.grid(column=1, row=1, columnspan=2)
myLabel0.config(font=("Courier", 20))
SearchBar.grid(column=1, row=2, columnspan=2)
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
    snapdealRating = int(snapdealpercent)/20
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
        shopcluesRating = int(rawRating.find('span').get('style')[6:-2])/14
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
    myLabel01 = Label(root, text=snapdealName.get_text(), wraplength=400, justify='left')
    myLabel02 = Label(root, text=snapdealFeatures.get_text().replace('\n', ''))
    myLabel03 = Label(root, text="Rating : "+str(snapdealRating))
    myLabel04 = Label(root, text="Price : "+snapdealPrice.get_text())
    myLabel01.grid(column=1, row=4)
    myLabel02.grid(column=1, row=5)
    myLabel03.grid(column=1, row=6)
    myLabel04.grid(column=1, row=7)
    def openLink1():
        webbrowser.open(link1)
    linkButton1 = Button(root, text="View product", command=openLink1, bg='green', fg='white')
    linkButton1.grid(column=1, row=9)
    #---------------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------Amazon-display-----------------------------------------------------------------------
    myLabel11 = Label(root, text=amazonName, wraplength=400, justify='left')
    myLabel12 = Label(root, text=amazonFeatures.get_text().replace('\n', ''), wraplength=400, justify='left')
    myLabel13 = Label(root, text="Rating : "+amazonRating.get_text())
    myLabel14 = Label(root, text="Price : "+amazonPrice.get_text())
    myLabel11.grid(column=2, row=4)
    myLabel12.grid(column=2, row=5)
    myLabel13.grid(column=2, row=6)
    myLabel14.grid(column=2, row=7)
    def openLink2():
        webbrowser.open(link2)
    linkButton2 = Button(root, text="View product", command=openLink2, bg='green', fg='white')
    linkButton2.grid(column=2, row=9)
    #---------------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------Shopclues-display-----------------------------------------------------------------------
    myLabel06 = Label(root, text=shopcluesName.get_text(), wraplength=400, justify='left')
    myLabel07 = Label(root, text=shopcluesFeatures.get_text().replace('\n', ''))
    myLabel08 = Label(root, text="Rating : "+str(shopcluesRating))
    myLabel09 = Label(root, text="Price : "+shopcluesPrice.get_text().replace(' ', ''))
    myLabel06.grid(column=1, row=10)
    myLabel07.grid(column=1, row=11)
    myLabel08.grid(column=1, row=12)
    myLabel09.grid(column=1, row=13)
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
    nameLabel.grid(column=2, row=10)
    offerLabel.grid(column=2, row=11)
    priceLabel.grid(column=2, row=12)
    ratingLabel.grid(column=2, row=13)
    def openLink4():
        webbrowser.open(link4)
    linkButton4 = Button(root, text="View product", command=openLink4, bg='green', fg='white')
    linkButton4.grid(column=2, row=14)
    #----------------------------------------------------------------------------------------------------------------------------------
    MyButton.grid_forget()
    exitButton = Button(root, text="Exit", command=root.quit, padx=20, bg='#333', fg='white')
    exitButton.grid(column=1, row=15, columnspan=2)
    #---------------------------------------------------------------------------------------------------------------------------------

#-----------------------Search button------------------------------
MyButton = Button(root, text="Compare",  command=onClick, bg='#333', fg='white')
MyButton.config(font=(15))
MyButton.grid(column=1, row=3, columnspan=2)
#------------------------------------------------------------------

root.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------------