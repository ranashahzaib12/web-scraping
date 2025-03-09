import requests 
from bs4 import BeautifulSoup

with open("demo.html" ,"r") as f:
    html_doc = f.read()

# Make Soup Object (FOr the purpose that the beautfiul soup could understand what the html content is for its own convinient)
# Running the "three sisters" document through Beautiful Soup gives us a BeautifulSoup object, which represents the document as a nested data structure:


soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify()) 
# Accessing different Tags using soup Object
# print(soup.title)
# print(soup.a)
# print(soup.find_all('a')) # All Anchor tags

# print(soup.find(id="link3")) # Printed link at id=3 inside the ANchor tag

# print(soup.get_text()) # Got all the text from html 

# One common task is extracting all the URLs found within a page's <a> tags:
# for link in soup.find_all('a'):
#     print(link.get('href'))
#     print(link.get_text()) # Got all the text that is inside the link

# print(soup.select("div.italic")) # div tags with italic
# print(soup.select("span#italic")) # span tags with italic

# # print(soup.span.get("class"))

# print(soup.find(id ="italic"))
# print(soup.find(class_="italic"))
# print(soup.find_all(class_="italic"))

# for child in soup.find(class_="container").children:
#     print(child) 

# for parent in soup.find(class_ = "box").parents:
#     print(parent)

# Modify existing TAGs
# cont = soup.find(class_="container")
# cont.name = "span"
# cont["class"] = "myclass Class2"
# cont.string= "I am a String"
# print(cont)

# Adding New Tags
# Step 1 prepare the tag 
# ulTag = soup.new_tag("ul")

# liTag = soup.new_tag("li")
# liTag.string = "Home"
# ulTag.append(liTag)

# liTag = soup.new_tag("li")
# liTag.string = "Abiut"
# ulTag.append(liTag)
# # Inserting happens in the same way as happen in the list methods of python 0th index ....
# soup.html.body.insert(0,ulTag)
# # saving the changes into a new modified,html files
# with open("modified.htm" , "w") as f:
#     f.write(str(soup))

# Finding the element with class 'container'
# cont = soup.find(class_="container")

# # Check if 'cont' is not None before trying to access its attributes
# print(cont.has_attr("contenteditable"))

# This OR That
# This OR That: Check if the tag has a 'class' but not an 'id' attribute
def has_class_but_not_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")

# Use find_all to get all tags matching the criteria
# results = soup.find_all(has_class_but_not_id)

def has_content(tag):
    return tag.has_attr("content")
results = soup.find_all(has_content) # Getting Meta Tagss

# Print the results
for result in results:
    print(result)