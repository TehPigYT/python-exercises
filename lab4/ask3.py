import unittest


class Stack:
    list_empty = "List doesn't have items."

    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)
        # print(self.data)

    def pop(self):
        if len(self.data) < 1:
            print(Stack.list_empty)
            return

        self.data.pop()
        # print(self.data)

    def clear(self):
        self.data = []
        # print("cleared")

    def __str__(self):
        if len(self.data) == 0:
            return Stack.list_empty

        str = "->" + "  ".join(f"{item}\n" for item in reversed(self.data))
        # print(str)
        return str


class TestHammingDistance(unittest.TestCase):
    def test_Stack(self):
        s = Stack()
        self.assertTrue(str(s) == "List doesn't have items.")
        s.push(1)
        self.assertTrue(str(s) == "->1\n")
        s.push(2)
        self.assertTrue(str(s) == "->2\n  1\n")
        s.push(3)
        self.assertTrue(str(s) == "->3\n  2\n  1\n")
        s.pop()
        self.assertTrue(str(s) == "->2\n  1\n")


if __name__ == "__main__":
    unittest.main()
