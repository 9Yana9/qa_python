from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_exceeding_character_limit(self):
        collector = BooksCollector()
        collector.add_new_book('Г' * 41)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('1984')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        assert collector.get_book_genre('Война и мир') == 'Фантастика'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('451 градус по Фаренгейту')
        collector.set_book_genre('451 градус по Фаренгейту', 'Фантастика')
        books = collector.get_books_with_specific_genre('Фантастика')
        assert '451 градус по Фаренгейту' in books

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Тома Сойера')
        collector.set_book_genre('Приключения Тома Сойера', 'Комедии')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')

        books_for_children = collector.get_books_for_children()
        assert 'Сияние' not in books_for_children

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        collector.delete_book_from_favorites('Гарри Поттер и философский камень')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
