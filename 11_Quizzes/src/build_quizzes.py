"""Build 11_Quizzes: booklet (LaTeX/PDF) with answer keys, README, self-check notebook,
per-unit quiz sections for the notes, and quiz-slide data for the PPT decks.
Run from repo root:  python 11_Quizzes/src/build_quizzes.py
"""
import os, sys, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "07_Interview_Prep", "src"))
sys.path.insert(0, os.path.join(ROOT, "06_Notebooks", "src"))
from quiz_data import QUIZ
from build_interview import tex, TITLES, CO
OUT = os.path.join(ROOT, "11_Quizzes")
LETTERS = "ABCD"
EXTRA = {"⁻³": r"$^{-3}$", "≡": r"$\equiv$", "∪": r"$\cup$", "₀": r"$_0$", "←": r"$\leftarrow$", "−": "--", "⁰": r"$^0$", "⁵": r"$^5$", "⁸": r"$^8$", "⁹": r"$^9$", "³": r"$^3$", "⁶": r"$^6$", "ᵏ": r"$^k$", "ₖ": r"$_k$",
         "₁": r"$_1$", "₂": r"$_2$", "□": r"$\square$", "⇔": r"$\Leftrightarrow$", "≺": r"$\prec$", "·": r"$\cdot$",
         "σ": r"$\sigma$", "θ": r"$\theta$", "φ": r"$\varphi$", "x₁": r"x$_1$"}
def t(s):
    for a, b in EXTRA.items():
        s = s.replace(a, "\x00" + str(list(EXTRA).index(a)) + "\x00")
    s = tex(s)
    for i, b in enumerate(EXTRA.values()):
        s = s.replace("\x00" + str(i) + "\x00", b)
    return s

def question_block(u, i, q):
    btl, stem, opts, ans, expl = q
    o = r"\\[1pt]".join(rf"\textbf{{\color{{navyL}}({LETTERS[k]})}}\ {t(x)}" for k, x in enumerate(opts))
    return rf"""\begin{{tcolorbox}}[enhanced,breakable,colback=white,colframe=navyL,arc=2mm,boxrule=0.7pt,left=3mm,right=3mm,top=2mm,bottom=2mm]
\textbf{{\color{{navy}}Q{u}.{i:02d}}}\quad {t(stem)}\hfill\btl{{{btl}}}\par\smallskip
{{\small {o}}}
\end{{tcolorbox}}"""

def key_table(u, qs):
    rows = []
    for i, (btl, stem, opts, ans, expl) in enumerate(qs, 1):
        rows.append((r"\rowcolor{ivory}" if i % 2 == 0 else "") + rf"Q{u}.{i:02d}&\textbf{{\color{{leaf}}{ans}}}&{t(expl)}\\")
    return "\n".join([r"\begin{longtable}{>{\leavevmode\bfseries\color{navy}}p{1.3cm} c p{13.2cm}}",
                      r"\rowcolor{navy}\textcolor{gold}{\textbf{Q.}}&\textcolor{gold}{\textbf{Ans}}&\textcolor{gold}{\textbf{Worked explanation}}\\\endhead"] + rows + [r"\end{longtable}"])

