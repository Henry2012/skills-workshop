import unittest

from status import is_terminal


class TerminalStateTests(unittest.TestCase):
    def test_terminal_states(self):
        for state in ("SUCCEEDED", "FAILED"):
            with self.subTest(state=state):
                self.assertTrue(is_terminal(state))

    def test_in_flight_states(self):
        for state in ("QUEUED", "RUNNING"):
            with self.subTest(state=state):
                self.assertFalse(is_terminal(state))

    def test_unknown_is_not_success(self):
        for state in ("HTTP 200", "", "UNKNOWN"):
            with self.subTest(state=state):
                self.assertFalse(is_terminal(state))


if __name__ == "__main__":
    unittest.main()
