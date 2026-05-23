# Lab 8 Task 1 Report

## Task 1A — Bare agent

Command:

```bash
cd ~/se-toolkit-lab-8/nanobot
uv run nanobot agent --logs --session cli:task1a-loop -c ./config.json -m "What is the agentic loop?"

Actual response copied from terminal:

The agentic loop is the fundamental cycle that AI agents follow to perceive, reason, act, and learn. It is the core pattern that enables autonomous behavior.

The basic loop is:

Observe → Reason → Act → Reflect → repeat

Observe: gather input from the environment.
Reason: analyze the situation and plan next steps.
Act: execute the chosen action.
Reflect: evaluate the outcome and continue the loop.

This confirmed that the bare nanobot agent can call the configured LLM endpoint.

Task 1B — Agent with LMS tools

Command:

cd ~/se-toolkit-lab-8/nanobot
uv run nanobot agent --logs --session cli:task1b-labs -c ./config.json -m "What labs are available?"

Actual response copied from terminal:

The following labs are available:

Lab 01 – Products, Architecture & Roles
Lab 02 — Run, Fix, and Deploy a Backend Service
Lab 03 — Backend API: Explore, Debug, Implement, Deploy
Lab 04 — Testing, Front-end, and AI Agents
Lab 05 — Data Pipeline and Analytics Dashboard
Lab 06 — Build Your Own Agent
Lab 07 — Build a Client with an AI Coding Agent
lab-08

Tool evidence copied from terminal logs:

MCP server 'lms': connected, 9 tools registered.
Tool call: mcp_lms_lms_labs({})

Health check response copied from terminal:

The LMS backend is healthy and has 56 items.

Task 1C — Skill prompt

I created the LMS skill prompt at:

nanobot/workspace/skills/lms/SKILL.md

The skill instructs the agent to use LMS MCP tools instead of guessing when the user asks about labs, tasks, learners, scores, pass rates, completion rates, groups, timelines, or backend health.

The skill strategy is:

Use mcp_lms_lms_health for backend health.
Use mcp_lms_lms_labs for lab lists.
Use mcp_lms_lms_pass_rates for per-task pass rates.
Use mcp_lms_lms_completion_rate for completion rate questions.
Use mcp_lms_lms_groups for group comparisons.
Use mcp_lms_lms_top_learners for top learner questions.
Use mcp_lms_lms_timeline for timeline questions.
Use mcp_lms_lms_sync_pipeline only when the user asks to refresh data.

This completed the skill prompt requirement for Task 1.
