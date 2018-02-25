from linked_list import SinglyLinkedList
# from linked_list import SinglyLinkedList


class SetupSinglyLinkedList:
    def setup_method(self):
        self.test_list = SinglyLinkedList()

        self.test_list.append(42)
        self.test_list.append(33)
        self.test_list.append('spam')
        self.test_list.prepend([])
        self.test_list.prepend({'a': 42})


class TestSinglyLinkedList(SetupSinglyLinkedList):
    def test_prepend(self):
        assert repr(self.test_list) == "LinkedList <[{'a': 42}, [], 42, 33, 'spam']>"

        self.test_list.prepend('first')

        assert repr(self.test_list) == "LinkedList <['first', {'a': 42}, [], 42, 33, 'spam']>"

    def test_append(self):
        assert repr(self.test_list) == "LinkedList <[{'a': 42}, [], 42, 33, 'spam']>"

        self.test_list.append('last')

        assert repr(self.test_list) == "LinkedList <[{'a': 42}, [], 42, 33, 'spam', 'last']>"

    def test_find(self):
        spam = self.test_list.find('spam')

        assert spam.data == 'spam'

        not_found = self.test_list.find('kek')
        assert not_found == None

    def test_remove(self):
        self.test_list.remove([])

        assert repr(self.test_list) == "LinkedList <[{'a': 42}, 42, 33, 'spam']>"

        self.test_list.remove(33)

        assert repr(self.test_list) == "LinkedList <[{'a': 42}, 42, 'spam']>"

    def test_reverse(self):
        self.test_list.reverse()

        assert repr(self.test_list) == "LinkedList <['spam', 33, 42, [], {'a': 42}]>"
