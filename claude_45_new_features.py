#!/usr/bin/env python3
"""
Claude 4.5 New Features Update - December 2025
===============================================
Comprehensive update covering:
- Practical Performance (Token Efficiency & Speed)
- Behavioral Differences (Communication Style & Prompting)
- Enhanced Stop Reasons (API Response Handling)

Based on official Anthropic documentation:
https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-5
"""

import anthropic
from typing import Optional, List, Dict, Any
from dataclasses import dataclass
from enum import Enum


# ============================================================================
# SECTION 1: PRACTICAL PERFORMANCE
# ============================================================================

class PracticalPerformance:
    """
    Claude 4.5 Practical Performance Improvements

    Key Metrics:
    - Token Efficiency: Up to 65% fewer tokens for same tasks
    - Speed: Significantly faster response times
    - Task Completion: Fewer iterations needed
    - Error Reduction: 50-75% reduction in tool calling errors
    """

    # Performance Benchmarks (from official documentation)
    BENCHMARKS = {
        "opus_4_5": {
            "swe_bench_verified": 80.9,  # Industry-leading
            "osworld": 66.3,  # Best computer use
            "token_efficiency": "65% fewer tokens",
            "tool_error_reduction": "50-75%",
            "focus_duration": "30+ hours autonomous",
        },
        "sonnet_4_5": {
            "swe_bench_verified": "State-of-the-art",
            "osworld": 61.4,
            "planning_improvement": "18%",
            "eval_score_improvement": "12%",
            "focus_duration": "30+ hours autonomous",
        },
        "haiku_4_5": {
            "performance_tier": "Near-frontier",
            "speed": "Fastest Claude model",
            "cost_tier": "$1/$5 per million tokens",
            "max_output_tokens": 64000,  # Increased from 8K
        }
    }

    def __init__(self, client: anthropic.Anthropic):
        self.client = client

    def demonstrate_token_efficiency(
        self,
        prompt: str,
        model: str = "claude-opus-4-5-20251101"
    ) -> Dict[str, Any]:
        """
        Demonstrate Claude 4.5's improved token efficiency.

        Opus 4.5 achieves higher pass rates while using up to 65% fewer tokens,
        giving developers real cost control without sacrificing quality.
        """
        response = self.client.messages.create(
            model=model,
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}]
        )

        return {
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
            "total_tokens": response.usage.input_tokens + response.usage.output_tokens,
            "stop_reason": response.stop_reason,
            "content": response.content[0].text,
            # Token efficiency tips
            "tips": [
                "Opus 4.5 requires fewer steps to solve tasks",
                "More precise instruction following = fewer retries",
                "Built-in token-efficient tool use (no beta header needed)",
            ]
        }

    def high_volume_processing(
        self,
        tasks: List[str],
        use_haiku: bool = True
    ) -> List[Dict[str, Any]]:
        """
        Haiku 4.5 for high-volume intelligent processing.

        Best for:
        - Real-time applications with fast response times
        - Cost-sensitive deployments at scale
        - Sub-agent architectures in multi-agent systems
        """
        model = "claude-haiku-4-5-20251001" if use_haiku else "claude-sonnet-4-5-20250929"
        results = []

        for task in tasks:
            response = self.client.messages.create(
                model=model,
                max_tokens=2048,
                messages=[{"role": "user", "content": task}]
            )
            results.append({
                "task": task[:50] + "...",
                "tokens_used": response.usage.output_tokens,
                "model": model,
            })

        return results


# ============================================================================
# SECTION 2: BEHAVIORAL DIFFERENCES
# ============================================================================

