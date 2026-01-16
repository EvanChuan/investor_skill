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
name: equity-fundamental-analysis
description: In-depth evaluation of individual company investment value. Through systematic analysis of business operations, customer base, business model, competitive advantages, financial health, management quality, product development, and operational risks, produce structured fundamental analysis scores and investment recommendations. Suitable for comprehensive company research before medium to long-term investment decisions.
version: 1.0.0
license: Proprietary
author: Evan
tags:
  - fundamental-analysis
  - equity-research
  - company-valuation
  - financial-analysis
  - investment-research
---

# Equity Fundamental Analysis

## Overview

This skill assists investors in systematically evaluating the investment value of individual companies through seven core analytical dimensions, conducting in-depth research on business fundamentals, competitive positioning, financial health, management capabilities, and potential risks, ultimately producing quantitative scores and specific investment recommendations.

**Core Value:**
Transform senior investors' company research methodology into a repeatable analytical process, ensuring each evaluation covers critical elements and avoids missing important risks or opportunities.

**Applicable Scenarios:**
- Need for in-depth research on specific stocks (pre-purchase / holding review / selling evaluation)
- Need for standardized company analysis reports
- Need to compare fundamental strengths of different companies in the same industry
- Need to identify key risks and growth drivers of a company

**Not Applicable Scenarios:**
- Short-term trading (this analysis focuses on medium to long-term value assessment)
- Pure technical analysis trading decisions
- Non-listed companies lacking public financial information

---

## Analytical Framework

This skill employs seven core analytical dimensions for progressive evaluation:

### 1. Business Understanding Analysis

**Objective:** Clearly understand what the company does, who they sell to, and how they make money

**Core Questions:**
- What does this company do? Can it be explained in one sentence?
- What are the business segments? What percentage of revenue does each account for?
- What is the function of the products/services? Is there genuine market demand?
- Who are the main customers? Are there well-known major clients or government contracts?
- Is customer demand real or inventory stockpiling behavior?

**Analytical Methods:**
- Browse company website to confirm business operations and product lines
- Review latest annual/quarterly reports and earnings calls to understand revenue structure
- Identify main customer groups and market positioning
- Evaluate authenticity and sustainability of product market demand

**Output Content:**
- Business description (1-2 paragraphs, clear and understandable)
- Product/service matrix (product name, function, target customers, revenue share)
- Major customer list and order nature
- Business understanding score (1-10 points)

> **Detailed Guide:** Reference `references/business-understanding-guide.md`

---

### 2. Business Model and Competitive Advantage Analysis

**Objective:** Evaluate the company's profit model, moat, and competitive position

**Core Questions:**
- What is the company's business model? How do they make money?
- Where are the competitive advantages? Is there an economic moat?
- Does the company possess key technologies, patents, or unique resources?
- How does it perform compared to competitors? Who is more profitable? Who is more favored by government/market?

**Analytical Content:**
- Business model breakdown (revenue sources, cost structure, gross margin levels)
- Moat assessment (network effects, switching costs, cost advantages, intangible assets, scale advantages)
- Competitor financial comparison (revenue, profitability, ROE, market share)
- Competitive position (leader / challenger / follower / niche player)

**Output Content:**
- Business model diagram (revenue sources and cost structure)
- Moat score (1-10 points) and type description
- Competitor comparison table
- Competitive advantage score (1-10 points)

> **Detailed Guide:** Reference `references/moat-analysis-framework.md`

---

### 3. Financial Health Analysis

**Objective:** Evaluate company's financial health, profitability quality, and growth potential

**Core Questions:**
- Is the company's financial health sound?
- Is profitability stable? How is the growth?
- Is cash flow sufficient? Is revenue quality high?
- What is the quality of accounts receivable and inventory?

**Analytical Framework:**

#### 3.1 Income Statement Analysis
- Revenue growth rate (YoY, QoQ, 3-year CAGR)
- Gross margin, operating margin, net margin trends
- EPS growth and non-operating income proportion

#### 3.2 Balance Sheet Analysis
- Current ratio, quick ratio (short-term solvency)
- Debt ratio (financial leverage risk)
- ROE, ROA (capital utilization efficiency)

#### 3.3 Cash Flow Statement Analysis
- Operating cash flow (positive and continuously growing)
- Free cash flow (FCF = Operating Cash Flow - Capital Expenditure)
- Revenue cash content (Operating Cash Flow / Revenue)

