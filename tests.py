from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_book_if_already_exists_not_add_again(self):
        collector = BooksCollector()
        collector.add_new_book('Лучше подавать холодным')
        collector.add_new_book('Лучше подавать холодным')
        assert len(collector.get_books_rating()) == 1

    def test_add_rating_if_no_book_collection_not_put_rating(self):
        collector = BooksCollector()
        collector.add_new_book("Шпаги над звездами")
        collector.set_book_rating("И пришел многоликий", 8)
        book_rating = collector.get_book_rating("И пришел многоликий")
        assert book_rating is None

    def test_add_new_book_and_rating_less_one(self):
        collector = BooksCollector()
        collector.add_new_book('Киндрет')
        collector.set_book_rating('Киндрет ', 0)
        book_rating = collector.get_book_rating("Киндрет")
        assert  book_rating == 1

    def test_add_new_book_and_rating_more_ten(self):
        collector = BooksCollector()
        collector.add_new_book('Башня шутов')
        collector.set_book_rating('Башня шутов', 12)
        book_rating = collector.get_book_rating("Башня шутов")
        assert book_rating == 1

    def test_book_not_added_no_rating(self):
        collector = BooksCollector()
        assert collector.get_book_rating("мудрость толпы") == None

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Имя ветра')
        collector.add_book_in_favorites('Имя ветра')
        assert 'Имя ветра' in collector.favorites

    def test_no_add_book_in_favorites_if_book_no_collection(self):
        collector = BooksCollector()
        collector.add_new_book('прежде чем их повесят')
        collector.add_book_in_favorites('Игра Эндера')
        collector.add_book_in_favorites('прежде чем их повесят')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Цветы для Элджеронона')
        collector.add_book_in_favorites ('Цветы для Элджеронона')
        collector.delete_book_from_favorites('Цветы для Элджеронона')
        assert len(collector.get_list_of_favorites_books()) == 0
