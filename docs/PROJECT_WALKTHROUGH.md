# Project Walkthrough

## 1. Raw Data Registration

The route CSV is uploaded to Databricks and registered as a raw table. This keeps ingestion separate from transformation so that downstream notebooks always have a known starting point.

## 2. ETL And Feature Engineering

The ETL notebook cleans the raw fields, standardizes numeric columns, converts operating-day fields into usable indicators, and computes route-distance metrics from airport coordinates.

The main output is the clean Delta table:

```text
workspace.eu_air_routes.eu_air_routes_clean
```

## 3. Exploratory Analysis

The EDA notebook reviews schema, nulls, route counts, airport patterns, geography, and distance-price behavior. These analyses guide the SQL dashboard design.

## 4. SQL Analytics

The SQL notebook converts common airline network questions into dashboard-ready queries:

- Which route pairs are busiest?
- Which countries produce the most weekly departures?
- How does average price change by distance bucket?
- Which routes operate every day?
- How are prices distributed by departure market?

## 5. Dashboard

The Databricks dashboard JSON captures the interactive dashboard build. It is designed for scanning market concentration, route frequency, and price behavior.

## 6. Machine Learning

The final notebook trains a regression model to estimate ticket price from route distance and frequency features. It is intentionally interpretable so results can be tied back to route economics.

## 7. Recommended Next Steps

- Add map screenshots from Databricks dashboard pages.
- Export cleaned summary tables for Power BI or Tableau.
- Add model metrics exports to `outputs/metrics/`.
- Compare linear regression with tree-based models.
- Add route-level anomaly detection for unusually expensive or underpriced routes.
