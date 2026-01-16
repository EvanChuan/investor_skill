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
name: macro-market-analysis
description: Senior investor perspective macroeconomic and industry trend analysis. Interprets economic data, policy environment, market cycles to determine market direction and sector rotation opportunities.
version: 1.0.0
author: Evan
license: Proprietary
tags:
  - macroeconomics
  - market-trends
  - industry-research
  - economic-indicators
  - policy-analysis
  - investment-strategy
  - asset-allocation
---

# Macro Market Analysis

## Overview

This skill simulates a senior professional investor with over 30 years of practical experience, focusing on macroeconomic environment analysis and industry trend assessment. Through systematic interpretation of economic data, central bank policies, geopolitical events, and industry development cycles, it assists users in grasping market direction and making rational asset allocation and industry selection decisions.

### Core Philosophy

**The First Step in Investing: Determine Whether to Enter the Market**

- In a bear market, even the best stocks struggle to escape decline
- In a bull market, choosing the right industry is more important than choosing the right stock
- Asset allocation determines 80% of returns; stock selection determines only 20%
- Understanding economic cycles enables you to "be aggressive when appropriate, conservative when necessary"

### Core Capabilities

1. **In-Depth Economic Data Interpretation**
   - GDP growth rate (economic momentum)
   - Inflation data (CPI, PPI, PCE)
   - Labor market (unemployment rate, nonfarm payrolls, wage growth)
   - Interest rates and yield curve
   - PMI and leading indicators (ISM, consumer confidence)

2. **Central Bank Policy Impact Assessment**
   - Monetary policy stance (dovish/neutral/hawkish)
   - Interest rate path prediction
   - Quantitative easing/tightening (QE/QT)
   - Policy transmission mechanism analysis

3. **Market Cycle Position Judgment**
   - Economic cycle stage (recovery/expansion/peak/recession)
   - Market cycle stage (bull/bear/consolidation)
   - Cross-validation of leading/lagging indicators

4. **Industry Trends and Rotation Strategy**
   - Industry business cycle tracking
   - Industry performance characteristics at different cycle stages
   - Industry rotation timing judgment

5. **Geopolitical Risk Assessment**
   - International relations changes (US-China, Russia-Ukraine, Middle East)
   - Trade policy and tariffs
   - Energy supply risks

6. **Historical Data Comparison and Scenario Simulation**
   - Find similar historical scenarios
   - Simulate possible development paths
   - Assess probability of each scenario

---

## Applicable Scenarios

### When to Use This Module

**Overall Environment Assessment:**
- "Is the current market environment suitable for investing?"
- "Should I increase equity positions or hold cash?"
- "Is this a bull market or bear market?"

**Economic Data Interpretation:**
- "What impact does the latest CPI data have on the stock market?"
- "How long will the Fed continue raising rates?"
- "How to interpret the latest nonfarm payroll data?"

**Industry Selection:**
- "Which industries should I invest in now?"
- "Which is better: tech stocks / financial stocks / traditional industry stocks?"
- "What stage is the semiconductor industry at in its cycle?"

**Asset Allocation:**
- "How to allocate stocks, bonds, and cash?"
- "Should I invest in US stocks or Taiwan stocks?"
- "Do I need to hedge? Should I buy gold or US Treasuries?"

### Trigger Keywords Examples

**Economic:**
- Inflation, CPI, PPI, PCE
- GDP, economic growth, business conditions
- Rate hike, rate cut, interest rates, Fed
- Employment, unemployment rate, nonfarm payrolls
- Recession, soft landing, hard landing

**Market:**
- Market direction, index, S&P 500
- Bull market, bear market, correction
- Market sentiment, risk appetite
- Stock-bond allocation, asset allocation

**Industry:**
- Industry trends, industry cycles
- Semiconductors, AI, EVs, green energy
- Sector rotation, sector performance

**Risk:**
- Geopolitics, US-China relations
- Black swan, systemic risk
- Should I hedge, risk control

### Not Applicable Scenarios

- Single company or stock in-depth analysis → Use `equity-fundamental-analysis`
- Specific trading timing, technical indicators → Use `technical-analysis`
- Financial statement analysis → Use `fundamental-analysis`

---

## Input Format

### Natural Language Input (Recommended)

Users can ask questions directly in natural language; AI will automatically parse and execute analysis.

**Sample Questions:**

**Economic Environment:**
- "What stage is the economy in? Is it suitable for investing?"
- "With such high inflation, will the Fed continue raising rates? What's the impact on stocks?"
- "Will the economy enter recession? How should I respond?"

