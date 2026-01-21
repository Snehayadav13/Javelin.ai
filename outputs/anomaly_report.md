# JAVELIN.AI - Anomaly Detection Report

*Generated: 2026-01-21 15:27:40*

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Anomalies Detected | 2428 |
| Sites with Anomalies | 1451 |
| Critical Anomalies | 747 |
| High Severity Anomalies | 479 |
| Medium Severity Anomalies | 1202 |

---

## Anomaly Distribution by Type

- **PATTERN_ANOMALY**: 1885 anomalies
- **STATISTICAL_OUTLIER**: 451 anomalies
- **CROSS_STUDY_ANOMALY**: 70 anomalies
- **VELOCITY_ANOMALY**: 19 anomalies
- **REGIONAL_ANOMALY**: 3 anomalies

### Pattern Anomaly Breakdown

- SINGLE_ISSUE_DOMINANCE: 680
- SAE_NOT_FLAGGED: 559
- SAE_WITHOUT_CODING: 312
- STALE_MISSING_DATA: 278
- MAJORITY_HIGH_RISK: 35
- ZERO_ISSUES_HIGH_VOLUME: 21


---

## Top 15 Sites by Anomaly Score

| Rank | Study | Site ID | Country | Score | Anomalies | Critical | High | Types |
|------|-------|---------|---------|-------|-----------|----------|------|-------|
| 1 | Study_21 | Site 522 | - | 1.200 | 2 | 2 | 0 | 2 |
| 2 | Study_24, Study_8 | Site 425 | - | 1.100 | 1 | 1 | 0 | 1 |
| 3 | Study_21 | Site 944 | - | 1.100 | 1 | 1 | 0 | 1 |
| 4 | Study_21 | Site 943 | - | 1.100 | 1 | 1 | 0 | 1 |
| 5 | Study_21 | Site 941 | - | 1.100 | 1 | 1 | 0 | 1 |
| 6 | Study_21 | Site 94 | - | 1.100 | 1 | 1 | 0 | 1 |
| 7 | Study_21 | Site 938 | - | 1.100 | 1 | 1 | 0 | 1 |
| 8 | Study_21 | Site 936 | - | 1.100 | 1 | 1 | 0 | 1 |
| 9 | Study_21 | Site 929 | - | 1.100 | 1 | 1 | 0 | 1 |
| 10 | Study_21 | Site 805 | - | 1.100 | 1 | 1 | 0 | 1 |
| 11 | Study_21 | Site 914 | - | 1.100 | 1 | 1 | 0 | 1 |
| 12 | Study_21 | Site 91 | - | 1.100 | 1 | 1 | 0 | 1 |
| 13 | Study_21 | Site 908 | - | 1.100 | 1 | 1 | 0 | 1 |
| 14 | Study_21 | Site 907 | - | 1.100 | 1 | 1 | 0 | 1 |
| 15 | Study_21 | Site 903 | - | 1.100 | 1 | 1 | 0 | 1 |


---

## Critical Anomalies (Immediate Action Required)


### 1. Study_1 - Site 27 (CHN)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 7.4σ above average (37 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 2. Study_21 - Site 1110 (USA)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 7.2σ above average (36 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 3. Study_21 - Site 1370 (BGR)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 5.5σ above average (28 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 4. Study_21 - Site 1389 (COL)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 7.4σ above average (37 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 5. Study_21 - Site 1436 (HUN)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 6.3σ above average (32 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 6. Study_21 - Site 1467 (LTU)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 6.1σ above average (31 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 7. Study_21 - Site 1510 (POL)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 6.8σ above average (34 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 8. Study_21 - Site 1513 (POL)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 5.7σ above average (29 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 9. Study_21 - Site 1514 (POL)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 8.4σ above average (42 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 10. Study_21 - Site 162 (PRT)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 7.6σ above average (38 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 11. Study_21 - Site 172 (ARG)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 5.3σ above average (27 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 12. Study_21 - Site 175 (ARG)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 5.9σ above average (30 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 13. Study_21 - Site 22 (USA)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 9.7σ above average (48 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 14. Study_21 - Site 356 (ARG)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 8.2σ above average (41 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 15. Study_21 - Site 520 (ESP)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 26.8σ above average (130 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 16. Study_21 - Site 911 (ARG)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 5.1σ above average (26 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 17. Study_21 - Site 916 (ARG)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 8.2σ above average (41 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 18. Study_21 - Site 921 (BRA)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 6.5σ above average (33 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 19. Study_21 - Site 925 (BRA)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 7.0σ above average (35 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 20. Study_21 - Site 930 (BRA)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 5.5σ above average (28 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 21. Study_21 - Site 950 (BRA)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 7.4σ above average (37 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 22. Study_21 - Site 991 (CHL)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 5.7σ above average (29 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 23. Study_22 - Site 2063 (USA)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 7.2σ above average (36 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 24. Study_4 - Site 211 (USA)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Sae Pending Count is 10.9σ above average (54 vs mean 1.6)
- **Recommendation**: Investigate elevated sae pending count at this site

