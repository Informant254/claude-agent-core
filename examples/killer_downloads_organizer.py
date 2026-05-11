"""
🚀 KILLER DEMO - Secure Downloads Organizer Agent
Showcases Claude Agent Core + Fortress Gate in action
"""

from claude_agent_core import ClaudeAgent, SecureFortressGate, ToolPolicy
import os
from pathlib import Path
import time

def main():
    print("🔐 Initializing Claude Agent Core with Fortress Protection...\n")
    
    # === Fortress Setup ===
    fortress = SecureFortressGate(
        vault_backend="dpapi",
        totp_label="DownloadsOrganizer",
        approval_timeout=90
    )
    
    # === Strict Policy ===
    policy = ToolPolicy(
        enforcement_level="strict",
        max_risk_score=75,
        require_approval_for=["file_write", "file_move", "file_delete", "system"]
    )
    
    # === Agent ===
    agent = ClaudeAgent(
        api_key=os.getenv("ANTHROPIC_API_KEY"),
        fortress=fortress,
        policy=policy,
        temperature=0.2,
        enable_audit_logging=True
    )
    
    print("✅ Secure Agent Ready!")
    print("   High-risk file operations will require your TOTP approval.\n")
    
    downloads_path = str(Path.home() / "Downloads")
    
    prompt = f"""
    You are an intelligent Downloads Organizer.
    Analyze the '{downloads_path}' folder and organize files into these categories:
    - Images, Videos, Documents, Archives, Code, Installers, Others
    
    Rules:
    - Create clean folder names
    - Don't delete anything without approval
    - Be safe and respectful of existing files
    """
    
    print("🤖 Asking agent to organize Downloads folder...\n")
    
    try:
        response = agent.chat(prompt)
        print(response)
        
        print("\n" + "="*60)
        print("🎉 Demo Complete!")
        print("This demo showed:")
        print("   • Clean tool calling")
        print("   • Automatic risk detection")
        print("   • Fortress human + TOTP gate for dangerous actions")
        print("   • Audit logging")
        print("="*60)
        
    except Exception as e:
        print(f"❌ Operation blocked or required approval: {e}")

if __name__ == "__main__":
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("⚠️  Please set your ANTHROPIC_API_KEY environment variable first.")
    else:
        main()
