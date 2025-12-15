# Claude 4.5 New Features Update - December 2025

## Table of Contents
1. [Practical Performance](#1-practical-performance)
2. [Behavioral Differences](#2-behavioral-differences)
3. [Enhanced Stop Reasons](#3-enhanced-stop-reasons)
4. [Migration Checklist](#4-migration-checklist)
5. [Quick Reference](#5-quick-reference)

---

## 1. Practical Performance

### 1.1 Token Efficiency

Claude 4.5 models achieve **significantly better token efficiency** compared to previous generations:

| Metric | Opus 4.5 | Sonnet 4.5 | Haiku 4.5 |
|--------|----------|------------|-----------|
| Token Reduction | Up to **65% fewer tokens** | Optimized | Most efficient |
| Tool Error Reduction | **50-75%** | Improved | Fast execution |
| Autonomous Focus | **30+ hours** | **30+ hours** | Real-time |

#### Key Performance Metrics

**Claude Opus 4.5:**
- SWE-bench Verified: **80.9%** (Industry-leading)
- OSWorld (Computer Use): **66.3%** (Best in class)
- Achieves higher pass rates while using **up to 65% fewer tokens**
- **50-75% reduction** in tool calling and build/lint errors
- Fewer iterations needed to complete complex tasks

**Claude Sonnet 4.5:**
- SWE-bench Verified: **State-of-the-art**
- OSWorld: **61.4%** (vs 42.2% for Sonnet 4)
- Planning performance: **+18%** improvement
- End-to-end eval scores: **+12%** improvement
- Can maintain focus for **30+ hours** on complex tasks

**Claude Haiku 4.5:**
- Near-frontier performance matching Sonnet 4
- Fastest response times in Claude family
- Max output tokens: **64,000** (increased from 8K)
- Pricing: **$1/$5 per million tokens**

### 1.2 Practical Benefits

```python
# Token efficiency in practice
# Opus 4.5 requires fewer steps to solve tasks
# and uses fewer tokens as a result

response = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=4096,
    messages=[{"role": "user", "content": prompt}]
)

# Built-in token-efficient tool use (no beta header needed)
# Claude 4 models have this built-in
```

---

## 2. Behavioral Differences

### 2.1 Communication Style Changes

Claude 4.5 models have a **refined communication approach**:

| Aspect | Previous Models | Claude 4.5 |
|--------|-----------------|------------|
| Style | Verbose | **Concise & Direct** |
| Updates | Detailed summaries | **Fact-based progress** |
| Tool summaries | Always provided | **May skip (use prompting)** |
| "Above and beyond" | Automatic | **Requires explicit request** |

### 2.2 Prompt Engineering Best Practices

#### Be Explicit with Instructions

Claude 4.5 models respond well to **clear, explicit instructions**:

**Less Effective:**
```
Create an analytics dashboard
```

**More Effective:**
```
Create an analytics dashboard. Include as many relevant features
and interactions as possible. Go beyond the basics to create
a fully-featured implementation.
```

#### Add Context for Better Results

**Less Effective:**
```
NEVER use ellipses
```

**More Effective:**
```
Your response will be read aloud by a text-to-speech engine,
so never use ellipses since the text-to-speech engine will
not know how to pronounce them.
```

#### Control Output Format

Three effective methods:
1. **Describe in natural language** what format you want
2. **Use XML tags** to structure output
3. **Match your prompt style** to desired output style

> **Tip:** Removing markdown from your prompt can reduce markdown in the output

#### Prevent Test Gaming

When Claude might hard-code solutions to pass tests:

```
Please write a high quality, general purpose solution.
Implement a solution that works correctly for all valid inputs,
not just the test cases.
Do not hard-code values or create solutions that only work
for specific test inputs.
Instead, implement the actual logic that solves the problem generally.
```

### 2.3 Opus 4.5 Specific Behaviors

| Issue | Cause | Fix |
|-------|-------|-----|
| Tools called too frequently | High system prompt sensitivity | Reduce aggressive language |
| Excessive abstraction | Eager implementation | Add specific constraints |
| Proposes without reading | Conservative exploration | Instruct to inspect code first |
| Generic-looking outputs | Default styling | Add frontend aesthetics snippet |
| "Think" word sensitivity | Extended thinking disabled | Avoid 'think' variants in prompts |

### 2.4 Alignment Improvements

Claude 4.5 is the **most aligned frontier model** with reduced:
- Sycophancy
- Deception
- Power-seeking
- Delusional thinking encouragement
- Prompt injection vulnerability

---

## 3. Enhanced Stop Reasons

### 3.1 All Stop Reason Values

| Stop Reason | Description | Action |
|-------------|-------------|--------|
| `end_turn` | Natural completion | Process response |
| `max_tokens` | Hit max_tokens limit | Continue generation |
| `model_context_window_exceeded` | **NEW** - Hit context limit | Handle context limit |
| `stop_sequence` | Hit custom stop sequence | Process partial |
| `tool_use` | Tool call requested | Execute tool |
| `pause_turn` | Server tool paused | Continue conversation |
| `refusal` | Safety refusal | Modify request |

### 3.2 New: model_context_window_exceeded

**Available by default in Sonnet 4.5 and newer models.**

For older models, use beta header: `model-context-window-exceeded-2025-08-26`

This enables requesting maximum tokens **without knowing input size**:

```python
# Get maximum possible output without calculating input size
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=64000,  # Set to model's maximum
    messages=[{"role": "user", "content": large_prompt}]
)

if response.stop_reason == "model_context_window_exceeded":
    # Got maximum possible given input size
    print(f"Generated {response.usage.output_tokens} tokens (context limit)")
elif response.stop_reason == "max_tokens":
    # Hit the requested max_tokens limit
    print(f"Generated {response.usage.output_tokens} tokens (max_tokens)")
else:
    # Natural completion
    print(f"Generated {response.usage.output_tokens} tokens (complete)")
```

### 3.3 Handling Truncated Responses

```python
def handle_truncated_response(response):
    if response.stop_reason in ["max_tokens", "model_context_window_exceeded"]:
        # Warn user about specific limit
        if response.stop_reason == "max_tokens":
            message = "[Response truncated due to max_tokens limit]"
        else:
            message = "[Response truncated due to context window limit]"

        return f"{response.content[0].text}\n\n{message}"

    return response.content[0].text
```

### 3.4 Handling pause_turn (Server Tools)

```python
def handle_paused_conversation(initial_response, max_retries=3):
    response = initial_response
    messages = [{"role": "user", "content": original_query}]

    for attempt in range(max_retries):
        if response.stop_reason != "pause_turn":
            break

        messages.append({"role": "assistant", "content": response.content})

        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            messages=messages,
            tools=original_tools
        )

    return response
```

### 3.5 Handling Empty Responses

Sometimes Claude returns empty responses with `end_turn`. Common causes:

**BAD Practice - Adding text after tool_result:**
```python
# DON'T DO THIS
messages = [
    {"role": "user", "content": [
        {"type": "tool_result", "tool_use_id": "123", "content": "result"},
        {"type": "text", "text": "Here's the result"}  # BAD!
    ]}
]
```

**GOOD Practice - Send tool results directly:**
```python
# DO THIS INSTEAD
messages = [
    {"role": "user", "content": [
        {"type": "tool_result", "tool_use_id": "123", "content": "result"}
    ]}  # Just the tool_result, no additional text
]
```

### 3.6 Handling Refusals

```python
if response.stop_reason == "refusal":
    # Claude declined due to safety concerns
    # Tip: Try Sonnet 4 for different restrictions
    print("Consider using claude-sonnet-4-20250514")
    # See: https://support.claude.com/en/articles/12449294
```

---

## 4. Migration Checklist

### 4.1 Sonnet 3.7 to Sonnet 4.5

```python
# Model string update
model = "claude-sonnet-4-5-20250929"  # was: claude-3-7-sonnet-20250219
```

**Breaking Changes:**
- [ ] Cannot use both `temperature` AND `top_p`
- [ ] Handle `refusal` stop_reason
- [ ] Update text editor: `text_editor_20250728` / `str_replace_based_edit_tool`
- [ ] Remove `undo_edit` command
- [ ] Remove `token-efficient-tools-2025-02-19` header
- [ ] Remove `output-128k-2025-02-19` header

**Recommendations:**
- [ ] Consider enabling extended thinking for complex tasks
- [ ] Handle `model_context_window_exceeded` stop reason
- [ ] Review prompts per Claude 4 best practices

### 4.2 Haiku 3.5 to Haiku 4.5

```python
# Model string update
model = "claude-haiku-4-5-20251001"  # was: claude-3-5-haiku-20241022
```

**Breaking Changes:**
- [ ] Cannot use both `temperature` AND `top_p`
- [ ] Only latest tool versions supported
- [ ] Handle `refusal` stop_reason
- [ ] New rate limits (separate from Haiku 3.5)

**New Capabilities:**
- [ ] Extended thinking support
- [ ] Context awareness
- [ ] 64K max output tokens (was 8K)

### 4.3 Opus 4.1 to Opus 4.5

```python
# Model string update
model = "claude-opus-4-5-20251101"  # was: claude-opus-4-1-20250805
```

**No breaking changes** - All API calls work without modification.

---

## 5. Quick Reference

### 5.1 Model Strings

| Model | Model String |
|-------|--------------|
| Opus 4.5 | `claude-opus-4-5-20251101` |
| Sonnet 4.5 | `claude-sonnet-4-5-20250929` |
| Haiku 4.5 | `claude-haiku-4-5-20251001` |
| Sonnet 4 | `claude-sonnet-4-20250514` |

### 5.2 Tool Versions (Claude 4.5)

| Tool | Type | Name |
|------|------|------|
| Text Editor | `text_editor_20250728` | `str_replace_based_edit_tool` |
| Code Execution | `code_execution_20250825` | `code_execution` |
| Bash | `bash_20250124` | `bash` |
| Computer | `computer_20250124` | `computer` |

### 5.3 Sampling Parameters

```python
# CORRECT - Use one or the other
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    temperature=0.7,  # OR top_p, NOT both
    messages=[...]
)

# WRONG - Will error in Claude 4.5
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    temperature=0.7,
    top_p=0.9,  # Cannot use both!
    messages=[...]
)
```

### 5.4 Removed Features

Features no longer supported in Claude 4.5:
- `token-efficient-tools-2025-02-19` (built-in now)
- `output-128k-2025-02-19` (only Sonnet 3.7)
- `undo_edit` command in text editor

---

## Official Documentation Links

- [What's New in Claude 4.5](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-5)
- [Migrating to Claude 4.5](https://platform.claude.com/docs/en/about-claude/models/migrating-to-claude-4)
- [Handling Stop Reasons](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)
- [Claude 4 Best Practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices)
- [Understanding Sonnet 4.5 Safety Filters](https://support.claude.com/en/articles/12449294)

---

*Document generated: December 2025*
*Based on official Anthropic documentation*
