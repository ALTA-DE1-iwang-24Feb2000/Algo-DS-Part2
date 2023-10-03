import unittest
from main import count_item_and_sort

class TestCountItemAndSort(unittest.TestCase):
    def test_case_1(self):
        result = count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"])
        expected_output = "golang->1 ruby->2 js->4"
        for item in expected_output.split():
            self.assertIn(item, result)

    def test_case_2(self):
        result = count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"])
        expected_output = "C->1 D->2 B->3 A->4"
        for item in expected_output.split():
            self.assertIn(item, result)

    def test_case_3(self):
        result = count_item_and_sort(["football", "basketball", "tenis"])
        expected_output = "basketball->1 football->1 tenis->1"
        for item in expected_output.split():
            self.assertIn(item, result)
if __name__ == "__main__":
    unittest.main()