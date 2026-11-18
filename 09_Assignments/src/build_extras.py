"""Build 08_Research_Ideas and 09_Assignments (LaTeX, Markdown, executed starter notebooks).
Run from repo root:  python 09_Assignments/src/build_extras.py
"""
import os, sys, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
for p in ("08_Research_Ideas/src", "09_Assignments/src", "07_Interview_Prep/src", "06_Notebooks/src"):
    sys.path.insert(0, os.path.join(ROOT, p))
from research_data import IDEAS
from assignments_data import ASSIGNMENTS
from build_interview import tex, TITLES, CO
from nb_common import box

LEVEL_COL = {"UG Project": "teal", "M.Tech / Minor Thesis": "navyL", "Ph.D. Direction": "crimson"}
CLEAN = {"✓": "[ok]", "→": "->", "×": "x", "°": " deg", "≥": ">=", "–": "-", "—": "--", "’": "'", "−": "-"}
def code_clean(s):
    for a, b in CLEAN.items(): s = s.replace(a, b)
    return s
LOGO = "https://raw.githubusercontent.com/drssnaiml1-cell/26UAMPC204-Artificial-Intelligence/main/assets/logo.png"

# ======================================================================= Research ideas
def research_tex():
    L = [r"\documentclass[11pt]{article}", r"\usepackage{../common/ai204}", r"\renewcommand{\doctitle}{Research Ideas}",
         r"\begin{document}",
         r"\aicover{Research Ideas Handbook}{20 unit-aligned research directions \textbullet\ UG projects, M.Tech theses and Ph.D. directions}{Gap \textbullet\ Method \textbullet\ Data \& Tools \textbullet\ Expected Outcome \textbullet\ Target Venues}",
         r"\section*{From classroom to research}",
         r"Every topic in this course is an active research area. Each idea below states the \textbf{gap}, a concrete \textbf{method}, the \textbf{data and tools} needed, the \textbf{expected outcome} and suitable \textbf{publication venues}. Levels indicate scope: \colorbox{teal!15}{\textcolor{teal}{\textbf{UG Project}}} (one semester), \colorbox{navyL!15}{\textcolor{navyL}{\textbf{M.Tech / Minor Thesis}}} (one year) and \colorbox{crimson!15}{\textcolor{crimson}{\textbf{Ph.D. Direction}}} (multi-year).",
         r"\begin{keypoint}[How to turn an idea into a paper]",
         r"(1) Read 15--20 recent papers and write a one-page gap statement. (2) Reproduce one baseline. (3) Propose one clear change and test it on a public dataset with proper metrics and statistics. (4) Report negative results honestly. (5) Release code and data on GitHub. (6) Choose the venue whose recent papers your work cites most.",
         r"\end{keypoint}",
         r"\begin{keypoint}[Research ethics]",
         r"Obtain consent and institutional approval before collecting data from people; anonymise records; follow dataset licences; never fabricate or selectively report results.",
         r"\end{keypoint}", r"\newpage"]
    for u, ideas in IDEAS.items():
        L.append(rf"\unitbanner{{{u}}}{{{tex(TITLES[u])}}}{{4 Research Ideas \textbullet\ {CO[u]}}}")
        for i, (t, lvl, gap, meth, tools, out, ven) in enumerate(ideas, 1):
            c = LEVEL_COL[lvl]
            L.append(rf"""\begin{{tcolorbox}}[enhanced,breakable,colback=white,colframe={c},arc=2mm,boxrule=0.9pt,
 title={{\textbf{{R{u}.{i}\quad {tex(t)}}}}},fonttitle=\color{{white}},colbacktitle={c}]
\colorbox{{{c}!15}}{{\scriptsize\bfseries\color{{{c}}} {tex(lvl).upper()}}}\par\smallskip
\begin{{tabularx}}{{\linewidth}}{{>{{\leavevmode\bfseries\color{{navy}}}}p{{3.0cm}}X}}
Research gap & {tex(gap)}\\
Method & {tex(meth)}\\
Data \& tools & {tex(tools)}\\
Outcome & {tex(out)}\\
Target venues & {tex(ven)}\\
\end{{tabularx}}
\end{{tcolorbox}}""")
        L.append(r"\newpage")
    L.append(r"\end{document}")
    return "\n".join(L)

def research_md():
    L = ["# 🔬 Research Ideas — 26UAMPC204 Artificial Intelligence", "",
         "20 unit-aligned research directions. **Levels:** 🟢 UG Project · 🔵 M.Tech / Minor Thesis · 🔴 Ph.D. Direction.", "",
         "📄 Full handbook: [AI_Research_Ideas.pdf](AI_Research_Ideas.pdf)", ""]
    icon = {"UG Project": "🟢", "M.Tech / Minor Thesis": "🔵", "Ph.D. Direction": "🔴"}
    for u, ideas in IDEAS.items():
        L += [f"## Unit {u}: {TITLES[u]}", ""]
        for i, (t, lvl, gap, meth, tools, out, ven) in enumerate(ideas, 1):
            L += [f"<details><summary>{icon[lvl]} <b>R{u}.{i} {t}</b> <i>({lvl})</i></summary>", "",
                  f"- **Gap:** {gap}", f"- **Method:** {meth}", f"- **Data & tools:** {tools}",
                  f"- **Expected outcome:** {out}", f"- **Target venues:** {ven}", "", "</details>", ""]
    return "\n".join(L) + "\n"

