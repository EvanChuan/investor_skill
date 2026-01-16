---
language: en
output_language: zh-TW
---

<!-- CRITICAL INSTRUCTION -->
**IMPORTANT: When using this skill, you MUST generate ALL responses in Traditional Chinese (繁體中文).**

This English documentation serves as a reference framework for the AI model.
However, all analysis outputs, reports, and recommendations must be written in Traditional Chinese.
<!-- END INSTRUCTION -->

---
name: industry-research
description: Industry research and sector rotation strategy. Integrates top global investment bank reports, identifies industry opportunities in business cycles, judges industry competitive landscape and long-term trends. Can be executed independently or build upon macroeconomic analysis to provide directional guidance for stock selection.
version: 2.2.0
author: Evan
license: Proprietary
tags:
  - industry-analysis
  - sector-rotation
  - investment-themes
  - supply-demand-analysis
  - competitive-landscape
  - megatrends
  - institutional-research
---

# Industry Research & Rotation

## Overview

This module focuses on in-depth industry-level research, integrating industry reports from top global investment banks and research institutions. Combined with current overall policy and economic conditions, it identifies industry opportunities in business cycles, judges industry competitive landscape and long-term trends, providing directional guidance for individual stock selection.

**Module Characteristics:**
- ✅ Can execute industry analysis independently
- ✅ Can build upon macroeconomic analysis results
- ✅ Dynamically tracks latest market trends
- ✅ Supports progressive dialogue for in-depth exploration

### Core Philosophy

**Choosing the Right Industry is More Important Than Choosing the Right Stock**

- When an industry has tailwinds, even mediocre companies can perform well (industry beta effect)
- When an industry faces headwinds, even excellent companies struggle to generate excess returns
- Positioning in the right industry at the right time yields twice the results with half the effort
- Structural growth outperforms cyclical rebounds: the power of long-term trends far exceeds short-term volatility

**Wisdom of Institutional Investors**

This module integrates the collective wisdom of top global investment banks and research institutions, dynamically tracking the latest market consensus. For detailed institutional tracking methods, refer to:
- `references/institutional/institutional-reports-tracking.md` - Institutional Report Tracking Methods
- `references/institutional/13f-holdings-analysis.md` - Hedge Fund Holdings Analysis

### Core Capabilities

1. **Institutional Report Integration** - Track 13F filings and top investment bank industry reports
2. **Industry Lifecycle Positioning** - Determine if industry is in introduction/growth/maturity/decline phase
3. **Supply-Demand Analysis & Business Cycle Tracking** - Identify supply-demand inflection points and industry cycle turning points
4. **Competitive Landscape Assessment** - Market concentration (HHI) and leading company moat analysis
5. **Technology Disruption Impact Assessment** - Disruptive innovation and technology maturity evaluation
6. **Industry Chain Upstream-Downstream Analysis** - Value chain breakdown and key bottleneck identification
7. **Sector Rotation Timing Judgment** - Dynamic allocation based on economic cycles and thematic investing

---

## Applicable Scenarios

### When to Use This Module

**Industry Trend Assessment:**
- "Which industries should I invest in now?"
- "What stage is the semiconductor / AI / EV / nuclear energy industry at?"
- "Which industries have structural growth opportunities?"

**Industry Comparison & Selection:**
- "Which is better: financial stocks / tech stocks / traditional industry stocks?"
- "Why do investment banks recommend defense stocks? What's the logic?"
- "Which segment of the AI industry chain has the most investment value?"

**Supply-Demand & Competition Analysis:**
- "How is industry supply and demand? Is inventory healthy?"
- "What is the competitive landscape of this industry? Who are the leaders?"
- "Who holds pricing power in the industry?"

**Portfolio Allocation:**
- "How to implement sector rotation strategy?"
- "What weight should each industry have?"
- "When should I rotate from tech stocks to financial stocks?"

### Trigger Keywords

**Industry Names:** Semiconductors, AI, EVs, nuclear energy, defense, finance, healthcare, energy, consumer goods

**Industry Related:** Industry trends, industry cycles, sector rotation, supply-demand, competitive landscape, industry chain

**Investment Themes:** AI computing power, data centers, military spending, nuclear power, de-dollarization, obesity drugs, GLP-1

### Not Applicable Scenarios

- Single company in-depth analysis → Use `equity-fundamental-analysis`
- Macroeconomic environment assessment → Use `macro-market-analysis`
- Technical charts and entry timing → Use `technical-analysis`

---

## Execution Workflow

### Step 1: Macroeconomic Environment Assessment (Dynamic Loading)

