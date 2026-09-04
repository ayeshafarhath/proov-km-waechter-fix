# analyze.py
# Trusted predictors of breakdown: km_since_service, avg_daily_km, load_factor.
# Untrusted: odometer_km (gap < 150 km), age_years (gap < 0.01 years).
# Reason: cars that broke down had driven furthest since their last service and worked hardest
# (higher daily km and heavier load), not because they were older or had more total mileage.

import pandas as pd

df = pd.read_csv("fleet_history.csv")

# ── 1. Compare broke-down group vs kept-going group ────────────────────────────
broke = df[df["broke_down"] == 1]
kept  = df[df["broke_down"] == 0]

print("Breakdown-risk factor analysis")
print("=" * 60)
print(f"Fleet: {len(df)} cars   |   Broke down: {len(broke)}   |   Kept going: {len(kept)}")
print()
print(f"{'Column':<25}  {'Broke':>8}  {'Kept':>8}  {'Gap':>8}  {'Trusted?'}")
print("-" * 60)

PREDICTORS = []
for col in ["odometer_km", "age_years", "km_since_service", "avg_daily_km", "load_factor"]:
    b_mean = broke[col].mean()
    k_mean = kept[col].mean()
    gap    = b_mean - k_mean
    # Relative gap > 10 % of the kept-group mean is considered meaningful.
    trusted = abs(gap) / k_mean > 0.10
    if trusted:
        PREDICTORS.append(col)
    tag = "YES" if trusted else "no"
    print(f"  {col:<23}  {b_mean:>8.2f}  {k_mean:>8.2f}  {gap:>+8.2f}  {tag}")

print()
print(f"Trusted predictors : {', '.join(PREDICTORS)}")
print(f"Untrusted (no gap) : odometer_km, age_years")
print()

# ── 2. Build a 0–100 risk score from the trusted predictors ───────────────────
# Each predictor is min-max normalised across the full fleet, then averaged.
score_cols = PREDICTORS
for col in score_cols:
    col_min = df[col].min()
    col_max = df[col].max()
    df[f"_norm_{col}"] = (df[col] - col_min) / (col_max - col_min)

norm_cols = [f"_norm_{c}" for c in score_cols]
df["risk_score"] = (df[norm_cols].mean(axis=1) * 100).round(1)

# ── 3. Print cars ranked by risk, highest first ───────────────────────────────
ranked = df[["car_id", "km_since_service", "avg_daily_km", "load_factor", "risk_score", "broke_down"]] \
    .sort_values("risk_score", ascending=False) \
    .reset_index(drop=True)

print("Cars ranked by breakdown risk (highest first)")
print("-" * 70)
print(f"  {'#':>3}  {'car_id':<10}  {'km_since_svc':>12}  {'daily_km':>8}  {'load':>6}  {'risk':>6}  {'broke?':>6}")
print("-" * 70)
for i, row in ranked.iterrows():
    marker = " *" if row["broke_down"] == 1 else ""
    print(
        f"  {i+1:>3}  {row['car_id']:<10}  {row['km_since_service']:>12.0f}  "
        f"{row['avg_daily_km']:>8.0f}  {row['load_factor']:>6.2f}  "
        f"{row['risk_score']:>6.1f}{marker}"
    )

print()
print("* = car that later broke down")
