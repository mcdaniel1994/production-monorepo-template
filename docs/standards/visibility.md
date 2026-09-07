# Public Web Visibility & Discoverability Standard

**Status:** Active · **Version:** 1.0 · **Last reviewed:** 2026-09-03 · **Next review:** 2026-12-03

**Applies to:** public websites and marketing pages, blogs, public documentation and knowledge bases, and public portions of customer or partner portals.
**Does not apply to:** authenticated applications, internal dashboards, operations interfaces, or anything behind a login. Those surfaces have different concerns and are governed separately.

The authority on how public-facing pages get found — by humans, search engines, AI search, answer engines, and agents.

Adopting projects should record their own local values for the items in Section 12 and otherwise use this file as written.

**The goal:** a public page is structured, described, and fast enough that both a person and a machine can find it and understand what it says.

---

## Before you start

Reference this file before generating or modifying any public-facing page. Work in this order, because each step depends on the one before it — metadata written against the wrong heading structure has to be redone:

1. **Audit** — existing structure, metadata, schema, crawler access.
2. **Structure** — semantic HTML, heading hierarchy, accessibility.
3. **Metadata** — title, description, canonical, Open Graph, social cards.
4. **Content** — clarity, accuracy, sourcing, answer legibility.
5. **Schema** — the correct JSON-LD type for the page, if any.
6. **Performance** — Core Web Vitals, image optimization.
7. **Validate** — rich results, schema validator, indexing check.
8. **Instrument** — confirm measurement is in place (Section 11).

If a step reveals a violation, fix it before moving on.

Scale the work to the change. Small edits validate only the affected concerns — an unrelated UI tweak does not trigger a full audit. New pages, redesigns, content architecture changes, and discoverability work apply the full standard.

**When a requirement conflicts with the implementation:** name the conflict, explain the constraint, propose a compliant alternative, and log the deviation in a code comment or PR description. Re-evaluate it at the next quarterly review. Never silently deprioritize a standard, and never guess.

**Priority when requirements compete:** accessibility → factual integrity → semantic correctness → security and privacy → user experience → performance → search/GEO/AEO → structured data → geographic optimization.

Never introduce false claims, inaccessible interfaces, poor UX, or unnecessary complexity to satisfy SEO or AI-discovery guidance.

**Examples:** adding a marketing page or blog post template; changing a public page's title, description, or heading structure; editing `robots.txt` or a sitemap; restyling a public component in a way that affects contrast or focus visibility.

**Non-examples:** anything behind authentication; an internal admin or operations screen; a backend service with no rendered public output.

---

## 1. Semantic HTML & rendering

Choose elements by purpose, not appearance: `<main>`, `<nav>`, `<article>`, `<section>`, `<aside>`, `<header>`, `<footer>`, `<ul>`/`<ol>`, `<blockquote>`, `<time>`.

Maintain a logical heading hierarchy with one `<h1>` per page. HTML5 permits multiple `<h1>` elements inside sectioning contexts, but one per page is the convention here for assistive-tech consistency. Never skip levels for visual styling; style the correct level instead. Prefer native elements over ARIA roles where native semantics exist.

Primary content must be present in the initial static or server-rendered HTML. Do not inject it client-side: most AI crawlers do not execute JavaScript reliably, and JS rendering budget is limited even for major search crawlers. For public routes, use static generation, SSR, or pre-rendering rather than client-only rendering.

---

## 2. Accessibility

Target **WCAG 2.2 AA**.

**Images.** Informative images need meaningful alt text; decorative images use `alt=""`. Do not pad alt text for SEO. Image filenames: lowercase, hyphens not underscores, descriptive.

**Keyboard.** Every interactive element must be keyboard reachable, expose a visible focus state, and have an accessible name. Icon-only controls need an accessible name.

**Forms.** Associate `<label>` elements with their controls. Placeholder text is not a label.

**Color.** Never rely on color alone to carry meaning. Maintain AA contrast: 4.5:1 for body text, 3:1 for large text.

**ARIA.** Use only where native HTML is insufficient.

**Testing.** Automate where possible, then manually test navigation, forms, lead capture, contact flows, dialogs, and primary CTAs. Test against a defined baseline screen reader and browser pairing rather than ad hoc — a common default is NVDA with Firefox on Windows, with a VoiceOver spot-check on macOS or iOS for any page meant to convert mobile users.

---

## 3. Crawlability & indexing

Important content must not require client-side JavaScript to become visible or understandable.

No accidental `<meta name="robots" content="noindex">` in production.

Connect important content through logical internal links. Links should exist because they help users or crawlers understand relationships — no arbitrary link quotas.

Use consistent canonical URLs. Self-referencing canonicals are the default for indexable public pages:

```html
<link rel="canonical" href="https://example.com/page">
```

