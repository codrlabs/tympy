import unittest
import timed_output as TO

TO.compare(["files/example_1.py", "files/example_2.py"],
           ["sum", "SuM"],
           [(4, 5), (4, 9)])