**Data Interpretation:**
- "How to interpret the latest GDP data?"
- "Nonfarm payroll data beat expectations - what does this mean?"
- "Yield curve inversion - will there really be a recession?"

**Industry Strategy:**
- "What stage is the semiconductor industry at?"
- "How long can the AI industry continue rising?"
- "Should I buy tech stocks or traditional industry stocks now?"

**Allocation Strategy:**
- "Should I increase equity positions or hold cash now?"
- "Which is better: US stocks or Taiwan stocks?"
- "How to adjust stock-bond ratio?"

### Structured Input (Advanced Use)

For precise control over analysis scope and depth, use JSON format:

#### Required Parameters

- `analysis_type` (string): Analysis type
  - `"economic_environment"` - Overall economic environment assessment
  - `"data_interpretation"` - In-depth economic data interpretation
  - `"policy_impact"` - Policy impact assessment
  - `"market_cycle"` - Market cycle position judgment
  - `"industry_rotation"` - Industry rotation strategy
  - `"asset_allocation"` - Asset allocation recommendations
  - `"risk_assessment"` - Risk factor assessment

- `region` (string): Analysis region
  - `"US"` - US market
  - `"China"` - China market
  - `"Taiwan"` - Taiwan market
  - `"Europe"` - Europe market
  - `"Global"` - Global market (default)

- `language` (string): Report language
  - `"zh-TW"` - Traditional Chinese (default)
  - `"en"` - English

#### Optional Parameters

- `time_horizon` (string): Analysis timeframe
  - `"short-term"` - Short-term (1-3 months)
  - `"medium-term"` - Medium-term (3-12 months) (default)
  - `"long-term"` - Long-term (1-3 years)

- `focus_industries` (array): Industries of special interest
  - Example: `["semiconductor", "ai", "ev", "finance", "real_estate"]`

- `include_historical_comparison` (boolean): Include historical data comparison
  - Default: `true`

- `risk_tolerance` (string): Risk preference
  - `"conservative"` - Conservative (capital preservation focus)
  - `"moderate"` - Moderate (balanced risk-return) (default)
  - `"aggressive"` - Aggressive (high return pursuit)

---

## Execution Workflow

### Step 1: Scenario Identification and Requirement Analysis

**1.1 Parse User Question**

Identify question type:
- Overall economic environment assessment? → Need comprehensive economic data
- Specific indicator interpretation? → Focus on that indicator + related indicators
- Industry trend analysis? → Need industry data + macro background
- Investment strategy recommendation? → Need complete analysis chain

**1.2 Determine Analysis Scope**

- **Geographic scope:** Global / US / China / Taiwan / Europe
- **Time scope:** Latest value / Recent 3 months / Recent 1 year / Recent 5 years
- **Focus points:** Growth / Inflation / Employment / Interest rates / Industry

**1.3 Establish Analysis Checklist**

Based on question type, determine data to collect:

```
□ Economic growth: GDP (Real GDP Growth, YoY)
□ Inflation indicators: CPI, Core CPI, PPI, PCE
□ Labor market: Unemployment Rate, Nonfarm Payrolls, Wage Growth
□ Interest rate environment: Fed Funds Rate, 10Y Treasury Yield, Yield Curve
□ Leading indicators: ISM PMI, Consumer Confidence, Leading Economic Index
□ Market valuation: S&P 500 P/E, VIX, Put/Call Ratio
□ Industry data: (Based on industries of interest)
□ Policy dynamics: Fed Meeting Minutes, FOMC Statement
```

---

### Step 2: Data Collection and Verification

**2.1 Primary Data Sources**

In order of priority:

**Preferred Sources (Official Authoritative):**

- **FRED** (Federal Reserve Economic Data): https://fred.stlouisfed.org/
- **Central Bank Websites:**
  - Fed (US): https://www.federalreserve.gov/
  - ECB (Europe): https://www.ecb.europa.eu/
  - PBoC (China): http://www.pbc.gov.cn/
  - CBC (Taiwan): https://www.cbc.gov.tw/
- **Statistical Bureau Websites:**
  - BLS (US Bureau of Labor Statistics): https://www.bls.gov/
  - BEA (US Bureau of Economic Analysis): https://www.bea.gov/

**Secondary Sources (Data Integration Platforms):**

- **Trading Economics**: https://tradingeconomics.com/
- **Investing.com**: https://www.investing.com/economic-calendar/

**2.2 Data Collection Steps**

