# project-ideas

A ranked backlog of project ideas to build, ordered by career impact.

![GitHub Repo stars](https://img.shields.io/github/stars/carlosferreyra/project-ideas?style=flat-square)
![Last updated](https://img.shields.io/badge/last%20updated-2026--04--17-blue?style=flat-square)

---

## How to use this list

This doc is auto-updated by a scheduled Claude agent. Ideas are ranked by career signal value — visibility to hiring managers, technical depth, and open-source appeal. Rankings favor Rust/systems work, data engineering angles (Databricks/GCP), and projects that extend the existing [wsr](https://github.com/carlosferreyra/wsr) / [codetwin](https://github.com/carlosferreyra/codetwin) ecosystem. To propose an idea, open an issue.

---

## Ranked Project Ideas

---

## 1. cargo-heatmap

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Rust, cargo, WASM, SVG

**Career signal:** Rust tooling ecosystem contribution — shows deep Cargo internals knowledge and open-source instincts that Big Tech infra teams actively look for.

**Description:** A `cargo` subcommand that profiles build times per crate and renders a browser-based SVG heatmap. Helps teams find slow dependencies at a glance. Fills a real gap in the Cargo ecosystem that developers search for regularly.

**Key features to build:**

- Parse `cargo build --timings` JSON output
- Render interactive SVG/HTML heatmap via a lightweight WASM renderer
- CLI flags: `--open`, `--json`, `--threshold <ms>`

**Estimated effort:** M

**Related existing work:** [wsr](https://github.com/carlosferreyra/wsr) (local CI runner — shares profiling motivation)

**Repo:** `carlosferreyra/cargo-heatmap`

---

## 2. wsr-cloud

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Rust, GCP Cloud Run, Pub/Sub, Terraform

**Career signal:** Extends an existing shipped project with a cloud backend — demonstrates full-cycle ownership from CLI to distributed infra, directly relevant to SRE/platform roles.

**Description:** A cloud companion to [wsr](https://github.com/carlosferreyra/wsr) that streams CI results to a GCP-hosted dashboard in real time. Workers run on Cloud Run, results land in BigQuery, and a simple UI shows run history. Ties directly into GCP Associate Cloud Engineer cert.

**Key features to build:**

- Rust agent that POSTs structured JSON run results to a Cloud Run endpoint
- Pub/Sub fan-out → BigQuery sink via Dataflow template
- Minimal Next.js or static HTML dashboard reading from BigQuery

**Estimated effort:** L

**Related existing work:** [wsr](https://github.com/carlosferreyra/wsr)

**Repo:** `carlosferreyra/wsr-cloud`

---

## 3. mcp-hub-registry

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** TypeScript, Rust (indexer), GitHub Actions, JSON Schema

**Career signal:** AI/MCP tooling is a hot hiring signal in 2025–2026. Maintaining a community registry positions you as an ecosystem contributor before the space matures.

**Description:** A machine-readable registry of MCP servers with a schema validator, auto-discovery via GitHub topic search, and a static site. Extends [mcp-hub](https://github.com/carlosferreyra/mcp-hub) into an authoritative community resource.

**Key features to build:**

- JSON/TOML registry schema with required fields (name, transport, auth, tools)
- GitHub Actions workflow that scrapes `topic:mcp-server` repos nightly and opens PRs for new entries
- Static site (Astro or plain HTML) rendered from the registry

**Estimated effort:** M

**Related existing work:** [mcp-hub](https://github.com/carlosferreyra/mcp-hub)

**Repo:** `carlosferreyra/mcp-hub-registry`

---

## 4. difflog

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Rust, git2-rs, SQLite

**Career signal:** Pure Rust systems project with a daily-use story — exactly the kind of tool that gets GitHub stars organically and shows up in "cool Rust projects" lists.

**Description:** A CLI that records every `git diff` at commit time into a local SQLite database and lets you query your personal change history with ripgrep-style search. Think `git log --all` but for the actual lines you wrote.

**Key features to build:**

- git2-rs hook installer (`post-commit`)
- Incremental diff → SQLite ingestion with FTS5 full-text index
- Query CLI: `difflog search <pattern>`, `difflog stats --week`

**Estimated effort:** M

**Repo:** `carlosferreyra/difflog`

---

## 5. codetwin-lsp

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Rust, LSP (tower-lsp), Claude API

**Career signal:** LSP projects are rare in portfolios and signal deep editor/tooling knowledge. Extending an existing shipped project (codetwin) into the editor layer is a strong narrative arc.

**Description:** A Language Server Protocol implementation for [codetwin](https://github.com/carlosferreyra/codetwin) that surfaces doc suggestions inline as you type. Uses the Claude API with prompt caching to minimize cost on repeated context.

**Key features to build:**

- LSP server skeleton with `textDocument/completion` and `textDocument/hover`
- Codetwin doc generation triggered on function hover
- VS Code extension wrapper for distribution

**Estimated effort:** L

**Related existing work:** [codetwin](https://github.com/carlosferreyra/codetwin)

**Repo:** `carlosferreyra/codetwin-lsp`

---

## 6. delta-doctor

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Python, PySpark, Databricks SDK, Great Expectations

**Career signal:** Directly leverages Databricks Data Engineer Associate cert. Data quality tooling is a top hiring signal for data platform roles at Big Tech.

**Description:** A CLI that runs health checks on Delta Lake tables (schema drift, partition skew, Z-order staleness, vacuum hygiene) and outputs a structured report. Think `cargo check` for Delta tables.

**Key features to build:**

- Databricks SDK–based table inspector (statistics, history, properties)
- Rule engine: configurable checks in TOML
- Output modes: `--json`, `--html`, GitHub Actions summary annotation

**Estimated effort:** M

**Related existing work:** [databricks-certification](https://github.com/carlosferreyra/databricks-certification), [data-engineering](https://github.com/carlosferreyra/data-engineering)

**Repo:** `carlosferreyra/delta-doctor`

---

## 7. interview-ready-cli

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Rust, Claude API, SQLite

**Career signal:** Meta/Google interviewers value candidates who build their own prep tooling — it shows initiative and shipping instinct. Public repo gets organic traffic from job seekers.

**Description:** A TUI-based coding interview trainer that pulls problems from a local SQLite bank, times your solution, and uses Claude to critique it with a "would this pass FAANG review?" rubric. Extends [interview-ready](https://github.com/carlosferreyra/interview-ready) from a notes repo into an interactive tool.

**Key features to build:**

- Problem bank TOML schema + seed data (LC-style problems with tags)
- Ratatui TUI: problem display, timer, code editor pane
- Claude API call on submit → structured feedback (correctness, time complexity, style)

**Estimated effort:** L

**Related existing work:** [interview-ready](https://github.com/carlosferreyra/interview-ready)

**Repo:** `carlosferreyra/interview-ready-cli`

---

## 8. llm-prices

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** TypeScript, GitHub Actions, JSON

**Career signal:** High organic search traffic ("LLM pricing comparison"), low build effort, and demonstrates awareness of the AI ecosystem — good conversation starter in interviews.

**Description:** A tiny GitHub repo that maintains a machine-readable JSON/YAML file of LLM model pricing (input/output tokens, context window, rate limits) updated weekly by a GitHub Actions scraper. Companion to [llm-knowledge-cutoff-dates](https://github.com/carlosferreyra/llm-knowledge-cutoff-dates).

**Key features to build:**

- Schema: provider → model → {input_price, output_price, context_window, updated_at}
- GitHub Actions scraper that opens a PR when prices change
- Rendered comparison table in README via a generation script

**Estimated effort:** S

**Related existing work:** [llm-knowledge-cutoff-dates](https://github.com/carlosferreyra/llm-knowledge-cutoff-dates)

**Repo:** `carlosferreyra/llm-prices`

---

## 9. pipewatch

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Rust, tokio, WebSocket, htmx

**Career signal:** Real-time systems + Rust async is a rare combo in portfolios. Demonstrates tokio proficiency and full-stack thinking without heavy frontend overhead.

**Description:** A lightweight process monitor that tails stdout/stderr of any shell pipeline and streams it live to a browser via WebSocket. Like `tail -f` with a browser UI and structured log filtering.

**Key features to build:**

- Rust binary that spawns a child process and captures its streams
- WebSocket server (tokio-tungstenite) broadcasting structured log lines
- Single-file htmx frontend with filter/search and ANSI color support

**Estimated effort:** M

**Repo:** `carlosferreyra/pipewatch`

---

## 10. awesome-uvx

**Status:** ~~idea~~ [`in-progress`](https://github.com/carlosferreyra/awesome-uvx) ~~done~~

**Stack:** Python, uv, Markdown, GitHub Actions

**Career signal:** Being the go-to curator for a fast-growing tool (uv) builds mindshare before the ecosystem saturates. Awesome lists consistently rank well in search.

**Description:** A curated list of tools and recipes for running Python scripts via `uvx` without a virtualenv. Already started — needs regular updates, a contribution guide, and a CI badge checker.

**Key features to build:**

- CI link checker (GitHub Actions)
- Category taxonomy: dev tools, data science, AI/LLM, system utilities
- Weekly auto-PR from a scraper of `uv`-compatible PyPI packages

**Estimated effort:** S

**Related existing work:** [awesome-uvx](https://github.com/carlosferreyra/awesome-uvx)

**Repo:** `carlosferreyra/awesome-uvx`

---

## 11. marimo-hub

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Python, marimo, Databricks, GitHub Actions

**Career signal:** Marimo is gaining traction fast. Being an early ecosystem contributor (notebook gallery, component library) creates durable visibility.

**Description:** A gallery of reusable marimo notebook templates for common data engineering patterns (ingestion, EDA, Delta Lake ops, ML feature pipelines). Each template is a runnable `.py` file with parameterized inputs.

**Key features to build:**

- Template schema: metadata frontmatter (tags, stack, runtime requirements)
- GitHub Actions CI that runs each template against a mock dataset
- Static gallery site rendered from template metadata

**Estimated effort:** M

**Related existing work:** [marimo-notebooks](https://github.com/carlosferreyra/marimo-notebooks)

**Repo:** `carlosferreyra/marimo-hub`

---

## 12. gcp-cost-sentinel

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Python, GCP Billing API, Cloud Functions, Telegram/Slack webhook

**Career signal:** FinOps awareness is a growing hiring criterion at Big Tech cloud teams. A working GCP cost alerting tool directly demonstrates GCP cert knowledge in practice.

**Description:** A serverless GCP Cloud Function that polls the Billing API daily, computes per-service spend deltas, and fires a Telegram or Slack alert when any service exceeds a configurable threshold. Lightweight alternative to GCP Budget Alerts for fine-grained control.

**Key features to build:**

- Cloud Function triggered by Cloud Scheduler (daily)
- Billing API client: fetch yesterday's spend by service
- Alert logic: configurable thresholds per service in TOML/env

**Estimated effort:** S

**Repo:** `carlosferreyra/gcp-cost-sentinel`

---

## 13. dotfiles-bootstrap

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Rust, shell, GitHub Actions

**Career signal:** A one-command dotfiles installer in Rust (not a bash script) is a strong flex — it's battle-tested, cross-platform, and demonstrates practical Rust beyond toy projects.

**Description:** A Rust binary that clones [dotfiles](https://github.com/carlosferreyra/dotfiles), resolves symlinks, installs packages via the system package manager, and sets up shell configs idempotently. Think `chezmoi` but hand-rolled and minimal.

**Key features to build:**

- TOML manifest: packages, symlinks, post-install hooks
- Idempotent installer with diff output (what changed vs. already installed)
- GitHub Actions test matrix: macOS, Ubuntu

**Estimated effort:** M

**Related existing work:** [dotfiles](https://github.com/carlosferreyra/dotfiles)

**Repo:** `carlosferreyra/dotfiles-bootstrap`

---

## 14. schema-drift-detector

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Python, Pydantic, Kafka (or Pub/Sub), Delta Lake

**Career signal:** Schema evolution is a senior data engineer topic. A working tool here signals production readiness beyond tutorials.

**Description:** A lightweight daemon that subscribes to a Kafka or Pub/Sub topic, infers the JSON schema of incoming messages, and alerts when the schema diverges from a registered baseline. Stores schema history in Delta Lake.

**Key features to build:**

- Pydantic-based schema inference from sampled messages
- Schema diff engine: added/removed/type-changed fields
- Alert sink: structured log, Slack webhook, or GCS file

**Estimated effort:** L

**Related existing work:** [data-engineering](https://github.com/carlosferreyra/data-engineering)

**Repo:** `carlosferreyra/schema-drift-detector`

---

## 15. vicode-plugins

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** TypeScript, VS Code API, Rust (optional native module)

**Career signal:** VS Code extension authorship is a niche skill that stands out. Extending an existing project (vicode) shows continuity of ownership.

**Description:** A plugin system for [vicode](https://github.com/carlosferreyra/vicode) that lets users define custom code transformation pipelines triggered by keybindings. Each plugin is a small JS/TS module with a defined input/output contract.

**Key features to build:**

- Plugin manifest schema + loader
- Built-in plugins: sort imports, extract variable, wrap in try/catch
- Plugin marketplace integration (VS Code extension gallery)

**Estimated effort:** M

**Related existing work:** [vicode](https://github.com/carlosferreyra/vicode)

**Repo:** `carlosferreyra/vicode-plugins`

---

## 16. bench-rs

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Rust, criterion, GitHub Actions, SVG chart

**Career signal:** Benchmarking infrastructure is critical at Big Tech. A clean benchmark harness with CI-tracked regressions is the kind of thing infra interviewers notice.

**Description:** A reusable benchmark harness template for Rust projects that tracks performance regressions across commits using criterion and renders per-benchmark trend charts in GitHub Actions PR summaries.

**Key features to build:**

- Criterion benchmark template with configurable sample sizes
- GitHub Actions workflow: run benches on PR, compare to `main`, post summary
- SVG trend chart generated from stored JSON results

**Estimated effort:** S

**Repo:** `carlosferreyra/bench-rs`

---

## Idea Graveyard

Ideas considered but deprioritized:

| Idea | Reason deprioritized |
| --- | --- |
| **Rust async runtime from scratch** | High learning value but near-zero open-source appeal; covered better by tokio docs. |
| **Personal finance tracker** | Saturated market; no Rust/data engineering angle that adds differentiation. |
| **LLM fine-tuning pipeline** | Requires GPU budget not practical without company resources; poor ROI for portfolio. |
| **Browser extension for job tracking** | TypeScript-only, no systems angle; dozens of identical tools already exist. |
| **Custom Neovim distro** | Dotfiles ecosystem overlap with no career signal beyond personal preference. |

---

## Resources

**Inspiration & signal:**

- [Awesome Rust](https://github.com/rust-unofficial/awesome-rust) — gaps in this list = open opportunities
- [Rust CLI Working Group](https://github.com/rust-cli/team) — community context for CLI tooling
- [levels.fyi open roles](https://www.levels.fyi/jobs) — filter by "infrastructure" / "data platform" for signal on what skills are valued
- [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/) — Big Tech hiring trends
- [Data Engineering Weekly](https://www.dataengineeringweekly.com/) — data platform tooling landscape
- [Hacker News "Show HN"](https://news.ycombinator.com/show) — calibrate what resonates with technical audiences
- [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) — gap analysis for self-hostable tooling ideas

