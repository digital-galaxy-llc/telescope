import os
import unittest

from telescope import get_client


class TestAnthropicClient(unittest.TestCase):
    def setUp(self):
        """
        Ensure ANTHROPIC_API_KEY is set for tests
        """
        if 'ANTHROPIC_API_KEY' not in os.environ:
            self.skipTest("ANTHROPIC_API_KEY environment variable not set")

    def test_get_client(self):
        """
        Test getting an Anthropic client
        """
        # Get Anthropic client
        client = get_client(vendor='anthropic')
        
        # Verify client is not None
        self.assertIsNotNone(client, "Client should not be None")
        
        # Verify default model
        self.assertEqual(client.model, 'claude-2.1', "Default model should be claude-2.1")

    def test_send_message(self):
        """
        Test sending a message to Anthropic client
        """
        # Get Anthropic client
        client = get_client(vendor='anthropic')
        
        # Send a test message
        response = client.send_message('What day is it today?')
        
        # Assert that the response is a non-empty string
        self.assertIsInstance(response, str, "Response should be a string")
        self.assertTrue(len(response) > 0, "Response should not be empty")

    def test_custom_model(self):
        """
        Test creating client with a custom model
        """
        custom_model = 'claude-3-sonnet-20240229'
        client = get_client(vendor='anthropic', model=custom_model)
        
        self.assertEqual(client.model, custom_model, "Should use specified model")

    def test_invalid_vendor(self):
        """
        Test getting a client with an invalid vendor
        """
        with self.assertRaises(ValueError, msg="Should raise ValueError for invalid vendor"):
            get_client(vendor='invalid_vendor')

    def test_missing_api_key(self):
        """
        Test behavior when no API key is provided
        """
        # Temporarily unset the API key
        original_key = os.environ.get('ANTHROPIC_API_KEY')
        try:
            if 'ANTHROPIC_API_KEY' in os.environ:
                del os.environ['ANTHROPIC_API_KEY']
            
            with self.assertRaises(ValueError, msg="Should raise ValueError when no API key is set"):
                get_client(vendor='anthropic')
        finally:
            # Restore the original API key
            if original_key:
                os.environ['ANTHROPIC_API_KEY'] = original_key


if __name__ == '__main__':
    unittest.main()
