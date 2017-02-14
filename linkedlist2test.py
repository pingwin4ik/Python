import unittest

from linkedEG import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def tearDown(self):
        self.list = None

    def test_put(self):
        self.list.put("David")
        self.assertTrue(self.list.head.get_data() == "David")
        self.assertTrue(self.list.head.get_next() is None)

    def test_put_two(self):
        self.list.put("David")
        self.list.put("Thomas")
        self.assertTrue(self.list.head.get_data() == "Thomas")
        head_next = self.list.head.get_next()
        self.assertTrue(head_next.get_data() == "David")

    def test_nextNode(self):
        self.list.put("Jacob")
        self.list.put("Pallymay")
        self.list.put("Rasmus")

        self.assertTrue(self.list.head.get_data() == "Rasmus")

        head_next = self.list.head.get_next()
        self.assertTrue(head_next.get_data() == "Pallymay")

        last = head_next.get_next()
        self.assertTrue(last.get_data() == "Jacob")

    def test_positive_get(self):
        self.list.put("Jacob")
        self.list.put("Pallymay")
        self.list.put("Rasmus")

        found = self.list.get("Jacob")
        self.assertTrue(found.get_data() == "Jacob")

        found = self.list.get("Pallymay")
        self.assertTrue(found.get_data() == "Pallymay")

        found = self.list.get("Jacob")
        self.assertTrue(found.get_data() == "Jacob")

    def test_getNone(self):
        self.list.put("Jacob")
        self.list.put("Pallymay")

        # make sure reg get works
        found = self.list.get("Jacob")

        self.assertTrue(found.get_data() == "Jacob")

        with self.assertRaises(ValueError):
            self.list.get("Vincent")

    def test_delete(self):
        self.list.put("Jacob")
        self.list.put("Pallymay")
        self.list.put("Rasmus")

        # Delete the list head
        self.list.delete("Rasmus")
        self.assertTrue(self.list.head.get_data() == "Pallymay")

        # Delete the list tail
        self.list.delete("Jacob")
        self.assertTrue(self.list.head.get_next() is None)

    def test_delete_value_not_in_list(self):
        self.list.put("Jacob")
        self.list.put("Pallymay")
        self.list.put("Rasmus")

        with self.assertRaises(ValueError):
            self.list.delete("Sunny")

    def test_delete_empty_list(self):
        with self.assertRaises(ValueError):
            self.list.delete("Sunny")

    def test_delete_next_reassignment(self):
        self.list.put("Jacob")
        self.list.put("Cid")
        self.list.put("Pallymay")
        self.list.put("Rasmus")

        self.list.delete("Pallymay")
        self.list.delete("Cid")

        self.assertTrue(self.list.head.next_node.get_data() == "Jacob")