# What I checked, and what the agent got wrong
I am Ayesha Farhath, I fixed km-waechter legacy code with Bob.


## What the agent got wrong
Bob first tried to keep duplicate function is_due() as alias to needs_service() to avoid breaking anything. I caught it because TASK.md says remove duplicate logic and keep single source of truth. Also Bob initially wanted to change settings.cfg thresholds from 0.8 to make tests pass, but TASK.md says keep settings.cfg exactly same. I told Bob to delete is_due() and not touch settings.cfg. I also made him use ValueError instead of bare except.

## What I checked before I accepted its work
How I know wear bug is fixed: Before fix, wear_percent() used // floor division, so 14,900 km out of 15,000 km interval showed 0% worn. After fix with / it shows 99.3% which is correct. I ran pytest test_km_waechter.py - wear tests green.
How I know 80% rule is untouched: I checked fleet_utils.py and settings.cfg - threshold 0.8 still there, not changed. Only // changed to /. I ran python verify.py and it shows 11/11 passing.


## What the data actually said
From fleet_history.csv analysis (120 cars, 26 broke down):
- odometer_km: 53,448 km broke vs 53,392 km kept = only 56km difference = NOT predictive
- age_years: 5.9 vs 5.9 years = identical = NOT predictive - these are obvious looking but failed
- km_since_service: 11,678 vs 7,261 km = big gap 4,417 km = PREDICTIVE
- avg_daily_km: 169 vs 131 km/day = big gap = PREDICTIVE
- load_factor: 0.69 vs 0.51 = big gap = PREDICTIVE

Conclusion: Total mileage and age don't predict breakdown. Real risk is how far since last service and hardest daily work with heavy load. I built 0-100 risk score in analyze.py using min-max normalization of 3 trusted columns.