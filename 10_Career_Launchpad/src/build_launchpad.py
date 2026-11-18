"""Build 10_Career_Launchpad: handbook (LaTeX/PDF), README, animated skill-outcome SVG and finale-deck data.
Run from repo root:  python 10_Career_Launchpad/src/build_launchpad.py
"""
import os, sys, json, base64, io
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "07_Interview_Prep", "src"))
from venues_data import HACKATHONS, CONFERENCES, JOURNALS, SKILL_BARS, END_PRODUCTS, CAN_DO
from build_interview import tex
OUT = os.path.join(ROOT, "10_Career_Launchpad")
F = "Times New Roman, Times, serif"

# ======================================================================= animated SVG
def skill_svg():
    from PIL import Image
    im = Image.open(os.path.join(ROOT, "assets", "logo.png")).convert("RGB"); im.thumbnail((140, 140))
    buf = io.BytesIO(); im.save(buf, "PNG", optimize=True); logo = base64.b64encode(buf.getvalue()).decode()
    W, H = 1200, 720
    units = [("I", "Agents"), ("II", "Search"), ("III", "Logic"), ("IV", "Uncertainty"), ("V", "Learning")]
    xs = [110 + i * 205 for i in range(5)]
    path_d = "M70 205 " + " ".join(f"L{x} 205" for x in xs) + " L1130 205"
    P = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
 <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0B1F4B"/><stop offset="1" stop-color="#1F3A7A"/></linearGradient>
 <linearGradient id="bar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#C9A227"/><stop offset="1" stop-color="#F6EBC8"/></linearGradient>
 <radialGradient id="glow"><stop offset="0" stop-color="#F6EBC8" stop-opacity=".9"/><stop offset="1" stop-color="#C9A227" stop-opacity="0"/></radialGradient>
</defs>
<style>
 .in {{ animation: in .8s ease-out backwards; }}
 @keyframes in {{ from {{ opacity: 0; transform: translateY(14px); }} to {{ opacity: 1; transform: none; }} }}
 .grow {{ transform-box: fill-box; transform-origin: left center; animation: grow 1.6s cubic-bezier(.2,.8,.2,1) backwards; }}
 @keyframes grow {{ from {{ transform: scaleX(0); }} to {{ transform: scaleX(1); }} }}
 .pulse {{ transform-box: fill-box; transform-origin: center; animation: pulse 2s ease-in-out infinite; }}
 @keyframes pulse {{ 0%,100% {{ transform: scale(1); }} 50% {{ transform: scale(1.12); }} }}
 .trophy {{ transform-box: fill-box; transform-origin: center bottom; animation: bounce 2.4s ease-in-out infinite; }}
 @keyframes bounce {{ 0%,100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-6px); }} }}
</style>
<rect width="{W}" height="{H}" rx="18" fill="url(#bg)"/>
<g class="in"><rect x="30" y="22" width="68" height="68" rx="9" fill="#FFFFFF" stroke="#C9A227" stroke-width="2.5"/>
<image x="34" y="26" width="60" height="60" href="data:image/png;base64,{logo}"/>
<text x="116" y="52" font-family="{F}" font-size="30" font-weight="bold" fill="#FFFFFF">End-of-Course Skill Outcome</text>
<text x="116" y="80" font-family="{F}" font-size="17" fill="#C9A227">26UAMPC204 Artificial Intelligence · from Unit I to job-ready AI engineer</text></g>
<path d="{path_d}" stroke="#C9A227" stroke-width="4" stroke-dasharray="10 8" fill="none" opacity=".7"/>
<circle r="9" fill="url(#glow)"><animateMotion dur="6s" repeatCount="indefinite" path="{path_d}"/></circle>
<circle r="4" fill="#FFFFFF"><animateMotion dur="6s" repeatCount="indefinite" path="{path_d}"/></circle>''']
    for i, ((u, name), x) in enumerate(zip(units, xs)):
        d = 0.3 + i * 0.35
        P.append(f'''<g class="in" style="animation-delay:{d:.2f}s"><circle class="pulse" style="animation-delay:{i*0.4:.1f}s" cx="{x}" cy="205" r="34" fill="#0B1F4B" stroke="#C9A227" stroke-width="3"/>
