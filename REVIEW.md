# GitHub review — 2026-10-04

Reviewed the authenticated `carlosferreyra` account, its personal repository inventory,
and repository inventories for FRRe-DS, Seminario-Integrador-2024, Kitsune-Studios,
ectorial, observatoriopublico, apuntes-frre, alumnithon, and informatorioar.
Also searched recent authored commits from 2026-09-01 and inspected selected
default-branch READMEs, commits, releases, and root file inventories.

## Status and scope

- `idea`: proposal or no implementation evidence.
- `in-progress`: implementation/scaffold exists, or a maintained project has remaining work.
- `done`: core deliverable shipped; maintenance can continue.

These are backlog classifications, not runtime certifications. No upstream project
was built or tested in this review. A release or README install command alone does
not prove all advertised features work. GitHub timestamps can reflect automation,
dependency updates, or instruction-file changes rather than product development.
Unchanged ideas retain their previous classification; the scan does not prove that
every suggested repository name is available. Original relative rankings are
preserved; appended entries have not been comparatively reranked.

## Evidence and changes

| Entry | Evidence | Assessment |
| --- | --- | --- |
| wsr | [June workspace commit](https://github.com/ectorial/wsr/commits/main/), [README](https://github.com/ectorial/wsr#readme), [releases](https://github.com/ectorial/wsr/releases) | Workspace scaffolds and early v0.0.2 release; keep in progress and remove planning-only description. |
| vicode | [README](https://github.com/carlosferreyra/vicode#readme), [v0.0.5 release](https://github.com/carlosferreyra/vicode/releases/tag/v0.0.5) | Rust Infrastructure-from-Code in early development; replace incorrect VS Code extension description. |
| korvex | [README and crate index](https://github.com/carlosferreyra/korvex#crates) | Include adapter crate and xtask; avoid claiming complete binding generation was verified. |
| codetwin / codetwin-lsp | [README](https://github.com/carlosferreyra/codetwin#readme), [commits](https://github.com/carlosferreyra/codetwin/commits/main/) | v2 scaffold with empty driver models; add core project and make editor idea depend on meaningful visualization. |
| awesome-uvx | [README](https://github.com/carlosferreyra/awesome-uvx#readme), [October catalog and September CI commits](https://github.com/carlosferreyra/awesome-uvx/commits/main/) | Maintained catalog; contribution guide, categories, data file, and sync already exist. |
| profilectl | [README](https://github.com/carlosferreyra/profilectl#readme), [roadmap](https://github.com/carlosferreyra/profilectl/blob/main/ROADMAP.md) | Replace overlapping dotfiles-bootstrap idea with existing project; current reset has stubbed commands. |
| vicode-drivers | [Vicode design](https://github.com/carlosferreyra/vicode#readme) | Proposed provider-driver follow-on replaces obsolete vicode-plugins idea. |
| awesome-bunx / awesome-cargo-install | [Bun catalog](https://github.com/carlosferreyra/awesome-bunx), [Cargo catalog](https://github.com/carlosferreyra/awesome-cargo-install) | Existing generated catalogs with September metadata maintenance; add as maintained work. |
| rust-template | [Repository](https://github.com/carlosferreyra/rust-template), [commits](https://github.com/carlosferreyra/rust-template/commits/main/) | Existing cargo-generate workspace/xtask template; add with generated-workspace verification as remaining work. |
| business-card | [README](https://github.com/carlosferreyra/business-card#readme), [v1.2.15 release](https://github.com/carlosferreyra/business-card/releases/tag/v1.2.15) | Shipped Rust CLI core; record done with maintenance tasks. |
| wasi-action-kit | [ectorial/actions](https://github.com/ectorial/actions) | LICENSE-only initial repository; reusable actions remain a proposal. |
| cli-catalog-validator | The three catalog repositories above | New inferred idea; no implementation claimed. |
| teaching-repo-auditor | [FRRe-DS course template](https://github.com/FRRe-DS/2026-TPI), [organization repositories](https://github.com/orgs/FRRe-DS/repositories) | New inferred idea; student repository activity is not attributed to Carlos. |

The personal `mise-setup` repository was also inspected. It mixes a migration plan
with subsequent history/bootstrap commits, so this review does not classify that
private machine configuration as a finished public portfolio project or reproduce
its contents. Other organizations supplied context but no sufficiently clear new
personal project to add.
