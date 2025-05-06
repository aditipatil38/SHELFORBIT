# import os
# import sys
# import django
# import random
#
# # Setup Django environment
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booksproject.settings")  # 🔁 Replace with your actual project name
# django.setup()
#
# from firstbook.models import Library
#
# def run():
#     city_names = [
#         "Delhi", "Mumbai", "Chennai", "Kolkata", "Bengaluru", "Hyderabad", "Ahmedabad",
#         "Pune", "Jaipur", "Lucknow", "Kanpur", "Nagpur", "Indore", "Bhopal", "Patna",
#         "Thane", "Agra", "Varanasi", "Surat", "Vadodara", "Coimbatore", "Ludhiana",
#         "Nashik", "Faridabad", "Meerut", "Rajkot", "Amritsar", "Allahabad", "Jodhpur"
#     ]
#
#     name_prefixes = [
#         "City Central", "Public", "Community", "State", "Knowledge Hub", "Heritage", "Urban", "Village",
#         "Grand", "Modern", "Digital", "National", "Metro", "Smart", "Civic"
#     ]
#
#     locations = [f"{random.choice(city_names)} - Sector {random.randint(1, 50)}" for _ in range(123)]
#     names = [f"{random.choice(name_prefixes)} Library" for _ in range(123)]
#
#     list1 = [Library(name=names[i], location=locations[i]) for i in range(60)]
#     list2 = [Library(name=names[i], location=locations[i]) for i in range(60, 123)]
#
#     Library.objects.bulk_create(list1)
#     Library.objects.bulk_create(list2)
#     print("done!")
#
# if __name__ == "__main__":
#     run()
#

