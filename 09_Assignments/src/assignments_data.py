"""Five unit-wise assignments: think-out-of-the-box questions and open-ended coding questions.
Each coding question has starter code that runs as-is (baseline) and TODOs for the student.
"""
ASSIGNMENTS = [
dict(unit="I", co="CO204.1", title="Agents in the Wild",
 due="End of Week 3",
 think=[
  ("L5", "If a self-driving car is perfectly rational for its performance measure but still hits a pedestrian in a sudden event, is the car 'to blame'? Argue from the definition of rationality, then propose how the performance measure itself should change."),
  ("L6", "Invent a new agent type that does not fit any of the five classical architectures (reflex, model, goal, utility, learning). Describe its internal structure with a diagram and give a real problem where it beats all five."),
  ("L4", "Your phone's keyboard autocomplete is an agent. Write its PEAS, classify its environment along all seven properties, and identify which property makes it hardest to design."),
  ("L5", "Design a 'Reverse Turing Test' in which a machine must decide whether it is talking to a human or another AI. What questions would it ask, and why might this become important by 2030?"),
 ],
 code=[
  ("Open-ended: a smarter vacuum world",
   "Extend the vacuum world to an n×n grid where dirt re-appears randomly. Design the best agent you can and justify its performance measure. Compare at least three agent designs over 500 runs.",
   r'''import random
def run(agent, n=4, steps=200, p_dirt=0.05, seed=0):
    rng = random.Random(seed); dirt = {(r, c): rng.random() < 0.5 for r in range(n) for c in range(n)}
    pos, score, mem = (0, 0), 0, {}
    for _ in range(steps):
        action = agent(pos, dirt[pos], mem, n)
        if action == "Suck" and dirt[pos]: dirt[pos] = False; score += 10
        elif action in ("Up", "Down", "Left", "Right"):
            dr, dc = {"Up": (-1, 0), "Down": (1, 0), "Left": (0, -1), "Right": (0, 1)}[action]
            pos = (min(max(pos[0] + dr, 0), n - 1), min(max(pos[1] + dc, 0), n - 1)); score -= 1
        for k in dirt:                                   # dirt re-appears
            if rng.random() < p_dirt: dirt[k] = True
    return score

def random_agent(pos, dirty, mem, n):
    return "Suck" if dirty else random.choice(["Up", "Down", "Left", "Right"])

print("Random agent mean score:", sum(run(random_agent, seed=s) for s in range(50)) / 50)
# TODO 1: write a model-based agent that remembers when it last visited each cell.
# TODO 2: write a utility-based agent that moves towards the cell most likely to be dirty.
# TODO 3: plot the score distributions of all agents and explain the winner.'''),
  ("Open-ended: formulate your own search problem",
   "Pick a real problem from your daily life (bus route to campus, cooking a meal, packing a bag). Formulate it with the five components and solve a small instance with BFS. Report the state-space size.",
   r'''from collections import deque
# Example formulation: the classic Farmer-Wolf-Goat-Cabbage river crossing.
# State: tuple of sides (0 = left, 1 = right) for (farmer, wolf, goat, cabbage)
def safe(s):
    f, w, g, c = s
    return not ((w == g != f) or (g == c != f))
def successors(s):
    f = s[0]
    for i in range(4):                     # farmer crosses alone (i=0) or with item i
        if s[i] == f:
            t = list(s); t[0] = 1 - f
            if i: t[i] = 1 - f
            t = tuple(t)
            if safe(t): yield t
def bfs(start, goal):
    q, par = deque([start]), {start: None}
    while q:
        s = q.popleft()
        if s == goal:
            path = []
            while s: path.append(s); s = par[s]
            return path[::-1]
        for n in successors(s):
            if n not in par: par[n] = s; q.append(n)
path = bfs((0, 0, 0, 0), (1, 1, 1, 1))
print(f"Solved in {len(path) - 1} crossings:", path)
# TODO: replace this with YOUR problem. State clearly: states, initial state, actions,
#       transition model, goal test and path cost. Count reachable states.'''),
  ("Open-ended: performance-measure stress test",
   "Write two performance measures for the same agent that lead to visibly different behaviour. Show the difference with a plot and explain which you would ship.",
   r'''# Starter idea: an elevator agent choosing which floor to serve next.
import random
def simulate(choose, steps=300, floors=10, seed=1):
    rng = random.Random(seed); waiting, pos, waits = {}, 0, []
    for t in range(steps):
        if rng.random() < 0.6: waiting.setdefault(rng.randrange(floors), []).append(t)
        if waiting:
            target = choose(pos, waiting)
            pos += (target > pos) - (target < pos)          # move one floor per time step
            if pos in waiting: waits += [t - a for a in waiting.pop(pos)]
    return sum(waits) / max(len(waits), 1), max(waits or [0])
nearest = lambda pos, w: min(w, key=lambda f: abs(f - pos))
oldest  = lambda pos, w: min(w, key=lambda f: min(w[f]))
print("nearest-first (mean wait, max wait):", simulate(nearest))
print("oldest-first  (mean wait, max wait):", simulate(oldest))
# TODO: define the performance measure you think is fair, design an agent for it,
#       and discuss the trade-off between mean and worst-case waiting time.'''),
 ]),
dict(unit="II", co="CO204.2", title="Search Beyond the Textbook",
 due="End of Week 6",
 think=[
  ("L5", "A* is optimal with an admissible heuristic. Give a real situation where you would deliberately use an inadmissible heuristic, and argue why the loss of optimality is acceptable."),
  ("L6", "Design a heuristic for finding the fastest route between two classrooms on your campus that accounts for stairs, lifts and crowds at bell time. Is it admissible? Prove or disprove it."),
  ("L4", "Why can a chess engine look 20 moves ahead but a cricket-captain AI cannot? Analyse the difference in branching factor, observability and stochasticity."),
  ("L6", "Invent a two-player game that is small enough to solve with Minimax but would be interesting for humans. Define its rules and predict who wins with perfect play."),
 ],
 code=[
  ("Open-ended: heuristic design challenge",
   "Invent at least two new admissible heuristics for the 8-puzzle (beyond misplaced tiles and Manhattan distance) and compare nodes expanded on 50 random solvable puzzles.",
   r'''import heapq, itertools, random
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
def succ(s):
    i = s.index(0); r, c = divmod(i, 3)
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc; t = list(s); t[i], t[j] = t[j], t[i]; yield tuple(t)
def manhattan(s):
    return sum(abs(k // 3 - (v - 1) // 3) + abs(k % 3 - (v - 1) % 3) for k, v in enumerate(s) if v)
def astar(start, h):
    tie = itertools.count(); fr = [(h(start), 0, next(tie), start)]; g = {start: 0}; n = 0
    while fr:
        f, gs, _, s = heapq.heappop(fr); n += 1
        if s == GOAL: return gs, n
        for t in succ(s):
            if gs + 1 < g.get(t, 99): g[t] = gs + 1; heapq.heappush(fr, (gs + 1 + h(t), gs + 1, next(tie), t))
def scramble(k, seed):
    rnd = random.Random(seed); s = GOAL
    for _ in range(k): s = rnd.choice(list(succ(s)))
    return s
puzzles = [scramble(30, i) for i in range(10)]
print("Manhattan: mean nodes expanded =", sum(astar(p, manhattan)[1] for p in puzzles) / len(puzzles))
# TODO 1: implement 'linear conflict' (Manhattan + 2 per pair of tiles in the same row/col in reverse order).
# TODO 2: invent your own heuristic and prove it is admissible.
# TODO 3: run on 50 puzzles and plot nodes expanded for each heuristic.'''),
  ("Open-ended: local search on a real optimisation problem",
   "Choose a real optimisation task (seating plan, delivery tour, playlist ordering) and solve it with hill climbing and simulated annealing. Report how often each reaches the best value you found.",
   r'''import math, random
random.seed(0)
cities = [(random.random(), random.random()) for _ in range(25)]
def length(t): return sum(math.dist(cities[t[i]], cities[t[i - 1]]) for i in range(len(t)))
def two_opt_neighbour(t):
    i, j = sorted(random.sample(range(len(t)), 2)); return t[:i] + t[i:j][::-1] + t[j:]
def anneal(T=1.0, cool=0.995, steps=20000):
    cur = list(range(len(cities))); random.shuffle(cur); best = cur
    for _ in range(steps):
        nxt = two_opt_neighbour(cur); d = length(nxt) - length(cur)
        if d < 0 or random.random() < math.exp(-d / T): cur = nxt
        if length(cur) < length(best): best = cur
        T *= cool
    return length(best)
print("Simulated annealing tour length:", round(anneal(), 3))
# TODO: implement hill climbing with random restarts, compare over 20 seeds,
#       and try a different cooling schedule. Which matters more: schedule or neighbourhood?'''),
  ("Open-ended: build and break a game AI",
   "Write a Minimax + alpha–beta agent for Connect-Three on a 4×4 board (or your own game). Then write an evaluation function for a depth-limited version and show a position where it blunders.",
   r'''import math
ROWS, COLS, WIN = 4, 4, 3
def moves(b): return [c for c in range(COLS) if b[0][c] == "."]
def drop(b, c, p):
    nb = [row[:] for row in b]
    for r in range(ROWS - 1, -1, -1):
        if nb[r][c] == ".": nb[r][c] = p; return nb
def winner(b):
    for r in range(ROWS):
        for c in range(COLS):
            for dr, dc in ((0, 1), (1, 0), (1, 1), (1, -1)):
                cells = [(r + k * dr, c + k * dc) for k in range(WIN)]
                if all(0 <= x < ROWS and 0 <= y < COLS for x, y in cells):
                    v = {b[x][y] for x, y in cells}
                    if len(v) == 1 and "." not in v: return v.pop()
    return None
def ab(b, p, a=-math.inf, be=math.inf):
    w = winner(b)
    if w: return 1 if w == "X" else -1
    if not moves(b): return 0
    best = -math.inf if p == "X" else math.inf
    for c in moves(b):
        v = ab(drop(b, c, p), "O" if p == "X" else "X", a, be)
        if p == "X": best = max(best, v); a = max(a, v)
        else: best = min(best, v); be = min(be, v)
        if a >= be: break
    return best
empty = [["."] * COLS for _ in range(ROWS)]
print("Value of the empty 4x4 Connect-Three board for X:", ab(empty, "X"))
# TODO: add a depth limit + evaluation function, measure nodes searched,
#       and find a position where the depth-limited agent makes a wrong move.'''),
 ]),
dict(unit="III", co="CO204.3", title="Logic Meets the Real World",
 due="End of Week 9",
 think=[
  ("L4", "Translate the Sanjivani attendance rule (minimum attendance required to sit the exam, with medical exceptions) into first-order logic. Which parts resist precise logical encoding, and why?"),
  ("L5", "LLMs often answer logic puzzles wrongly. Is a resolution theorem prover 'smarter' than an LLM? Argue both sides with a concrete example."),
  ("L6", "Design a knowledge graph of your own life (people, places, courses, skills). What new facts can you infer with three rules? What privacy risks would publishing it create?"),
  ("L5", "A semantic network says 'penguins are birds' and 'birds fly'. Propose a principled way to handle exceptions without rewriting every rule, and evaluate its weaknesses."),
 ],
 code=[
  ("Open-ended: your own expert knowledge base",
   "Encode at least 15 facts and 8 rules about a domain you know well (cricket rules, a recipe, a game). Answer five non-trivial queries with forward chaining and print the derivation trace.",
   r'''FACTS = {("course", "AI"), ("course", "DSA"), ("prereq", "DSA", "AI"), ("passed", "asha", "DSA")}
RULES = [  # (head, [body]) with variables starting with '?'
    (("can_register", "?s", "?c"), [("passed", "?s", "?p"), ("prereq", "?p", "?c")]),
]
def match(pat, fact, th):
    if len(pat) != len(fact): return None
    th = dict(th)
    for p, f in zip(pat, fact):
        p = th.get(p, p)
        if p.startswith("?"): th[p] = f
        elif p != f: return None
    return th
def forward(facts):
    facts = set(facts); changed = True
    while changed:
        changed = False
        for head, body in RULES:
            thetas = [{}]
            for lit in body:
                thetas = [t2 for t in thetas for f in facts if (t2 := match(lit, f, t)) is not None]
            for t in thetas:
                new = tuple(t.get(x, x) for x in head)
                if new not in facts: facts.add(new); changed = True; print("derived", new)
    return facts
forward(FACTS)
# TODO: replace with YOUR domain (>= 15 facts, >= 8 rules, including one recursive rule),
#       add an explanation trace for each derived fact, and pose five queries.'''),
  ("Open-ended: resolution vs model checking",
   "Implement CNF conversion for propositional sentences and compare the speed of resolution and truth-table model checking as the number of symbols grows from 4 to 16.",
   r'''import itertools, random, time
def random_kb(n, m, seed=0):
    rnd = random.Random(seed)
    return [[(rnd.randrange(n), rnd.random() < 0.5) for _ in range(3)] for _ in range(m)]
def satisfiable_tt(kb, n):
    for vals in itertools.product([False, True], repeat=n):
        if all(any(vals[v] == sign for v, sign in cl) for cl in kb): return True
    return False
for n in (4, 8, 12, 16):
    kb = random_kb(n, int(4.2 * n)); t = time.time()
    print(f"n={n:2d}: satisfiable={satisfiable_tt(kb, n)}  truth-table time={time.time() - t:.3f}s")
# TODO 1: implement propositional resolution (or DPLL) and time it on the same KBs.
# TODO 2: plot time vs n on a log scale and explain the curve. What is special about m/n ~ 4.2?'''),
  ("Open-ended: mini ontology with SPARQL",
   "Build a small ontology (≥ 20 triples) for the AI&DS department and answer four questions with SPARQL queries.",
   r'''try:
    from rdflib import Graph, Namespace, RDF, Literal
    EX = Namespace("http://example.org/aids#"); g = Graph()
    g.add((EX.AI, RDF.type, EX.Course)); g.add((EX.AI, EX.hasCredits, Literal(3)))
    g.add((EX.AI, EX.taughtIn, EX.Semester3)); g.add((EX.DSA, EX.prerequisiteOf, EX.AI))
    q = "SELECT ?c WHERE { ?c <http://example.org/aids#prerequisiteOf> <http://example.org/aids#AI> }"
    print("Prerequisites of AI:", [str(r.c).split("#")[1] for r in g.query(q)])
except ImportError:
    print("Install rdflib first:  pip install rdflib")
# TODO: model courses, faculty, labs and skills (>= 20 triples) and write four SPARQL queries,
#       one of which needs a property path (e.g. prerequisites of prerequisites).'''),
 ]),
dict(unit="IV", co="CO204.4", title="Reasoning When Nothing Is Certain",
 due="End of Week 12",
 think=[
  ("L5", "A COVID-style rapid test is advertised as '95% accurate'. Explain to your family, without formulas, why a positive result might still be more likely wrong than right. When does it become reliable?"),
  ("L6", "Design a STRIPS model for 'getting ready for college in the morning'. Where does the classical-planning assumption fail in real life, and how would you repair the plan on the fly?"),
  ("L4", "Is 'tall' better modelled by probability or fuzzy logic? Construct a situation where using the wrong one leads to a bad decision."),
  ("L5", "Bayesian networks need a causal structure. What goes wrong if an expert draws an arrow in the wrong direction? Propose a test to detect it from data."),
 ],
 code=[
  ("Open-ended: build a Bayesian network for a decision you care about",
   "Choose a diagnosis or decision (laptop won't boot, will it rain at college, should I take the bus). Build a network with ≥ 5 nodes, justify every CPT, and answer three queries with enumeration.",
   r'''import itertools
# Starter: Rain -> WetRoad <- Sprinkler ; WetRoad -> Slip
P_R, P_S = 0.3, 0.2
P_W = {(True, True): 0.99, (True, False): 0.9, (False, True): 0.8, (False, False): 0.05}
P_SL = {True: 0.2, False: 0.01}
def joint(r, s, w, sl):
    p = (P_R if r else 1 - P_R) * (P_S if s else 1 - P_S)
    p *= P_W[(r, s)] if w else 1 - P_W[(r, s)]
    return p * (P_SL[w] if sl else 1 - P_SL[w])
def query(var_index, evidence):
    num = {True: 0.0, False: 0.0}
    for vals in itertools.product((True, False), repeat=4):
        if all(vals[i] == v for i, v in evidence.items()): num[vals[var_index]] += joint(*vals)
    z = sum(num.values()); return {k: round(v / z, 4) for k, v in num.items()}
print("P(Rain | Slip) =", query(0, {3: True}))
# TODO: design YOUR network (>= 5 nodes), justify CPTs from data or experts,
#       answer three queries and run a sensitivity analysis on one CPT entry.'''),
  ("Open-ended: fuzzy controller you can feel",
   "Design a fuzzy controller for something physical (fan speed, phone brightness, shower temperature). Plot membership functions and the control surface, then argue whether a simple formula would do better.",
   r'''import numpy as np
def tri(x, a, b, c): return np.maximum(np.minimum((x - a) / (b - a + 1e-9), (c - x) / (c - b + 1e-9)), 0)
def fan_speed(temp):
    cold, warm, hot = tri(temp, 0, 10, 22), tri(temp, 15, 25, 35), tri(temp, 28, 40, 52)
    z = np.linspace(0, 100, 501)
    low, med, high = tri(z, -1, 0, 50), tri(z, 20, 50, 80), tri(z, 50, 100, 101)
    agg = np.maximum.reduce([np.minimum(cold, low), np.minimum(warm, med), np.minimum(hot, high)])
    return float((agg * z).sum() / (agg.sum() + 1e-9))      # centroid defuzzification
for t in (12, 24, 31, 38): print(f"{t} °C -> fan speed {fan_speed(t):.1f}%")
# TODO: add a second input (humidity), write >= 6 rules, plot the 3-D control surface,
#       and compare with a hand-written linear formula.'''),
  ("Open-ended: planning with surprises",
   "Implement a forward STRIPS planner for a delivery robot. Then make one action randomly fail and add execution monitoring with re-planning. Measure how often goals are still reached.",
   r'''from collections import deque
ACTIONS = {  # name: (preconditions, add, delete)
    "move(A,B)": ({"at(A)"}, {"at(B)"}, {"at(A)"}), "move(B,A)": ({"at(B)"}, {"at(A)"}, {"at(B)"}),
    "move(B,C)": ({"at(B)"}, {"at(C)"}, {"at(B)"}), "move(C,B)": ({"at(C)"}, {"at(B)"}, {"at(C)"}),
    "pick(A)": ({"at(A)", "parcel(A)", "free"}, {"holding"}, {"parcel(A)", "free"}),
    "drop(C)": ({"at(C)", "holding"}, {"parcel(C)", "free"}, {"holding"}),
}
def plan(state, goal):
    q, seen = deque([(frozenset(state), [])]), set()
    while q:
        s, p = q.popleft()
        if goal <= s: return p
        if s in seen: continue
        seen.add(s)
        for a, (pre, add, dele) in ACTIONS.items():
            if pre <= s: q.append(((s - dele) | add, p + [a]))
print(plan({"at(B)", "parcel(A)", "free"}, {"parcel(C)"}))
# TODO: make 'move' fail with probability 0.2, monitor the state after each step,
#       re-plan on failure, and report the success rate and extra steps over 1000 runs.'''),
 ]),
dict(unit="V", co="CO204.5", title="Learning Machines and Responsible AI",
 due="End of Week 15",
 think=[
  ("L5", "A decision tree for loan approval uses 'pin code' as its top split. Is the model biased even if it never sees religion or caste? Explain proxy discrimination and propose a test."),
  ("L6", "Design an expert system that could replace your college's help-desk for one week. Which questions must still go to a human, and how would the system know?"),
  ("L4", "Why did expert systems decline in the 1990s while machine learning rose? Would a 2030 'expert system' built on LLMs suffer the same problems?"),
  ("L5", "Should AI-generated assignments be banned, allowed or required? Take a position, then write the strongest argument against it."),
 ],
 code=[
  ("Open-ended: interpretable model vs black box",
   "Train a decision tree and one other model on a public dataset. Compare accuracy, extract the tree's rules, and decide whether the accuracy gain of the other model is worth the loss of interpretability.",
   r'''from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
X, y = load_breast_cancer(return_X_y=True)
for name, m in (("Decision tree (depth 3)", DecisionTreeClassifier(max_depth=3, random_state=0)),
                ("Random forest", RandomForestClassifier(n_estimators=200, random_state=0))):
    print(f"{name:24s} 5-fold accuracy = {cross_val_score(m, X, y, cv=5).mean():.3f}")
# TODO: print the tree's rules, compute recall for the malignant class, and write a
#       one-page recommendation for a hospital: which model, at what threshold, and why.'''),
  ("Open-ended: perceptron to multilayer network",
   "Implement a perceptron and a 2-layer network from scratch with NumPy. Show the perceptron failing on XOR and the network succeeding; visualise both decision boundaries.",
   r'''import numpy as np
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]); y_xor = np.array([0, 1, 1, 0])
w, b = np.zeros(2), 0.0
for epoch in range(20):
    for xi, yi in zip(X, y_xor):
        pred = int(w @ xi + b >= 0); w += (yi - pred) * xi; b += (yi - pred)
print("Perceptron predictions on XOR:", [int(w @ xi + b >= 0) for xi in X], "target:", y_xor.tolist())
# TODO 1: implement a 2-2-1 network with sigmoid units and back-propagation; train on XOR.
# TODO 2: plot decision boundaries for both models.
# TODO 3: what is the smallest network that solves 3-input parity? Find it experimentally.'''),
  ("Open-ended: fairness audit",
   "Using a dataset with a sensitive attribute (or a synthetic one you generate), train a classifier, measure accuracy and selection rate per group, and test one mitigation technique.",
   r'''import numpy as np
from sklearn.linear_model import LogisticRegression
rng = np.random.default_rng(0); n = 4000
group = rng.integers(0, 2, n)                         # synthetic sensitive attribute
skill = rng.normal(0, 1, n); proxy = skill + 0.8 * group + rng.normal(0, 0.5, n)
label = (skill + rng.normal(0, 0.5, n) > 0).astype(int)
Xf = np.c_[proxy]; model = LogisticRegression().fit(Xf, label); pred = model.predict(Xf)
for g in (0, 1):
    m = group == g
    print(f"group {g}: accuracy={np.mean(pred[m] == label[m]):.3f}  selection rate={pred[m].mean():.3f}")
# TODO: explain why the groups differ even though 'group' is not a feature,
#       apply one mitigation (re-weighting, group thresholds, removing the proxy),
#       and report the accuracy-fairness trade-off in a small model card.'''),
 ]),
]
