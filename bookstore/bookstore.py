#bookstore = {
#   'name' : name,
#   'authors' : [{'name': 'Edgar Allan Poe', 
#                 'nationality': 'US',
#                 'id' : 193048091},
#                {'name': 'J.K. Rowling', 
#                 'nationality': 'Norwegian',
#                 'id' : 12342314}
#               ],
#}
#
#authorsList = bookstore['authors']
#firstAuthorDictionary = authorsList[0]
#firstAuthorName = firstAuthorDictionary['name']



#store = create_bookstore("rmotr's bookstore")
#{'name' : name, 'authors' : []}
#poe = add_author(store, 'Edgar Allan Poe', 'US')

def create_bookstore(name):
    bookstore = {'name' : name, 'authors' : [], 'books' : [], 'last_author_id' : 0, 'last_book_id' : 0}
    return bookstore

def add_author(bookstore, name, nationality):
    bookstore['last_author_id'] += 1
    new_author = {'name' : name, 'nationality' : nationality, 'id' : bookstore['last_author_id']}
    bookstore['authors'].append(new_author)
    return new_author

def get_author_by_name(bookstore, name):
    authorsList = bookstore['authors']
    #For each author(dictionary) in the authors list(list of dictionaries) in the bookstore dictionary
    for author in authorsList:  
        #If the dicitonary name matches the input name, return that author dictionary 
        if author['name'] == name:
            return author


def get_author_by_id(bookstore, author_id):
    authorsList = bookstore['authors']
    #For each author(dictionary) in the authors list(list of dictionaries) in the bookstore dictionary
    for author in authorsList:  
        #If the dicitonary id matches the input id, return that author dictionary 
        if author['id'] == author_id:
            return author

def add_book(bookstore, title, isbn, author_id):
    bookstore['last_book_id'] += 1
    new_book = {'title' : title, 'isbn' : isbn, 'author_id' : author_id, 'id' : bookstore['last_book_id']}
    bookstore['books'].append(new_book)
    return new_book


def get_book_by_title(bookstore, title):
    booklist = bookstore['books']
    for book in booklist:
        if book['title'] == title:
            return book

def get_book_by_id(bookstore, book_id):
    booklist = bookstore['books']
    for book in booklist:
        if book['id'] == book_id:
            return book


def get_books_by_author(bookstore, author_id):
    #Here - List Variable
    authorBookList = []
    booklist = bookstore['books']
    for book in booklist:
        if book['author_id'] == author_id:
            authorBookList.append(book)
    return authorBookList
    #Here - Return that List
