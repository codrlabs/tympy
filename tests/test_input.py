import pytest
import tympy as TO

# Use pytest's skip decorator at the class level to skip all tests within the class
@pytest.mark.skip(reason="These tests are visually verified and cannot be automated for now.")
class TestTympy:
    t = TO

    def test_compare_with_multiple_files_and_functions(self):
        self.t.compare(["example_1.py", "example_2.py", "example_3.py"],
                       ["sum", "SuM", "SuMIT"],
                       [(5,  9), (9,  5), (5,  9)])

    def test_compare_with_mismatched_length(self):
        with pytest.raises(Exception):
            self.t.compare(["example_1.py", "example_2.py"],
                           ["sum", "SuM", "SuMIT"],
                           [(5,  9), (9,  5), (5,  9)])

    def test_compare_with_single_string_function(self):
        self.t.compare(["example_1.py", "example_2.py"],
                       "subtract",
                       [(5,  9), (9,  5)])

    def test_compare_with_single_tuple_argument(self):
        self.t.compare(["example_1.py", "example_3.py"],
                       ["sum", "SuMIT"],
                       (5,  9))

    def test_compare_with_single_string_argument(self):
        self.t.compare(["example_1.py", "example_2.py"],
                       ["printNOW", "printNoW"],
                       "Hello World!")