<text x="{x}" y="214" text-anchor="middle" font-family="{F}" font-size="24" font-weight="bold" fill="#C9A227">{u}</text>
<text x="{x}" y="262" text-anchor="middle" font-family="{F}" font-size="16" fill="#FFFFFF">{name}</text></g>''')
    P.append(f'''<g class="in" style="animation-delay:2.1s"><g class="trophy">
<path d="M1105 170 h50 v18 a25 25 0 0 1 -50 0 z" fill="#C9A227"/><rect x="1122" y="212" width="16" height="12" fill="#C9A227"/><rect x="1110" y="224" width="40" height="8" rx="2" fill="#C9A227"/>
<path d="M1105 176 h-10 a12 12 0 0 0 12 16" stroke="#C9A227" stroke-width="4" fill="none"/><path d="M1155 176 h10 a12 12 0 0 1 -12 16" stroke="#C9A227" stroke-width="4" fill="none"/></g>
<text x="1130" y="262" text-anchor="middle" font-family="{F}" font-size="16" font-weight="bold" fill="#F6EBC8">Job-ready</text></g>''')
    P.append(f'<text x="60" y="320" font-family="{F}" font-size="20" font-weight="bold" fill="#C9A227" class="in" style="animation-delay:2.3s">Competency reached by the end of the course</text>')
    from xml.sax.saxutils import escape as esc
    for i, (skill, lvl, ev) in enumerate(SKILL_BARS):
        skill, ev = esc(skill), esc(ev)
        y = 345 + i * 40; d = 2.5 + i * 0.18; w = int(560 * lvl / 100)
        P.append(f'''<g class="in" style="animation-delay:{d:.2f}s">