**Check if there are prior macroeconomic analysis results:**

```
IF prior macro analysis exists in conversation history:
→ Read and reference the following information:
    - Economic cycle stage (recovery/expansion/peak/recession)
    - Market risk appetite (Risk-On / Risk-Off)
    - Central bank policy stance and interest rate environment
    - Recommended equity position percentage
→ Indicate in response: "Based on prior macroeconomic analysis..."

ELSE (no prior macro analysis):
→ Search for current macroeconomic conditions independently:
    - Search keywords: "2026 economic outlook" "US/China/global economic conditions"
    - Search keywords: "Fed/ECB/central bank latest policy"
    - Search keywords: "2026 GDP/inflation/interest rate forecast"
→ Quickly summarize current economic environment (2-3 paragraphs)
→ Indicate in response: "Based on latest economic data search..."
```

**Preliminary industry direction screening based on economic environment:**

For detailed sector rotation strategy and economic cycle correspondence table, refer to:
- `references/frameworks/sector-rotation-by-cycle.md`

**Output Format (Concise Version):**
```
## Current Economic Environment Overview

[Source description: prior analysis results OR latest search results]

- **Economic Cycle:** [Recovery/Expansion/Peak/Recession]
- **Central Bank Policy:** [Accommodative/Neutral/Restrictive]
- **Risk Appetite:** [Risk-On / Risk-Off]
- **Priority Industry Directions:** [Industry categories recommended based on cycle]
```

---

### Step 2: Institutional Report Integration & Consensus Tracking

**Dynamic search for latest institutional views:**

```
Search Strategy:

1. Latest top investment bank reports (past 1-3 months):
    - "J.P. Morgan 2026 industry outlook"
    - "Goldman Sachs [target industry] report"
    - "Morgan Stanley sector allocation recommendations"
    - "BlackRock 2026 investment themes"

2. 13F holdings changes (latest quarter):
    - "Bridgewater / Berkshire latest holdings"
    - "Hedge fund [target industry] holdings changes"

3. Industry expert perspectives:
    - "McKinsey / BCG / Gartner [target industry] trends"
```

**Institutional Consensus Scoring System:**
```
Unanimous Bullish (5 points): ≥80% institutions recommend overweight
Moderately Bullish (4 points): 60-79% institutions recommend overweight
Neutral (3 points): 40-59% institutions recommend overweight
Moderately Bearish (2 points): 20-39% institutions recommend overweight
Unanimous Bearish (1 point): <20% institutions recommend overweight
```

**Detailed Methods Reference:**
- `references/institutional/institutional-reports-tracking.md`
- `references/institutional/13f-holdings-analysis.md`
- `references/institutional/consensus-scoring-system.md`

**Output Format (Concise Version):**
```
## Institutional Consensus Tracking

### Top Investment Bank Views

- **J.P. Morgan:** [Core view] (source link)
- **Goldman Sachs:** [Core view] (source link)
- **BlackRock:** [Core view] (source link)

### Institutional Consensus Score

[Target Industry]: ⭐⭐⭐⭐ (4.2/5.0) - Moderately Bullish Consensus

### Key Findings

[3-5 key takeaways]
```

---

### Step 3: In-Depth Industry Analysis (Seven-Step Framework)

Execute standardized analysis for target industry:

1. **Industry Chain Breakdown** - Upstream, midstream, downstream value chain and profit distribution
2. **Supply-Demand Relationship Analysis** - Demand drivers, capacity utilization, inventory cycles
3. **Competitive Landscape Analysis** - Market concentration (HHI), leading company moats
4. **Technology & Policy Drivers** - Disruptive innovation, government subsidies and regulatory support
5. **Industry Valuation Levels** - P/E ratio historical percentile, relative valuation
6. **Leading & Lagging Indicators** - Set warning indicators and trigger conditions
7. **Bubble Risk Assessment** - Valuation, sentiment, fundamentals, institutional checklist

**Detailed Framework Reference:**
- `references/frameworks/seven-step-industry-analysis.md`
- `references/frameworks/supply-demand-framework.md`
- `references/frameworks/competitive-landscape-framework.md`
- `references/frameworks/bubble-risk-assessment.md`

