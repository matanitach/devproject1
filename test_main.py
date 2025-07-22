import unittest
import sys
import os

# Add the current directory to Python path to import main
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


class TestMainApp(unittest.TestCase):

    def test_app_runs_without_error(self):
        """Test that the main application runs without throwing exceptions"""
        try:
            # Import and run main logic here
            # For now, we'll just test that main.py can be imported
            import main
            self.assertTrue(True, "Main app imported successfully")
        except Exception as e:
            self.fail(f"Main app failed to run: {e}")

    def test_python_version(self):
        """Test that we're running on the correct Python version"""
        version_info = sys.version_info
        self.assertGreaterEqual(version_info.major, 3)
        self.assertGreaterEqual(version_info.minor, 8)

    def test_basic_math(self):
        """Simple test to verify testing framework works"""
        self.assertEqual(2 + 2, 4)
        self.assertNotEqual(2 + 2, 5)

    def test_environment(self):
        """Test that we're in the expected environment"""
        self.assertTrue(os.path.exists('main.py'), "main.py should exist")


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
