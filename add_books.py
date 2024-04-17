import requests

url = "http://localhost:5001/books"

books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "published_year": 1925},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "published_year": 1960},
    {"title": "1984", "author": "George Orwell", "published_year": 1949},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "published_year": 1813},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "published_year": 1951},
    {"title": "Animal Farm", "author": "George Orwell", "published_year": 1945},
    {"title": "Brave New World", "author": "Aldous Huxley", "published_year": 1932},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "published_year": 1954},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "published_year": 1937},
    {"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "published_year": 1997},
    {"title": "The Chronicles of Narnia", "author": "C.S. Lewis", "published_year": 1950},
    {"title": "Frankenstein", "author": "Mary Shelley", "published_year": 1818},
    {"title": "Moby-Dick", "author": "Herman Melville", "published_year": 1851},
    {"title": "Alice's Adventures in Wonderland", "author": "Lewis Carroll", "published_year": 1865},
    {"title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "published_year": 1890},
    {"title": "Jane Eyre", "author": "Charlotte Brontë", "published_year": 1847},
    {"title": "Wuthering Heights", "author": "Emily Brontë", "published_year": 1847},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "published_year": 1866},
    {"title": "The Odyssey", "author": "Homer", "published_year": "8th century BCE"},
    {"title": "The Great Expectations", "author": "Charles Dickens", "published_year": 1861}
]

for book_data in books:
    response = requests.post(url, json=book_data)
    print(response.status_code)  

print("Book data is successfully added!")
