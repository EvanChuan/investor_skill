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
name: valuation-analysis
description: |
  Stage 4: Valuation & Margin of Safety.
  After completing macro environment, industry positioning, and company fundamental assessments, systematically determine stock price levels, fair value ranges, and margin of safety, outputting specific price ranges and actionable recommendations.
version: 1.0.0
author: Evan
license: Proprietary
tags:
  - valuation
  - margin-of-safety
  - equity-analysis
  - investment-strategy
  - fundamental-analysis
---

# Valuation & Margin of Safety Skill

## Skill Overview

This skill is used for "Stage 4: Valuation & Margin of Safety", assuming users have completed:
- Stage 1: Macro Market Analysis
- Stage 2: Industry Research & Rotation
- Stage 3: Fundamental Analysis

The goal is to answer four core questions:
1. Is this stock currently expensive or cheap?
2. What is the fair value range?
3. How significant is the downside risk?
4. At what price can buying begin?

The output includes target price ranges, current price rating, recommended actions, and margin of safety percentage.

---

## Input Format

Supports two main usage scenarios:

1. Natural language commands
2. Structured JSON (convenient for program/skill integration)

### 1. Natural Language Examples

- "幫我用估值框架分析 TSLA，評估目前價位的貴賤，給出保守/中性/樂觀目標價與安全邊際。"
  (Use valuation framework to analyze TSLA, assess current price level, provide conservative/neutral/optimistic target prices and margin of safety)

- "請用相對估值 + DCF 檢查這家公司現在是否有 30% 以上的安全邊際，並給出操作建議。"
  (Use relative valuation + DCF to check if this company has >30% margin of safety and provide recommendations)

- "幫我針對這間成長股做估值分析，參考同業 P/E、P/S 與未來 3 年成長率。"
  (Perform valuation analysis for this growth stock, referencing peer P/E, P/S, and next 3-year growth rates)

### 2. Structured JSON Input

For complete JSON input format and field descriptions, refer to `templates/valuation-input-schema.json`.

Simplified example:

```json
{
  "ticker": "TSLA",
  "company_name": "Tesla Inc.",
  "current_price": 230.5,
  "business_model": "growth",
  "time_horizon": "3-5Y",
  "methods": {
    "relative_valuation": true,
    "absolute_valuation_dcf": true,
    "asset_valuation": false
  },
  "reference_context": {
    "macro_view": "soft-landing",
    "industry_cycle": "expansion",
    "company_quality": "high"
  }
}
```

---

## Analysis Workflow

The valuation analysis process consists of five main steps, with tools and weights dynamically selected based on company type and data completeness.

> **Before starting analysis, it's recommended to review `references/valuation-checklist.md` to ensure data preparation is complete.**

### Step 1: Define Valuation Premises and Scenarios

1. **Verify Input Conditions**
    - Confirm ticker, currency, industry, business model (growth stock / value stock / cyclical stock / high dividend).
    - Check if current stock price, total market cap, basic financial ratios are complete.

2. **Establish Valuation Scenarios**
    - Time horizon: Short-term (within 1 year) vs Medium-term (3–5 years) vs Long-term (5+ years).
    - Risk tolerance: Conservative / Moderate / Aggressive.
    - Macro and industry premises: Reference conclusions from previous stages (economic position, interest rate environment, industry cycle).

3. **Classify Company Type**
    - Mature stable cash flow: Suitable for DCF, DDM, historical valuation comparison.
    - High growth but volatile: Emphasize PEG, EV/EBITDA, growth-adjusted P/S.
    - Asset-intensive / cyclical stocks: Consider asset value method, liquidation value, replacement cost.

> If input information is insufficient, prompt user to supplement or guide to use valuation assumption templates in references.

---

### Step 2: Relative Valuation Analysis

Use relative valuation metrics to answer "Compared to history and peers, is it expensive or cheap now?"

1. **Historical Valuation Comparison**
    - Obtain company's historical P/E, P/B, EV/EBITDA, P/S distribution (range: past 3 or 5 years).
    - Mark current position: Low range (historical 0–25% percentile), Mid range (25–75%), High range (75–100%).
    - If company growth rate changes significantly, adjust reference weight for historical valuation.

2. **Peer Valuation Comparison**
    - Select peer group from same industry + similar business model.
    - Compare:
        - P/E vs peer average + company growth rate
        - EV/EBITDA vs peers
        - P/B vs company ROE (high ROE can accept higher P/B)
        - PEG (P/E ÷ EPS growth rate) within reasonable range (around 1 or industry-adjusted).
    - Assign premium or discount rating based on company quality (moat, profit stability).