# ======================================================================= Assignments
def assign_tex():
    L = [r"\documentclass[11pt]{article}", r"\usepackage{../common/ai204}", r"\renewcommand{\doctitle}{Assignments}",
         r"\begin{document}",
         r"\aicover{Assignment Booklet}{5 unit-wise assignments \textbullet\ think-out-of-the-box questions \textbullet\ open-ended coding problems with starter code}{Creativity \textbullet\ Critical thinking \textbullet\ Implementation \textbullet\ Responsible AI}",
         r"\section*{Instructions}",
         r"\begin{itemize}\item Each assignment has \textbf{Part A} (4 think-out-of-the-box questions, answer in 250--400 words each) and \textbf{Part B} (3 open-ended coding problems).",
         r"\item Starter code for Part B is in \texttt{09\_Assignments/notebooks/}; it runs as-is and prints a baseline. Complete every \texttt{TODO}.",
         r"\item There is no single correct answer. Marks reward originality, sound reasoning, working code, clear plots and honest discussion of limitations.",
         r"\item Submit a PDF report plus a GitHub link. You may use AI tools only if you state how you used them; copied or undisclosed AI text earns zero.\end{itemize}",
         r"\begin{center}\begin{tabular}{l p{9.5cm} c}\rowcolor{navy}\textcolor{gold}{\textbf{Criterion}}&\textcolor{gold}{\textbf{What earns full marks}}&\textcolor{gold}{\textbf{Marks}}\\",
         r"Originality&Ideas not found in the textbook; creative but defensible&5\\",
         r"\rowcolor{ivory}Reasoning&Correct use of course concepts; arguments with evidence&5\\",
         r"Implementation&Working, readable code; all TODOs completed; tests or checks&6\\",
         r"\rowcolor{ivory}Analysis&Plots, comparisons, honest limitations&4\\\midrule",
         r"\textbf{Total}&&\textbf{20}\\\end{tabular}\end{center}",
         r"\begin{center}\begin{tabular}{c l c c}\rowcolor{navy}\textcolor{gold}{\textbf{No.}}&\textcolor{gold}{\textbf{Title}}&\textcolor{gold}{\textbf{Unit / CO}}&\textcolor{gold}{\textbf{Due}}\\"]
    for k, a in enumerate(ASSIGNMENTS, 1):
        L.append((r"\rowcolor{ivory}" if k % 2 == 0 else "") + rf"{k}&{tex(a['title'])}&Unit {a['unit']} / {a['co']}&{a['due']}\\")
    L += [r"\end{tabular}\end{center}", r"\newpage"]
    for k, a in enumerate(ASSIGNMENTS, 1):
        L.append(rf"\unitbanner{{{a['unit']}}}{{Assignment {k}: {tex(a['title'])}}}{{{a['co']} \textbullet\ Due: {a['due']}}}")
        L.append(r"\subsection*{\color{navy}Part A --- Think out of the box}")
        for i, (btl, q) in enumerate(a["think"], 1):
            L.append(rf"""\begin{{tcolorbox}}[enhanced,colback=goldL,colframe=gold!80!black,arc=2mm,boxrule=0.8pt,left=3mm]
\textbf{{\color{{navy}}A{k}.{i}}}\quad {tex(q)}\hfill\btl{{{btl}}}
\end{{tcolorbox}}""")
        L.append(r"\subsection*{\color{navy}Part B --- Open-ended coding problems}")
        outs = json.load(open(os.path.join(ROOT, "09_Assignments", "notebooks", f".outputs_{k}.json")))
        for i, (t, prompt, code) in enumerate(a["code"], 1):
            L += [rf"\subsubsection*{{B{k}.{i}\quad {tex(t)}}}", tex(prompt),
                  r"\begin{lstlisting}[style=py]", code_clean(code), r"\end{lstlisting}"]
            if outs[i - 1].strip():
                L += [r"\noindent{\small\bfseries\color{gold!70!black}Baseline output of the starter code}",
                      r"\begin{lstlisting}[style=out]", code_clean(outs[i - 1].strip()), r"\end{lstlisting}"]
        L.append(r"\newpage")
    L.append(r"\end{document}")
    return "\n".join(L)

