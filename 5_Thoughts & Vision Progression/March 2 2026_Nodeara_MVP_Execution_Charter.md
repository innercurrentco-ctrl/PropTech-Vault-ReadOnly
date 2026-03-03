
# Nodeara – MVP Execution Charter (Final Consolidated Direction)

## Core Decision (Locked In)

We are building the Housing Intent & Creator Monetization Layer first.

Not listings.
Not scheduling.
Not AI offers.
Not tokenization.

Wedge = Creator Monetization + Structured Intent Capture.

---

# Tooling Stack (Final Decision)

Development Environment:
- Cursor IDE (Pro plan sufficient)
- GPT-4 class model (architecture + debugging partner)
- Claude (optional large file review)

Backend:
- NestJS (TypeScript)

Frontend:
- Next.js (TypeScript, mobile-first responsive)

Database:
- PostgreSQL (Docker locally)

Queue / Async:
- Redis + BullMQ

Version Control:
- Git + GitHub

Project Management:
- Linear

Documentation:
- Obsidian (ideas)
- Markdown in repo (technical specs)

---

# Why Cursor (Now)

You are committed to shipping.
You want speed + learning simultaneously.
Cursor gives:
- In-repo AI assistance
- Multi-file awareness
- Cleaner TypeScript workflow

Migration rule:
If you ever feel lost in abstractions → slow down and understand.
Tool does not replace thinking.

---

# Phase Structure

## Phase 1 (Weeks 1–4)
Build Event + Intent Core

- NestJS project scaffold
- PostgreSQL connection
- Event table (append-only)
- POST /events endpoint
- IntentProfile table
- Simple intent rules engine

Success Metric:
Events stored → Intent stage updates reliably.

---

## Phase 2 (Weeks 5–8)
Creator + Campaign Infrastructure

- Creator model
- Campaign model
- Attribution linkage
- Basic creator dashboard (metrics + payout estimate)
- GET /me/recommendations (simple weighted logic)

Success Metric:
Creator sees metrics from real event data.

---

## Phase 3 (Weeks 9–12)
Sponsor Pilot Layer

- Sponsor bundle mapping
- Content tag categorization
- Campaign landing pages (mobile-first)
- Screenshot-worthy dashboard

Success Metric:
1 small sponsor pilot signed.

---

# Development Philosophy

- Modular monolith (no premature microservices)
- Raw events immutable
- Business logic lives in backend
- Frontend is thin
- Rules-first, ML later
- No feature creep

---

# Discipline Rules

- Build boring core first
- No jumping to Phase C/D features
- No rewriting stack every month
- Ship small increments weekly
- Always push to GitHub

---

# What We Are Not Doing (Yet)

- Native 4K video hosting at scale
- AI offer drafting
- Escrow automation
- Tokenization
- Marketplace takeover narrative

We earn the right to expand.

---

# Execution Rhythm

Weekly cadence:
- Build
- Test
- Commit
- Review
- Refactor

Monthly cadence:
- Creator onboarding test
- Data review
- Architecture sanity check

---

# Identity

We are not building a flashy content empire.

We are building infrastructure.

Creators optimize yield.
Sponsors buy structured exposure.
Users generate intent signals.
Nodeara owns coordination.

Quiet execution.
Long horizon.
Serious system.

---

# Final Commitment

Cursor + GPT + NestJS + Next.js + Postgres + Linear + GitHub.

Start Phase 1.
