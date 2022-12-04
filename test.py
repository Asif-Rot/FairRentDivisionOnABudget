import unittest
from fairpy.fairpy.agentlist import AgentList
from main import algorithm1, algorithm2


class TestMain(unittest.TestCase):
    def test_algo1(self):
        ex1 = AgentList({"Alice": {'1': 250, '2': 250, '3': 500}, "Bob": {'1': 250, '2': 250, '3': 500},
                         "Clair": {'1': 250, '2': 500, '3': 250}})
        self.assertEqual(algorithm1(ex1, 1000, {'Alice': 250, 'Bob': 320, 'Clair': 430}),
                         (709.99, "(Alice gets {1} with rent 70, Bob gets {2} with rent 320,"
                                  "Clair gets {3} with rent 320))"))

    def test_algo2(self):
        ex1 = AgentList({"Alice": {'1': 250, '2': 250, '3': 500}, "Bob": {'1': 250, '2': 250, '3': 500},
                         "Clair": {'1': 250, '2': 500, '3': 250}})
        self.assertEqual(algorithm2(ex1, 1000, {'Alice': 250, 'Bob': 320, 'Clair': 430}),
                         (920, "(Alice gets {1} with rent 130, Bob gets {2} with rent 270,"
                               "Clair gets {3} with rent 520)"))


if __name__ == '__main__':
    unittest.main()
