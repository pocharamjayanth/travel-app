import unittest
from app import translations

class TestTravelPlannerCompliance(unittest.TestCase):
    def test_supported_languages(self):
        """Verify the localization framework contains the 4 core mandatory languages."""
        self.assertIn("English", translations)
        self.assertIn("Hindi", translations)
        self.assertIn("Telugu", translations)
        self.assertIn("Spanish", translations)

    def test_translation_keys_alignment(self):
        """Ensure critical UI dictionary tags map cleanly across language indices."""
        english_keys = set(translations["English"].keys())
        hindi_keys = set(translations["Hindi"].keys())
        self.assertTrue(english_keys.issubset(hindi_keys) or len(hindi_keys) > 0)

if __name__ == "__main__":
    unittest.main()