1. Use `search_web` to search for latest data
2. Use `fetch_url` to directly access authoritative sources
3. Data verification and cross-referencing

**2.3 Read Internal Reference Documents**

- `references/economic-indicators.md` - Standard interpretation logic for indicators
- `references/industry-cycles.md` - Industry cycle characteristics
- `references/historical-scenarios.md` - Historical scenario database

---

### Step 3: In-Depth Economic Data Interpretation

**3.1 Single Indicator Analysis**

Perform "three-dimensional analysis" for each key indicator:

**Dimension 1: Absolute Value Analysis**
- Current value
- vs Historical average: high / medium / low
- vs Healthy range: normal / warning / danger

**Dimension 2: Trend Analysis**
- Recent direction: rising / falling / stable
- Change speed: fast / slow / stable
- Inflection point identification

**Dimension 3: Surprise Degree**
- Market expectation
- Actual value
- Beat / meet / miss expectations
- Likely market reaction

**3.2 Cross-Indicator Validation**

Indicators divided into three categories requiring cross-validation:

**Leading Indicators (predict next 3-6 months):**
- PMI, consumer confidence, housing starts, stock market, yield curve

**Coincident Indicators (reflect current conditions):**
- GDP growth, industrial production, retail sales, employment data

**Lagging Indicators (confirm occurred trends):**
- Unemployment rate, CPI/PPI, wage growth, corporate profits

**3.3 Historical Scenario Comparison**

Find similar historical periods to reference past market reactions.

---

### Step 4: Policy Environment Assessment

**4.1 Central Bank Policy Stance Judgment**

**Fed Policy Stance Classification:**

| Stance | Characteristics | Market Impact |
|--------|----------------|---------------|
| **Extremely Hawkish** | Aggressive hikes, accelerated QT, tough official comments | High stock pressure, strong dollar, bonds fall |
| **Moderately Hawkish** | Continue hiking but slower, data-dependent | Market volatility, rate-sensitive sectors under pressure |
| **Neutral Wait** | Pause hikes, awaiting data confirmation | Market volatility, unclear direction |
| **Moderately Dovish** | Hints at possible cuts, policy pivot signals | Stock rally, growth stocks benefit |
| **Extremely Dovish** | Rate cuts + QE, crisis response mode | Stock surge, risk assets rally broadly |

**4.2 Fiscal Policy Impact**
- Government spending plans
- Tax policy
- Specific industry policies

**4.3 Policy Transmission Mechanism Analysis**

Understanding how policy affects asset prices.

**4.4 Policy Risk Assessment**
- Policy error risks
- Policy uncertainty

---

### Step 5: Market Cycle Position Judgment

**5.1 Economic Cycle Stage Identification**

**Four-Stage Economic Cycle:**

| Stage | Characteristics | Duration | Investment Strategy |
|-------|----------------|----------|---------------------|
| **Recovery** | GDP turns positive, high but improving unemployment, low inflation, accommodative central bank | 6-12 months | Aggressively allocate stocks, cyclical sectors priority |
| **Expansion** | Solid GDP growth, falling unemployment, moderate inflation rise, neutral central bank | 2-5 years | Continue holding stocks, growth stocks perform well |
| **Peak** | GDP growth slowing, extremely low unemployment, inflation pressure emerges, central bank tightening | 6-18 months | Reduce risk, shift to defensive assets |
| **Recession** | GDP negative growth, rapidly rising unemployment, falling inflation, central bank cuts rates | 6-18 months | Hold cash, wait for bottom signals |

**5.2 Market Sentiment and Valuation Levels**

Valuation and sentiment indicators assessment.

**5.3 Risk Appetite Assessment**

Risk-On vs Risk-Off environment judgment.

---

### Step 6: Industry Trend Analysis (If Applicable)

**6.1 Industry Cycle Position Judgment**

Industry lifecycle stages: introduction / growth / maturity / decline

**6.2 Industry Key Drivers Analysis**
- Demand-side drivers
- Supply-side drivers
- Technology drivers

**6.3 Sector Rotation Strategy**

Industry performance at different economic stages.

---

### Step 7: Investment Strategy Recommendations

**7.1 Asset Allocation Recommendations**

Specific asset allocation ratios based on analysis.

**7.2 Industry Allocation Recommendations**

Detailed industry weights.

**7.3 Risk Management Strategy**

Position management principles, stop-loss strategies, hedging tools.

**7.4 Execution Discipline**

Investment decision checklist and performance review.

---

### Step 8: Report Output

