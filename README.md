# RadSafe: gamified radiation safety training (pilot prototype)

*Radiation Safety. Real Decisions. Better Outcomes.*

Single-file HTML/JS game (`radsafe.html`, no external dependencies) hosted in Streamlit for pilot testing.
**Simulated, unreviewed training content. Not a qualification, regulatory certification or evidence of competency.**

## Contents
- 3 knowledge scenarios + 4 interactive simulations (PPE preparation, radiology room hazard hunt, operating-theatre fluoroscopy with illustrative scatter, incident response)
- Learner dashboard, points, badges, demo certificates, leaderboard (simulated peers)
- RPO dashboard: charts, filter/sort/search, CSV export, scenario review status, simulation results kept separate from knowledge-assessment results

## Run locally
```
pip install -r requirements.txt
streamlit run app.py
```
(You can also just open `radsafe.html` in a browser.)

## Deploy (Streamlit Community Cloud)
1. `git init && git add . && git commit -m "RadSafe pilot" && git branch -M main`
2. Create an empty GitHub repo, then `git remote add origin <url> && git push -u origin main`
3. At share.streamlit.io choose **New app**, pick the repo, branch `main`, main file `app.py`, then Deploy.
4. Optional access code: App settings > Secrets > `PILOT_PASSWORD = "your-code"`.
Note: free apps sleep when idle; wake before demos. Use a private repo/app if content should not be public.

## Architecture
`app.py` embeds `radsafe.html`. Game logic, scenario/mission data, scoring (`finish()`, `scoreStage()`), persistence (`localStorage`, key `radsafe.v1`) and views all live in that file; missions are data-driven (`SC`, `RM`, `IT`, `TS`, `TD`, `CT`, `RI`).

## Known limitations
- Progress is stored per browser/device; there is no server, login or central results, so the RPO dashboard shows simulated learners plus the local browser's own record only.
- Passcode gate is not real authentication. localStorage is demo-only (no sensitive data).
- Drag-and-drop was verified by logic tests only; test touch/drag in real browsers before demos.
- The incident and fluoroscopy content is fictional and illustrative; scatter visuals are not dosimetry.
- Production needs: auth, server-side records (e.g. Supabase), LMS/xAPI export, content versioning and approval.

## Content requiring qualified review (RPO / medical physicist)
PPE sets per procedure (all missions); controlled-area and positioning guidance; fluoroscopy scatter explanations; incident actions, notification list and report fields; all "source" placeholders; pass mark (70%) and scoring weights; certificate wording; badge criteria.

## Tests run
`node test_logic.js` (run from this folder): headless logic test that plays all four missions end to end, checks scores, badges, no duplicate points, view rendering and the trainer table. Last result: all checks pass. Not tested: real browser rendering, touch, drag-and-drop, screen readers, Streamlit deployment itself.