**Output Format (Progressive Dialogue):**
```
## [Target Industry] In-Depth Analysis

### Industry Chain Structure

[Brief description of upstream, midstream, downstream, highlight key segments]

### Supply-Demand Status

- **Demand Drivers:** [Main growth momentum]
- **Supply Conditions:** [Capacity utilization/inventory levels]
- **Supply-Demand Score:** [1-10 points]

### Competitive Landscape

- **Market Concentration:** [High/Medium/Low]
- **Leading Companies:** [List top 3-5]
- **Entry Barriers:** [High/Medium/Low]

### Technology & Policy

- **Technology Trends:** [Key technological changes]
- **Policy Support:** [Government subsidies/regulatory impact]

### Valuation & Risk

- **Valuation Levels:** [Position relative to history/peers]
- **Bubble Risk:** [Low/Medium/High]

***
💡 **Want to dive deeper into any section?**
You can further ask:
- "Which segment of the industry chain has the highest profit?"
- "Who are the main competitors? Strengths and weaknesses analysis?"
- "What leading indicators can be tracked?"
```

---

### Step 4: Core Investment Trend Assessment (Dynamic Update)

**Real-time search and analysis of current hot trends:**

```
Search Strategy:

1. Current popular investment themes (past 1 month):
    - "2026 investment themes"
    - "2026 megatrends" "emerging sectors 2026"

2. Industry heat and capital flows:
    - "[Year] ETF fund flows"
    - "institutional investors [industry] allocation"

3. Policy and geopolitical drivers:
    - "US/China/EU industrial policy 2026"
    - "geopolitical impact [industry]"

4. Technology breakthroughs and innovation:
    - "breakthrough technology 2026"
    - "disruptive innovation [industry]"
```

**Trend Evaluation Framework:**
```
Score each identified trend:

1. Institutional Consensus (0-5 points): Top investment bank recommendation level
2. Policy Support (0-5 points): Government subsidies and regulatory strength
3. Technology Maturity (0-5 points): Commercialization progress
4. Market Size Potential (0-5 points): TAM and growth potential
5. Time Horizon (Short-term/Medium-term/Long-term): Trend sustainability

Total ≥ 18 points → Core Trend (⭐⭐⭐⭐⭐)
Total 15-17 points → Important Trend (⭐⭐⭐⭐)
Total 12-14 points → Watch Trend (⭐⭐⭐)
Total < 12 points → Observe Trend (⭐⭐)
```

**Detailed Analysis Reference:**
- `references/themes/trend-evaluation-framework.md` - Trend Evaluation Methodology
- `references/themes/policy-tracking.md` - Policy Tracking Guide
- `references/themes/technology-maturity-assessment.md` - Technology Maturity Assessment

**Output Format (Dynamically Generated):**
```
## Current Core Investment Trends (Based on Latest Search)

### 🔥 Core Trends (⭐⭐⭐⭐⭐)

1. **[Trend Name]**
    - Drivers: [Key momentum]
    - Institutional Consensus: [X/5] | Policy Support: [X/5] | Tech Maturity: [X/5]
    - Beneficiary Industries: [List 2-3]
    - Investment Timeline: [Short-term/Medium-term/Long-term]

2. **[Trend Name]**
    ...

### ⚡ Important Trends (⭐⭐⭐⭐)

[Same format as above]

### 👀 Emerging Trends (⭐⭐⭐)

[Early-stage but high-potential trends]

***
📊 **Data Sources:** [List main reference sources and timestamps]
💡 **Want to explore a specific trend?** Ask: "Detailed analysis of [Trend Name]"
```

---

### Step 5: Sector Rotation Strategy Formulation

**Rotation Timing Judgment (Trigger if any condition met):**
- Economic cycle stage transition
- Central bank policy stance shift
- Industry supply-demand relationship reversal
- Institutional consensus score change ≥1.0 point
- Key leading indicators turn for consecutive 2 months

**Dynamic Allocation Recommendations (Based on Current Environment):**
```
Based on Step 1 (Economic Environment) + Step 2 (Institutional Consensus) + Step 4 (Trend Assessment)
→ Generate industry allocation recommendations for current timepoint
```

**Detailed Strategy Reference:**
- `references/frameworks/sector-rotation-by-cycle.md`
- `references/frameworks/rotation-decision-checklist.md`

**Output Format (Concise Version):**
```
## Industry Allocation Recommendations (Based on [Date] Environment)

| Industry | Allocation Weight | Allocation Logic | Risk Alerts |
|----------|------------------|------------------|-------------|
| [Industry A] | 25-30% | [Core rationale] | [Main risks] |
| [Industry B] | 15-20% | [Core rationale] | [Main risks] |
| ... | ... | ... | ... |

### Rotation Signal Tracking

- ✅ [Triggered signals]
- ⏳ [Near-trigger signals]

***
💡 **Allocation Principles:**
- Single industry cap: 30%
- Top 3 combined: 60-70%
- Reserve 10-15% cash flexibility
```