# import os
# import sys
# import django
#
# # Setup Django environment
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booksproject.settings")
# django.setup()
#
# from firstbook.models import Book
#
# def run():
#     List1 = [
#         Book(name='The White Tiger', author='Aravind Adiga', publisher='HarperCollins'),
#         Book(name='The God of Small Things', author='Arundhati Roy', publisher='Penguin India'),
#         Book(name='Wings of Fire', author='Dr. A.P.J. Abdul Kalam', publisher='Penguin India'),
#         Book(name='Sapiens: A Brief History of Humankind', author='Yuval Noah Harari', publisher='Harvill Secker'),
#         Book(name='Pride and Prejudice', author='Jane Austen', publisher='T. Egerton'),
#         Book(name='The Alchemist', author='Paulo Coelho', publisher='HarperCollins'),
#         Book(name='One Indian Girl', author='Chetan Bhagat', publisher='Rupa Publications'),
#         Book(name='Becoming', author='Michelle Obama', publisher='Crown Publishing Group'),
#         Book(name='The Immortals of Meluha', author='Amish Tripathi', publisher='Westland Press'),
#         Book(name='The Kite Runner', author='Khaled Hosseini', publisher='Riverhead Books'),
#         Book(name='The Hunger Games', author='Suzanne Collins', publisher='Scholastic Press'),
#         Book(name='To Kill a Mockingbird', author='Harper Lee', publisher='J.B. Lippincott & Co.'),
#         Book(name='1984', author='George Orwell', publisher='Secker & Warburg'),
#         Book(name='The Great Gatsby', author='F. Scott Fitzgerald', publisher='Charles Scribner\'s Sons'),
#         Book(name='Harry Potter and the Sorcerer\'s Stone', author='J.K. Rowling', publisher='Bloomsbury'),
#         Book(name='The Silent Patient', author='Alex Michaelides', publisher='Celadon Books'),
#         Book(name='Educated', author='Tara Westover', publisher='Random House'),
#         Book(name='The Secret', author='Rhonda Byrne', publisher='Atria Publishing Group'),
#         Book(name='The Power of Now', author='Eckhart Tolle', publisher='New World Library'),
#         Book(name='Shantaram', author='Gregory David Roberts', publisher='St. Martin\'s Press'),
#         Book(name='The Night Circus', author='Erin Morgenstern', publisher='Doubleday'),
#         Book(name='The Book Thief', author='Markus Zusak', publisher='Knopf'),
#         Book(name='Rich Dad Poor Dad', author='Robert T. Kiyosaki', publisher='Warner Books'),
#         Book(name='Life of Pi', author='Yann Martel', publisher='Knopf Canada'),
#         Book(name='The Girl on the Train', author='Paula Hawkins', publisher='Riverhead Books'),
#         Book(name='A Brief History of Time', author='Stephen Hawking', publisher='Bantam Books'),
#         Book(name='The 5 AM Club', author='Robin Sharma', publisher='HarperCollins'),
#         Book(name='The Power of Habit', author='Charles Duhigg', publisher='Random House'),
#         Book(name='The Fountainhead', author='Ayn Rand', publisher='Bobbs-Merrill'),
#         Book(name='Norwegian Wood', author='Haruki Murakami', publisher='Kodansha'),
#         Book(name='The Diary of a Young Girl', author='Anne Frank', publisher='Contact Publishing'),
#         Book(name='Gone with the Wind', author='Margaret Mitchell', publisher='Macmillan'),
#         Book(name='Catcher in the Rye', author='J.D. Salinger', publisher='Little, Brown and Company'),
#         Book(name='The Shining', author='Stephen King', publisher='Doubleday'),
#         Book(name='The Lion King', author='Disney', publisher='Disney Press'),
#         Book(name='The Road', author='Cormac McCarthy', publisher='Alfred A. Knopf'),
#         Book(name='The Brothers Karamazov', author='Fyodor Dostoevsky', publisher='The Russian Messenger'),
#         Book(name='The Fountainhead', author='Ayn Rand', publisher='Bobbs-Merrill'),
#         Book(name='The Murder of Roger Ackroyd', author='Agatha Christie', publisher='Collins'),
#         Book(name='The Wind-Up Bird Chronicle', author='Haruki Murakami', publisher='Shinchosha'),
#         Book(name='Indian Summer', author='Alex von Tunzelmann', publisher='Simon & Schuster'),
#         Book(name='The Namesake', author='Jhumpa Lahiri', publisher='Houghton Mifflin Harcourt'),
#         Book(name='The Inheritance of Loss', author='Kiran Desai', publisher='Atlantic Monthly Press'),
#         Book(name='Midnight\'s Children', author='Salman Rushdie', publisher='Jonathan Cape'),
#         Book(name='The Zookeeper\'s Wife', author='Diane Ackerman', publisher='W.W. Norton & Company'),
#         Book(name='The Immortalists', author='Chloe Benjamin', publisher='G.P. Putnam\'s Sons'),
#         Book(name='Rani Padmini', author='Nikhil Ghosh', publisher='Prabhat Prakashan'),
#         Book(name='Two States', author='Chetan Bhagat', publisher='Rupa Publications'),
#         Book(name='The Cuckoo\'s Calling', author='Robert Galbraith', publisher='Sphere'),
#         Book(name='The Outsider', author='Stephen King', publisher='Scribner'),
#         Book(name='The Subtle Art of Not Giving a F*ck', author='Mark Manson', publisher='HarperOne'),
#         Book(name='Dr. Kalam\'s Vision', author='Dr. A.P.J. Abdul Kalam', publisher='Rupa Publications'),
#         Book(name='The Last Lecture', author='Randy Pausch', publisher='Hyperion'),
#         Book(name='The Best of Me', author='Nicholas Sparks', publisher='Grand Central Publishing'),
#         Book(name='How to Win Friends and Influence People', author='Dale Carnegie', publisher='Simon & Schuster'),
#         Book(name='The Monk Who Sold His Ferrari', author='Robin Sharma', publisher='HarperCollins'),
#         Book(name='The Art of War', author='Sun Tzu', publisher='Shambhala'),
#         Book(name='I Am Malala', author='Malala Yousafzai', publisher='Little, Brown and Company'),
#         Book(name='The Fault in Our Stars', author='John Green', publisher='Dutton Books'),
#         Book(name='The Hunger Games: Catching Fire', author='Suzanne Collins', publisher='Scholastic Press'),
#         Book(name='Homo Deus: A Brief History of Tomorrow', author='Yuval Noah Harari', publisher='Harvill Secker')
#     ]
#
#     List2 = [
#         Book(name='The Pilgrimage', author='Paulo Coelho', publisher='HarperCollins'),
#         Book(name='The Art of Racing in the Rain', author='Garth Stein', publisher='HarperCollins'),
#         Book(name='The Book of Indian Birds', author='Salim Ali', publisher='Oxford University Press'),
#         Book(name='The Adventures of Sherlock Holmes', author='Sir Arthur Conan Doyle', publisher='George Newnes Ltd.'),
#         Book(name='The Secret Garden', author='Frances Hodgson Burnett', publisher='Frederick A. Stokes Company'),
#         Book(name='Angels and Demons', author='Dan Brown', publisher='Simon & Schuster'),
#         Book(name='The Girl with the Dragon Tattoo', author='Stieg Larsson', publisher='Norstedts Förlag'),
#         Book(name='The Red Tent', author='Anita Diamant', publisher='St. Martin\'s Press'),
#         Book(name='The Time Traveler\'s Wife', author='Audrey Niffenegger', publisher='Audrey Niffenegger'),
#         Book(name='The Henna Artist', author='Alka Joshi', publisher='Mira Books'),
#         Book(name='Atonement', author='Ian McEwan', publisher='Nan A. Talese'),
#         Book(name='The Giver', author='Lois Lowry', publisher='Houghton Mifflin'),
#         Book(name='The Shogun', author='James Clavell', publisher='Dell Publishing'),
#         Book(name='The Night Manager', author='John le Carré', publisher='Hodder & Stoughton'),
#         Book(name='The Four Agreements', author='Don Miguel Ruiz', publisher='Amber-Allen Publishing'),
#         Book(name='The Woman in White', author='Wilkie Collins', publisher='Bradbury and Evans'),
#         Book(name='The Book of Dust', author='Philip Pullman', publisher='David Fickling Books'),
#         Book(name='A Tale of Two Cities', author='Charles Dickens', publisher='Chapman & Hall'),
#         Book(name='Shoe Dog', author='Phil Knight', publisher='Scribner'),
#         Book(name='The Little Prince', author='Antoine de Saint-Exupéry', publisher='Reynal & Hitchcock'),
#         Book(name='The Picture of Dorian Gray', author='Oscar Wilde', publisher='Ward, Lock and Company'),
#         Book(name='The Count of Monte Cristo', author='Alexandre Dumas', publisher='Maiden Lane'),
#         Book(name='Les Misérables', author='Victor Hugo', publisher='A. Lacroix, Verboeckhoven & Cie'),
#         Book(name='The Girl Who Played with Fire', author='Stieg Larsson', publisher='Norstedts Förlag'),
#         Book(name='The Secret History', author='Donna Tartt', publisher='Knopf'),
#         Book(name='The Nightingale', author='Kristin Hannah', publisher='St. Martin\'s Press'),
#         Book(name='All the Light We Cannot See', author='Anthony Doerr', publisher='Scribner'),
#         Book(name='The Time Traveler\'s Wife', author='Audrey Niffenegger', publisher='Harcourt'),
#         Book(name='Room', author='Emma Donoghue', publisher='Little, Brown and Company'),
#         Book(name='The Handmaid\'s Tale', author='Margaret Atwood', publisher='McClelland and Stewart'),
#         Book(name='The Underground Railroad', author='Colson Whitehead', publisher='Doubleday'),
#         Book(name='The Water Dancer', author='Ta-Nehisi Coates', publisher='One World'),
#         Book(name='Middlesex', author='Jeffrey Eugenides', publisher='Farrar, Straus and Giroux'),
#         Book(name='A Little Life', author='Hanya Yanagihara', publisher='Doubleday'),
#         Book(name='Atonement', author='Ian McEwan', publisher='Nan A. Talese'),
#         Book(name='An Artist of the Floating World', author='Kazuo Ishiguro', publisher='Faber and Faber'),
#         Book(name='The Remains of the Day', author='Kazuo Ishiguro', publisher='Faber and Faber'),
#         Book(name='The Sense of an Ending', author='Julian Barnes', publisher='Jonathan Cape'),
#         Book(name='Never Let Me Go', author='Kazuo Ishiguro', publisher='Faber and Faber'),
#         Book(name='The Book Thief', author='Markus Zusak', publisher='Knopf'),
#         Book(name='The Night Watchman', author='Louise Erdrich', publisher='HarperCollins'),
#         Book(name='The 100-Year-Old Man Who Climbed Out the Window and Disappeared', author='Jonas Jonasson', publisher='Other Press'),
#         Book(name='The Help', author='Kathryn Stockett', publisher='Amy Einhorn Books'),
#         Book(name='To Kill a Mockingbird', author='Harper Lee', publisher='J.B. Lippincott & Co.'),
#         Book(name='The Outsiders', author='S.E. Hinton', publisher='Viking Press'),
#         Book(name='The Hound of the Baskervilles', author='Arthur Conan Doyle', publisher='George Newnes Ltd.'),
#         Book(name='War and Peace', author='Leo Tolstoy', publisher='The Russian Messenger'),
#         Book(name='Anna Karenina', author='Leo Tolstoy', publisher='The Russian Messenger'),
#         Book(name='Crime and Punishment', author='Fyodor Dostoevsky', publisher='The Russian Messenger'),
#         Book(name='The Complete Maus', author='Art Spiegelman', publisher='Pantheon'),
#         Book(name='The Hitchhiker\'s Guide to the Galaxy', author='Douglas Adams', publisher='Pan Books'),
#         Book(name='Siddhartha', author='Hermann Hesse', publisher='New Directions'),
#         Book(name='The Prophet', author='Kahlil Gibran', publisher='Knopf'),
#         Book(name='The Power of Now', author='Eckhart Tolle', publisher='New World Library'),
#         Book(name='The Art of Happiness', author='Dalai Lama', publisher='Riverhead Books'),
#         Book(name='The Bhagavad Gita', author='Vyasa', publisher='Gita Press'),
#         Book(name='The Holy Bible', author='Various', publisher='Various'),
#         Book(name='Ramayana', author='Valmiki', publisher='Various'),
#         Book(name='Mahabharata', author='Vyasa', publisher='Various'),
#         Book(name='The Book of Awakening', author='Mark Nepo', publisher='Conari Press'),
#         Book(name='The Dalai Lama\'s Cat', author='David Michie', publisher='Hay House'),
#         Book(name='The Tao of Pooh', author='Benjamin Hoff', publisher='Viking Press')
#     ]
#
#     Book.objects.bulk_create(List1)
#     Book.objects.bulk_create(List2)
#     print("done!")
#
# if __name__ == "__main__":
#     run()