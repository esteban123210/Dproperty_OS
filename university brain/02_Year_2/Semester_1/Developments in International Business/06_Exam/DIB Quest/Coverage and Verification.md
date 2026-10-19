# DIB Quest coverage and verification

**Prepared:** 19 October 2026  
**Content base:** Existing course source notes at commit `a884601e20274ca52f5f9f308177cd89048ffcda`.  
**Artifact:** Self-contained `DIB-Quest.html`; all game scripts, styles, questions and reference text are embedded.

## Requirement audit

| Requirement | Evidence |
|---|---|
| Repository updated with recent information | Anonymized Shopee draft summary and review archived separately, with estimate explicitly non-official; course hub and exam index link the game and review |
| User selects a level | Four always-selectable grade-ambition tracks; browser test verifies selected state and differentiated descriptions |
| Level-appropriate information and quizzes | Core definitions at Foundations; mechanisms/application at Application; evidence/comparisons/boundaries at Analysis; conditional writing and rubric at Mastery |
| Whole supplied course represented | 47 named topics across all seven sessions, mapped below; 58 offline source notes; original source gaps remain explicit |
| Gamified practice | Session missions, mixed raids, XP, streaks, eight badges, repair queues and milestone progress |
| Meaningful feedback and progression | Answer explanations; first unassisted correct attempt clears each quiz skill; hints do not clear; repeated correct answers cannot farm XP |
| Written exam preparation | 47 topic prompts and four mock-exam prompts; saved drafts, length gates, guides, five-criterion self-review, optional 120-minute timer |
| Cumulative completion | 47 / 94 / 141 / 192 milestones for the four tracks; all-topic completion arithmetic verified |
| Personal progress persistence | Browser reload, text backup and confirmed restore tested; no remote storage or requests |
| Offline and responsive | Tested under file:// in Chrome at desktop and 390px mobile widths; no horizontal overflow or runtime errors |

## Verification scope

Browser checks exercise the real interface for level selection, session lessons, wrong answers, repair, hinted answers without credit, correct scoring, repeat XP protection, local-storage reload, writing minimum lengths, rubric scoring, mock response gating, timer controls, full-text source search and backup-text restore. Content validation checks all 141 question structures, all topic-to-source references, all 51 writing guides and all seven session distributions. Automated checks do not establish educational calibration to actual Dutch grades or independently grade essay quality.

Native file downloading was canceled by the test environment's Chrome sandbox. The working backup-text export/restore path was therefore tested as the robust fallback; native downloading is offered but not represented as verified in every browser. The optional timer is page-session state rather than a persistent high-stakes examination tool.

## Topic-to-source coverage

