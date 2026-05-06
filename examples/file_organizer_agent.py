import os
from claude_agent_core.client import ClaudeClient

def main():
    # This example demonstrates how to build a simple File Organizer Agent
    # that can analyze a directory and suggest organization strategies.
    
    client = ClaudeClient() # Assumes ANTHROPIC_API_KEY is in .env
    
    directory_to_scan = "./test_files"
    if not os.path.exists(directory_to_scan):
        os.makedirs(directory_to_scan)
        # Create some dummy files
        open(f"{directory_to_scan}/report.pdf", "w").close()
        open(f"{directory_to_scan}/image.png", "w").close()
        open(f"{directory_to_scan}/script.py", "w").close()

    files = os.listdir(directory_to_scan)
    prompt = f"I have the following files in a directory: {files}. Suggest a folder structure to organize them."
    
    print(f"🔍 Agent is analyzing {len(files)} files...")
    response = client.generate_response(prompt)
    
    print("\n🤖 Agent Suggestion:")
    print(response)

if __name__ == "__main__":
    main()
