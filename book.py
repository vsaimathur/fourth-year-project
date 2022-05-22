class Book:
	def __int__(self, name, author, pages):
		self.name = name
		self.author = author
		self.pages = pages

	def getAuthorName(self):
		return self.author
	
	def getBookName(self):
		return self.name
		
	def getPages(self):
		return self.pages

	def setAuthorName(self, authorName):
		self.author = authorName
		
	def setBookName(self, bookName):
		self.name = bookName
		
	def setPages(self, pages):
		self.pages = pages

	def __str__(self):
		printBookString = "The book " + self.name + " Written by " + self.author + " has " + str(self.pages) + " pages."
		return printBookString

arrBooks = []

def addBook(name, author, pages):
	newBook = Book()
	newBook.setPages(pages)
	newBook.setBookName(name)
	newBook.setAuthorName(author)
	arrBooks.append(newBook)

def removeBook(name):
    for i in range(len(arrBooks)):
        if(arrBooks[i] == name):
            break
    arrBooks.pop(i)
    
def getBook(name):
	for i in range(len(arrBooks)):
		if(arrBooks[i].name == name):
			break
	return arrBooks[i]

addBook("The Adventures of Sherlock Homes", "Conan Doyle", 100)
addBook("One piece", "Eiichiro Oda", 500)
addBook("Naruto", "Mashashi kishimoto", 200)
addBook("Detective Conan", "Gosho Aoyama", 250)
addBook("No Game No Life", "Yuu Kamiya", 50)
addBook("Bakuman", "Takeshi Obata", 75)
addBook("Haikyu!!", "Haruichi Furudate", 125)

print(getBook("Bakuman"))
print(getBook("Naruto"))
print(getBook("The Adventures of Sherlock Homes"))

removeBook("The Adventures of Sherlock Homes")