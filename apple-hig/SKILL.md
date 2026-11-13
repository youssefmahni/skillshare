---
name: apple-hig
description: Apple Human Interface Guidelines (HIG) authority for iOS, iPadOS, macOS, tvOS, visionOS, watchOS, iPhone Duo, and games. Use when designing, reviewing, or auditing Apple-platform UI, Liquid Glass, SF Symbols, Dynamic Type, navigation, controls, accessibility, or whenever a request mentions HIG, Apple design guidelines, or platform-native conventions. Retrieves cited guidance from the official 173-page snapshot and the DarkCoders RAG (domain hig).
---

# Apple Human Interface Guidelines

Use this skill as the authority for Apple-platform design decisions. The corpus is a snapshot of Apple's official Markdown HIG; it is not a substitute for judgment, and it is never a substitute for citing the guidance.

## Corpus

| Item | Value |
|---|---|
| Pages | 173 (official Markdown, English) |
| Snapshot | 2026-11-08 |
| Cleaned text | `~/.config/opencode/knowledge/apple-hig/rag/` |
| Raw pages | `~/.config/opencode/knowledge/apple-hig/pages/` |
| Manifest + page→URL map | `~/.config/opencode/knowledge/apple-hig/manifest.json` |
| Browsable index | `~/.config/opencode/knowledge/apple-hig/index.md` |
| Platform coverage | `~/.config/opencode/knowledge/apple-hig/platform-map.md` |
| RAG | `domain=hig`, `framework=APPLE_HIG`, ~2,250 chunks |

Coverage: Getting started and design principles; Foundations (accessibility, app icons, branding, color, dark mode, icons, images, immersive experiences, inclusion, layout, materials, motion, privacy, RTL, SF Symbols, spatial layout, typography, writing); Patterns (25); Components (8 categories, 74 pages); Inputs (13); Technologies (30), including Apple Pay, App Clips, CarPlay, Mac Catalyst, widgets, Live Activities, and visionOS.

## Retrieval protocol (mandatory)

1. Search the RAG first:
   - Tool: `ciso_rag_search`
   - Parameters: `domain="hig"`, `framework="APPLE_HIG"`, `limit=5..10`, `rerank=true`
   - Query with platform + component + task terms, e.g. `"visionOS ornament placement"`, `"iOS tab bar customization"`, `"macOS toolbar split view"`.
2. Deduplicate passages by `document_id + header_path` before reasoning. The server can return the same passage twice.
3. If results are thin or the exact page is known, read the cleaned file directly:
   - `~/.config/opencode/knowledge/apple-hig/rag/apple-hig__<slug>.md`
   - Find slugs with `grep -ril "keyword" ~/.config/opencode/knowledge/apple-hig/rag/` or `index.md`.
4. If the snapshot lacks the page, or the question depends on the newest OS release, fetch the live page:
   - `https://developer.apple.com/design/human-interface-guidelines/<slug>`
   - Prefer the official Markdown endpoint by appending `.md`.
5. Never answer a HIG question from memory alone. If you cannot retrieve a citation, say so.

## Citation contract

- RAG `file_name` is `apple-hig__<slug>.md`; the URL is `https://developer.apple.com/design/human-interface-guidelines/<slug>`.
- Cite the page and section, e.g. `[Color > Liquid Glass color](https://developer.apple.com/design/human-interface-guidelines/color)`.
- Label every statement as one of:
  - **HIG**: directly supported by a retrieved passage.
  - **Platform convention**: implied by multiple HIG pages but not stated verbatim.
  - **Design judgment**: your recommendation, not an Apple rule.
- Do not invent numeric specs, control sizes, or OS-version claims. If a number is not in the retrieved text, say it is not in the snapshot and fetch the live page.

## Platform matrix

| Platform | Non-negotiables |
|---|---|
| iOS | Touch targets, safe areas, tab/navigation bars, sheets, Dynamic Type, gestures, permission prompts, Liquid Glass adaptivity |
| iPadOS | Size classes, multitasking, pointer/keyboard, sidebars, split views, popovers, Apple Pencil |
| macOS | Menu bar, windows, toolbars, sidebars, menus, keyboard shortcuts, pointer, window controls, density |
| tvOS | Focus-driven navigation, 10-foot legibility, remote input, top shelf, limited text entry |
| visionOS | Spatial layout, windows/volumes/immersive spaces, ornaments, eyes/hands, depth, materials, comfort |
| watchOS | Glanceable content, complications, Digital Crown, Always On, small-screen hierarchy |
| iPhone Duo | Continuity across displays, fold/open transitions, layout adaptation |
| Games | Controller support, focus, onboarding, pause/resume, platform game services |

Cross-platform foundations apply everywhere: accessibility, color, typography, layout, materials, motion, privacy, inclusion, right-to-left, writing.

## Review workflow

1. Establish the platform, surface, input methods, and OS target. If unknown, ask one clarifying question.
2. Retrieve the governing pages; read the relevant sections, including platform-specific subsections.
3. Evaluate in this order:
   - Platform fit: navigation model, controls, windows/scenes, menu bar/ornaments/complications.
   - Hierarchy and layout: safe areas, alignment, density, size classes, adaptation.
   - Typography: Dynamic Type, SF fonts, truncation, tracking, legibility.
   - Color and materials: semantic colors, light/dark/increased contrast, Liquid Glass, vibrancy.
   - Controls: correct control for the job, states, hit targets, labels.
   - Navigation and modality: hierarchy, back behavior, sheets, alerts, undo.
   - Accessibility: VoiceOver labels/traits, focus order, contrast, Reduce Motion/Transparency, captions.
   - Motion and feedback: purposeful, interruptible, respects settings.
   - Privacy and permissions: purpose strings, just-in-time prompts, location button.
   - Content and writing: sentence case, tone, localization, RTL.
   - Input: touch, pointer, keyboard, controller, eyes/hands, Digital Crown.
4. Separate blockers from polish. A platform-convention violation that confuses people is a blocker; a spacing preference is not.

## Output contract

```
## Verdict
One paragraph: ship, fix, or redesign, and why.

## Findings
| # | Severity | Issue | HIG guidance | Fix |
|---|----------|-------|--------------|-----|
| 1 | Blocker/High/Medium/Low | ... | [Page > Section](url) | ... |

## What already follows HIG
Short list of correct decisions.

## Open questions
Only questions that change the recommendation.
```

- Every finding row gets a citation or is explicitly marked **Design judgment**.
- Fixes must be concrete: control, placement, behavior, state, or content change.
- Do not pad the review. If there are three real findings, report three.

## Hard rules

- Do not apply iOS patterns to macOS, tvOS, visionOS, or watchOS. Each platform has its own navigation and input model.
- Do not fake Liquid Glass with custom blur/transparency; use system materials and test Reduce Transparency and Increase Contrast.
- Accessibility is not optional. VoiceOver, Dynamic Type, contrast, and hit targets are review blockers.
- Do not cite a page you did not retrieve.
- Do not claim Apple endorsement, certification, or App Review approval.
- If the question is implementation-level (SwiftUI/UIKit code), settle the HIG intent here and hand off to `persona-apple-hig-builder` (preferred), or use `mobile-ios-design` / `liquid-glass-design` for implementation patterns.

## Refresh

- Run `/hig-sync` to crawl the official Markdown, upload changed pages, and verify retrieval.
- The sync is hash-based: unchanged pages are skipped; changed pages replace their old chunks.
- Check `manifest.json.snapshot`. If it is older than 90 days, refresh before relying on specifics.
- `manifest.json.removed_since_last_run` lists pages Apple removed; treat them as retired, not current.