External links use `rel="noopener"`; add `noreferrer` only when intentionally stripping referrer data.

Return correct status codes: `200` for valid pages, `301`/`308` for intentional permanent redirects, `404` for missing content. Never return a fake `200` for a missing page.

---

## 4. Metadata

Every indexable public page provides:

- **`<title>`** — unique and descriptive, written for humans. Search engines truncate on pixel width (~600px), not character count, and rewrite titles often, so lead with clarity about the page's subject rather than optimizing to a character target or forcing keyword positions.
- **`<meta name="description">`** — an accurate summary that helps the right user decide to visit. Descriptions are frequently rewritten by search engines; write the first sentence as if it will be the entire snippet, because often it will.
- **Canonical URL.**
- **Open Graph:** `og:title`, `og:description`, `og:image` (1200×630), `og:url`, `og:type`.
- **Social card metadata** for platforms that support it.

Derive metadata from a shared source rather than maintaining duplicates by hand.

Title, description, primary heading, visible content, and structured data must all describe the same subject. Metadata must never claim something the page does not contain.

---

## 5. Content quality & trust

SEO, GEO, AEO, and E-E-A-T all demand the same thing: content that is true, specific, and genuinely useful. E-E-A-T is a quality framework, not a score to optimize, and trustworthiness outranks every other signal.

The useful reframe for AI search: generative engines don't rank pages, they cite sources. Content earns citation by being clearly written, accurate, specific, and easy to extract an answer from.

**Write content that is** primarily for people, clear about its subject, factual, specific, well structured, original, and easy to understand. Use descriptive headings, short paragraphs, and — where they genuinely aid comprehension — definitions, examples, lists, tables, citations, and sourced statistics. Make important answers easy to locate near the top, without forcing every page into an artificial Q&A shape.

**Avoid** keyword stuffing, generic AI filler, unnecessary repetition, fabricated quotations or statistics, and anything added solely to manipulate search or AI systems. These techniques never override accessibility, factual accuracy, semantic correctness, or user experience.

**Experience.** Where relevant, show genuine first-hand work: real implementations, screenshots, working demos, architecture diagrams, lessons learned, operational experience. Never manufacture experience that did not happen.

**Expertise.** Show it through technically accurate explanations, useful depth, appropriate terminology, clear reasoning, real author information including roles and tenure, and authoritative sourcing for factual claims.

**Authoritativeness.** Build it through consistent author and organizational identity, original work, an accurate About page, and links to primary sources. The organization's entity description must stay consistent across pages, metadata, and schema.

**Trustworthiness.** Content must accurately represent the project, author, organization, and product. Never invent or exaggerate customers, testimonials, employees or headcount, locations or addresses, business history, statistics, reviews, credentials, certifications, partnerships, awards, quotes, revenue, product capabilities, or operational claims. Do not exaggerate scope.

Portfolio, demo, and pre-launch projects must clearly distinguish simulated functionality from real production operations, and must not present planned capabilities as shipped ones.

**Freshness.** Use accurate `datePublished` and `dateModified`. Show "Last updated" where freshness materially matters. Flag content older than 12 months at quarterly review. Never bump dates just to appear fresh.

---

## 6. Structured data (JSON-LD)

Use JSON-LD when it meaningfully describes the page, choosing the Schema.org type that matches actual content — for example `Organization`, `Person`, `WebSite`, `WebPage`, `Article`, `BlogPosting`, `BreadcrumbList`, `FAQPage`, `SoftwareApplication`. Do not add schema merely because a type exists.

Structured data must reflect visible page content, contain factual information, use properties appropriate to the chosen type, and stay consistent with canonical URLs and site identity. Do not invent properties to look more complete, and do not assume `headline`, `datePublished`, `dateModified`, `author`, or `publisher` apply to every type — they do not.

Organization schema (`name`, `url`, `logo`, `sameAs`, `foundingDate`, `areaServed`, and similar) must contain only publicly supportable facts. Omit any property that cannot be substantiated rather than filling it with a plausible value.

Use stable URLs or identifiers so entities stay consistent across pages.

Validate with a rich results test and a Schema.org markup validator before shipping. Do not ship schema with critical errors.

---

## 7. Performance & Core Web Vitals

Target good vitals at roughly the 75th percentile:

| Metric | Target |
|---|---:|
| LCP | ≤ 2.5 s |
| INP | ≤ 200 ms |
| CLS | ≤ 0.1 |

Prefer minimal JavaScript, static or server-rendered content, optimized images, explicit dimensions or aspect ratios, modern formats (WebP/AVIF), efficient font loading, code splitting, and caching. Avoid unnecessary hydration on primarily static pages.

Lazy-load below-the-fold images, but never the likely LCP element such as the hero image. Set dimensions to prevent layout shift.

Do not sacrifice accessibility or functionality to improve a synthetic score. Optimize for actual user impact.

