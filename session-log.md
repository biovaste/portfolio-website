# Session Log — Portfolio Website

_Project-scoped fallback for sessions that cannot write the global workspace log._

## 2026-09-08 19:28 — Portfolio corrected, focused and deployed
- **Project(s):** income / portfolio website
- **Did:** Corrected public career dates, titles and degree; refreshed the HTML and PDF CV; reduced projects to Veikkaajat, GymTrack and AutoSlide; updated the GymTrack product description; linked Veikkaajat; added a visible update date; removed public referee information. Committed and deployed commit `4b401a4` to `main`.
- **Strongest output:** `income/income-project/portfolio-website/` — the deployed portfolio and corrected public CV at https://henri.hithitpull.fi.
- **Incomplete:** GymTrack public/private launch direction; professional photo; possible work-history timeline; any future sanitized job-tracker case study.
- **Files touched:** `index.html` — public content and project selection · `henri-haukkovaara-cv.{html,pdf}` — corrected public CV · `next-session-brief.md` — live handoff · `../../cv-factual-accuracy.md` — referee permission boundary.
- **Pointers:** Git commit `4b401a4`; live site https://henri.hithitpull.fi.
- **Next:** Decide whether GymTrack will be public before adding any link.

## 2026-09-12 — GymTrack demo linked, carousel replaced by a timeline, language pass
- **Project(s):** income / portfolio website
- **Did:** Linked the GymTrack card to the public demo at https://demo.gymtrack.hithitpull.fi and noted that the demo runs on generated data and resets. Replaced the seven-tab work carousel with a collapsible timeline: seven native `<details>` entries on a rail, each showing name, dates, role and a one-line summary without a click, AQVA open by default, carousel JavaScript deleted. Ran a language pass over the prose: removed the five em dashes the style guide forbids, rewrote two run-on "Features include" lists, cut an empty security claim, and replaced a sentence fragment in the AutoSlide card.
- **Decisions:** GymTrack gets the demo link and no repository link, on the grounds that the demo proves the product while the repo creates ongoing upkeep and a second surface to defend. Veikkaajat already carries the "here is my code" signal.
- **Assessment raised for Henri:** the site names almost no tools, while `cv-factual-accuracy.md` confirms GA4, GTM, GSC, Merchant Center, Google Ads, Meta Ads, Shopify with Liquid, Mailchimp, Microsoft Clarity, Hotjar, Looker Studio, Refox, WordPress and seven Adobe applications. Also absent: the CRO instrumentation work (Clarity and Hotjar setup, weekly monitoring, hypothesis validation), the Looker Studio dashboards built for the marketing team and the CEO, website-launch ownership (a named rejection reason at Matrix42), and content and creative production. Recommended against adding Google Analytics.
- **Incomplete:** professional photo and the two-column About, blocked on a photo file; skills strip; website-launch wording.
- **Files touched:** `index.html` · `next-session-brief.md` · `session-log.md`.
