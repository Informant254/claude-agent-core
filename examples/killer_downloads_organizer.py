from claude_agent_core import ClaudeAgent
import os
from pathlib import Path

def main():
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("Please set ANTHROPIC_API_KEY environment variable")
        return
    
    agent = ClaudeAgent()
    downloads = str(Path.home() / "Downloads")
    
    prompt = f"""You are a helpful file organizer.
Analyze the Downloads folder at: {downloads}
Suggest a clean organization structure.
Be safe and conservative."""
    
    print("Running demo...")
    response = agent.chat(prompt)
    print("\nResponse:")
    print(response.content)

if __name__ == "__main__":
    main()