class BehavioralDifferences:
    """
    Claude 4.5 Behavioral Differences from Previous Models

    Key Changes:
    1. More concise, direct communication style
    2. Fact-based progress updates
    3. May skip verbose summaries after tool calls
    4. Requires explicit direction for "above and beyond" behavior
    5. Highly responsive to system prompts
    """

    # Known behavioral patterns
    BEHAVIORAL_PATTERNS = {
        "communication_style": {
            "concise": True,
            "direct": True,
            "natural": True,
            "verbose_summaries": "Optional (use prompting)",
        },
        "instruction_following": {
            "precision": "High - follows exactly what's asked",
            "above_and_beyond": "Requires explicit request",
            "details_attention": "Very high - pay attention to examples",
        },
        "system_prompt_sensitivity": {
            "level": "Highly responsive",
            "warning": "Aggressive language may cause overtriggering",
        },
        "alignment_improvements": {
            "sycophancy": "Reduced",
            "deception": "Reduced",
            "power_seeking": "Reduced",
            "delusional_encouragement": "Reduced",
            "prompt_injection_defense": "Improved",
        }
    }

    @staticmethod
    def get_prompt_engineering_tips() -> Dict[str, Any]:
        """
        Claude 4 Best Practices for Prompt Engineering.

        Returns guidelines for optimal prompting with Claude 4.5 models.
        """
        return {
            "be_explicit": {
                "description": "Claude 4 models respond well to clear, explicit instructions",
                "less_effective": "Create an analytics dashboard",
                "more_effective": """Create an analytics dashboard. Include as many
relevant features and interactions as possible. Go beyond the basics
to create a fully-featured implementation.""",
            },

            "add_context": {
                "description": "Provide context or motivation behind instructions",
                "less_effective": "NEVER use ellipses",
                "more_effective": """Your response will be read aloud by a text-to-speech
engine, so never use ellipses since the text-to-speech engine will not
know how to pronounce them.""",
            },

            "control_format": {
                "tip_1": "Describe desired format in natural language",
                "tip_2": "Use XML tags to structure output",
                "tip_3": "Match your prompt style to desired output style",
                "note": "Removing markdown from prompt can reduce markdown in output",
            },

            "avoid_test_gaming": {
                "description": "Prevent hard-coded solutions for test cases",
                "recommended_prompt": """Please write a high quality, general purpose solution.
Implement a solution that works correctly for all valid inputs, not just the test cases.
Do not hard-code values or create solutions that only work for specific test inputs.
Instead, implement the actual logic that solves the problem generally.""",
            },

            "leverage_thinking": {
                "description": "Use thinking capabilities for complex tasks",
                "example": """After receiving tool results, carefully reflect on their quality
and determine optimal next steps before proceeding. Use your thinking
to plan and iterate based on this new information.""",
            },

            "think_word_sensitivity": {
                "warning": "Opus 4.5 is sensitive to 'think' and its variants",
                "applies_when": "Extended thinking is NOT enabled",
                "recommendation": "Be careful with prompts containing 'think' words",
            }
        }

    @staticmethod
    def get_opus_45_specific_behaviors() -> Dict[str, str]:
        """
        Opus 4.5 Specific Behavioral Patterns.

        Based on official migration documentation.
        """
        return {
            "tool_overtriggering": {
                "issue": "Tools may be called too frequently",
                "cause": "Opus 4.5 is more responsive to system prompts",
                "fix": "Reduce aggressive language in prompts",
            },
            "excessive_abstraction": {
                "issue": "May create unwanted files or excessive abstraction",
                "fix": "Add specific constraints to limit scope",
            },
            "overly_conservative_exploration": {
                "issue": "May propose solutions without reading files",
                "fix": "Instruct to inspect relevant code before proposing fixes",
            },
            "frontend_aesthetics": {
                "note": "May produce generic-looking outputs",
                "fix": "Add frontend aesthetics snippet for improved design",
            }
        }


# ============================================================================
# SECTION 3: ENHANCED STOP REASONS
# ============================================================================

