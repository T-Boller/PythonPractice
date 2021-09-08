#Get the details of a blog post from a user, initially stored as individual items. 

#1. Store this in a dictionary called blogPost1. Choose suitable key names for the data, and take the user inputs as the values. ------------------
#2. Write a function for displaying the blog names, alongside their key names in a user friendly format. -----------------
#3. Write a function that takes the items from the user in the format for a 2D list, and then converts this into a dictionary object. -------------
#4. Write a function that allows you to update the post, store it back in the dictionary. ----------------------

# from datetime import date

# postAuthor = input("Please enter the author's name: ")
# keyAuthor = "author"
# postDate = input("What is today's date: ")
# postDate = date.today()
# keyDate = "date"
# postContents = input("Enter your post: ")
# keyContents = "contents"
# postWhole = [postAuthor, postDate, postContents]
  
# blogPost1[f"{keyAuthor}"] = postAuthor
# blogPost1[f"{keyDate}"] = postDate
# blogPost1[f"{keyContents}"] = postContents


def blogInput(): #function, this creates the list from user input
  from datetime import date #import libaray for current date
  blogList =([]) #list, empty
  postAuthor = input("Please enter the author's name: ") #ask for input
  keyAuthor = "author" #key, assigned to 'author'
  postDate = date.today() #current date
  keyDate = "date" #key, assigned to 'date'
  postContents = input("Enter your post: ") #ask for input
  keyContents = "contents" #key, assigned to 'contents'
  blogList.append([keyAuthor, postAuthor])  #adds authour input to list
  blogList.append([keyDate, str(postDate)]) #adds date in string format to list
  blogList.append([keyContents, postContents]) #adds contents input to list
  return blogList #exit function and pass blogList forward

def blogConvert(blogList): #function, converts the list to a dictionary
  blogPost1 = {} #dictionary, empty
  for row in blogList: #for how many rows there are, adds list data into the relevant dictionary index
    key = row[0]
    value = row[1]
    blogPost1[f'{key}'] = value 
 
  return blogPost1 #exit function and pass blogPost1 forward

def blogChange(blogPost2): #function, updates blog depending on input
  from datetime import date
  askUpdate = input("Do you want to update a blogpost? y/n: ").lower() #ask for input, converts to lowercase
  if askUpdate == "y": #if statement that updates dictionary if input is 'y'
    displayPost(blogPost2)
    updateConfirm = input("Is this the post you want to update? y/n: ").lower() #ask for input, converts to lowercase
    if updateConfirm == "y": #if statement that confirms the update
      newName = input("Please enter a new author name: ") # ask for new name input
      newDate = date.today() #update current date
      newContents = input("Please enter the new blog contents: ") #ask for new contents input
      blogPost2["author"] = newName #assigns new values to the 3 keys
      blogPost2["date"] = str(newDate)
      blogPost2["contents"] = newContents
      return blogPost2 #exit function and pass blogPost2 forward
    else:
      print("There are no other blog posts") #prints, if update confirmation input is 'n'
  else:
    print("ok") #prints if updating blog input is 'n'

def displayPost(blogPost2): #function, displays dictionary in user friendly format
  for key, value in blogPost2.items(): #for each key in the list, prints the key, value as a string
    print (key + ": " + str(value))

def main():
  blogList = blogInput() #List
  blogPost2 = blogConvert(blogList) #dicttomionary
  newBlog = blogChange(blogPost2) #dictionary update
  displayPost(blogPost2) #displays the dictionary with increased readability
   
main()
