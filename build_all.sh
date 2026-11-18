#!/usr/bin/env bash
# Rebuild every artefact of the 26UAMPC204 course handbook.
set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"; cd "$ROOT"
tex() { (cd "$1" && xelatex -interaction=nonstopmode "$2.tex" >/dev/null && xelatex -interaction=nonstopmode "$2.tex" >/dev/null && rm -f *.aux *.log *.out *.toc && echo "  ✓ $1/$2.pdf"); }

echo "1/5 Executing lab notebooks …";           python 06_Notebooks/src/build_notebooks.py
echo "1b  Interview prep (notebook, handbook, unit inserts, PPT data) …"; python 07_Interview_Prep/src/build_interview.py; tex 07_Interview_Prep AI_Interview_Skills_Handbook
echo "1c  Research ideas and assignments …"; python 09_Assignments/src/build_extras.py; tex 08_Research_Ideas AI_Research_Ideas; tex 09_Assignments AI_Assignments_Booklet
echo "2/5 Building lab manual …";              python 05_Lab_Manual/src/build_lab_manual.py; tex 05_Lab_Manual AI_Lab_Manual_26UAMPC204
echo "3/5 Building unit notes …"
for f in Unit_1_Notes Unit_2_Notes Unit_3_Notes Unit_4_Notes Unit_5_Notes AI_Complete_Notes; do tex 01_Unit_Notes/latex $f; done
mv 01_Unit_Notes/latex/*.pdf 01_Unit_Notes/pdf/
echo "4/5 Question bank and projects …";       python 03_Question_Bank/src/generate.py
tex 03_Question_Bank AI_Question_Bank_BTL; tex 04_Projects AI_Projects_Portfolio
echo "5/5 PowerPoint decks …"
(cd 02_PPT/src && node build.js && cd .. && python src/animate.py Unit_*_AI_26UAMPC204.pptx \
  && soffice --headless --convert-to pdf --outdir pdf Unit_*_AI_26UAMPC204.pptx >/dev/null) || echo "  (skipped PPT: needs node + pptxgenjs + LibreOffice)"
echo "Done."
