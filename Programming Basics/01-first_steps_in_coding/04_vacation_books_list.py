#⦁	Брой страници в текущата книга – цяло число;Страници, които може да прочита за 1 час – цяло число;Броя на дните, за които трябва да прочете книгата – цяло число;
number_pages_in_this_book = int(input())
number_pages_red_for_hour = int(input())
days_to_read_the_book = int(input())
pages_every_day = number_pages_in_this_book / number_pages_red_for_hour
total = pages_every_day / days_to_read_the_book
print(total)