---

## 8. Machine-readable discovery & crawler access

These endpoints supplement the website — they never replace semantic HTML, accessibility, crawlable links, metadata, canonical URLs, structured data, or normal crawling. Generate them from the same authoritative source data as the site. Never maintain a second hand-written copy of site facts for AI ingestion, and never expose authenticated or internal content through any of them.

### `robots.txt`

Maintain an explicit crawler policy that avoids blocking public content, protects routes that should not be crawled, and references the sitemap by absolute URL.

Distinguish crawler purposes rather than treating all AI bots alike: traditional search indexing, AI search, user-triggered retrieval, model training, and other automated access. Search and AI-search crawlers should normally be allowed wherever public visibility is the goal. Training-crawler access is a separate policy decision for each project, reviewed quarterly.

Vendor crawler names and behavior change constantly. Keep the current allow/disallow list in the `robots.txt` implementation itself or a dedicated crawler reference — do not embed a vendor list in this standard.

### Sitemaps

Use a sitemap index when the site has multiple logical groups (`sitemap-pages.xml`, `sitemap-posts.xml`, `sitemap-docs.xml`); a single `sitemap.xml` is fine for a small site. Include only canonical, public, indexable URLs, and keep generated output synchronized with the real site.

### `rss.xml`

Provide a feed once the site publishes regularly updated content — posts, updates, changelogs, public knowledge content. Expose accurate titles, canonical URLs, publication dates, and descriptions, generated automatically. Defer it until such content exists.

### `llms.txt`

A concise, curated map of the site's most important public information for AI agents — not another sitemap. Include the project name, a short description, resource groups, canonical links, and a brief note on what each resource contains.

```markdown
# Project Name

> Concise description of the site or project.

## Documentation
- [Architecture](https://example.com/docs/architecture): System architecture overview.

## About
- [About](https://example.com/about): Organization and author information.
```

Keep it concise, current, and public. Generate from authoritative site data where practical.

### `llms-full.txt`

An optional emerging convention — a larger consolidated Markdown representation of public content. Not an established replacement for crawling. If implemented: generate automatically from authoritative sources, include only public content, keep it synchronized, exclude internal docs and secrets, and keep its growth bounded. Prefer `llms.txt` linking out over concatenating the whole site.

---

## 9. Localization & geographic targeting

Do not publish localized copies of pages without the supporting localization architecture. A single-language site should omit `hreflang` entirely rather than declare it incorrectly.

**Do not ship translated pages until hreflang is implemented.** When translations launch, every translated page declares each available language, includes a self-referential tag, and uses `x-default` for fallback:

```html
<link rel="alternate" hreflang="en" href="...">
<link rel="alternate" hreflang="es" href="...">
<link rel="alternate" hreflang="x-default" href="...">
```

Localized pages get their own canonical URLs, reference their alternates, use human-quality translation — no auto-translate shortcuts at scale — and preserve accurate metadata and structured data.

Reference real service geography naturally in page copy. Maintain business profiles and local citations only for genuine operating locations. Geographic claims must reflect actual service availability. Never invent local presence for local SEO.

---

## 10. Validation

For new pages or major changes, check semantic structure, accessibility, rendered HTML, metadata, canonical URL, indexing directives, structured data, sitemap inclusion, internal linking, responsive behavior, Core Web Vitals risk, and any affected machine-readable endpoints.

For small changes, validate only the affected concerns.

Automate where practical — linting, accessibility tests, HTML checks, build validation, schema tests, broken-link checks, Lighthouse or equivalent. Automation should enforce the standard without making normal development rigid.

---

## 11. Measurement & review cadence

**Monthly:** organic traffic, queries and CTR, indexing status, Core Web Vitals.

**Quarterly:** AI citation tracking, traffic split, backlinks, schema validation, crawler access verification, logged overrides, content older than 12 months, and any changes to WCAG, Core Web Vitals, search-engine guidance, structured-data requirements, or agent-ingestion conventions.

**Annually:** full audit, competitive analysis, alignment with real performance data.

**Triggered:** major platform changes, traffic or citation drops, structural issues, new public surfaces.

Keep fast-changing detail out of this document and in implementation-specific references: crawler user-agent names, vendor bot policies, platform behavior, GEO research, and analytics procedures. Update those independently.

---


## Core principle

Build public web surfaces first for **people**, while making their meaning, structure, identity, and public information easy for machines to understand. Accessibility, truthful content, semantic structure, performance, discoverability, structured data, and agent accessibility should reinforce one another rather than compete.

---

## Exceptions

Follow the exception mechanics in [`README.md`](README.md#exceptions). The conflict-handling and priority guidance in [Before you start](#before-you-start) governs how to weigh competing requirements *within* this standard; the exception path governs deviating *from* it.
