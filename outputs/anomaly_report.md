# JAVELIN.AI - Anomaly Detection Report

*Generated: 2026-01-21 15:13:56*

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Anomalies Detected | 6760 |
| Sites with Anomalies | 2286 |
| Critical Anomalies | 762 |
| High Severity Anomalies | 4525 |
| Medium Severity Anomalies | 1473 |

---

## Anomaly Distribution by Type

- **STATISTICAL_OUTLIER**: 6162 anomalies
- **PATTERN_ANOMALY**: 518 anomalies
- **CROSS_STUDY_ANOMALY**: 63 anomalies
- **VELOCITY_ANOMALY**: 17 anomalies


---

## Top 10 Sites by Anomaly Score

| Rank | Study | Site ID | Score | Anomalies | Critical | High | Types |
|------|-------|---------|-------|-----------|----------|------|-------|
| 1 | Study_24 | Site 888 | 1.150 | 13 | 8 | 4 | 3 |
| 2 | Study_24, Study_8 | Site 425 | 1.100 | 1 | 1 | 0 | 1 |
| 3 | Study_2 | Site 30 | 1.100 | 1 | 1 | 0 | 1 |
| 4 | Study_2 | Site 2 | 1.100 | 1 | 1 | 0 | 1 |
| 5 | Study_21 | Site 921 | 1.100 | 6 | 5 | 0 | 2 |
| 6 | Study_21 | Site 1555 | 1.100 | 2 | 2 | 0 | 1 |
| 7 | Study_21 | Site 1640 | 1.100 | 9 | 6 | 3 | 2 |
| 8 | Study_21 | Site 162 | 1.100 | 6 | 5 | 0 | 2 |
| 9 | Study_23 | Site 3 | 1.100 | 4 | 4 | 0 | 1 |
| 10 | Study_22 | Site 1752 | 1.100 | 1 | 1 | 0 | 1 |


---

## Critical Anomalies (Immediate Action Required)


### 1. Study_1 - Site 12 (KOR)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 6.7 standard deviations above the mean (0.445 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site

### 2. Study_1 - Site 17 (ESP)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 7.8 standard deviations above the mean (0.509 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site

### 3. Study_1 - Site 27 (CHN)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 5.0 standard deviations above the mean (0.340 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site

### 4. Study_1 - Site 6 (AUT)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 4.2 standard deviations above the mean (0.295 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site

### 5. Study_13 - Site 110 (AUS)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 4.3 standard deviations above the mean (0.303 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site

### 6. Study_16 - Site 618 (USA)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 5.1 standard deviations above the mean (0.346 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site

### 7. Study_16 - Site 628 (CAN)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 5.2 standard deviations above the mean (0.355 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site

### 8. Study_16 - Site 635 (GRC)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 5.8 standard deviations above the mean (0.389 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site

### 9. Study_16 - Site 638 (BEL)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 4.1 standard deviations above the mean (0.287 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site

### 10. Study_16 - Site 646 (FRA)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 4.1 standard deviations above the mean (0.288 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site

### 11. Study_16 - Site 659 (ITA)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 4.5 standard deviations above the mean (0.311 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site

### 12. Study_16 - Site 662 (ITA)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 4.1 standard deviations above the mean (0.292 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site

### 13. Study_16 - Site 741 (CHN)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 4.5 standard deviations above the mean (0.312 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site

### 14. Study_16 - Site 759 (TUR)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 5.8 standard deviations above the mean (0.388 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site

### 15. Study_17 - Site 15 (CAN)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 4.3 standard deviations above the mean (0.300 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site

### 16. Study_17 - Site 325 (USA)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 4.3 standard deviations above the mean (0.303 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site

### 17. Study_17 - Site 466 (FRA)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 4.5 standard deviations above the mean (0.314 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site

### 18. Study_19 - Site 155 (TWN)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 4.2 standard deviations above the mean (0.295 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site

### 19. Study_19 - Site 417 (KOR)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 4.3 standard deviations above the mean (0.302 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site