class StopReason(Enum):
    """
    All possible stop_reason values from Claude API.

    New in Claude 4.5: model_context_window_exceeded
    """
    END_TURN = "end_turn"              # Natural completion
    MAX_TOKENS = "max_tokens"          # Hit max_tokens limit
    STOP_SEQUENCE = "stop_sequence"    # Hit custom stop sequence
    TOOL_USE = "tool_use"              # Calling a tool
    PAUSE_TURN = "pause_turn"          # Server tool paused (web search)
    REFUSAL = "refusal"                # Safety refusal
    MODEL_CONTEXT_WINDOW_EXCEEDED = "model_context_window_exceeded"  # NEW in 4.5


class EnhancedStopReasons:
    """
    Enhanced Stop Reasons in Claude 4.5

    New Features:
    - model_context_window_exceeded: Explicitly indicates context limit hit
    - Better handling of refusal cases
    - Improved pause_turn for server tools

    Available by default in Sonnet 4.5 and newer models.
    For older models, use beta header: model-context-window-exceeded-2025-08-26
    """

    def __init__(self, client: anthropic.Anthropic):
        self.client = client

    def handle_response(self, response) -> Dict[str, Any]:
        """
        Comprehensive stop_reason handler for Claude 4.5.

        Returns appropriate action based on stop reason.
        """
        stop_reason = response.stop_reason

        handlers = {
            "end_turn": self._handle_end_turn,
            "max_tokens": self._handle_max_tokens,
            "stop_sequence": self._handle_stop_sequence,
            "tool_use": self._handle_tool_use,
            "pause_turn": self._handle_pause_turn,
            "refusal": self._handle_refusal,
            "model_context_window_exceeded": self._handle_context_exceeded,  # NEW
        }

        handler = handlers.get(stop_reason, self._handle_unknown)
        return handler(response)

    def _handle_end_turn(self, response) -> Dict[str, Any]:
        """
        Handle natural completion.

        Note: Empty responses with end_turn may indicate:
        - Text added immediately after tool_result (BAD practice)
        - Sending Claude's completed response back unchanged
        """
        content = response.content[0].text if response.content else ""

        if not content or len(content.strip()) == 0:
            return {
                "status": "empty_response",
                "action": "add_continuation_prompt",
                "warning": "Don't add text after tool_result blocks",
                "fix": "Send tool results directly without additional text",
            }

        return {
            "status": "complete",
            "content": content,
        }

    def _handle_max_tokens(self, response) -> Dict[str, Any]:
        """Handle max_tokens limit reached."""
        return {
            "status": "truncated",
            "reason": "max_tokens",
            "content": response.content[0].text if response.content else "",
            "action": "continue_generation",
            "message": "[Response truncated due to max_tokens limit]",
        }

    def _handle_context_exceeded(self, response) -> Dict[str, Any]:
        """
        Handle model_context_window_exceeded (NEW in Claude 4.5).

        This stop reason allows requesting maximum tokens without
        knowing the exact input size beforehand.

        Available by default in Sonnet 4.5 and newer models.
        """
        return {
            "status": "truncated",
            "reason": "model_context_window_exceeded",
            "content": response.content[0].text if response.content else "",
            "action": "context_limit_reached",
            "message": "[Response truncated due to context window limit]",
            "usage": {
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens,
            },
            "tip": "Response is valid but limited by context window, not max_tokens",
        }

    def _handle_tool_use(self, response) -> Dict[str, Any]:
        """Handle tool use request."""
        tool_calls = [
            {"name": c.name, "input": c.input, "id": c.id}
            for c in response.content if c.type == "tool_use"
        ]
        return {
            "status": "tool_use",
            "tool_calls": tool_calls,
            "action": "execute_tools",
        }

    def _handle_pause_turn(self, response) -> Dict[str, Any]:
        """
        Handle pause_turn for server tools (like web search).

        Used when Claude needs to pause a long-running operation.
        """
        return {
            "status": "paused",
            "reason": "pause_turn",
            "content": response.content,
            "action": "continue_conversation",
            "note": "Continue with same tools to resume",
        }

    def _handle_refusal(self, response) -> Dict[str, Any]:
        """
        Handle refusal due to safety concerns.

        Tip: If frequent refusals with Sonnet 4.5 or Opus 4.1,
        try Sonnet 4 which has different usage restrictions.
        """
        return {
            "status": "refused",
            "reason": "refusal",
            "action": "modify_request",
            "tip": "Consider using Sonnet 4 (claude-sonnet-4-20250514) for different restrictions",
            "docs": "https://support.claude.com/en/articles/12449294",
        }

    def _handle_stop_sequence(self, response) -> Dict[str, Any]:
        """Handle custom stop sequence."""
        return {
            "status": "stopped",
            "reason": "stop_sequence",
            "stop_sequence": response.stop_sequence,
            "content": response.content[0].text if response.content else "",
        }

    def _handle_unknown(self, response) -> Dict[str, Any]:
        """Handle unknown stop reason."""
        return {
            "status": "unknown",
            "stop_reason": response.stop_reason,
            "content": response.content,
        }

    def get_max_possible_tokens(
        self,
        prompt: str,
        model: str = "claude-sonnet-4-5-20250929"
    ) -> Dict[str, Any]:
        """
        Get maximum possible tokens without calculating input size.

        New pattern enabled by model_context_window_exceeded stop reason.
        """
        response = self.client.messages.create(
            model=model,
            max_tokens=64000,  # Set to model's maximum
            messages=[{"role": "user", "content": prompt}]
        )

        result = {
            "output_tokens": response.usage.output_tokens,
            "input_tokens": response.usage.input_tokens,
            "stop_reason": response.stop_reason,
            "content": response.content[0].text if response.content else "",
        }

        if response.stop_reason == "model_context_window_exceeded":
            result["status"] = "context_limit_reached"
            result["note"] = "Generated maximum possible given input size"
        elif response.stop_reason == "max_tokens":
            result["status"] = "max_tokens_reached"
            result["note"] = "Hit the requested max_tokens limit"
        else:
            result["status"] = "natural_completion"
            result["note"] = "Response completed naturally"

        return result


