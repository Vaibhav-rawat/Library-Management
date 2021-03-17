'''This program shows the concept of Object Oriented Programming is python
Author - Vaibhav Rawat
Purpose - Python Problem Solving'''
class Library:
    def __init__(self,list_of_manga,name_of_library):
        self.list_of_manga=list_of_manga
        self.name_of_library=name_of_library
        self.lend_manga={}
    def display(self):
        for i,j in enumerate(self.list_of_manga):
            print(f'{i+1}:{j}')
    def add_book(self):
        new=input('What is the manga name ?\n')
        if new not in self.list_of_manga:
            self.list_of_manga.append(new)
            print('book added')
        else:
            print('book already present')
    def lend_book(self,manga,name):
        if manga in self.list_of_manga:
            if self.lend_manga=={} or manga not in self.lend_manga.values():
                self.lend_manga.update({name: manga})
                print(self.lend_manga)
                print('book lent,enjoy reading\n')
            else:
                print('book is lent by someone')
        else:
            print('This manga is not available in the library\n')
    
    def delete_book(self,remove_book):
        if remove_book in self.list_of_manga:
            self.list_of_manga.remove(remove_book)
            print('book deleted\n')
        else:
            print('manga not present in the libraray\n')
    
    def return_book(self,manga,name):
        if manga in self.list_of_manga and self.lend_manga=={}:
            print('no book was lent so you cannot return\n')
        elif manga in self.list_of_manga:
            for i,j in self.lend_manga.copy().items():
                if name in i and manga in j:
                    self.lend_manga.pop(name)
                    print('manga returned')
                else:
                    print('Either the original lender is not present or this manga was not issued to this lender\n')
        else:
            print('book not present in library')

            
    
def main():
    # books={}
    list_of_manga=['dr stone','jujutsu kaisen','one punch man','slime']
    name_of_library='vaibhav_library'
    Librarian_name='vaibhav'
    p=Library(list_of_manga,name_of_library)
    print('1 to display\n2 to add book\n3 to lend book\n4 to remove book\n5 to return book\nq to exit')
    flag=False
    while(flag is not True):
        a=input('Input choice \n')
        if a=='1':
            p.display()

        elif a=='q':
            print('exited')
            flag=True

        elif a=='2':
            p.add_book()

        elif a=='3':
            manga=input('which book you want to lend?')
            name=input('what is your name?')
            p.lend_book(manga,name)

        elif a=='4':
            correct_name=input('Enter correct librarian name\n')
            if correct_name==Librarian_name:
                remove_book=input('Enter the manga you want to delete')
                p.delete_book(remove_book)           
            else:
                print('you are not the librarian\n')
        
        elif a=='5':
            manga=input('which manga you want to return?\n')
            name=input('what is your name?\n')
            p.return_book(manga,name)
        else:
            print('enter the correct input')

if __name__ == "__main__":
    main()