3. **Establish Relative Valuation Fair Range**
    - Based on peer and historical data, derive reasonable multiple ranges:
        - Conservative multiple: Peer lower quartile or historical lower percentile, discount further if necessary.
        - Neutral multiple: Peer median or historical median.
        - Optimistic multiple: Peer upper quartile or historical upper percentile, only for scenarios with clear growth support.

4. **Convert Multiples to Price Ranges**
    - Use EPS, BVPS, EBITDA and other corresponding metrics to calculate stock price ranges for the three valuations.

> For interpretation of each metric and common ranges, detailed explanations are in `references/relative-valuation.md`.

---

### Step 3: Absolute Valuation Analysis

Through DCF and DDM (when applicable) estimate company's intrinsic value, answering "If cash flows are discounted, what is this company worth?"

1. **DCF (Discounted Cash Flow)**
    - Determine valuation period: Typically 5–10 year valuation period + terminal value.
    - Cash flow selection: FCF to Firm or FCF to Equity, depending on data and purpose.
    - Main inputs:
        - Revenue growth rate assumptions (divided into early high growth + later convergence phases).
        - Profit margin and FCF Margin evolution.
        - Capital expenditure and reinvestment needs.
        - Discount rate (WACC or cost of equity).
        - Terminal growth rate (long-term steady state, usually close to long-term nominal GDP / inflation + real growth).
    - Establish three scenarios: conservative / base / optimistic, output intrinsic value per share.

2. **DDM (Dividend Discount Model)**
    - Only applicable to companies with stable dividends and predictable dividend policies.
    - Establish dividend growth rate assumptions and discount rate, calculate theoretical value.
    - Cross-check DDM results with DCF/relative valuation.

3. **Model Sensitivity Testing**
    - Review valuation sensitivity to discount rate and long-term growth rate.
    - Mark key variables where valuation is most sensitive, prompt users to track subsequently.

> Specific DCF / DDM templates, commonly used discount rates and growth rate ranges are in `references/absolute-valuation.md`.

---

### Step 4: Asset Value and Downside Protection

Use asset-side and liquidation value to assess downside risk, answering "In worst case, what is this company worth at minimum?"

1. **Asset Value Method**
    - Assess identifiable assets:
        - Cash and equivalents.
        - Financial assets and investment positions.
        - Land, plant, and equipment (consider depreciation and revaluation).
        - Intangible assets (brands, patents) usually treated conservatively.
    - Establish "Adjusted Book Value" and estimate value per share based on assets.

2. **Liquidation Value / Replacement Cost**
    - For asset-intensive, cyclical stocks, or distressed companies, use discounted asset value.
    - Consider: inventory discount, equipment depreciation, disposal costs, debt repayment priority.
    - Provide rough "worst-case value per share" range.

3. **Combine Debt Structure**
    - Check debt ratio, debt maturity structure, and interest coverage ratio.
    - Determine if shareholder residual equity still has margin of safety under stress scenarios.

> More detailed asset adjustment methods can be found in `references/asset-valuation.md`.

---

### Step 5: Integrate Valuation Results and Margin of Safety

Integrate relative valuation, absolute valuation, and asset value into one set of "actionable" price ranges and ratings.

1. **Integrate Different Valuation Methods**
    - Establish valuation matrix:
        - Relative valuation (multiples method) → Price range A
        - Absolute valuation (DCF/DDM) → Price range B
        - Asset/liquidation value → Price floor C
    - Set weights based on company type and data reliability, calculate comprehensive fair value range.

2. **Target Price Ranges (Conservative / Neutral / Optimistic)**
    - Conservative target price: Lean toward asset value + relative valuation low end + DCF conservative scenario.
    - Neutral target price: Median of concentrated ranges from most methods.
    - Optimistic target price: Growth and positive assumptions more optimistic but still reasonably supported.

3. **Margin of Safety Calculation**
    - Using "neutral target price" as baseline:
        - Margin of Safety = (Neutral Target Price − Current Stock Price) ÷ Neutral Target Price.
    - Can also calculate margin of safety relative to "conservative target price" as needed.
    - Grade margin of safety:
        - ≥ 40%: Deep margin of safety.
        - 20–40%: Sufficient margin of safety.
        - 10–20%: Limited margin of safety.
        - < 10%: Insufficient or no margin of safety.

