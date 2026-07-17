# Authoritative Source Register

Last verified: 2026-07-16.

This register follows the source hierarchy that every SKILL.md declares under
`## Authoritative sources`. Tier 1 outranks Tier 2, and so on. Where sources
conflict, resolve through `source-hierarchy-resolver` — never by preferring the
more convenient one.

**How to read the status column.** An instrument that has been amended is not
dead: it remains in force *as amended*. Cite the base instrument together with
its amendment (`UU 1/2025 jo. UU 16/2025`), never the base alone. Citing an
unamended base text as though it were operative is the most likely way this
register produces a confidently wrong answer.

---

## Tier 1 — Law, regulation, and official decision

Verified 2026-07-16 against the JDIH database of Badan Pemeriksa Keuangan
(`peraturan.bpk.go.id`) and Sekretariat Negara (`setneg.go.id`). Each entry
records the gazette citation (Lembaran Negara / Tambahan Lembaran Negara) so a
reviewer can pull the authenticated text rather than trust this file.

### 1.1 Establishing statute — as amended

| # | Instrument | Title | Enacted | Gazette | Status |
|---|---|---|---|---|---|
| 1 | **UU No. 1 Tahun 2025** | Perubahan Ketiga atas Undang-Undang Nomor 19 Tahun 2003 tentang Badan Usaha Milik Negara | 24 Feb 2025 | LN 2025 (25), TLN 7097, 94 hlm. | Berlaku — **diubah dengan UU 16/2025** |
| 2 | **UU No. 16 Tahun 2025** | Perubahan Keempat atas Undang-Undang Nomor 19 Tahun 2003 tentang Badan Usaha Milik Negara | 6 Oct 2025 | LN 2025 (162), TLN 7142, 51 hlm. | **Berlaku — operative amendment** |

- <https://peraturan.bpk.go.id/Details/314622/uu-no-1-tahun-2025>
- <https://peraturan.bpk.go.id/Details/330668/uu-no-16-tahun-2025>

**What UU 1/2025 establishes** (per the BPK abstract, verified 2026-07-16):

- The President, as Head of Government, holds the power to manage BUMN as part of
  state financial management power, including ownership of separated state assets
  (*kekayaan negara yang dipisahkan*).
- **Pasal 3E** — in exercising BUMN management, the President delegates part of
  that authority to Badan Pengelola Investasi Daya Anagata Nusantara, formed by
  this Law. The Badan is an Indonesian legal entity wholly owned by the
  Government of Indonesia, formed to increase and optimize the investment and
  operations of BUMN and other sources of funds.
- **Pasal 3G** — the Badan's capital derives from state capital participation
  (*penyertaan modal negara*) and/or other sources.
- BUMN administration rests on economic democracy: *kebersamaan*; *efisiensi
  berkeadilan*; *berkelanjutan*; *berwawasan lingkungan*; maintaining balance,
  progress, and unity of the national economy; and good corporate governance.

**What UU 16/2025 changes** (per the BPK abstract, verified 2026-07-16) — each
item below has direct consequences for skills in this package:

- change of institutional nomenclature for the body carrying out governmental
  tasks in the BUMN field, and **separation of supervisory and operational
  functions**;
- State ownership of **Series A Dwiwarna shares** with special rights in BUMN;
- **prohibition on BUMN organs holding concurrent positions**, including minister
  and deputy minister (*larangan organ BUMN merangkap jabatan*);
- **financial examination of BUMN by Badan Pemeriksa Keuangan (BPK)**.

> TODO(legal): the four bullets above are abstract-level. Before any skill relies
> on them, the accountable legal owner must pin each to its specific pasal/ayat
> in the authenticated PDF and record the article number here. This register
> deliberately does not guess article numbers it has not read.

### 1.2 Implementing regulation — as amended

| # | Instrument | Title | Enacted | Gazette | Status |
|---|---|---|---|---|---|
| 3 | **PP No. 10 Tahun 2025** | Organisasi dan Tata Kelola Badan Pengelola Investasi Daya Anagata Nusantara | 24 Feb 2025 | LN 2025 (26), TLN 7098, 22 hlm. | Berlaku — **diubah dengan PP 19/2026** |
| 4 | **PP No. 19 Tahun 2026** | Perubahan atas Peraturan Pemerintah Nomor 10 Tahun 2025 tentang Organisasi dan Tata Kelola Badan Pengelola Investasi Daya Anagata Nusantara | 8 Apr 2026 | LN 2026 (39), TLN 7172, 15 hlm. | **Berlaku — operative amendment** |

- <https://peraturan.bpk.go.id/Details/314627/pp-no-10-tahun-2025>
- <https://peraturan.bpk.go.id/Details/349414/pp-no-19-tahun-2026>

**What PP 10/2025 establishes** (per the BPK abstract, verified 2026-07-16):

- The Badan carries out governmental tasks in BUMN management as regulated by the
  BUMN Law; the President delegates part of his tasks and authority to it.
- The Badan is an Indonesian legal entity wholly owned by the Government.
- **Organ Badan consists of Dewan Pengawas and Badan Pelaksana.**
- The regulation exists to give Danantara an adequate legal foundation to carry
  out BUMN management effectively.