# ============================================================================
# SECTION 4: COMPLETE RESPONSE HANDLING PATTERNS
# ============================================================================

class ResponseHandler:
    """
    Complete response handling patterns for Claude 4.5.
    """

    def __init__(self, client: anthropic.Anthropic):
        self.client = client
        self.stop_handler = EnhancedStopReasons(client)

    def handle_truncated_response(
        self,
        response,
        original_prompt: str
    ) -> str:
        """
        Handle truncated responses (max_tokens or context_exceeded).
        """
        if response.stop_reason not in ["max_tokens", "model_context_window_exceeded"]:
            return response.content[0].text

        # Option 1: Warn user
        if response.stop_reason == "max_tokens":
            message = "[Response truncated due to max_tokens limit]"
        else:
            message = "[Response truncated due to context window limit]"

        return f"{response.content[0].text}\n\n{message}"

    def continue_generation(
        self,
        original_prompt: str,
        partial_response: str,
        model: str = "claude-sonnet-4-5-20250929"
    ) -> str:
        """Continue generation from truncated response."""
        messages = [
            {"role": "user", "content": original_prompt},
            {"role": "assistant", "content": partial_response},
            {"role": "user", "content": "Please continue from where you left off."}
        ]

        continuation = self.client.messages.create(
            model=model,
            max_tokens=4096,
            messages=messages
        )

        return partial_response + continuation.content[0].text

    def get_complete_response(
        self,
        prompt: str,
        model: str = "claude-sonnet-4-5-20250929",
        max_attempts: int = 3
    ) -> str:
        """
        Get complete response, handling truncation automatically.
        """
        messages = [{"role": "user", "content": prompt}]
        full_response = ""

        for _ in range(max_attempts):
            response = self.client.messages.create(
                model=model,
                max_tokens=4096,
                messages=messages
            )

            full_response += response.content[0].text

            if response.stop_reason not in ["max_tokens", "model_context_window_exceeded"]:
                break

            # Continue from where it left off
            messages = [
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": full_response},
                {"role": "user", "content": "Please continue from where you left off."}
            ]

        return full_response

    def handle_paused_conversation(
        self,
        initial_response,
        original_query: str,
        tools: List[Dict],
        model: str = "claude-sonnet-4-5-20250929",
        max_retries: int = 3
    ):
        """
        Handle pause_turn for server tools like web search.
        """
        response = initial_response
        messages = [{"role": "user", "content": original_query}]

        for _ in range(max_retries):
            if response.stop_reason != "pause_turn":
                break

            messages.append({"role": "assistant", "content": response.content})

            response = self.client.messages.create(
                model=model,
                messages=messages,
                tools=tools
            )

        return response

    def handle_tool_workflow(
        self,
        user_query: str,
        tools: List[Dict],
        model: str = "claude-sonnet-4-5-20250929",
        execute_tool_fn=None
    ):
        """
        Complete tool use workflow with proper stop reason handling.
        """
        messages = [{"role": "user", "content": user_query}]

        while True:
            response = self.client.messages.create(
                model=model,
                messages=messages,
                tools=tools
            )

            if response.stop_reason == "tool_use":
                # Execute tools
                tool_results = []
                for content in response.content:
                    if content.type == "tool_use":
                        if execute_tool_fn:
                            result = execute_tool_fn(content.name, content.input)
                        else:
                            result = f"Tool {content.name} executed"

                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": content.id,
                            "content": str(result)
                        })

                # IMPORTANT: Don't add text after tool_result
                messages.append({"role": "assistant", "content": response.content})
                messages.append({"role": "user", "content": tool_results})

            elif response.stop_reason == "pause_turn":
                # Continue for server tools
                messages.append({"role": "assistant", "content": response.content})

            else:
                # Final response (end_turn, refusal, etc.)
                return response


