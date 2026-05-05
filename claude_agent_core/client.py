import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

class ClaudeClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY must be provided or set in environment variables.")
        self.client = anthropic.Anthropic(api_key=self.api_key)

    def generate_response(self, prompt, model="claude-3-5-sonnet-20240620", max_tokens=1024):
        message = self.client.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text
