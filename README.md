# The Legacy Fix — ProoV x IBM Bob | Fixed by Ayesha Farhath

## 🏆 Certification
✅ **ProoV Certificate** - AI-Assisted Code Modernization with IBM (05 Sep 2026) - `PRV-2026-C23DBDFE`

✅ **IBM SkillsBuild** - IBM Bobathon: The Legacy Fix - Modernize a Real Car-Company Service (04 Sep 2026)


🔗 Project: https://projectstudy.in/explore/experience-legacy-fix

📁 My Repo: Fixed 11/11 tests passing


## 🔧 What I Fixed
- **Fixed hidden bug:** Car at 14,900/15,000 km reported 0% wear (nearly due but let through) - Now correctly flags as due
- **Modernized 2013-era legacy code:** Cleaned `config_loader.py`, `fleet_utils.py`, `log_util.py` - removed dead code, dated style
- **All 11/11 tests passing** - verified with `python verify.py` and `pytest`
- **Added breakdown-risk data analysis** (`fleet_history.csv` - 120 cars): Found gap since last service + driving hardness predicts breakdown, not mileage/age


## 📝 NOTES
See `NOTES.md` for what my AI agent got wrong that I caught and corrected.

---

# The Legacy Fix — a ProoV Guided Project, powered by IBM Bob

This repo is the starting point of [The Legacy Fix](https://projectstudy.in/explore/experience-legacy-fix), a ProoV
challenge. You are fixing **KM-Wächter**, the service that decides when each of Vossberg
Mobility's 6,000 cars needs a service and prints the nightly fleet-health report. It has
hidden bugs, several tests fail, and the code is written in an old style. Your job is to
fix and modernize it — with IBM Bob (or another AI coding agent; another agent works just
as well) doing the heavy lifting while you direct and audit it.

> **Fictional company disclaimer.** Vossberg Mobility and KM-Wächter are invented for
> teaching and are labelled as such in-app. They are not a real company. Industry figures
> referenced in the accompanying brief come from public sources.

## How to run

You do not need Python installed to do this task — your AI agent can run all of this for
you. If you do want to run it yourself, you need `python3`:

```
pip install pytest pandas
pytest          # the test suite (currently red)
python verify.py  # your acceptance check: is the job actually done?
```

The test suite is **red on purpose** — that is the starting point of the task, not a bug in
this template.

## What's in this repo

- **`TASK.md`** — your mission brief. Read this first; it has every step of the task,
  what NOT to change, and how to hand the work back in.
- **`verify.py`** — your own acceptance check. It does not grade you — it tells you,
  mechanically, whether the job is actually done, so "finished" is something you checked
  rather than something your AI agent told you. Run `python verify.py` before you hand in.
- **`km_wachter.py` / `fleet_report.py`** — the two core modules with the hidden bugs.
- **`config_loader.py` / `fleet_utils.py` / `log_util.py`** — 2013-era helper modules: dated
  style, dead code, and at least one more quiet problem no test catches.
- **`settings.cfg`** — the maintenance rules, read at runtime. The values must not change.
- **`test_km_wachter.py` / `test_fleet_report.py`** — the test suite (currently red).
- **`analyze.py`** — the "make it smarter" capstone: a data-driven breakdown-risk analysis.
- **`fleet_history.csv`** — 120 labelled cars for the analysis step.
- **`NOTES.md`** — write this yourself: what your AI agent got wrong that you caught.

---

This challenge is part of the ProoV project "The Legacy Fix" — https://projectstudy.in/explore/experience-legacy-fix
