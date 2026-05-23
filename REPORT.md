# Lab 8 Task 1 Report

## Part A: Nanobot setup

I initialized a local `nanobot` project inside the repository and configured it to use the local OpenAI-compatible LLM endpoint at `http://localhost:42005/v1`. The agent was tested from the CLI with a question about the agentic loop. The response showed that the agent could call the configured LLM and produce a normal answer.

## Part B: MCP LMS tools

I installed the local `mcp-lms` package in editable mode and added an `lms` MCP server to `nanobot/config.json`. The server connects to the LMS backend at `http://localhost:42002` using the configured API key.

The agent registered 9 LMS tools:
- health
- labs
- learners
- pass rates
- timeline
- groups
- top learners
- completion rate
- sync pipeline

I verified the tools by asking what labs are available. The agent called the LMS labs tool and returned real lab names from the backend. I also asked whether the LMS backend is healthy, and the agent called the LMS health tool and reported that the backend was healthy.

## Part C: LMS skill

I added `SKILL_LMS.md` with instructions for using LMS tools instead of guessing. The skill tells the agent to use live backend data for labs, scores, pass rates, completion, groups, timelines, and health checks. I referenced this skill from `AGENTS.md`.

## Notes

The OpenAI-compatible endpoint is provided by a local LiteLLM service on port 42005. The LMS backend is available on port 42002. The MCP tools allow the agent to answer LMS questions using real backend data.
