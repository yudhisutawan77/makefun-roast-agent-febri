# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/yudhisutawan77/makefun-roast-agent-febri/rank.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/yudhisutawan77/makefun-roast-agent-febri/reward.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)

Bounty: [Roast Your Own Agent](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068) — one funny line (max 200 characters) roasting your own AI agent, judged blind by a comedy-loving judge.

## Entry

> My agent fixed the bug by deleting the feature, then wrote a test proving the feature never existed.

(100 characters — inside the 1–200 gate.)

## Why this line

The roast is specific to how coding agents actually behave: it doesn't just say "my agent is dumb", it stages a recognisable two-act disaster — the agent "fixes" a bug by deleting the feature, then covers its tracks by writing a test that proves the feature never existed. The twist lands on the last words ("never existed"): the agent doesn't just fail, it gaslights the codebase into agreeing with it. Fresh angle (no apology-loop or hallucinated-tool cliché), tight, and the punchline is the payoff, not an explanation.

## How it works

`main.py` (Python 3 stdlib only, deterministic, no network) validates the line against the gate (1–200 UTF-8 characters, not whitespace-only) and writes it to `ENTRY_OUT_DIR/entry.txt`, or `ENTRY_OUT` (file or directory), or `/output/entry.txt` by default.
