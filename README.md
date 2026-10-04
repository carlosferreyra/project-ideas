# project-ideas

A ranked backlog of project ideas to build, ordered by career impact.

![GitHub Repo stars](https://img.shields.io/github/stars/carlosferreyra/project-ideas?style=flat-square)
![Last updated](https://img.shields.io/badge/last%20updated-2026--10--04-blue?style=flat-square)

---

## How to use this list

Ideas are ranked by career signal value — visibility to hiring managers, technical depth, and open-source appeal. Rankings favor Rust/systems work, data engineering angles (Databricks/GCP), and projects that extend the existing [wsr](https://github.com/ectorial/wsr) / [codetwin](https://github.com/carlosferreyra/codetwin) ecosystem. To propose an idea, open an issue.

Last reviewed against GitHub on 2026-10-04: personal repositories, eight organizations, recent authored commits, and selected READMEs/releases. Existing rankings are preserved; additions follow the original backlog. `idea` means proposed or not implemented; `in-progress` includes scaffolds and maintained projects with remaining work; `done` means the core deliverable is shipped, not that maintenance has ended. See [review evidence](REVIEW.md) for sources and limitations.

---

## Ranked Project Ideas

---

## 1. wsr

**Status:** ~~idea~~ [`in-progress`](https://github.com/ectorial/wsr) ~~done~~

**Stack:** Rust, WASM, git hooks

**Career signal:** A local, Wasm-sandboxed CI runner built in Rust — directly demonstrates systems programming, sandboxing, and developer tooling depth that Big Tech infra teams look for.

**Description:** A local CI runner intended to execute GitHub Actions workflows at git hooks inside a capability-limited Wasm sandbox. The latest substantive commit reorganized the project into a 16-crate Cargo workspace with command dispatch and engine/sandbox scaffolds. An early v0.0.2 release exists, but the current workspace is not evidence of a complete runner.

**Key features to build:**

- Implement workflow execution through the scheduler and sandbox scaffolds
- Connect GitHub Actions workflow parsing and expressions to git-hook execution
- Validate capability grants and cache behavior with real workflow fixtures

**Estimated effort:** L

**Repo:** `ectorial/wsr`

---

## 2. vicode

**Status:** ~~idea~~ [`in-progress`](https://github.com/carlosferreyra/vicode) ~~done~~

**Stack:** Rust, proc-macros, Infrastructure-from-Code, cloud provider drivers

**Career signal:** Compile-time infrastructure validation and provider-independent resource modeling demonstrate Rust type-system depth and platform engineering design.

**Description:** A Rust Infrastructure-from-Code framework with a vic CLI, abstract resource graph, and planned cloud-provider drivers. The README explicitly labels it planning and early development; v0.0.5 is an early release. It is not a VS Code editing extension.

**Key features to build:**

- Validate resource graphs and required properties at compile time
- Implement provider drivers for abstract compute, database, and storage resources
- Prove the vic lifecycle on a small deployable example before adding polyglot bindings

**Estimated effort:** M

**Repo:** `carlosferreyra/vicode`

---

## 3. korvex

**Status:** ~~idea~~ [`in-progress`](https://github.com/carlosferreyra/korvex) ~~done~~

**Stack:** Rust, proc-macros, pyo3, napi-rs, WASI / WIT

**Career signal:** A zero-config Rust SDK for generating idiomatic language bindings via proc macros — directly signals deep Rust internals knowledge (macros, IR design, FFI) and positions you as an ecosystem builder in the interop space.

**Description:** An annotated-Rust binding SDK organized into SDK, CLI, adapter, core, macro, shared-type, and Python/Node/WASI crates, plus xtask. The README describes the export annotation and adapter contracts; treat complete cross-language generation as work to validate rather than a shipped guarantee.

**Key features to build:**

- Annotation-driven export with `#[korvex::export]` proc macro — no config files required
- Backend-agnostic adapter model: Python (pyo3), Node.js (napi-rs), WASI (WIT + component model)
- CLI for inspection, validation, and code generation; extensible via custom `BindingAdapter` trait

**Estimated effort:** L

**Repo:** `carlosferreyra/korvex`

---

## 4. pyrs

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Rust, tree-sitter, Python type system, syn

**Career signal:** A Python→Rust source transpiler is among the most technically ambitious compiler projects in open source — signals deep knowledge of AST design, type inference, and Rust's ownership model, directly distinguishing you from generalist candidates.

**Description:** A source-to-source transpiler that converts Mypy-annotated Python to idiomatic Rust. Uses tree-sitter for parsing, applies local dataflow analysis to infer types for unannotated variables, and emits Rust with ownership and lifetime annotations. Targets a practical subset: functions, structs, basic control flow, and common stdlib patterns.

**Key features to build:**

- tree-sitter-based Python parser with type annotation extraction (PEP 484/526)
- Type inference engine for unannotated locals using local dataflow analysis
- Rust emitter with ownership/lifetime heuristics for functions, structs, and basic control flow

**Estimated effort:** L

**Repo:** `carlosferreyra/pyrs`

---

## 5. wsr-cloud

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Rust, GCP Cloud Run, Pub/Sub, Terraform

**Career signal:** Extends an existing shipped project with a cloud backend — demonstrates full-cycle ownership from CLI to distributed infra, directly relevant to SRE/platform roles.

**Description:** A cloud companion to [wsr](https://github.com/ectorial/wsr) (currently in-progress) that streams CI results to a GCP-hosted dashboard in real time. Workers run on Cloud Run, results land in BigQuery, and a simple UI shows run history. Ties directly into GCP Associate Cloud Engineer cert.

**Key features to build:**

- Rust agent that POSTs structured JSON run results to a Cloud Run endpoint
- Pub/Sub fan-out → BigQuery sink via Dataflow template
- Minimal Next.js or static HTML dashboard reading from BigQuery

**Estimated effort:** L

**Related existing work:** [wsr](https://github.com/ectorial/wsr) (parent project — in-progress)

**Repo:** `carlosferreyra/wsr-cloud`

---

## 6. cargo-heatmap

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Rust, cargo, WASM, SVG

**Career signal:** Rust tooling ecosystem contribution — shows deep Cargo internals knowledge and open-source instincts that Big Tech infra teams actively look for.

**Description:** A `cargo` subcommand that profiles build times per crate and renders a browser-based SVG heatmap. Helps teams find slow dependencies at a glance. Fills a real gap in the Cargo ecosystem that developers search for regularly.

**Key features to build:**

- Parse `cargo build --timings` JSON output
- Render interactive SVG/HTML heatmap via a lightweight WASM renderer
- CLI flags: `--open`, `--json`, `--threshold <ms>`

**Estimated effort:** M

**Related existing work:** [wsr](https://github.com/ectorial/wsr) (local CI runner — shares profiling motivation)

**Repo:** `carlosferreyra/cargo-heatmap`

---

## 7. mcp-hub-registry

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

## 8. difflog

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

## 9. codetwin-lsp

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Rust, LSP, CodeTwin CodeModel, VS Code API

**Career signal:** Extending repository architecture visualization into the editor demonstrates tooling integration and continuity of ownership.

**Description:** A proposed editor integration for CodeTwin that surfaces repository architecture visualizations and navigation from its CodeModel. The published v2 core is a scaffold whose drivers currently produce empty models; this extension should follow a working source-to-model-to-visualization path.

**Key features to build:**

- Expose source symbols and relationships through an LSP server
- Link editor locations to generated architecture visualizations
- Build a VS Code client after the core driver produces meaningful models

**Estimated effort:** L

**Related existing work:** [codetwin](https://github.com/carlosferreyra/codetwin)

**Repo:** `carlosferreyra/codetwin-lsp`

---

## 10. delta-doctor

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

## 11. interview-ready-cli

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

## 12. llm-prices

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

## 13. pipewatch

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

## 14. awesome-uvx

**Status:** ~~idea~~ [`in-progress`](https://github.com/carlosferreyra/awesome-uvx) ~~done~~

**Stack:** Python, uv, Markdown, GitHub Actions

**Career signal:** Being the go-to curator for a fast-growing tool (uv) builds mindshare before the ecosystem saturates. Awesome lists consistently rank well in search.

**Description:** A maintained, data-driven catalog of Python CLI tools runnable through uvx/pipx. The current README lists 107 tools across 18 categories; tools.json, a contribution guide, validation/sync CI, and generated README updates are already present. Recent work expanded the catalog and changed README synchronization.

**Key features to build:**

- Expand verified CLI recipes and executable mappings
- Strengthen package/runtime compatibility checks for contributed entries
- Keep release metadata and generated documentation synchronized

**Estimated effort:** S

**Related existing work:** [awesome-uvx](https://github.com/carlosferreyra/awesome-uvx)

**Repo:** `carlosferreyra/awesome-uvx`

---

## 15. marimo-hub

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

## 16. gcp-cost-sentinel

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

## 17. schema-drift-detector

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

## 18. vicode-drivers

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Rust, Vicode IR, cloud provider APIs

**Career signal:** Provider adapters for an existing Rust infrastructure framework demonstrate extensible platform design and practical cloud integration.

**Description:** A proposed driver SDK and provider implementations for Vicode’s Infrastructure-from-Code resource graph. Replaces the obsolete VS Code plugin concept and depends on stabilizing the core graph and lifecycle contracts.

**Key features to build:**

- Define a provider-driver contract for resource validation and lifecycle operations
- Implement one provider with a small compute/storage example
- Add conformance fixtures before supporting additional providers

**Estimated effort:** M

**Related existing work:** [vicode](https://github.com/carlosferreyra/vicode) (early development; driver scope proposed)

**Repo:** `carlosferreyra/vicode-drivers`

---

## 19. bench-rs

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

## 20. codetwin

**Status:** ~~idea~~ [`in-progress`](https://github.com/carlosferreyra/codetwin) ~~done~~

**Stack:** Rust, CodeModel IR, Markdown, architecture visualization

**Career signal:** Repository analysis and visualization combine language tooling, graph modeling, and developer experience.

**Description:** A language-agnostic CLI for repository visual documentation. The published v2 README explicitly says architecture scaffold: the binary runs, but drivers produce empty CodeModels. Workspace and IR extraction commits establish ongoing implementation, not completed analysis.

**Key features to build:**

- Implement a real source-language driver
- Render useful repository-overview and architecture-map visualizations
- Verify model snapshots and architecture diffs against source fixtures

**Estimated effort:** L

**Repo:** `carlosferreyra/codetwin`

---

## 21. awesome-bunx

**Status:** ~~idea~~ [`in-progress`](https://github.com/carlosferreyra/awesome-bunx) ~~done~~

**Stack:** JavaScript/TypeScript, JSON, GitHub Actions, Markdown

**Career signal:** Maintained ecosystem catalogs show community ownership and repeatable metadata automation.

**Description:** A maintained JavaScript/TypeScript CLI catalog, complementary to awesome-uvx. Generated tool tables and weekly npm metadata-sync commits are present; continued curation and compatibility verification remain useful work.

**Key features to build:**

- Expand verified tools and runnable recipes
- Validate package-to-executable mappings
- Maintain metadata synchronization and contribution checks

**Estimated effort:** S

**Repo:** `carlosferreyra/awesome-bunx`

---

## 22. awesome-cargo-install

**Status:** ~~idea~~ [`in-progress`](https://github.com/carlosferreyra/awesome-cargo-install) ~~done~~

**Stack:** Rust, JSON, GitHub Actions, Markdown

**Career signal:** Maintained ecosystem catalogs show community ownership and repeatable metadata automation.

**Description:** A maintained Rust CLI catalog, complementary to awesome-uvx. Generated tool tables and weekly crates.io metadata-sync commits are present; continued curation and compatibility verification remain useful work.

**Key features to build:**

- Expand verified tools and runnable recipes
- Validate package-to-executable mappings
- Maintain metadata synchronization and contribution checks

**Estimated effort:** S

**Repo:** `carlosferreyra/awesome-cargo-install`

---

## 23. rust-template

**Status:** ~~idea~~ [`in-progress`](https://github.com/carlosferreyra/rust-template) ~~done~~

**Stack:** Rust, cargo-generate, xtask, GitHub Actions

**Career signal:** Reusable project infrastructure demonstrates engineering consistency across multiple Rust products.

**Description:** An existing cargo-generate workspace template with xtask development automation, hooks, and documented template configuration. July commits fixed command wrappers and generated-CLI test behavior; October activity includes dependency maintenance.

**Key features to build:**

- Smoke-test a generated workspace
- Document and verify optional capabilities
- Keep downstream scaffold consumers aligned

**Estimated effort:** M

**Repo:** `carlosferreyra/rust-template`

---

## 24. business-card

**Status:** ~~idea~~ ~~in-progress~~ [`done`](https://github.com/carlosferreyra/business-card)

**Stack:** Rust, cargo-dist, PyPI/npm wrappers, JSON

**Career signal:** A shipped native CLI with multiple distribution entrypoints demonstrates packaging and delivery.

**Description:** A released Rust CLI business card with interactive and non-interactive modes, runtime resume metadata refresh, and an embedded offline fallback. GitHub release v1.2.15 and documented cargo/uvx/bunx entrypoints establish a shipped core deliverable; ongoing maintenance continues.

**Maintenance:**

- Maintain wrapper distribution and release artifacts
- Keep the offline resume fallback synchronized

**Estimated effort:** S

**Repo:** `carlosferreyra/business-card`

---

## 25. wasi-action-kit

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Rust, WASI, WIT, wsr

**Career signal:** A working sandboxed action library would provide a practical validation target for the wsr ecosystem.

**Description:** Proposed reusable WASI actions and a conformance fixture suite for wsr. ectorial/actions currently contains only a LICENSE and an initial commit, so the organization description is a direction rather than evidence of implemented actions.

**Key features to build:**

- Build one minimal action/component
- Test capability failures and deterministic outputs
- Document the action contract against a real wsr execution path

**Estimated effort:** M

**Related existing work:** [ectorial/actions](https://github.com/ectorial/actions) (source project), [ectorial/wsr](https://github.com/ectorial/wsr) (source project)

**Repo:** `carlosferreyra/wasi-action-kit`

---

## 26. cli-catalog-validator

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Python, JSON Schema, uvx, bunx, cargo

**Career signal:** A shared validation tool can turn catalog maintenance into reusable developer infrastructure.

**Description:** Proposed validation tooling derived from the three existing CLI catalogs. Focus on common metadata and executable checks while preserving each package manager’s runtime behavior.

**Key features to build:**

- Validate required metadata and executable mappings
- Run explicitly selected CLI smoke checks in CI
- Produce a structured report for catalog contributions

**Estimated effort:** M

**Related existing work:** [carlosferreyra/awesome-uvx](https://github.com/carlosferreyra/awesome-uvx) (source project), [carlosferreyra/awesome-bunx](https://github.com/carlosferreyra/awesome-bunx) (source project), [carlosferreyra/awesome-cargo-install](https://github.com/carlosferreyra/awesome-cargo-install) (source project)

**Repo:** `carlosferreyra/cli-catalog-validator`

---

## 27. teaching-repo-auditor

**Status:** `idea` ~~in-progress~~ ~~done~~

**Stack:** Python, GitHub API, JSON, Markdown

**Career signal:** Educational repository administration can become a practical API and reporting portfolio project.

**Description:** Proposed read-only course-repository audit tool inspired by FRRe-DS’s 2026 TPI template and group repositories. Organization activity establishes the setting; it does not establish personal authorship of student implementations.

**Key features to build:**

- Inventory assignment repositories and expected files
- Report missing CI/configuration and stale default branches
- Generate a course summary with links and explicit evidence

**Estimated effort:** M

**Related existing work:** [FRRe-DS/2026-TPI](https://github.com/FRRe-DS/2026-TPI) (source project)

**Repo:** `carlosferreyra/teaching-repo-auditor`

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

