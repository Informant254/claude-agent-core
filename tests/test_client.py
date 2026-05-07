import unittest
from unittest.mock import MagicMock, patch

from claude_agent_core.client import ClaudeClient


class ClaudeClientTests(unittest.TestCase):
    def test_generate_response_joins_text_blocks(self):
        fake_message = MagicMock()
        fake_message.content = [MagicMock(text="hello"), MagicMock(text=" world")]
        api = MagicMock()
        api.messages.create.return_value = fake_message

        client = ClaudeClient(
            api_key="test-key",
            load_environment=False,
            client=api,
        )
        response = client.generate_response("  say hi  ")

        self.assertEqual(response, "hello world")
        api.messages.create.assert_called_once()

    def test_rejects_empty_prompt(self):
        client = ClaudeClient(
            api_key="test-key",
            load_environment=False,
            client=MagicMock(messages=MagicMock(create=MagicMock())),
        )

        with self.assertRaises(ValueError):
            client.generate_response("   ")

    def test_requires_api_key(self):
        with patch.dict("os.environ", {}, clear=True):
            with self.assertRaises(ValueError):
                ClaudeClient(load_environment=False)


if __name__ == "__main__":
    unittest.main()