### 1.3 Appointment decision

| # | Instrument | Title | Signed |
|---|---|---|---|
| 5 | **Keppres No. 30 Tahun 2025** | Pengangkatan Dewan Pengawas dan Badan Pelaksana Badan Pengelola Investasi Daya Anagata Nusantara, Danantara Indonesia | 24 Feb 2025 |

Source: Sekretariat Negara —
<https://www.setneg.go.id/baca/index/presiden_prabowo_tandatangani_tiga_produk_hukum_strategis_investasi_nasional>

> TODO(legal): verify Keppres 30/2025 against JDIH Setneg and confirm whether it
> has been superseded by later appointment decisions. Named office-holders change;
> no skill should hard-code them.

---

## Tier 2 — Danantara and entity policy, delegation, charter, standard

**This tier is empty. That is the single largest gap in this package.**

Every skill in `04-skills/` declares Tier 2 sources under `## Authoritative
sources`, and not one of them can currently point to a real document. Until this
tier is populated, the skills reason about a *generic* sovereign fund, not about
Danantara. The following are required and can only come from inside Danantara:

- [ ] BPI Danantara Dewan Pengawas charter
- [ ] Badan Pelaksana delegation of authority matrix (the operative source for
      `decision-rights-checker` and `mandate-authority-interpreter`)
- [ ] DIM Investment Committee charter, quorum, and approval thresholds
      (required by `investment-committee-memo` and `human-approval-orchestrator`)
- [ ] DAM active-ownership and transformation policy
- [ ] DDMF development-finance and additionality policy
- [ ] investment policy statement, mandate limits, risk appetite, concentration
      and liquidity limits (required by `portfolio-diversification-analyzer`,
      `concentration-and-liquidity-risk`, `risk-adjusted-return-analyzer`)
- [ ] valuation policy and model-approval standard (required by
      `valuation-orchestrator`, `dcf-model-challenger`)
- [ ] conflict-of-interest, related-party, and recusal policy
- [ ] data classification standard and approved-AI-environment policy
- [ ] procurement and integrity due-diligence standard
- [ ] whistleblowing and escalation procedure

---

## Tier 3 — Audited or owner-certified internal data

**Empty.** Requires named systems of record, data owners, and lineage. No skill
should cite a figure whose owner and effective date cannot be named.

---

## Tier 4 — Independent external evidence

Institutional context, verified 2026-07-16. **Corporate self-description, not a
legal instrument** — outranked by Tier 1 on every point of authority, mandate, or
decision right. Useful for framing and terminology; never sufficient as the basis
of a decision.

| # | Source | URL |
|---|---|---|
| 6 | Danantara Indonesia — About | <https://www.danantaraindonesia.co.id/about> |
| 7 | Danantara Indonesia — Ecosystem (BPI, DAM, DIM, DDMF) | <https://www.danantaraindonesia.co.id/> |
| 8 | Danantara Investment Management | <https://www.danantaraindonesia.co.id/dim> |
| 9 | Danantara Asset Management — strategic agenda | <https://www.danantaraindonesia.co.id/dam/strategic-agenda> |
| 10 | Danantara corporate statement | <https://www.danantaraindonesia.co.id/media-center/announcement/corporate-statement> |

> OPEN QUESTION(governance): this package's entity model (BPI / DAM / DIM / DDMF)
> is drawn from Tier 4 marketing pages, not from Tier 1. Reporting on PP 19/2026
> indicates it permits **more than one investment holding and operational
> holding**, with all holding shares retained by Danantara and establishment
> subject to Presidential approval. If that is correct, the fixed four-entity
> model hard-coded into the `entity` column of `master_skill_registry.csv` and
> into 133 skills may not match the operative structure. This must be resolved
> against the authenticated PP 19/2026 text before the registry is trusted.
> It is a question for the accountable owner, not one this register can settle.

---

## Tier 5 — Prior decisions and precedent

Context only. Never a substitute for current analysis. **Empty.**

---

## Tooling and specification sources

Not part of the decision-source hierarchy; they govern how skills are built, not
what they may conclude.

| # | Source | URL |
|---|---|---|
| 11 | Claude Code — Agent Skills | <https://docs.anthropic.com/en/docs/claude-code/skills> |
| 12 | Agent Skills specification (name ≤64 chars, description ≤1024 chars) | <https://agentskills.io/specification> |
| 13 | Agent Skills — optimizing descriptions | <https://agentskills.io/skill-creation/optimizing-descriptions> |

---

## Internal doctrine input

| # | Source | Note |
|---|---|---|
| 14 | User-provided Danantara principles, Danantara Way formulation, and the five core tensions | Doctrine input, **not an authoritative source**. It shapes how skills reason; it does not establish authority, mandate, or fact. |

---

## Maintenance

- Re-verify Tier 1 whenever an amendment is reported, and at minimum annually.
  UU 16/2025 (Oct 2025) and PP 19/2026 (Apr 2026) both landed after this package's
  doctrine was drafted; neither was cited anywhere in it.
- Record for every source: owner, title, version, effective date, retrieval date,
  classification, and exact location.
- A source that cannot be retrieved by an independent reviewer is not a source.
