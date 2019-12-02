class Ebook:
    def __init__(self, title, author, page_count, isopen = False, current_page=None):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isopen = False
        self.current_page = None
        
    def book_open(self):
        self.isopen = True
    def book_close(self):
        self.isopen = False 
    def set_current_page(self,current_page):
        self.current_page = current_page
    def next_page(self):
        if self.isopen == True and self.current_page < 400:
            self.current_page += 1
    def prev_page(self):
        if self.isopen == True and self.current_page > 0:
            self.current_page -= 1
    def __str__(self):
        return f'Current page: {self.current_page} Is open: {self.isopen}'

book1 = Ebook("Title", "John Doe", 400)
print(book1)
book1.book_open()
book1.set_current_page(300)
book1.next_page()
book1.next_page()
print(book1)
