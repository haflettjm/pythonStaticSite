import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_url(self):
        node = TextNode("This is a text node", "bold", "https://www.example.com")
        self.assertEqual(node.url, "https://www.example.com")
    def test_none(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.url, None)
        

if __name__ == "__main__":
    unittest.main()
