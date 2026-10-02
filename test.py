import unittest
from main import to_upper

class Mytestcase(unittest.TestCase):
    def test_to_upper(self):
        name = "monika"
        up = to_upper(name)
        self.assertEqual(up,"MONIKA")
if __name__ == "__main__":
    unittest.main()