### 25. Study_16 - Site 625 (CAN)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: Missing Visit Count is 6.9σ above average (10 vs mean 0.5)
- **Recommendation**: Investigate elevated missing visit count at this site


---

## Regional Anomalies

- **NOR** (EMEA): NOR has 25.6% high-risk subject rate (30/135 subjects)
- **NZL** (ASIA): NZL has 29.7% high-risk subject rate (54/201 subjects)
- **Multiple** (ASIA): ASIA region DQI (0.060) is 1.1σ above other regions


---

## Cross-Study Anomalies (Repeat Offender Sites)

- **Site 1018** (USA): Site is high risk in 1/2 studies: Study_24
- **Site 1027** (USA): Site is high risk in 1/2 studies: Study_22
- **Site 1034** (USA): Site is high risk in 1/2 studies: Study_24
- **Site 1059** (USA): Site is high risk in 1/2 studies: Study_21
- **Site 110** (AUS): Site is high risk in 3/6 studies: Study_13, Study_24, Study_7
- **Site 1179** (USA): Site is high risk in 1/2 studies: Study_21
- **Site 1180** (USA): Site is high risk in 1/2 studies: Study_21
- **Site 1181** (USA): Site is high risk in 1/2 studies: Study_21
- **Site 1184** (USA): Site is high risk in 1/2 studies: Study_22
- **Site 12** (KOR): Site is high risk in 2/5 studies: Study_1, Study_7
- **Site 1336** (AUS): Site is high risk in 1/2 studies: Study_21
- **Site 1343** (AUS): Site is high risk in 1/2 studies: Study_22
- **Site 14** (ESP): Site is high risk in 4/10 studies: Study_17, Study_5, Study_6, Study_7
- **Site 1645** (IND): Site is high risk in 1/2 studies: Study_24
- **Site 1646** (IND): Site is high risk in 1/2 studies: Study_24
- **Site 1648** (IND): Site is high risk in 1/2 studies: Study_24
- **Site 1675** (MYS): Site is high risk in 1/2 studies: Study_24
- **Site 17** (ESP): Site is high risk in 2/4 studies: Study_1, Study_7
- **Site 19** (USA): Site is high risk in 3/5 studies: Study_1, Study_17, Study_5
- **Site 2013** (USA): Site is high risk in 1/2 studies: Study_24
- **Site 2015** (USA): Site is high risk in 1/2 studies: Study_24
- **Site 2030** (USA): Site is high risk in 1/2 studies: Study_24
- **Site 2161** (IND): Site is high risk in 1/2 studies: Study_24
- **Site 2184** (CHN): Site is high risk in 1/2 studies: Study_24
- **Site 2188** (ISR): Site is high risk in 1/2 studies: Study_24
- **Site 259** (IND): Site is high risk in 2/5 studies: Study_24, Study_5
- **Site 261** (IND): Site is high risk in 1/2 studies: Study_5
- **Site 267** (IND): Site is high risk in 1/2 studies: Study_5
- **Site 27** (CHN): Site is high risk in 1/2 studies: Study_1
- **Site 280** (ESP): Site is high risk in 1/2 studies: Study_5
- **Site 281** (ESP): Site is high risk in 2/3 studies: Study_24, Study_5
- **Site 282** (ESP): Site is high risk in 1/2 studies: Study_5
- **Site 283** (ESP): Site is high risk in 1/2 studies: Study_5
- **Site 292** (ROU): Site is high risk in 1/2 studies: Study_5
- **Site 308** (SVK): Site is high risk in 1/2 studies: Study_5
- **Site 309** (SVK): Site is high risk in 1/2 studies: Study_5
- **Site 313** (SVK): Site is high risk in 1/2 studies: Study_5
- **Site 326** (USA): Site is high risk in 2/5 studies: Study_24, Study_5
- **Site 327** (USA): Site is high risk in 3/5 studies: Study_17, Study_24, Study_5
- **Site 328** (USA): Site is high risk in 1/2 studies: Study_5
- **Site 329** (USA): Site is high risk in 1/2 studies: Study_5
- **Site 336** (USA): Site is high risk in 1/2 studies: Study_5
- **Site 338** (USA): Site is high risk in 2/2 studies: Study_24, Study_5
- **Site 340** (USA): Site is high risk in 1/2 studies: Study_5
- **Site 341** (USA): Site is high risk in 1/2 studies: Study_21
- **Site 343** (USA): Site is high risk in 1/2 studies: Study_5
- **Site 355** (POL): Site is high risk in 1/2 studies: Study_22
- **Site 425** (CHN): Site is high risk in 2/2 studies: Study_24, Study_8
- **Site 426** (CHN): Site is high risk in 1/2 studies: Study_24
- **Site 462** (JPN): Site is high risk in 1/2 studies: Study_10
- **Site 476** (DNK): Site is high risk in 1/2 studies: Study_11
- **Site 482** (FRA): Site is high risk in 1/2 studies: Study_11
- **Site 493** (DEU): Site is high risk in 1/2 studies: Study_19
- **Site 50** (CAN): Site is high risk in 2/5 studies: Study_10, Study_24
- **Site 507** (ITA): Site is high risk in 2/4 studies: Study_11, Study_24
- **Site 51** (CAN): Site is high risk in 1/2 studies: Study_24
- **Site 597** (USA): Site is high risk in 2/3 studies: Study_13, Study_24
- **Site 6** (AUT): Site is high risk in 2/5 studies: Study_1, Study_24
- **Site 778** (ISR): Site is high risk in 1/2 studies: Study_19
- **Site 834** (ITA): Site is high risk in 1/2 studies: Study_21
- **Site 87** (CZE): Site is high risk in 4/10 studies: Study_10, Study_13, Study_20, Study_7
- **Site 880** (ESP): Site is high risk in 1/2 studies: Study_24
- **Site 883** (ESP): Site is high risk in 1/2 studies: Study_24
- **Site 884** (ESP): Site is high risk in 1/2 studies: Study_24
- **Site 887** (ESP): Site is high risk in 1/2 studies: Study_24
- **Site 888** (ESP): Site is high risk in 1/2 studies: Study_24
- **Site 904** (ESP): Site is high risk in 1/2 studies: Study_24
- **Site 953** (CAN): Site is high risk in 1/2 studies: Study_24
- **Site 986** (CHL): Site is high risk in 1/2 studies: Study_24
- **Site 998** (NOR): Site is high risk in 1/2 studies: Study_21


---

## Recommendations Summary

Based on the anomaly analysis, key actions:


### CRITICAL Priority

- Investigate elevated edrr open issues at this site
- Investigate elevated sae pending count at this site
- Investigate elevated lab issues count at this site
- Investigate elevated missing visit count at this site
- Investigate elevated max days page missing at this site

### HIGH Priority

- Site-wide quality intervention needed - majority of subjects have issues
- Critical - single site driving majority of Study_15 data quality issues
- Investigate elevated max days page missing at this site
- Investigate elevated max days outstanding at this site
- Investigate elevated subject count at this site

### MEDIUM Priority

- Check if SAE adverse event terms are being routed to coding team
- Investigate elevated edrr open issues at this site
- Focus intervention specifically on lab issues - appears to be root cause
- Verify all data sources are being captured for this site
- Investigate elevated sae pending count at this site


---

*Report generated by JAVELIN.AI Anomaly Detection Engine v2.0*