### 20. Study_19 - Site 467 (AUS)

- **Type**: STATISTICAL_OUTLIER (Z-Score)
- **Description**: avg_dqi_score is 4.3 standard deviations above the mean (0.298 vs mean 0.045)
- **Recommendation**: Investigate why avg_dqi_score is unusually high at this site


---

## Regional Anomalies

*No regional anomalies detected.*


---

## Cross-Study Anomalies

- **Site 1018**: Site Site 1018 is high risk in 1/2 studies: Study_21, Study_24
- **Site 1027**: Site Site 1027 is high risk in 1/2 studies: Study_21, Study_22
- **Site 1034**: Site Site 1034 is high risk in 1/2 studies: Study_21, Study_24
- **Site 1059**: Site Site 1059 is high risk in 1/2 studies: Study_21, Study_22
- **Site 110**: Site Site 110 is high risk in 3/6 studies: Study_13, Study_24, Study_4, Study_7, Study_8, Study_9
- **Site 1179**: Site Site 1179 is high risk in 1/2 studies: Study_21, Study_22
- **Site 1180**: Site Site 1180 is high risk in 1/2 studies: Study_21, Study_22
- **Site 1181**: Site Site 1181 is high risk in 1/2 studies: Study_21, Study_22
- **Site 1184**: Site Site 1184 is high risk in 1/2 studies: Study_21, Study_22
- **Site 1336**: Site Site 1336 is high risk in 1/2 studies: Study_21, Study_22
- **Site 1343**: Site Site 1343 is high risk in 1/2 studies: Study_21, Study_22
- **Site 1645**: Site Site 1645 is high risk in 1/2 studies: Study_22, Study_24
- **Site 1646**: Site Site 1646 is high risk in 1/2 studies: Study_22, Study_24
- **Site 1648**: Site Site 1648 is high risk in 1/2 studies: Study_22, Study_24
- **Site 1675**: Site Site 1675 is high risk in 1/2 studies: Study_22, Study_24
- **Site 17**: Site Site 17 is high risk in 2/4 studies: Study_1, Study_21, Study_22, Study_7
- **Site 19**: Site Site 19 is high risk in 3/5 studies: Study_1, Study_17, Study_21, Study_22, Study_5
- **Site 2013**: Site Site 2013 is high risk in 1/2 studies: Study_22, Study_24
- **Site 2015**: Site Site 2015 is high risk in 1/2 studies: Study_22, Study_24
- **Site 2030**: Site Site 2030 is high risk in 1/2 studies: Study_22, Study_24
- **Site 2161**: Site Site 2161 is high risk in 1/2 studies: Study_23, Study_24
- **Site 2184**: Site Site 2184 is high risk in 1/2 studies: Study_24, Study_25
- **Site 2188**: Site Site 2188 is high risk in 1/2 studies: Study_24, Study_25
- **Site 261**: Site Site 261 is high risk in 1/2 studies: Study_21, Study_5
- **Site 267**: Site Site 267 is high risk in 1/2 studies: Study_22, Study_5
- **Site 27**: Site Site 27 is high risk in 1/2 studies: Study_1, Study_21
- **Site 280**: Site Site 280 is high risk in 1/2 studies: Study_21, Study_5
- **Site 281**: Site Site 281 is high risk in 2/3 studies: Study_21, Study_24, Study_5
- **Site 282**: Site Site 282 is high risk in 1/2 studies: Study_21, Study_5
- **Site 283**: Site Site 283 is high risk in 1/2 studies: Study_21, Study_5
- **Site 292**: Site Site 292 is high risk in 1/2 studies: Study_22, Study_5
- **Site 308**: Site Site 308 is high risk in 1/2 studies: Study_22, Study_5
- **Site 309**: Site Site 309 is high risk in 1/2 studies: Study_22, Study_5
- **Site 313**: Site Site 313 is high risk in 1/2 studies: Study_22, Study_5
- **Site 327**: Site Site 327 is high risk in 3/5 studies: Study_17, Study_21, Study_24, Study_5, Study_8
- **Site 328**: Site Site 328 is high risk in 1/2 studies: Study_22, Study_5
- **Site 329**: Site Site 329 is high risk in 1/2 studies: Study_22, Study_5
- **Site 336**: Site Site 336 is high risk in 1/2 studies: Study_22, Study_5
- **Site 338**: Site Site 338 is high risk in 2/2 studies: Study_24, Study_5
- **Site 340**: Site Site 340 is high risk in 1/2 studies: Study_22, Study_5
- **Site 341**: Site Site 341 is high risk in 1/2 studies: Study_21, Study_5
- **Site 343**: Site Site 343 is high risk in 1/2 studies: Study_22, Study_5
- **Site 355**: Site Site 355 is high risk in 1/2 studies: Study_22, Study_7
- **Site 425**: Site Site 425 is high risk in 2/2 studies: Study_24, Study_8
- **Site 426**: Site Site 426 is high risk in 1/2 studies: Study_24, Study_8
- **Site 462**: Site Site 462 is high risk in 1/2 studies: Study_10, Study_22
- **Site 476**: Site Site 476 is high risk in 1/2 studies: Study_11, Study_22
- **Site 482**: Site Site 482 is high risk in 1/2 studies: Study_11, Study_22
- **Site 493**: Site Site 493 is high risk in 1/2 studies: Study_11, Study_19
- **Site 507**: Site Site 507 is high risk in 2/4 studies: Study_11, Study_21, Study_24, Study_25
- **Site 51**: Site Site 51 is high risk in 1/2 studies: Study_10, Study_24
- **Site 597**: Site Site 597 is high risk in 2/3 studies: Study_13, Study_22, Study_24
- **Site 778**: Site Site 778 is high risk in 1/2 studies: Study_19, Study_25
- **Site 834**: Site Site 834 is high risk in 1/2 studies: Study_21, Study_22
- **Site 880**: Site Site 880 is high risk in 1/2 studies: Study_21, Study_24
- **Site 883**: Site Site 883 is high risk in 1/2 studies: Study_21, Study_24
- **Site 884**: Site Site 884 is high risk in 1/2 studies: Study_21, Study_24
- **Site 887**: Site Site 887 is high risk in 1/2 studies: Study_21, Study_24
- **Site 888**: Site Site 888 is high risk in 1/2 studies: Study_21, Study_24
- **Site 904**: Site Site 904 is high risk in 1/2 studies: Study_21, Study_24
- **Site 953**: Site Site 953 is high risk in 1/2 studies: Study_21, Study_24
- **Site 986**: Site Site 986 is high risk in 1/2 studies: Study_21, Study_24
- **Site 998**: Site Site 998 is high risk in 1/2 studies: Study_21, Study_22


---

## Recommendations Summary

Based on the anomaly analysis, the following actions are recommended:

1. Investigate why lab_issues_count_sum is unusually high at this site
2. Focus intervention on missing_visits - appears to be primary problem
3. Focus intervention on missing_pages - appears to be primary problem
4. Investigate why uncoded_whodd_count_sum is unusually high at this site
5. High issue concentration - prioritize for immediate intervention
6. Review site for unusual missing_pages_count_sum pattern
7. Investigate why inactivated_forms_count_sum is unusually high at this site
8. Review site for unusual uncoded_whodd_count_sum pattern
9. Review site for unusual inactivated_forms_count_sum pattern
10. Review site for unusual subjects_with_issues pattern
11. Single site driving majority of Study_14 issues - immediate site review needed
12. Focus intervention on sae - appears to be primary problem
13. Investigate why missing_visit_count_sum is unusually high at this site
14. Review site for unusual subject_count pattern
15. Cross-functional review needed - site shows consistent quality issues across programs


---

*Report generated by JAVELIN.AI Anomaly Detection Engine*