| Session | Topic | Source note |
|---|---|---|
| 1 | IB, MNEs and FDI | [Session 1 Slides - Lecture Notes](../../03_Readings/Session_01/Session%201%20Slides%20-%20Lecture%20Notes.md) |
| 1 | Liability of foreignness and FSAs | [Zaheer 1995 - Overcoming the Liability of Foreignness](../../03_Readings/Session_01/Zaheer%201995%20-%20Overcoming%20the%20Liability%20of%20Foreignness.md) |
| 1 | Semi-globalization and globaloney | [Ghemawat 2012 - Actually the World Isnt Flat](../../03_Readings/Session_01/Ghemawat%202012%20-%20Actually%20the%20World%20Isnt%20Flat.md) |
| 1 | Testing deglobalization narratives | [Altman et al 2024 - Challenging the Deglobalization Narrative](../../03_Readings/Session_01/Altman%20et%20al%202024%20-%20Challenging%20the%20Deglobalization%20Narrative.md) |
| 1 | Transaction costs and the boundary of the firm | [Session 1 Slides - Lecture Notes](../../03_Readings/Session_01/Session%201%20Slides%20-%20Lecture%20Notes.md) |
| 1 | Value chains, outsourcing and offshoring | [Session 1 Slides - Lecture Notes](../../03_Readings/Session_01/Session%201%20Slides%20-%20Lecture%20Notes.md) |
| 2 | Ashraf et al 2026 - Localization Matters More Than Ever | [Ashraf et al 2026 - Localization Matters More Than Ever](../../03_Readings/Session_02/Ashraf%20et%20al%202026%20-%20Localization%20Matters%20More%20Than%20Ever.md) |
| 2 | Born globals and international new ventures | [Session 2 Slides - Lecture Notes](../../03_Readings/Session_02/Session%202%20Slides%20-%20Lecture%20Notes.md) |
| 2 | Culture, distance and measurement | [Session 2 Slides - Lecture Notes](../../03_Readings/Session_02/Session%202%20Slides%20-%20Lecture%20Notes.md) |
| 2 | Dunning 2000 - The Eclectic Paradigm | [Dunning 2000 - The Eclectic Paradigm](../../03_Readings/Session_02/Dunning%202000%20-%20The%20Eclectic%20Paradigm.md) |
| 2 | Ghemawat 2001 - Distance Still Matters | [Ghemawat 2001 - Distance Still Matters](../../03_Readings/Session_02/Ghemawat%202001%20-%20Distance%20Still%20Matters.md) |
| 2 | Institutions, location and economic systems | [Session 2 Slides - Lecture Notes](../../03_Readings/Session_02/Session%202%20Slides%20-%20Lecture%20Notes.md) |
| 2 | Luo and Tung 2018 - A General Theory of Springboard MNEs | [Luo and Tung 2018 - A General Theory of Springboard MNEs](../../03_Readings/Session_02/Luo%20and%20Tung%202018%20-%20A%20General%20Theory%20of%20Springboard%20MNEs.md) |
| 2 | Uppsala learning and commitment | [Session 2 Slides - Lecture Notes](../../03_Readings/Session_02/Session%202%20Slides%20-%20Lecture%20Notes.md) |
| 2 | IKEA India - Case Note | [IKEA India - Case Note](../../04_Cases/Session_02/IKEA%20India%20-%20Case%20Note.md) |
| 3 | Atradius and export-credit insurance | [Atradius 2026 - Export Credit Agencies Guest Lecture](../../03_Readings/Session_03/Atradius%202026%20-%20Export%20Credit%20Agencies%20Guest%20Lecture.md) |
| 3 | Bamford et al 2020 - Joint Ventures and Partnerships in a Downturn | [Bamford et al 2020 - Joint Ventures and Partnerships in a Downturn](../../03_Readings/Session_03/Bamford%20et%20al%202020%20-%20Joint%20Ventures%20and%20Partnerships%20in%20a%20Downturn.md) |
| 3 | Beugelsdijk et al 2018 - Cultural Distance and Firm Internationalization | [Beugelsdijk et al 2018 - Cultural Distance and Firm Internationalization](../../03_Readings/Session_03/Beugelsdijk%20et%20al%202018%20-%20Cultural%20Distance%20and%20Firm%20Internationalization.md) |
| 3 | Entry modes and establishment modes | [Session 3 Slides - Lecture Notes](../../03_Readings/Session_03/Session%203%20Slides%20-%20Lecture%20Notes.md) |
| 3 | Global integration and local responsiveness | [Session 3 Slides - Lecture Notes](../../03_Readings/Session_03/Session%203%20Slides%20-%20Lecture%20Notes.md) |
| 3 | Meyer et al 2009 - Institutions Resources and Entry Strategies | [Meyer et al 2009 - Institutions Resources and Entry Strategies](../../03_Readings/Session_03/Meyer%20et%20al%202009%20-%20Institutions%20Resources%20and%20Entry%20Strategies.md) |
| 3 | Santos and Williamson 2015 - The New Mission for Multinationals | [Santos and Williamson 2015 - The New Mission for Multinationals](../../03_Readings/Session_03/Santos%20and%20Williamson%202015%20-%20The%20New%20Mission%20for%20Multinationals.md) |
| 3 | Popeyes China - Case Note | [Popeyes China - Case Note](../../04_Cases/Session_03/Popeyes%20China%20-%20Case%20Note.md) |
| 4 | Henisz and Zelner 2010 - The Hidden Risks in Emerging Markets | [Henisz and Zelner 2010 - The Hidden Risks in Emerging Markets](../../03_Readings/Session_04/Henisz%20and%20Zelner%202010%20-%20The%20Hidden%20Risks%20in%20Emerging%20Markets.md) |
| 4 | Henisz et al 2014 - Spinning Gold | [Henisz et al 2014 - Spinning Gold](../../03_Readings/Session_04/Henisz%20et%20al%202014%20-%20Spinning%20Gold.md) |
| 4 | Location timing and firm–state bargaining | [Session 4 Slides - Lecture Notes](../../03_Readings/Session_04/Session%204%20Slides%20-%20Lecture%20Notes.md) |
| 4 | Ramamurti 2001 - The Obsolescing Bargaining Model | [Ramamurti 2001 - The Obsolescing Bargaining Model](../../03_Readings/Session_04/Ramamurti%202001%20-%20The%20Obsolescing%20Bargaining%20Model.md) |
| 4 | Rice and Zegart 2018 - Managing 21st Century Political Risk | [Rice and Zegart 2018 - Managing 21st Century Political Risk](../../03_Readings/Session_04/Rice%20and%20Zegart%202018%20-%20Managing%2021st%20Century%20Political%20Risk.md) |
| 4 | AES Telasi - Case Note | [AES Telasi - Case Note](../../04_Cases/Session_04/AES%20Telasi%20-%20Case%20Note.md) |
| 5 | Chipman 2016 - Why Your Company Needs a Foreign Policy | [Chipman 2016 - Why Your Company Needs a Foreign Policy](../../03_Readings/Session_05/Chipman%202016%20-%20Why%20Your%20Company%20Needs%20a%20Foreign%20Policy.md) |
| 5 | Estrin and Hancke 2026 - Geopolitics Geoeconomics and Organizational Models | [Estrin and Hancke 2026 - Geopolitics Geoeconomics and Organizational Models](../../03_Readings/Session_05/Estrin%20and%20Hancke%202026%20-%20Geopolitics%20Geoeconomics%20and%20Organizational%20Models.md) |
| 5 | Meyer and Thein 2014 - International Sanctions Against Myanmar | [Meyer and Thein 2014 - International Sanctions Against Myanmar](../../03_Readings/Session_05/Meyer%20and%20Thein%202014%20-%20International%20Sanctions%20Against%20Myanmar.md) |
| 5 | Mol et al 2023 - Should I Stay or Should I Go | [Mol et al 2023 - Should I Stay or Should I Go](../../03_Readings/Session_05/Mol%20et%20al%202023%20-%20Should%20I%20Stay%20or%20Should%20I%20Go.md) |
| 5 | Risk, uncertainty and strategic response | [Session 5 Slides - Lecture Notes](../../03_Readings/Session_05/Session%205%20Slides%20-%20Lecture%20Notes.md) |
| 5 | Supranational institutions, industrial policy and blocs | [Session 5 Slides - Lecture Notes](../../03_Readings/Session_05/Session%205%20Slides%20-%20Lecture%20Notes.md) |
| 5 | NVIDIA Between Two Giants - Case Note | [NVIDIA Between Two Giants - Case Note](../../04_Cases/Session_05/NVIDIA%20Between%20Two%20Giants%20-%20Case%20Note.md) |
| 6 | Anwar 2026 - The Algorithmic Boardroom | [Anwar 2026 - The Algorithmic Boardroom](../../03_Readings/Session_06/Anwar%202026%20-%20The%20Algorithmic%20Boardroom.md) |
| 6 | Hennart 2019 - Digitalized Service Multinationals | [Hennart 2019 - Digitalized Service Multinationals](../../03_Readings/Session_06/Hennart%202019%20-%20Digitalized%20Service%20Multinationals.md) |
| 6 | Lindner et al 2025 - AI and Augmented Decision Making | [Lindner et al 2025 - AI and Augmented Decision Making](../../03_Readings/Session_06/Lindner%20et%20al%202025%20-%20AI%20and%20Augmented%20Decision%20Making.md) |
| 6 | Moses et al 2025 - Data Accuracy in West African Markets | [Moses et al 2025 - Data Accuracy in West African Markets](../../03_Readings/Session_06/Moses%20et%20al%202025%20-%20Data%20Accuracy%20in%20West%20African%20Markets.md) |
| 6 | Network effects, complementors and digital distance | [Session 6 Slides - Lecture Notes](../../03_Readings/Session_06/Session%206%20Slides%20-%20Lecture%20Notes.md) |
| 6 | Acorai - Case Note | [Acorai - Case Note](../../04_Cases/Session_06/Acorai%20-%20Case%20Note.md) |
| 7 | Kim 2020 - Whats the Best Pace of Expansion | [Kim 2020 - Whats the Best Pace of Expansion](../../03_Readings/Session_07/Kim%202020%20-%20Whats%20the%20Best%20Pace%20of%20Expansion.md) |
| 7 | Kim et al 2020 - Fast Internationalization Across Regions | [Kim et al 2020 - Fast Internationalization Across Regions](../../03_Readings/Session_07/Kim%20et%20al%202020%20-%20Fast%20Internationalization%20Across%20Regions.md) |
| 7 | Lu and Beamish 2004 - The S Curve Hypothesis | [Lu and Beamish 2004 - The S Curve Hypothesis](../../03_Readings/Session_07/Lu%20and%20Beamish%202004%20-%20The%20S%20Curve%20Hypothesis.md) |
| 7 | Sustainable value and evidence quality | [Kim 2020 - Whats the Best Pace of Expansion](../../03_Readings/Session_07/Kim%202020%20-%20Whats%20the%20Best%20Pace%20of%20Expansion.md) |
| 7 | Shopee - Case Note | [Shopee - Case Note](../../04_Cases/Session_07/Shopee%20-%20Case%20Note.md) |

## Limits and interpretation

Grade bands are ambitions for cognitive demand, not validated grade predictions. Completion means the specified practice milestones have been covered. Written milestones are self-reviewed; seek external feedback and delayed retrieval to assess retention and transfer.

Missing Session 7 slides, textbook chapters and announced guest material remain unavailable. The standalone source library contains knowledge-file text rather than every PDF image. Historical course examples and mock narratives are not independently checked current events. The Shopee source's operating-expense and geographic-unit ambiguities remain flagged in the canonical notes.
