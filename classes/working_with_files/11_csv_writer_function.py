import csv

books = [
    ["title", "author", "pages", "publisher", "year_of_publishing"],
    ["One Minute Manager", "Ken Blanchard", 85, "Unknown", 1980],
    ["Python Programming", "Mark Lutz", 1300, "Wiley", 2008],
    ["Who moved my cheese", "Spencer Johnson", 90, "Penguin", 1970],
    ["Word Power Made Easy", "Norman Lewis", 600, "Goyal Publishing", 1970],
]

with open("books.csv", "w", newline="") as file:
    w_obj = csv.writer(file)
    w_obj.writerows(books)