def booklet():
    L = [r"\documentclass[11pt]{article}", r"\usepackage{../common/ai204}", r"\renewcommand{\doctitle}{Unit Quizzes}",
         r"\begin{document}",
         r"\aicover{Complex Unit Quizzes}{75 multi-step questions \textbullet\ 15 per unit \textbullet\ answer keys with worked explanations}{Compute \textbullet\ Trace \textbullet\ Analyse \textbullet\ Evaluate}",
         r"\section*{How to use these quizzes}",
         r"\begin{itemize}\item Each unit has 15 multiple-choice questions that need computation, algorithm tracing or analysis, mostly at Bloom's levels L3--L5. Recall alone will not answer them.",
         r"\item Suggested format: 30 minutes per unit quiz, +1 for a correct answer, no negative marking. Use as a pre-CIA diagnostic or a flipped-classroom warm-up.",
         r"\item Answer keys with worked explanations follow each unit, on a new page, so the questions can be printed alone.",
         r"\item Self-check online: \texttt{11\_Quizzes/Quiz\_SelfCheck.ipynb} grades your answers and explains every mistake.\end{itemize}",
         r"\begin{center}\begin{tabular}{c l c c}\rowcolor{navy}\textcolor{gold}{\textbf{Unit}}&\textcolor{gold}{\textbf{Title}}&\textcolor{gold}{\textbf{CO}}&\textcolor{gold}{\textbf{Questions}}\\"]
    for k, u in enumerate(QUIZ):
        L.append((r"\rowcolor{ivory}" if k % 2 else "") + rf"{u}&{t(TITLES[u])}&{CO[u]}&15\\")
    L += [r"\end{tabular}\end{center}", r"\newpage"]
    for u, qs in QUIZ.items():
        L.append(rf"\unitbanner{{{u}}}{{Quiz: {t(TITLES[u])}}}{{15 Questions \textbullet\ 30 min \textbullet\ {CO[u]}}}")
        L += [question_block(u, i, q) for i, q in enumerate(qs, 1)]
        L += [r"\newpage", rf"\section*{{Answer key and explanations --- Unit {u}}}", key_table(u, qs), r"\newpage"]
    L.append(r"\end{document}")
    return "\n".join(L)

def notes_insert(u):
    qs = QUIZ[u]
    L = [r"\section{Unit Quiz --- test yourself}",
         r"{\small\color{slate}Fifteen multi-step questions. Answer before checking the key on the next page. Self-check notebook: \texttt{11\_Quizzes/Quiz\_SelfCheck.ipynb}.}\par\medskip"]
    L += [question_block(u, i, q) for i, q in enumerate(qs, 1)]
    L += [r"\newpage", rf"\subsection*{{Answer key --- Unit {u} quiz}}", key_table(u, qs)]
    return "\n".join(L)

def readme():
    L = ["# 🧩 Complex Unit Quizzes — 26UAMPC204 Artificial Intelligence", "",
         "75 multi-step questions (15 per unit) that require computing, tracing or analysing, mostly at Bloom's L3–L5.", "",
         "📄 Printable booklet with answer keys: [AI_Unit_Quizzes.pdf](AI_Unit_Quizzes.pdf) · ✅ Auto-graded self-check: [Quiz_SelfCheck.ipynb](Quiz_SelfCheck.ipynb)", "",
         "Click a question to reveal the answer and worked explanation.", ""]
    for u, qs in QUIZ.items():
        L += [f"## Unit {u}: {TITLES[u]} ({CO[u]})", ""]
        for i, (btl, stem, opts, ans, expl) in enumerate(qs, 1):
            L += [f"**Q{u}.{i:02d}** `{btl}` {stem}", ""]
            L += [f"- ({LETTERS[k]}) {x}" for k, x in enumerate(opts)]
            L += ["", f"<details><summary>Show answer</summary>", "", f"**Answer: ({ans})** — {expl}", "", "</details>", ""]
    return "\n".join(L) + "\n"