#### 3.4 Profitability Quality Assessment
- Accounts receivable turnover rate (risk of false revenue)
- Inventory turnover rate (risk of inventory impairment)
- Three-statement reconciliation (consistency of income statement, balance sheet, cash flow statement)

**Output Content:**
- Financial indicators summary table (3-5 year trends)
- Profitability quality score (1-10 points)
- Financial health rating (Excellent / Good / Fair / Poor)
- Key financial risk alerts

> **Detailed Guide:** Reference `references/financial-analysis-metrics.md`

---

### 4. Management and Corporate Governance Analysis

**Objective:** Evaluate management capabilities, integrity, and corporate governance standards

**Core Questions:**
- How are management capabilities and integrity?
- Does the leader have industry influence?
- Is corporate governance sound? Is information transparent?
- How to track management dynamics? Which social media to follow?

**Evaluation Dimensions:**
- Leader background and capabilities (educational background, industry experience, industry reputation)
- Corporate governance structure (board composition, ownership structure, related party transactions)
- Information transparency (earnings call quality, annual report detail)
- Tracking channels (social media, industry interviews, investor relations page)

**Output Content:**
- Management capability score (1-10 points)
- Corporate governance rating (Excellent / Good / Fair / Poor)
- Key personnel introduction
- Tracking recommendations (earnings call dates, social media accounts, industry conferences)

> **Detailed Guide:** Reference `references/management-evaluation-guide.md`

---

### 5. Product Development and Future Roadmap Analysis

**Objective:** Understand product lifecycle, technological breakthroughs, and future growth potential

**Core Questions:**
- What lifecycle stage is the product at?
- Are there new products or technological breakthroughs?
- What is the next new product? When will it be launched?
- How do consumers/market evaluate the product?

**Tracking Content:**
- Existing product maturity (introduction / growth / maturity / decline)
- New product development progress and market potential
- Technological breakthroughs, patent applications, and R&D investment
- Consumer reviews and market response (reviews, sales data)

**Output Content:**
- Product lifecycle positioning
- Product development score (1-10 points)
- Future product roadmap
- Technological competitiveness assessment

> **Detailed Guide:** Reference `references/product-lifecycle-analysis.md`

---

### 6. Event-Driven Factors Tracking

**Objective:** Identify key events that may affect stock price and investment opportunities

**Core Questions:**
- What important events might affect company performance recently?
- When is the earnings release date? What are the earnings expectations?
- Are there major investments such as M&A, capacity expansion, or new factory construction?
- Are there investment opportunities with asymmetric risk-return?

**Key Tracking Events:**
- Earnings release dates (quarterly reports, annual reports, earnings calls)
- Shareholder meetings (strategy disclosure, shareholder Q&A)
- New product launches (technological breakthroughs, market response)
- Production expansion / new factory construction progress (affecting future capacity)
- Industry conferences / major announcements by leading companies
- M&A integration, regulatory changes, litigation disputes

**Output Content:**
- Recent key event calendar (including dates and potential impacts)
- Event-driven investment opportunity identification
- Risk/reward assessment

> **Detailed Guide:** Reference `references/event-driven-checklist.md`

---

### 7. Operational Risk Assessment

**Objective:** Identify main risks faced by the company and response strategies

**Core Questions:**
- What are the main risks faced by the company?
- What is the probability and impact of these risks?
- Are there any fatal risks that cannot be tolerated?
- Are risks already reflected in the stock price?

**Risk Categories:**

#### 7.1 Operational Risks
- Customer concentration risk (top 5 customers account for >50%)
- Supply chain disruption risk
- Insufficient or excess capacity
- Technological lag or disruption

#### 7.2 Financial Risks
- Excessive debt (debt ratio >70%)
- Interest rate risk, exchange rate risk
- Liquidity risk (short-term solvency)

#### 7.3 Industry Risks
- Industry business cycle
- Technological revolution impact
- Intensified competition, price wars

#### 7.4 Macro and Governance Risks
- Policy and regulatory changes
- Geopolitical risks
- Corporate governance issues (related party transactions, financial fraud)

**Output Content:**
- Risk rating (Low / Medium / High)
- Main risk list (top 5 items)
- Risk matrix diagram (probability × impact)
- Risk response recommendations

> **Detailed Guide:** Reference `references/risk-assessment-matrix.md`

---

## Usage

### Input Format

