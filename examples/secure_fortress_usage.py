from claude_agent_core import ClaudeAgent, SecureFortressGate, ToolPolicy
import os
import time

def main():
    print("Initializing Secure Claude Agent...")
    
    fortress = SecureFortressGate()
    policy = ToolPolicy(enforcement_level="strict")
    
    agent = ClaudeAgent(
        fortress=fortress,
        policy=policy
    )
    
    print("Secure agent ready.")
    
    # Test query
    response = agent.chat("Explain how to stay safe while using AI agents.")
    print("\nResponse:")
    print(response.content if hasattr(response, 'content') else response)

if __name__ == "__main__":
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("Please set ANTHROPIC_API_KEY environment variable.")
    else:
        main()