import csv

book_id_list = []
title_list = []
author_list = []
category_list = []
quantity_list = []
price_list = []
total_price_list = []


def read_data():  # read data from the csv file and append it to the lists
    count_books = 0
    csv_file = open('Inventory.csv')
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        book_id_list.append(row[0])
        title_list.append(row[1])
        author_list.append(row[2])
        category_list.append(row[3])
        quantity_list.append(row[4])
        price_list.append(row[5])
        total_price_list.append(row[6])
        count_books = count_books + 1
    if count_books > 0:
        print('The file has been read successfully')
        print('The number of books in the inventory is: ', count_books)
    csv_file.close()


def list_data():  # print the data that has been read from the csv file
    print(f'{"Book ID":<10}{"Title":<60}{"Author":<30}{"Category":<20}{"Quantity":<10}{"Price":<10}{"Total Price":<10}')
    for book in range(len(book_id_list)):
        print(f'{book_id_list[book]:<10}{title_list[book]:<60}{author_list[book]:<30}{category_list[book]:<20}'
              f'{quantity_list[book]:<10}{price_list[book]:<10}{total_price_list[book]:<10}')

# def list_data():
#     print('Book ID\t', 'Title\t\t\t\t\t\t', 'Author\t\t\t\t\t\t', 'Category\t\t\t', 'Quantity\t', 'Price\t', 'Total Price\t')
#     for book in range(len(book_id_list)):
        # print(book_id_list[book], '\t', title_list[book], '\t\t\t\t\t\t', author_list[book], '\t\t\t\t\t\t', category_list[book], '\t\t\t', quantity_list[book], '\t', price_list[book], '\t', total_price_list[book])

def search_by_title():  # search for a book by title
    search_title = input('please enter the title of the book: ')
    for title in range(len(title_list)):
        if search_title.lower() in title_list[title].lower():
            print(f'{"Book ID":<10}{"Title":<60}{"Author":<30}{"Category":<20}{"Quantity":<10}{"Price":<10}{"Total Price":<10}')
            print(f'{book_id_list[title]:<10}{title_list[title]:<60}{author_list[title]:<30}{category_list[title]:<20}'
                  f'{quantity_list[title]:<10}{price_list[title]:<10}{total_price_list[title]:<10}')


def search_by_author():  # search for a book by author
    search_author = input('please enter the author of the book: ')
    for author in range(len(author_list)):
        if search_author.lower() in author_list[author].lower():
            print(f'{"Book ID":<10}{"Title":<60}{"Author":<30}{"Category":<20}{"Quantity":<10}{"Price":<10}{"Total Price":<10}')
            print(f'{book_id_list[author]:<10}{title_list[author]:<60}{author_list[author]:<30}{category_list[author]:<20}'
                  f'{quantity_list[author]:<10}{price_list[author]:<10}{total_price_list[author]:<10}')


def add_new_book():  # add a new book to the inventory
    new_book_id = input('please enter the book ID: ')
    new_title = input('please enter the title of the book: ')
    new_author = input('please enter the author of the book: ')
    new_category = input('please enter the category of the book: ')
    new_quantity = input('please enter the quantity of the book: ')
    new_price = input('please enter the price of the book: ')
    new_total_price = int(new_quantity) * float(new_price)

    book_id_list.append(new_book_id)
    title_list.append(new_title)
    author_list.append(new_author)
    category_list.append(new_category)
    quantity_list.append(new_quantity)
    price_list.append(new_price)
    total_price_list.append(new_total_price)
    print('The book has been added successfully')


def delete_book():  # delete a book from the inventory
    delete_book_id = input('please enter the book ID: ')
    for book in range(len(book_id_list)):
        if delete_book_id == book_id_list[book]:
            book_id_list.remove(book_id_list[book])
            title_list.remove(title_list[book])
            author_list.remove(author_list[book])
            category_list.remove(category_list[book])
            quantity_list.remove(quantity_list[book])
            price_list.remove(price_list[book])
            total_price_list.remove(total_price_list[book])
    print('The book has been deleted successfully')


def add_to_stock():  # add quantity to a book
    add_book_id = input('please enter the book ID: ')
    add_quantity = input('please enter the quantity: ')
    for book in range(len(book_id_list)):
        if add_book_id == book_id_list[book]:
            quantity_list[book] = int(quantity_list[book]) + int(add_quantity)
            total_price_list[book] = int(
                quantity_list[book]) * float(price_list[book])
    print('The quantity has been added successfully')


def remove_from_stock():  # remove quantity from a book
    remove_book_id = input('please enter the book ID: ')
    remove_quantity = input('please enter the quantity: ')
    for book in range(len(book_id_list)):
        if remove_book_id == book_id_list[book]:
            if int(remove_quantity) <= int(quantity_list[book]):
                quantity_list[book] = int(
                    quantity_list[book]) - int(remove_quantity)
                total_price_list[book] = int(
                    quantity_list[book]) * float(price_list[book])
    print('The quantity has been removed successfully')


def total_cost():  # calculate the total cost of the inventory
    total = 0
    for value in range(len(total_price_list)):
        total = total + float(total_price_list[value])
    print('The total value of the inventory is: ', total)


def save_data():  # save the data to a csv file
    csv_file = open('Inventory.csv', 'w', newline='')
    csv_writer = csv.writer(csv_file)
    grouping_list = list(zip(book_id_list, title_list, author_list, category_list, quantity_list, price_list, total_price_list))
    for row in range(len(grouping_list)):
        csv_writer.writerow(grouping_list[row])
    csv_file.close()
    print('The data has been saved successfully')


def menu():
    while True:
        print('************************************************************************')
        print(' 1. Read Data')
        print(' 2. List Data')
        print(' 3. Search by Title')
        print(' 4. Search by Author')
        print(' 5. Add New Book')
        print(' 6. Delete Book')
        print(' 7. Add to Stock')
        print(' 8. Remove from Stock')
        print(' 9. Total Cost')
        print('10. Save Data')
        print('11. Exit')
        print('************************************************************************')
        choice = input('please enter your choice: ')
        if choice == '1':
            read_data()
        elif choice == '2':
            list_data()
        elif choice == '3':
            search_by_title()
        elif choice == '4':
            search_by_author()
        elif choice == '5':
            add_new_book()
        elif choice == '6':
            delete_book()
        elif choice == '7':
            add_to_stock()
        elif choice == '8':
            remove_from_stock()
        elif choice == '9':
            total_cost()
        elif choice == '10':
            save_data()
        elif choice == '11':
            print('Thank you for using the system')
            break
        else:
            print('invalid choice')


def welcome_screen():
    print('************************************************************************')
    print('welocme to FEPS bookshop inventory system\n')
    menu()


def main():
    welcome_screen()


main()