<text x="60" y="{y+19}" font-family="{F}" font-size="16" fill="#FFFFFF">{skill}</text>
<rect x="400" y="{y+4}" width="560" height="20" rx="10" fill="#FFFFFF" fill-opacity=".12"/>
<rect class="grow" style="animation-delay:{d+0.1:.2f}s" x="400" y="{y+4}" width="{w}" height="20" rx="10" fill="url(#bar)"/>
<text x="{400+w-8}" y="{y+19}" text-anchor="end" font-family="{F}" font-size="13" font-weight="bold" fill="#0B1F4B">{lvl}%</text>
<text x="975" y="{y+19}" font-family="{F}" font-size="13" font-style="italic" fill="#D9E2F3">{ev}</text></g>''')
    P.append(f'<text x="60" y="{H-22}" font-family="{F}" font-size="13" fill="#D9E2F3" class="in" style="animation-delay:4.2s">Target competency levels for a student who completes all labs, assignments and the mini-project. Evidence column shows where each skill is demonstrated.</text>')
    P.append("</svg>")
    open(os.path.join(ROOT, "assets", "skill_outcome_animated.svg"), "w").write("\n".join(P))

# ======================================================================= handbook (LaTeX)
def handbook():
    L = [r"\documentclass[11pt]{article}", r"\usepackage{../common/ai204}", r"\renewcommand{\doctitle}{Career Launchpad}",
         r"\begin{document}",
         r"\aicover{Career Launchpad}{End-of-course skill outcome \textbullet\ Top AI hackathons \textbullet\ Conferences \textbullet\ Journals}{From classroom to competitions, publications and jobs}",
         r"\section*{End-of-course skill outcome}",
         r"\begin{outcome}[By the end of 26UAMPC204 you can \dots]\begin{enumerate}"]
    L += [rf"\item {tex(c)}" for c in CAN_DO]
    L += [r"\end{enumerate}\end{outcome}",
          r"\subsection*{Competency map}", r"\begin{center}\begin{tikzpicture}[x=1cm,y=-0.78cm]"]
    for i, (s, lvl, ev) in enumerate(SKILL_BARS):
        L.append(rf"\node[anchor=east,font=\small\color{{navy}}] at (6.2,{i}) {{{tex(s)}}};")
        L.append(rf"\fill[navy!10,rounded corners=3pt] (6.4,{i-0.28}) rectangle (14.4,{i+0.28});")
        L.append(rf"\fill[gold,rounded corners=3pt] (6.4,{i-0.28}) rectangle ({6.4+8*lvl/100:.2f},{i+0.28});")
        L.append(rf"\node[anchor=east,font=\scriptsize\bfseries\color{{navy}}] at ({6.3+8*lvl/100:.2f},{i}) {{{lvl}\%}};")
    L += [r"\end{tikzpicture}\\{\small\color{slate}Target competency for a student who completes every lab, assignment and the mini-project.}\end{center}",
          r"\subsection*{What you walk out with (end products)}",
          r"\begin{tabularx}{\linewidth}{>{\leavevmode\bfseries\color{navy}}p{4.2cm}X}\toprule"]
    L += [rf"{tex(a)} & {tex(b)}\\" for a, b in END_PRODUCTS]
    L += [r"\bottomrule\end{tabularx}",
          r"\subsection*{Skill passport --- sign-off by the course faculty}",
          r"\begin{center}\small\begin{tabularx}{\linewidth}{c X c c}",
          r"\rowcolor{navy}\textcolor{gold}{\textbf{\#}}&\textcolor{gold}{\textbf{Can-do statement}}&\textcolor{gold}{\textbf{Evidence (link)}}&\textcolor{gold}{\textbf{Faculty sign}}\\"]
    for i, c in enumerate(CAN_DO, 1):
        L.append((r"\rowcolor{ivory}" if i % 2 == 0 else "") + rf"{i}&{tex(c)}&\rule{{2.6cm}}{{0.4pt}}&\rule{{2cm}}{{0.4pt}}\\[6pt]")
    L += [r"\end{tabularx}\end{center}", r"\newpage",
          r"\section*{Top AI hackathons and competitions}",
          r"{\small\color{slate}Windows were checked against the 2025--26 editions in November 2026; dates move every year, so always confirm on the official site before planning.}\par\medskip"]
    for i, (n, org, lvl, win, who, fit, units, url) in enumerate(HACKATHONS, 1):
        L.append(rf"""\begin{{tcolorbox}}[enhanced,breakable,colback=white,colframe=navy,arc=2mm,boxrule=0.8pt,left=3mm,right=3mm,
 title={{\textbf{{H{i}.\ {tex(n)}}}\hfill\colorbox{{gold}}{{\scriptsize\bfseries\color{{navy}} {lvl.upper()}}}}},fonttitle=\color{{white}},colbacktitle=navy]
\begin{{tabularx}}{{\linewidth}}{{>{{\leavevmode\bfseries\color{{navy}}}}p{{2.7cm}}X}}
Organiser & {tex(org)}\\ Typical window & {tex(win)}\\ Who can enter & {tex(who)}\\ AI fit & {tex(fit)}\\
Course units & Unit {units}\qquad \textbf{{\color{{navy}}Official site:}} \url{{{url}}}\\
\end{{tabularx}}\end{{tcolorbox}}""")
    L += [r"\begin{keypoint}[Hackathon playbook]",
          r"Form a team in week 1 with mixed skills (algorithms, ML, UI, pitching) $\rightarrow$ formulate the problem with PEAS $\rightarrow$ build the simplest working baseline first $\rightarrow$ add one AI technique that clearly improves it $\rightarrow$ rehearse a 3-minute demo with numbers $\rightarrow$ publish the repository with a README.",
          r"\end{keypoint}", r"\newpage",
          r"\section*{Top AI conferences}",
          r"{\small\color{slate}CORE ranks from the CORE conference portal; re-check before citing. ``---'' = not ranked by CORE (national venue).}\par\medskip",
          r"\begin{center}\small\begin{longtable}{>{\leavevmode\bfseries\color{navy}}l p{5.4cm} c c p{4.2cm}}",
          r"\rowcolor{navy}\textcolor{gold}{\textbf{Venue}}&\textcolor{gold}{\textbf{Full name / focus}}&\textcolor{gold}{\textbf{CORE}}&\textcolor{gold}{\textbf{Units}}&\textcolor{gold}{\textbf{Student entry point}}\\\endhead"]
    for i, (a, full, core, units, focus, tip) in enumerate(CONFERENCES):
        L.append((r"\rowcolor{ivory}" if i % 2 else "") + rf"{tex(a)}&{tex(full)}\newline{{\scriptsize\color{{slate}}{tex(focus)}}}&{core}&{units}&{tex(tip)}\\")
    L += [r"\end{longtable}\end{center}",
          r"\section*{Top AI journals}",
          r"\begin{center}\small\begin{longtable}{>{\leavevmode\bfseries\color{navy}}p{6.2cm} p{2.8cm} c p{4cm}}",
          r"\rowcolor{navy}\textcolor{gold}{\textbf{Journal}}&\textcolor{gold}{\textbf{Publisher}}&\textcolor{gold}{\textbf{Units}}&\textcolor{gold}{\textbf{Focus / standing}}\\\endhead"]
    for i, (n, pub, units, focus, tier) in enumerate(JOURNALS):
        L.append((r"\rowcolor{ivory}" if i % 2 else "") + rf"{tex(n)}&{tex(pub)}&{units}&{tex(focus)}\newline{{\scriptsize\color{{teal}}{tex(tier)}}}\\")
    L += [r"\end{longtable}\end{center}",
          r"\begin{caution}[Avoid predatory venues]",
          r"Check that a journal is indexed in Scopus or Web of Science (or listed in UGC-CARE where required), never pay to publish without a real peer review, and be wary of unsolicited e-mail invitations promising fast acceptance.",
          r"\end{caution}",
          r"\begin{keypoint}[A realistic student publication path]",
          r"Course project $\rightarrow$ workshop paper or student track (AAAI student abstracts, ACL student research workshop, CODS-COMAD young researchers) $\rightarrow$ conference main track or IEEE Access $\rightarrow$ Q1 journal with your supervisor.",
          r"\end{keypoint}", r"\end{document}"]
    return "\n".join(L)

def readme():
    L = ["<p align=\"center\"><img src=\"../assets/skill_outcome_animated.svg\" width=\"100%\" alt=\"End-of-course skill outcome\"></p>", "",
         "# 🚀 Career Launchpad — 26UAMPC204 Artificial Intelligence", "",
         "📄 Printable handbook: [AI_Career_Launchpad.pdf](AI_Career_Launchpad.pdf)", "",
         "## 🎓 By the end of this course you can …", ""]
    L += [f"- [x] {c}" for c in CAN_DO]
    L += ["", "## 📦 End products every student walks out with", "", "| Product | What it is |", "|---|---|"]
    L += [f"| **{a}** | {b} |" for a, b in END_PRODUCTS]
    L += ["", "## 🏆 Top AI hackathons & competitions", "",
          "> Windows were checked against the 2025–26 editions (November 2026). Dates move every year, so always confirm on the official site.", "",
          "| Hackathon | Organiser | Level | Typical window | AI fit | Units |", "|---|---|:-:|---|---|:-:|"]
    L += [f"| [**{n}**]({url}) | {org} | {lvl} | {win} | {fit} | {u} |" for n, org, lvl, win, who, fit, u, url in HACKATHONS]
    L += ["", "## 🎤 Top AI conferences", "", "CORE ranks from the CORE portal; re-check before citing. `—` = national venue, not ranked by CORE.", "",
          "| Venue | Full name | CORE | Units | Student entry point |", "|---|---|:-:|:-:|---|"]
    L += [f"| **{a}** | {full} — *{focus}* | `{core}` | {u} | {tip} |" for a, full, core, u, focus, tip in CONFERENCES]
    L += ["", "## 📚 Top AI journals", "", "| Journal | Publisher | Units | Focus | Standing |", "|---|---|:-:|---|---|"]
    L += [f"| **{n}** | {p} | {u} | {f} | {t} |" for n, p, u, f, t in JOURNALS]
    L += ["", "> ⚠️ **Avoid predatory venues:** check Scopus / Web of Science indexing (or UGC-CARE where required), never pay to publish without real peer review, and ignore unsolicited \"fast acceptance\" e-mails.", ""]
    return "\n".join(L) + "\n"

def finale_json():
    return {"can_do": CAN_DO, "skills": SKILL_BARS, "products": END_PRODUCTS,
            "hackathons": [[h[0], h[3]] for h in HACKATHONS[:6]],
            "conferences": [c[0] for c in CONFERENCES], "journals": [j[0] for j in JOURNALS[:8]]}

if __name__ == "__main__":
    skill_svg()
    open(os.path.join(OUT, "AI_Career_Launchpad.tex"), "w").write(handbook())
    open(os.path.join(OUT, "README.md"), "w").write(readme())
    json.dump(finale_json(), open(os.path.join(ROOT, "02_PPT", "src", "finale.json"), "w"), indent=1, ensure_ascii=False)
    print("✓ launchpad handbook, README, skill SVG and finale data written")