def notebook():
    import nbformat
    from nbclient import NotebookClient
    LOGO = "https://raw.githubusercontent.com/drssnaiml1-cell/26UAMPC204-Artificial-Intelligence/main/assets/logo.png"
    nb = nbformat.v4.new_notebook(); nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
    nb.cells.append(nbformat.v4.new_markdown_cell(f'''<div style="background:#0B1F4B;padding:22px 26px;border-radius:12px;border:3px solid #C9A227;font-family:'Times New Roman',serif">
<img src="{LOGO}" alt="Sanjivani University" width="92" style="float:right;background:#FFFFFF;border:2px solid #C9A227;border-radius:8px;padding:3px;margin-left:14px">
<div style="color:#C9A227;font-size:14px;letter-spacing:2px;font-weight:bold">26UAMPC204 · ARTIFICIAL INTELLIGENCE · SELF-CHECK</div>
<div style="color:#FFFFFF;font-size:30px;font-weight:bold;margin-top:6px">Complex Unit Quizzes — Auto-Grader</div>
<div style="color:#F6EBC8;font-size:15px;margin-top:8px">1) Run the first cell · 2) <code>show_quiz("II")</code> · 3) fill <code>my_answers</code> · 4) <code>grade("II", my_answers)</code></div>
<div style="clear:both"></div></div>'''))
    data = json.dumps({u: [[b, s, o, a, e] for b, s, o, a, e in qs] for u, qs in QUIZ.items()}, ensure_ascii=False)
    nb.cells.append(nbformat.v4.new_code_cell(f'''import json
QUIZ = json.loads(r"""{data}""")
L = "ABCD"
def show_quiz(unit):
    for i, (btl, stem, opts, ans, expl) in enumerate(QUIZ[unit], 1):
        print(f"Q{{unit}}.{{i:02d}} [{{btl}}] {{stem}}")
        for k, o in enumerate(opts): print(f"     ({{L[k]}}) {{o}}")
        print()
def grade(unit, answers):
    qs = QUIZ[unit]; score = 0
    for i, (btl, stem, opts, ans, expl) in enumerate(qs, 1):
        given = str(answers.get(i, "")).strip().upper()
        if given == ans: score += 1
        else: print(f"✗ Q{{unit}}.{{i:02d}}: you said {{given or '—'}}, correct is {{ans}}. {{expl}}\\n")
    pct = 100 * score / len(qs)
    badge = "🏆 Excellent" if pct >= 85 else "✅ Good" if pct >= 65 else "📘 Revise the unit notes"
    print(f"Score: {{score}}/{{len(qs)}} ({{pct:.0f}}%)  {{badge}}")
    return score
print("Loaded", sum(len(v) for v in QUIZ.values()), "questions across units", ", ".join(QUIZ))'''))
    nb.cells.append(nbformat.v4.new_markdown_cell("## 1 · Read a quiz"))
    nb.cells.append(nbformat.v4.new_code_cell('show_quiz("II")'))
    nb.cells.append(nbformat.v4.new_markdown_cell("## 2 · Enter your answers and grade them\n\nThe example below is a sample attempt; replace it with your own answers."))
    nb.cells.append(nbformat.v4.new_code_cell('my_answers = {1: "B", 2: "B", 3: "A", 4: "B", 5: "B", 6: "C", 7: "A", 8: "B",\n              9: "B", 10: "B", 11: "C", 12: "C", 13: "C", 14: "C", 15: "B"}\ngrade("II", my_answers)'))
    nb.cells.append(nbformat.v4.new_markdown_cell("## 3 · Your turn\n\nPick any unit (`\"I\"` to `\"V\"`), run `show_quiz`, fill `my_answers`, then `grade`."))
    nb.cells.append(nbformat.v4.new_code_cell('# show_quiz("IV")\n# my_answers = {1: "", 2: "", ...}\n# grade("IV", my_answers)'))
    NotebookClient(nb, timeout=120, kernel_name="python3", resources={"metadata": {"path": OUT}}).execute()
    nbformat.write(nb, os.path.join(OUT, "Quiz_SelfCheck.ipynb"))
    print("✓ Quiz_SelfCheck.ipynb executed")

def ppt_json():
    pick = {}
    for u, qs in QUIZ.items():
        hard = sorted(enumerate(qs, 1), key=lambda x: (-int(x[1][0][1]), x[0]))[:3]
        pick[u] = [[f"Q{u}.{i:02d}", q[1], q[2]] for i, q in sorted(hard)]
    return pick

if __name__ == "__main__":
    notebook()
    open(os.path.join(OUT, "AI_Unit_Quizzes.tex"), "w").write(booklet())
    open(os.path.join(OUT, "README.md"), "w").write(readme())
    for k, u in enumerate(QUIZ, 1):
        open(os.path.join(ROOT, "01_Unit_Notes", "latex", f"unit{k}_quiz.tex"), "w").write(notes_insert(u))
    json.dump(ppt_json(), open(os.path.join(ROOT, "02_PPT", "src", "quiz.json"), "w"), indent=1, ensure_ascii=False)
    print("✓ booklet, README, notes inserts and PPT quiz data written")
