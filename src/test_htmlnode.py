import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "TestTextHere")
        node2 = HTMLNode("p", "TestTextHere")
        self.assertEqual(node, node2)

    def test_props(self):
        testProps = {'href':"www.google.com", 'target':"_blank"}
        node = HTMLNode(None, None, None, testProps)
        actual = node.props_to_html()
        real ='href="www.google.com" target="_blank"'
        self.assertEqual(actual, real)
    
    def test_none(self):
        node = HTMLNode("b", "bold", None, {"p":"test1", "b":"test2"})
        self.assertEqual(node.__repr__(), "HTMLNode(tag:b, value:bold, children:, props:p=\"test1\" b=\"test2\")")
        

if __name__ == "__main__":
    unittest.main()