4. **Current Price Rating**
    - Severely undervalued: Current price significantly below conservative target, no structural fundamental deterioration.
    - Undervalued: Current price below neutral target, clear margin of safety.
    - Fair: Current price near neutral target ± certain range.
    - Overvalued: Current price significantly above neutral target, requires very optimistic growth assumptions to be reasonable.
    - Severely overvalued: Current price above optimistic target, or requires unrealistic assumptions.

5. **Actionable Recommendation**
    - Aggressive Buy: Severely undervalued + margin of safety ≥ 40%, and liquidity & risk controllable.
    - Buy on Dips: Undervalued + margin of safety 20–40%, suitable for gradual accumulation.
    - Hold: Fair valuation, good company quality, no clear reason to add or reduce.
    - Take Profit on Rallies: Overvalued range, recommend gradual profit-taking or position reduction.
    - Sell: Severely overvalued or fundamental deterioration, risk-reward no longer reasonable.

---

## Output Format

Output is divided into "Summary Conclusion" and "Detailed Explanation" for progressive disclosure in conversation.

### 1. Summary Conclusion

- Target price ranges (conservative / neutral / optimistic)
- Current price rating
- Margin of safety percentage
- Recommended action
- One-sentence rationale (integrating macro, industry, and company fundamentals)

Example (natural language):

> - Conservative target price: approximately 180–190.
> - Neutral target price: approximately 210.
> - Optimistic target price: approximately 240.
> - Current stock price 185, belongs to "undervalued" range, margin of safety approximately 12%.
> - Recommended action: Buy on dips, gradual accumulation.

### 2. Detailed Explanation

Breakdown by sections:

1. **Relative Valuation Results**
    - Historical multiples position, peer comparison, PEG assessment.

2. **Absolute Valuation Results**
    - DCF/DDM three scenarios' key assumptions and valuations.
    - Sensitivity to discount rate and long-term growth rate.

3. **Asset and Downside Analysis**
    - Adjusted book value, liquidation value range, debt pressure.

4. **Risks and Trigger Conditions**
    - Which variables, if deviating from assumptions, require valuation re-examination (e.g., growth slowdown, interest rate changes).

5. **Recommended Actions and Execution Strategy**
    - Recommended buying range, staged entry points, risk management tips.

### 3. Structured Output (JSON)

For programmatic processing or integration with other systems, can output structured JSON format.

For complete JSON output format, refer to `templates/valuation-output-schema.json`.

---

## Quality Control & Checklist

**Before completing valuation analysis, please review:**

- `references/valuation-checklist.md`
    - Data preparation checklist
    - Valuation method execution checklist
    - Valuation results verification checklist
    - Risk assessment checklist
    - Report output checklist
    - Common errors self-check list

This checklist ensures completeness, consistency, and reliability of valuation analysis.

---

## References

Detailed formulas, common parameters, and case studies are in the following reference documents:

- `references/relative-valuation.md`
    - P/E, P/B, PEG, EV/EBITDA, P/S metric descriptions and common ranges
    - Typical valuation ranges and pitfalls for different industries

- `references/absolute-valuation.md`
    - DCF and DDM modeling steps
    - Discount rate estimation, terminal value treatment, and sensitivity analysis

- `references/asset-valuation.md`
    - Asset adjustment and liquidation value estimation methods
    - Practical considerations for cyclical and asset-heavy stock valuation

- `references/valuation-checklist.md`
    - Five major valuation analysis checklists
    - Common errors and avoidance methods

- `templates/valuation-output-schema.json`
    - Standardized JSON output format
    - Field definitions and examples

---

## Usage Tips

1. **Progressive Analysis**: Can start with quick relative valuation assessment, then dive into DCF and asset analysis as needed.

2. **Multi-method Cross-validation**: Single method prone to bias, use at least 2-3 methods.

3. **Dynamically Adjust Weights**: Growth stocks emphasize DCF and PEG, value stocks emphasize P/B and asset value, cyclical stocks emphasize EV/EBITDA and historical valuation.

4. **Regular Re-evaluation**: When market environment, industry cycle, and company fundamentals change, should re-evaluate.

5. **Risk First**: Valuation is always a product of assumptions, risk management is more important than precise valuation.

---

**Version History**

- v1.0.0 (2026-01-15): Initial release, integrated five-step valuation process and complete reference documentation system