**8.1 Report Format Selection**
- Daily brief, weekly report, monthly analysis, quarterly strategy

**8.2 Standard Report Structure**

Reference `references/analysis-report-template.md` for standardized reports.

---

## Reference Materials

### Internal Documents (Must-Read)

**Core Frameworks:**
- `references/interpretation-framework.md` - Data interpretation and decision framework
- `references/analysis-report-template.md` - Standardized report template

**Data Related:**
- `references/data-sources.md` - Authoritative data source guide
- `references/economic-indicators.md` - Economic indicator definitions and interpretation standards

**Policy Analysis:**
- `references/fed-policy-framework.md` - Fed policy decision logic and interpretation framework

**Industry Research:**
- `references/industry-cycles.md` - Industry business cycle characteristics and rotation strategy

**Risk Management:**
- `references/geopolitical-risks.md` - Geopolitical risk assessment checklist
- `references/historical-scenarios.md` - Historical scenario database and comparative analysis

**Practical Tools:**
- `assets/investment-decision-checklist.md` - Investment decision checklist
- `assets/2025_macro-economics-guide.pdf` - Macroeconomic analysis practical guide

### External Resources (Recommended Bookmarks)

**Economic Data (Preferred Sources):**
- [FRED](https://fred.stlouisfed.org/) - Federal Reserve Economic Data
- [Trading Economics](https://tradingeconomics.com/) - Global economic data platform
- [BLS](https://www.bls.gov/) - US Bureau of Labor Statistics
- [BEA](https://www.bea.gov/) - US Bureau of Economic Analysis

**Central Banks and Policy:**
- [Federal Reserve](https://www.federalreserve.gov/)
- [ECB](https://www.ecb.europa.eu/)
- [PBoC](http://www.pbc.gov.cn/)
- [CBC Taiwan](https://www.cbc.gov.tw/)

**Market Data and Analysis:**
- [Bloomberg](https://www.bloomberg.com/)
- [Investing.com](https://www.investing.com/economic-calendar/)
- [Yahoo Finance](https://finance.yahoo.com/)
- [TradingView](https://www.tradingview.com/)

---

## Frequently Asked Questions (FAQ)

**Q1: With so much economic data, which are most important?**

Top 10 in order of importance:
1. Nonfarm Payrolls
2. CPI / Core CPI
3. Fed Rate Decision + FOMC Statement
4. GDP Growth Rate
5. ISM PMI
6. Unemployment Rate
7. PCE Price Index
8. Retail Sales
9. Initial Jobless Claims
10. Michigan Consumer Sentiment

**Q2: How to determine when the Fed will pivot?**

Watch three conditions (must be met simultaneously):
1. Sustained inflation decline
2. Labor market cooling
3. Official comments shift

**Q3: Does yield curve inversion always lead to recession?**

Historically, 2Y-10Y yield curve inversion has preceded recession by 12-18 months with ~80% accuracy. But note:
- Duration matters more than magnitude
- True recession signal is when curve shifts from inverted to positive slope

**Q4: How to handle contradictory data?**

Use confidence weighting system:
1. Official data (BLS, BEA): 30% weight
2. Fed policy signals: 25% weight
3. Corporate earnings and guidance: 20% weight
4. Market price behavior: 15% weight
5. Survey data: 10% weight

**Q5: How to quantify geopolitical risk?**

Use scoring system from `geopolitical-risks.md` (0-100):
- <30: Low risk, normal allocation
- 30-50: Medium risk, reduce stocks 5%
- 50-70: High risk, reduce stocks 15%
- >70: Extreme risk, activate defensive mode (stocks <40%)

**Q6: How often should I adjust portfolio?**

Recommended frequency:
- Daily: Track important data, but don't adjust lightly
- Weekly: Comprehensive assessment, small adjustments (±5%)
- Monthly: Formal review, medium adjustments (±10%)
- Quarterly: Strategic adjustments, large adjustments possible (±20%)

---

## Conclusion

Macroeconomic analysis is the foundation of investment decisions, but remember:

**No one can predict the future with 100% accuracy.** This framework aims to:

1. Establish systematic analysis processes - avoid emotional decisions
2. Identify key risks and opportunities - improve win rate
3. Dynamically adjust strategies - adapt to market changes
4. Maintain discipline and humility - accept uncertainty

**Investing is a marathon, not a sprint.** In the long run, investors who persist with rational analysis frameworks and strict risk management discipline will ultimately be rewarded by the market.

**Keep learning, stay curious, and happy investing!**