def assign_md():
    L = ["# 📝 Assignments — 26UAMPC204 Artificial Intelligence", "",
         "Five unit-wise assignments. **Part A:** think-out-of-the-box questions. **Part B:** open-ended coding problems with runnable starter code in [`notebooks/`](notebooks).", "",
         "📄 Printable booklet: [AI_Assignments_Booklet.pdf](AI_Assignments_Booklet.pdf) · Rubric: originality 5 · reasoning 5 · implementation 6 · analysis 4 = **20 marks**", ""]
    for k, a in enumerate(ASSIGNMENTS, 1):
        L += [f"## Assignment {k}: {a['title']} (Unit {a['unit']} · {a['co']} · due {a['due']})", "",
              f"▶️ Starter notebook: [`Assignment_{k}_Starter.ipynb`](notebooks/Assignment_{k}_Starter.ipynb)", "",
              "### Part A — Think out of the box", ""]
        L += [f"{i}. **[{btl}]** {q}" for i, (btl, q) in enumerate(a["think"], 1)]
        L += ["", "### Part B — Open-ended coding", ""]
        L += [f"{i}. **{t}** — {p}" for i, (t, p, _) in enumerate(a["code"], 1)]
        L.append("")
    return "\n".join(L) + "\n"

def assign_notebooks():
    import nbformat
    from nbclient import NotebookClient
    d = os.path.join(ROOT, "09_Assignments", "notebooks"); os.makedirs(d, exist_ok=True)
    for k, a in enumerate(ASSIGNMENTS, 1):
        nb = nbformat.v4.new_notebook(); nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
        nb.cells.append(nbformat.v4.new_markdown_cell(f'''<div style="background:#0B1F4B;padding:22px 26px;border-radius:12px;border:3px solid #C9A227;font-family:'Times New Roman',serif">
<img src="{LOGO}" alt="Sanjivani University" width="92" style="float:right;background:#FFFFFF;border:2px solid #C9A227;border-radius:8px;padding:3px;margin-left:14px">
<div style="color:#C9A227;font-size:14px;letter-spacing:2px;font-weight:bold">26UAMPC204 · ARTIFICIAL INTELLIGENCE · ASSIGNMENT {k} · UNIT {a['unit']} · {a['co']}</div>
<div style="color:#FFFFFF;font-size:30px;font-weight:bold;margin-top:6px">{a['title']}</div>
<div style="color:#F6EBC8;font-size:15px;margin-top:8px">Due: {a['due']} · Name: ____________ · Roll No: ________</div>
<div style="clear:both"></div></div>'''))
        nb.cells.append(nbformat.v4.new_markdown_cell("## 🧠 Part A — Think out of the box\n\nAnswer each in 250–400 words in the markdown cells below.\n\n" +
                        "\n".join(f"{i}. **[{b}]** {q}" for i, (b, q) in enumerate(a["think"], 1))))
        for i in range(1, 5):
            nb.cells.append(nbformat.v4.new_markdown_cell(f"**Answer A{k}.{i}:** _write here_"))
        nb.cells.append(nbformat.v4.new_markdown_cell("## 💻 Part B — Open-ended coding\n\nThe starter code runs as-is and prints a baseline. Complete every `TODO`."))
        for i, (t, p, code) in enumerate(a["code"], 1):
            nb.cells.append(nbformat.v4.new_markdown_cell(f"### B{k}.{i} · {t}\n\n" + box("Task", p, "#1F3A7A", "#EEF2F8")))
            nb.cells.append(nbformat.v4.new_code_cell(code))
            nb.cells.append(nbformat.v4.new_code_cell(f"# Your solution for B{k}.{i}\n"))
        nb.cells.append(nbformat.v4.new_markdown_cell("## 📋 Reflection\n\nWhat surprised you? What would you do with one more week? How did you use AI tools, if at all?"))
        NotebookClient(nb, timeout=600, kernel_name="python3", resources={"metadata": {"path": d}}).execute()
        nbformat.write(nb, os.path.join(d, f"Assignment_{k}_Starter.ipynb"))
        outs, j = [], 0
        for c in nb.cells:
            if c.cell_type == "code" and not c.source.startswith("# Your solution"):
                outs.append("".join(o.get("text", "") for o in c.get("outputs", []) if o.get("output_type") == "stream"))
        json.dump(outs, open(os.path.join(d, f".outputs_{k}.json"), "w"), ensure_ascii=False)
        print(f"✓ Assignment_{k}_Starter.ipynb")

if __name__ == "__main__":
    assign_notebooks()
    R = os.path.join(ROOT, "08_Research_Ideas"); A = os.path.join(ROOT, "09_Assignments")
    open(os.path.join(R, "AI_Research_Ideas.tex"), "w").write(research_tex())
    open(os.path.join(R, "README.md"), "w").write(research_md())
    open(os.path.join(A, "AI_Assignments_Booklet.tex"), "w").write(assign_tex())
    open(os.path.join(A, "README.md"), "w").write(assign_md())
    print("✓ research ideas and assignment booklet written")