```json
{
  "analysis_type": "fundamental_analysis",
  "ticker": "2330.TW",
  "company_name": "台積電 (TSMC)",
  "analysis_date": "2026-01-16",
  "language": "zh-TW",
  "depth": "comprehensive",
  "compare_peers": true,
  "peer_tickers": ["UMC", "ASX"]
}
```

**Parameter Descriptions:**

- `ticker`: Stock ticker (required)
- `company_name`: Company name (optional, for search convenience)
- `depth`: Analysis depth (`basic` / `comprehensive`)
- `compare_peers`: Whether to perform peer comparison (`true` / `false`)
- `peer_tickers`: Competitor stock tickers (if compare_peers = true)

---

## Output Format

### Complete Analysis Report Structure

```markdown
# [Company Name] Fundamental Analysis Report

**Analysis Date:** YYYY-MM-DD  
**Stock Ticker:** XXXX  
**Industry Classification:** XXXX  
**Analyst:** Senior Investor AI

***

## Executive Summary

[3-5 sentences summarizing investment value and key findings]

- **Fundamental Score:** X/10
- **Investment Recommendation:** Buy / Hold / Watch / Sell
- **Key Strengths:** [1-2 items]
- **Main Risks:** [1-2 items]
- **Target Price Range:** XXX - XXX (reference only)

***

## 1. Business Operations

### 1.1 Business Description
[Explain what the company does in plain language]

### 1.2 Product/Service Matrix
| Product Name | Function | Target Customers | Revenue Share |
|--------------|----------|------------------|---------------|
| ...          | ...      | ...              | ...           |

### 1.3 Major Customers and Orders
- Notable clients: [list]
- Government contracts: [yes/no, scale]
- Customer demand assessment: [genuine demand / stockpiling behavior]

**Business Understanding Score:** X/10

***

## 2. Business Model and Competitive Advantage

### 2.1 Business Model
[Revenue sources, cost structure, gross margin levels]

### 2.2 Moat Assessment
- **Moat Type:** [Network effects / Switching costs / Cost advantages / Intangible assets / Scale advantages]
- **Moat Strength:** X/10
- **Description:** [Why there is a moat]

### 2.3 Competitor Comparison
| Company | Revenue (billion) | Gross Margin | Net Margin | ROE | Market Share |
|---------|------------------|--------------|------------|-----|--------------|
| This Company | ... | ... | ... | ... | ... |
| Competitor A | ... | ... | ... | ... | ... |
| Competitor B | ... | ... | ... | ... | ... |

**Competitive Position:** [Leader / Challenger / Follower / Niche]  
**Competitive Advantage Score:** X/10

***

## 3. Financial Health Analysis

### 3.1 Income Statement Key Indicators (Past 3-5 Years)
| Item | 2025 | 2024 | 2023 | Trend |
|------|------|------|------|-------|
| Revenue Growth Rate | X% | X% | X% | ↑/→/↓ |
| Gross Margin | X% | X% | X% | ↑/→/↓ |
| Operating Margin | X% | X% | X% | ↑/→/↓ |
| Net Margin | X% | X% | X% | ↑/→/↓ |
| EPS | X | X | X | ↑/→/↓ |

### 3.2 Balance Sheet Key Indicators
| Item | Value | Standard | Assessment |
|------|-------|----------|-----------|
| Current Ratio | X% | >150% | ✓/✗ |
| Quick Ratio | X% | >100% | ✓/✗ |
| Debt Ratio | X% | <50% | ✓/✗ |
| ROE | X% | >15% | ✓/✗ |
| ROA | X% | >10% | ✓/✗ |

### 3.3 Cash Flow and Profitability Quality
- Operating Cash Flow: XXX billion (YoY +/-X%)
- Free Cash Flow: XXX billion
- Revenue Cash Content: XX% (Operating Cash Flow/Revenue)
- Accounts Receivable Turnover Days: XX days
- Inventory Turnover Days: XX days

**Financial Health Score:** X/10  
**Rating:** Excellent / Good / Fair / Poor

***

## 4. Management and Corporate Governance

### 4.1 Key Leaders
- **CEO:** [Name, background, industry status]
- **Management Team:** [Key member profiles]

### 4.2 Corporate Governance
- Independent director ratio: X%
- Major shareholder holdings: X%
- Management holdings: X%
- Information transparency: High / Medium / Low

### 4.3 Tracking Recommendations
- Earnings calls: [Date / Link]
- Industry conferences: [Name / Date]
- Social media tracking: [Twitter / LinkedIn / Official blog]

**Management Score:** X/10  
**Governance Rating:** Excellent / Good / Fair / Poor

***

## 5. Product Development and Future Roadmap

### 5.1 Product Lifecycle
- Main product: [Product name] ([Growth / Maturity / Decline])
- New product: [Product name] (Expected YYYY-Q# launch)
- Technological breakthrough: [Description]

### 5.2 Market Evaluation
- Consumer review: [Positive / Neutral / Negative]
- Market penetration rate: X%
- Future growth potential: [High / Medium / Low]

**Product Development Score:** X/10

***

## 6. Event-Driven Factors

### 6.1 Recent Key Events
| Date | Event | Potential Impact | Importance |
|------|-------|-----------------|-----------|
| YYYY-MM-DD | Earnings Release | [Earnings expectation] | High/Med/Low |
| YYYY-MM-DD | New Product Launch | [Market potential] | High/Med/Low |
| YYYY-MM-DD | Capacity Expansion | [Capacity increase X%] | High/Med/Low |

### 6.2 Investment Opportunity Identification
- [Whether there are opportunities with asymmetric risk-return]
- [Description]

***

## 7. Risk Assessment

### 7.1 Main Risk List
1. **[Risk Name]** (Probability: High/Med/Low, Impact: High/Med/Low)
   - Description: [Detailed description]
   - Response: [Recommendation]

2. **[Risk Name]** (Probability: High/Med/Low, Impact: High/Med/Low)
   - Description: [Detailed description]
   - Response: [Recommendation]

[List up to top 5 key risks]

### 7.2 Risk Matrix
| Risk | Probability | Impact | Overall Rating |
|------|------------|--------|----------------|
| ... | ... | ... | ... |

**Risk Rating:** Low / Medium / High

***

## 8. SWOT Analysis

| Strengths | Weaknesses |
|-----------|------------|
| - [Strength 1] | - [Weakness 1] |
| - [Strength 2] | - [Weakness 2] |

| Opportunities | Threats |
|--------------|---------|
| - [Opportunity 1] | - [Threat 1] |
| - [Opportunity 2] | - [Threat 2] |

***

## 9. Comprehensive Evaluation and Investment Recommendation

### 9.1 Score Summary
| Evaluation Item | Score | Weight | Weighted Score |
|----------------|-------|--------|----------------|
| Business Understanding | X/10 | 15% | X.X |
| Competitive Advantage | X/10 | 25% | X.X |
| Financial Health | X/10 | 25% | X.X |
| Management Quality | X/10 | 15% | X.X |
| Product Development | X/10 | 10% | X.X |
| Risk Control | X/10 | 10% | X.X |

**Fundamental Overall Score:** X.X/10

### 9.2 Investment Recommendation
- **Rating:** Buy / Hold / Watch / Sell
- **Rationale:** [3-5 sentences explaining]
- **Suitable Investors:** [Value / Growth / Income]
- **Suggested Position:** X-X% of portfolio

### 9.3 Follow-up Focus Points
- [Tracking item 1]
- [Tracking item 2]
- [Tracking item 3]

***

**Disclaimer:** This analysis is for reference only and does not constitute investment advice. Investment decisions should be based on individual risk tolerance and comprehensive research.
```

---

## Scoring Criteria

Each dimension uses a 1-10 point scale:

- **9-10 points:** Excellent level, industry-leading, clear long-term competitive advantage
- **7-8 points:** Superior level, healthy fundamentals, solid competitiveness
- **5-6 points:** Average level, stable performance, no obvious advantages or disadvantages
- **3-4 points:** Below average, notable problems or risks exist
- **1-2 points:** Serious problems, deteriorating fundamentals, high risk

---

## Reference Materials

For detailed analytical methods, scoring standards, and case examples for this skill, please refer to the following documents:

- `references/business-understanding-guide.md` - Business Operations Analysis Guide
- `references/moat-analysis-framework.md` - Economic Moat Assessment Framework
- `references/financial-analysis-metrics.md` - Financial Indicator Interpretation Manual
- `references/management-evaluation-guide.md` - Management Evaluation Criteria
- `references/product-lifecycle-analysis.md` - Product Lifecycle Analysis
- `references/event-driven-checklist.md` - Event-Driven Investment Checklist
- `references/risk-assessment-matrix.md` - Risk Assessment Matrix Tool
- `references/case-studies.md` - Actual Case Study Examples

---

## Version History

- **v1.0.0** (2026-01-16) - Initial version, established seven analytical dimensions framework
