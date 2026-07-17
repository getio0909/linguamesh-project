# ADR-0001: Federated Polyrepository Workspace

Status: Accepted

Date: 2026-07-17

## Context

LinguaMesh ships a shared Rust core, localization data, and four clients with independent native toolchains and release artifacts. A monorepo would couple permissions and CI while Git submodules would add brittle synchronization state.

## Decision

Use seven canonical sibling repositories coordinated by `linguamesh-project`. `workspace-manifest.toml` defines the inventory; bootstrap scripts clone missing siblings without replacing existing work. `release-manifest.toml` pins a known-good compatible release train.

## Consequences

Repositories can build and release independently, but cross-repository changes require explicit identifiers, compatibility transitions, conformance evidence, and manifest updates. CI must detect stale goal or contract revisions.

## Alternatives considered

A monorepo and Git submodules were rejected for the initial architecture. Optional repositories require a later ADR demonstrating independent release, licensing, security, or size needs.

## Compatibility and rollback

The manifest schema is versioned. Rollback selects a previous verified release train; it never rewrites repository history.