# ============================================================================
# SECTION 5: MIGRATION HELPERS
# ============================================================================

class MigrationHelper:
    """
    Helper class for migrating to Claude 4.5 models.
    """

    # Model strings mapping
    MODEL_MAPPING = {
        # From -> To
        "claude-3-7-sonnet-20250219": "claude-sonnet-4-5-20250929",
        "claude-3-5-haiku-20241022": "claude-haiku-4-5-20251001",
        "claude-opus-4-1-20250805": "claude-opus-4-5-20251101",
        "claude-sonnet-4-20250514": "claude-sonnet-4-5-20250929",
    }

    # Breaking changes by migration path
    BREAKING_CHANGES = {
        "sonnet_3_7_to_4_5": [
            "Cannot use both temperature AND top_p",
            "Handle 'refusal' stop_reason",
            "Update text_editor_20250728 and str_replace_based_edit_tool",
            "Remove undo_edit command",
            "Remove token-efficient-tools-2025-02-19 header",
            "Remove output-128k-2025-02-19 header",
        ],
        "haiku_3_5_to_4_5": [
            "Cannot use both temperature AND top_p",
            "Only latest tool versions supported",
            "Handle 'refusal' stop_reason",
            "New rate limits (separate from Haiku 3.5)",
        ],
        "opus_4_1_to_opus_4_5": [],  # No breaking changes
        "sonnet_4_to_4_5": [
            "Cannot use both temperature AND top_p",
        ],
    }

    @staticmethod
    def get_sampling_params(temperature: float = None, top_p: float = None) -> Dict:
        """
        Get valid sampling parameters for Claude 4.5.

        BREAKING CHANGE: Cannot specify both temperature and top_p.
        """
        if temperature is not None and top_p is not None:
            raise ValueError(
                "Claude 4.5 cannot use both temperature and top_p. "
                "Please specify only one."
            )

        params = {}
        if temperature is not None:
            params["temperature"] = temperature
        if top_p is not None:
            params["top_p"] = top_p

        return params

    @staticmethod
    def get_tool_config(tool_type: str) -> Dict[str, str]:
        """
        Get correct tool configuration for Claude 4.5.
        """
        tools = {
            "text_editor": {
                "type": "text_editor_20250728",  # Updated from 20250124
                "name": "str_replace_based_edit_tool",  # Updated from str_replace_editor
            },
            "code_execution": {
                "type": "code_execution_20250825",  # Updated from 20250522
                "name": "code_execution",
            },
            "bash": {
                "type": "bash_20250124",
                "name": "bash",
            },
            "computer": {
                "type": "computer_20250124",
                "name": "computer",
            },
        }
        return tools.get(tool_type, {})