---

### Step 6: Analysis Results Output (Progressive Presentation in Dialogue)

**Output Principles:**
- ✅ Present core results directly in dialogue (3-5 paragraphs)
- ✅ Use structured formats (tables/lists/scores)
- ✅ Provide interactive guidance for users to ask deeper questions
- ❌ Do not pre-generate complete multi-page reports

**Standard Output Structure (Concise Version):**
```markdown
# [Target Industry/Theme] Industry Research Analysis

## 📊 Executive Summary
- **Industry Rating:** [Buy/Hold/Watch/Reduce]
- **Institutional Consensus:** ⭐⭐⭐⭐ (4.2/5.0)
- **Industry Sentiment:** [1-10 points]
- **Allocation Recommendation:** [Overweight/Neutral/Underweight]
- **Investment Timeline:** [Short-term/Medium-term/Long-term]

## 🎯 Core Findings
[3-5 most important conclusions, each 1-2 sentences]

## 💼 Institutional Views Summary
[Top investment bank core views, 2-3 paragraphs]

## 📈 Industry Fundamentals
[Supply-demand/competitive landscape/valuation key data, presented in table format]

## ⚠️ Risk Alerts
[Main risk factors, 3-5 points]

## 🎬 Next Steps Recommendations
[Specific actionable suggestions]

***
## 💬 Want to Learn More?

You can continue asking:
- "Specific company recommendations in this industry?" → Trigger stage 3 stock analysis
- "Detailed industry chain upstream-downstream breakdown?" → Deep dive into industry chain
- "Compare with [other industry]?" → Multi-industry comparison analysis
- "Generate complete PDF report" → Trigger full report template
```

**Complete Report Template (Use only when explicitly requested):**

- `references/templates/industry-report-template.md` - 15-20 page in-depth report
- `references/templates/sector-comparison-template.md` - Multi-industry comparison report
- `references/templates/quick-insight-template.md` - 2-3 page quick insight

---

## Reference Documentation System

### Core Framework Documents (Must-Read)

**Analytical Methodology:**

- `references/frameworks/seven-step-industry-analysis.md`
- `references/frameworks/sector-rotation-by-cycle.md`
- `references/frameworks/supply-demand-framework.md`
- `references/frameworks/competitive-landscape-framework.md`

**Institutional Tracking:**

- `references/institutional/institutional-reports-tracking.md`
- `references/institutional/13f-holdings-analysis.md`
- `references/institutional/consensus-scoring-system.md`

**Trend Assessment:**

- `references/themes/trend-evaluation-framework.md`
- `references/themes/policy-tracking.md`
- `references/themes/technology-maturity-assessment.md`

**Data Sources:**

- `references/data-sources/industry-data-sources.md`
- `references/data-sources/leading-indicators.md`

**Practical Templates:**

- `references/templates/industry-report-template.md`
- `references/templates/quick-insight-template.md`
- `references/templates/rotation-decision-checklist.md`

### External Resources (Curated)

**Top Investment Bank Research:**

- [J.P. Morgan Markets](https://www.jpmorgan.com/insights/research)
- [Goldman Sachs Research](https://www.goldmansachs.com/insights/pages/top-of-mind.html)
- [Morgan Stanley Research](https://www.morganstanley.com/ideas)
- [BlackRock Investment Institute](https://www.blackrock.com/corporate/insights/blackrock-investment-institute)

**Complete Resource List:** `references/data-sources/external-resources.md`

---

## Frequently Asked Questions

**Q1: Can the module operate independently without prior macroeconomic analysis?**
Yes. The module will automatically search for latest economic data and environment assessment, quickly establishing background context.

**Q2: How to determine which lifecycle stage an industry is in?**
Use three indicators: revenue growth rate, market penetration rate, competitive landscape. See `references/frameworks/seven-step-industry-analysis.md` for details.

**Q3: How to ensure timeliness of trend analysis?**
Dynamically search for latest 1-3 months' institutional reports and market data with each execution, avoiding outdated information.

**Q4: What is the best timing for sector rotation?**
Leading the market by 1-2 months is optimal. Use rotation signal confirmation checklist (at least 3 conditions met). See `references/frameworks/rotation-decision-checklist.md` for details.

**Q5: How to avoid over-concentration in industry allocation?**
Use "331 allocation principle": single industry cap 30%, top three combined 60-70%, others diversified 30-40%.

**Q6: What if I need a complete report?**
Explicitly request in dialogue: "Generate complete industry research report", and the system will use standard template to produce 15-20 page in-depth analysis.
