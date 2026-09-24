# FA2 practice pack — start here

Reconstructed from your two uploaded PDFs. **60 marks: P1 40 + P2 20.**
This is a practice reconstruction, not an official Infosys distribution.

## What to open

1. `docs/FA2_Practice_Question_Paper.pdf` — clean, printable assessment.
2. `FA2_Mock_P1.py` and `FA2_Mock_P2.py` — incomplete Python templates.
3. `docs/REFERENCE_SYNTAX.md` — optional syntax reference, recreated because the
   reference mentioned in the paper was not attached.
4. `docs/SELF_CHECK.md` — behavior checklist to use after your attempt.
5. `docs/RECONSTRUCTION_NOTES.md` — source mapping, missing/cropped material,
   clarifications and validation limits.

The `data` folder contains all four claims, the predefined evidence and the
translation source article. Required data is also embedded in the templates,
matching the original design; no CSV, vector database or external dataset is needed.
The `originals` folder preserves both PDFs unchanged. The code photos contain some
attempted answers, so avoid them during a closed-book practice run.

## Windows setup

Extract the ZIP first. Open its `FA2_Practice_Pack` folder in VS Code, then open a
terminal in that folder. Use Python 3.11 or 3.12 for this practice environment.
These are setup choices, not recovered exam requirements.

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
.\.venv\Scripts\python.exe check_setup.py
```

If you use Python 3.12, replace `-3.11` with `-3.12`. Activation is optional;
using the interpreter's full relative path avoids PowerShell activation issues.
On macOS/Linux use `python3 -m venv .venv`, `.venv/bin/python -m pip install -r requirements.txt`
and `cp .env.example .env`.

Configure your authorized AWS profile or temporary lab credentials locally.
The screenshots use ChatBedrockConverse and show `amazon.nova-lite-v1:0` in
`us-east-1`. Model access depends on your AWS account and lab setup. Use an
approved model ID/inference profile if your environment requires a different one.
The pack does not contain credentials. Never submit your .env file.

The dependency ranges are a suggested modern environment, not a tested lockfile
or a claim about packages installed in your Infosys lab. Prefer the lab's existing
package versions if they are prescribed. See the reference's official links.

## Practice workflow

- Read the question paper and preserve all fixed names.
- Complete the TODO blocks in both Python files. The first unfinished function
  raises `NotImplementedError`; this is intentional.
- Keep the imports provided. Add further imports if your approach needs them.
- The module-level `None` / empty values are placeholders, not working LLM or
  tool configurations. Replace them in their TODO sections.
- Use the original Bedrock interface for exam-style practice.
- Run your completed files:

```powershell
.\.venv\Scripts\python.exe FA2_Mock_P1.py
.\.venv\Scripts\python.exe -X utf8 FA2_Mock_P2.py
```

For submission practice, copy/rename them to `FA2_Mock_<Emp_Num>_P1.py` and
`FA2_Mock_<Emp_Num>_P2.py`, replacing `<Emp_Num>` with your employee number.
Do not type angle brackets into a Windows filename.

No assessment duration was visible in the PDFs. Choose your own timer or use
whatever duration your trainer specifies. The pack deliberately contains no
completed solution files. The self-check is not an official marking rubric.

## Validation status

The Python files were checked for syntax and fixed names; data copies were checked
for consistency; the question PDF was rendered and inspected; ZIP integrity was
checked. The unfinished templates and live Bedrock calls were not executed as
completed applications. `check_setup.py` checks imports without invoking a model;
it does not validate credentials, permissions, or your answers.
