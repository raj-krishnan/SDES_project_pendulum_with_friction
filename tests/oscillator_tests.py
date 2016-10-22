from oscillator.oscillator import Oscillator
import unittest


class TestOscillator(unittest.TestCase):
    def test_flags_incorrect_arguments(self):
        self.assertRaises(TypeError, Oscillator, "42", "answer", "everything")

    def test_flags_incorrect_initialisation(self):
        self.assertRaises(TypeError, Oscillator, [42, 42, 42], 42, 42)

    def test_state_unchanged_after_zero_time(self):
        oscillator = Oscillator()
        self.assertListEqual(oscillator.state,
                             list(oscillator.get_trajectory(0, 1)[0]))

    def test_amplitude_decreases_when_friction_present(self):
        oscillator = Oscillator(alpha=1.0, radius=1.0)
        self.assertTrue(oscillator.state[0]
                        > oscillator.get_trajectory(10.0, 500)[-1][0])


if __name__ == '__main__':
    unittest.main()
