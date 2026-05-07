import unittest

from claude_agent_core.policy import ToolPolicy


class ToolPolicyTests(unittest.TestCase):
    def test_allows_named_tool_inside_size_limit(self):
        policy = ToolPolicy(allowed_tools={"search"}, max_argument_bytes=64)

        decision = policy.evaluate("search", {"query": "agent sandboxing"})

        self.assertTrue(decision.allowed)
        self.assertFalse(decision.requires_confirmation)

    def test_denies_tool_not_in_allowlist(self):
        policy = ToolPolicy(allowed_tools={"search"})

        decision = policy.evaluate("shell", {"cmd": "date"})

        self.assertFalse(decision.allowed)
        self.assertIn("not in the allowed tool set", decision.reason)

    def test_confirmation_required_blocks_require_allowed(self):
        policy = ToolPolicy(
            allowed_tools={"deploy"},
            confirmation_required={"deploy"},
        )

        decision = policy.evaluate("deploy", {"target": "production"})

        self.assertTrue(decision.allowed)
        self.assertTrue(decision.requires_confirmation)
        with self.assertRaises(PermissionError):
            policy.require_allowed("deploy", {"target": "production"})

    def test_rejects_oversized_arguments(self):
        policy = ToolPolicy(allowed_tools={"write_file"}, max_argument_bytes=10)

        decision = policy.evaluate("write_file", {"content": "x" * 100})

        self.assertFalse(decision.allowed)
        self.assertIn("exceed", decision.reason)


if __name__ == "__main__":
    unittest.main()