# ============================================================================
# SECTION 6: USAGE EXAMPLES
# ============================================================================

def example_practical_performance():
    """Example: Demonstrating token efficiency."""
    client = anthropic.Anthropic()
    perf = PracticalPerformance(client)

    result = perf.demonstrate_token_efficiency(
        prompt="Write a function to sort a list in Python",
        model="claude-opus-4-5-20251101"
    )

    print(f"Input tokens: {result['input_tokens']}")
    print(f"Output tokens: {result['output_tokens']}")
    print(f"Tips: {result['tips']}")


def example_behavioral_differences():
    """Example: Getting prompt engineering tips."""
    tips = BehavioralDifferences.get_prompt_engineering_tips()

    print("=== Be Explicit ===")
    print(f"Less effective: {tips['be_explicit']['less_effective']}")
    print(f"More effective: {tips['be_explicit']['more_effective']}")

    print("\n=== Opus 4.5 Specific ===")
    opus_tips = BehavioralDifferences.get_opus_45_specific_behaviors()
    for behavior, details in opus_tips.items():
        print(f"\n{behavior}:")
        for key, value in details.items():
            print(f"  {key}: {value}")


def example_enhanced_stop_reasons():
    """Example: Handling enhanced stop reasons."""
    client = anthropic.Anthropic()
    handler = EnhancedStopReasons(client)

    # Get max possible tokens without knowing input size
    result = handler.get_max_possible_tokens(
        prompt="Explain quantum computing in detail",
        model="claude-sonnet-4-5-20250929"
    )

    print(f"Stop reason: {result['stop_reason']}")
    print(f"Status: {result['status']}")
    print(f"Output tokens: {result['output_tokens']}")


def example_complete_workflow():
    """Example: Complete tool workflow with stop reason handling."""
    client = anthropic.Anthropic()
    handler = ResponseHandler(client)

    # Define tools
    tools = [
        {
            "name": "calculator",
            "description": "Performs arithmetic operations",
            "input_schema": {
                "type": "object",
                "properties": {
                    "operation": {"type": "string"},
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["operation", "a", "b"]
            }
        }
    ]

    def execute_tool(name: str, input: Dict) -> str:
        if name == "calculator":
            a, b = input["a"], input["b"]
            ops = {
                "add": a + b,
                "subtract": a - b,
                "multiply": a * b,
                "divide": a / b if b != 0 else "Error: Division by zero"
            }
            return ops.get(input["operation"], "Unknown operation")
        return "Tool not found"

    response = handler.handle_tool_workflow(
        user_query="What is 1234 + 5678?",
        tools=tools,
        execute_tool_fn=execute_tool
    )

    print(f"Final response: {response.content[0].text}")


if __name__ == "__main__":
    print("=" * 60)
    print("Claude 4.5 New Features Update")
    print("=" * 60)

    print("\n1. Behavioral Differences Tips:")
    example_behavioral_differences()

    print("\n" + "=" * 60)
    print("Migration Checklist:")
    print("=" * 60)

    helper = MigrationHelper()
    for path, changes in helper.BREAKING_CHANGES.items():
        print(f"\n{path}:")
        if changes:
            for change in changes:
                print(f"  - {change}")
        else:
            print("  No breaking changes")
