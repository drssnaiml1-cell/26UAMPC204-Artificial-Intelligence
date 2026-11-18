# 🧩 Complex Unit Quizzes — 26UAMPC204 Artificial Intelligence

75 multi-step questions (15 per unit) that require computing, tracing or analysing, mostly at Bloom's L3–L5.

📄 Printable booklet with answer keys: [AI_Unit_Quizzes.pdf](AI_Unit_Quizzes.pdf) · ✅ Auto-graded self-check: [Quiz_SelfCheck.ipynb](Quiz_SelfCheck.ipynb)

Click a question to reveal the answer and worked explanation.

## Unit I: Introduction to AI and Intelligent Agents (CO204.1)

**QI.01** `L4` Classify poker (Texas Hold'em) along observability, agents, determinism, episodes, dynamics and discreteness.

- (A) Fully observable, multi-agent, deterministic, episodic, static, discrete
- (B) Partially observable, multi-agent, stochastic, sequential, static, discrete
- (C) Partially observable, single-agent, stochastic, sequential, dynamic, continuous
- (D) Fully observable, multi-agent, stochastic, episodic, dynamic, discrete

<details><summary>Show answer</summary>

**Answer: (B)** — Opponents' cards are hidden (partial), other players are agents (multi), the deal is random (stochastic), bets affect later decisions (sequential), nothing changes while you think (static), and actions and cards are discrete.

</details>

**QI.02** `L3` Jugs of 4 L and 3 L start empty. What is the minimum number of operations to leave exactly 2 L in the 4-L jug?

- (A) 4
- (B) 5
- (C) 6
- (D) 7

<details><summary>Show answer</summary>

**Answer: (C)** — BFS gives (0,0)→(0,3)→(3,0)→(3,3)→(4,2)→(0,2)→(2,0): six operations. No shorter sequence puts 2 L in the 4-L jug (four steps reach 2 L only in the 3-L jug).

</details>

**QI.03** `L3` How many distinct states does the two-square vacuum world have?

- (A) 4
- (B) 6
- (C) 8
- (D) 16

<details><summary>Show answer</summary>

**Answer: (C)** — The agent is in one of 2 squares and each square is dirty or clean: 2 × 2² = 8 states.

</details>

**QI.04** `L3` How many states of the 8-puzzle are reachable from a given start state?

- (A) 9! = 362,880
- (B) 9!/2 = 181,440
- (C) 8! = 40,320
- (D) 8!/2 = 20,160

<details><summary>Show answer</summary>

**Answer: (B)** — Moves preserve inversion parity, so the 9! arrangements split into two disconnected halves of 181,440 states each.

</details>

**QI.05** `L4` A car-routing agent must trade off travel time, fuel cost and passenger comfort under uncertain traffic. Which architecture is the minimum that handles this properly?

- (A) Simple reflex
- (B) Model-based reflex
- (C) Goal-based
- (D) Utility-based

<details><summary>Show answer</summary>

**Answer: (D)** — Conflicting objectives and uncertain outcomes need a utility function and expected-utility maximisation; a binary goal cannot rank partial successes.

</details>

**QI.06** `L2` What a rational agent should do at a given moment does NOT depend on which of these?

- (A) Its performance measure
- (B) Its prior knowledge of the environment
- (C) The percepts it will receive in the future
- (D) The actions it can perform

<details><summary>Show answer</summary>

**Answer: (C)** — Rationality depends on the performance measure, prior knowledge, available actions and the percept sequence to date, not on future percepts it cannot yet know.

</details>

**QI.07** `L4` A simple reflex vacuum agent with no location sensor keeps moving Left forever in a clean square. Which change fixes this without adding internal state?

- (A) A larger rule table
- (B) Randomising its movement choice
- (C) A faster processor
- (D) Removing the Suck action

<details><summary>Show answer</summary>

**Answer: (B)** — Randomised reflex agents escape such infinite loops; the alternative is internal state (a model-based agent).

</details>

**QI.08** `L2` In a learning agent, which component proposes exploratory actions that may be sub-optimal now but informative later?

- (A) Critic
- (B) Learning element
- (C) Performance element
- (D) Problem generator

<details><summary>Show answer</summary>

**Answer: (D)** — The problem generator suggests exploratory actions; the critic gives feedback against the performance standard.

</details>

**QI.09** `L4` Chess played with a clock is best described as which kind of environment?

- (A) Static
- (B) Semi-dynamic
- (C) Dynamic
- (D) Continuous

<details><summary>Show answer</summary>

**Answer: (B)** — The board does not change while the agent thinks, but its performance score (time left) does, which makes it semi-dynamic.

</details>

**QI.10** `L3` Three missionaries and three cannibals cross a river in a 2-person boat; cannibals may never outnumber missionaries on either bank. What is the minimum number of crossings?

- (A) 7
- (B) 9
- (C) 11
- (D) 13

<details><summary>Show answer</summary>

**Answer: (C)** — BFS over states (M, C, boat side) finds the classic 11-crossing solution; no shorter safe sequence exists.

</details>

**QI.11** `L3` In the complete-state formulation of 8-queens with one queen per column in any row, how many states exist?

- (A) 8! = 40,320
- (B) 8⁸ = 16,777,216
- (C) C(64,8) ≈ 4.4 × 10⁹
- (D) 2,057

<details><summary>Show answer</summary>

**Answer: (B)** — Each of 8 columns independently chooses one of 8 rows: 8⁸ states. 2,057 is the size of the incremental 'no attacks' formulation.

</details>

**QI.12** `L1` The Total Turing Test adds which two capabilities to those needed for the standard test?

- (A) Planning and learning
- (B) Computer vision and robotics
- (C) Speech and translation
- (D) Memory and reasoning

<details><summary>Show answer</summary>

**Answer: (B)** — It requires perceiving objects (vision) and manipulating them (robotics) in addition to NLP, knowledge representation, reasoning and learning.

</details>

**QI.13** `L2` Which of these is NOT one of the five components of a well-defined search problem?

- (A) Transition model
- (B) Goal test
- (C) Heuristic function
- (D) Action cost

<details><summary>Show answer</summary>

**Answer: (C)** — A problem is initial state, actions, transition model, goal test and path cost. A heuristic belongs to a solution method, not to the problem definition.

</details>

**QI.14** `L4` A thermostat rule 'IF temperature < 18 °C THEN heater ON' is an example of which agent?

- (A) Simple reflex
- (B) Model-based reflex
- (C) Goal-based
- (D) Learning

<details><summary>Show answer</summary>

**Answer: (A)** — It maps the current percept directly to an action through a condition–action rule, with no history or goals.

</details>

**QI.15** `L5` An agent's performance measure is 'number of support tickets closed per hour'. What is the most likely failure?

- (A) The agent becomes too slow
- (B) The agent closes tickets without solving them
- (C) The agent cannot perceive tickets
- (D) The agent needs a utility function

<details><summary>Show answer</summary>

**Answer: (B)** — Reward hacking: optimising a proxy of the desired outcome. Measure the environment state you want (problems resolved, not reopened).

</details>

## Unit II: Problem Solving by Search (CO204.2)

**QII.01** `L3` With branching factor b = 10 and the shallowest goal at depth d = 5, how many nodes does a complete search tree contain up to depth 5?

- (A) 100,000
- (B) 111,111
- (C) 123,456
- (D) 1,111,111

<details><summary>Show answer</summary>

**Answer: (B)** — 1 + 10 + 100 + 1,000 + 10,000 + 100,000 = 111,111.

</details>

**QII.02** `L3` For b = 10 and d = 5, how many nodes does iterative-deepening search generate in total?

- (A) 111,111
- (B) 123,456
- (C) 222,222
- (D) 611,110

<details><summary>Show answer</summary>

**Answer: (B)** — N(IDS) = 6·1 + 5·10 + 4·100 + 3·1,000 + 2·10,000 + 1·100,000 = 123,456, only about 11% more than BFS.

</details>

**QII.03** `L3` Start state 7 2 4 / 5 _ 6 / 8 3 1 with goal 1 2 3 / 4 5 6 / 7 8 _. What are h₁ (misplaced tiles) and h₂ (Manhattan distance)?

- (A) h₁ = 6, h₂ = 14
- (B) h₁ = 8, h₂ = 18
- (C) h₁ = 7, h₂ = 14
- (D) h₁ = 6, h₂ = 12

<details><summary>Show answer</summary>

**Answer: (A)** — Misplaced: 7, 4, 5, 8, 3, 1 → 6. Manhattan: 7→2, 2→0, 4→3, 5→1, 6→0, 8→1, 3→3, 1→4, total 14.

</details>

**QII.04** `L4` Graph: S→A (1), S→B (4), A→C (2), B→C (1), C→G (3), A→G (9); h(S)=6, h(A)=5, h(B)=4, h(C)=3, h(G)=0. In what order does A* expand nodes, and what is the path cost?

- (A) S, B, C, G; cost 8
- (B) S, A, C, G; cost 6
- (C) S, A, G; cost 10
- (D) S, A, B, C, G; cost 6

<details><summary>Show answer</summary>

**Answer: (B)** — f(A)=6, f(B)=8 → expand A; f(C)=6, f(G via A)=10 → expand C; f(G)=6 → goal. Path S–A–C–G with cost 6.

</details>

**QII.05** `L4` MAX root over three MIN nodes with leaves (3, 12, 8), (2, 4, 6), (14, 5, 2), evaluated left to right with alpha–beta. What is the root value and how many leaves are pruned?

- (A) Root 3; 2 leaves pruned
- (B) Root 2; 2 leaves pruned
- (C) Root 3; 0 leaves pruned
- (D) Root 5; 3 leaves pruned

<details><summary>Show answer</summary>

**Answer: (A)** — First MIN = 3 so α = 3. In the second MIN, the first leaf 2 ≤ α, so 4 and 6 are pruned. Third MIN = 2. Root = max(3, ≤2, 2) = 3.

</details>

**QII.06** `L3` Simulated annealing at temperature T = 1 proposes a move that worsens the objective by 2 (ΔE = −2). What is the acceptance probability?

- (A) 0.865
- (B) 0.500
- (C) 0.135
- (D) 0.018

<details><summary>Show answer</summary>

**Answer: (C)** — P = e^(ΔE/T) = e^(−2) ≈ 0.135.

</details>

**QII.07** `L3` Bidirectional BFS with b = 10 and d = 6. Roughly how many nodes are generated, compared with one-directional BFS?

- (A) About 2,000 vs 1,000,000
- (B) About 20,000 vs 1,000,000
- (C) About 1,000 vs 100,000
- (D) About 200 vs 10,000

<details><summary>Show answer</summary>

**Answer: (A)** — Each search goes to depth d/2 = 3: 2 × 10³ = 2,000 nodes versus about 10⁶ for one direction.

</details>

**QII.08** `L3` A* expanded N = 52 nodes to find a solution at depth 5. What is the effective branching factor b*?

- (A) 1.42
- (B) 1.92
- (C) 2.78
- (D) 3.10

<details><summary>Show answer</summary>

**Answer: (B)** — Solve N + 1 = 1 + b* + b*² + … + b*⁵ = 53; b* ≈ 1.92.

</details>

**QII.09** `L4` Uniform-cost search and BFS return different solutions only when …

- (A) the goal is deep
- (B) step costs are not all equal
- (C) the graph has cycles
- (D) the heuristic is inadmissible

<details><summary>Show answer</summary>

**Answer: (B)** — With equal step costs, shallowest equals cheapest. Different costs make UCS (cheapest g) and BFS (shallowest) diverge.

</details>

**QII.10** `L3` In Australia map colouring, after WA = red and NT = green, which variable does MRV choose next, and with which value?

- (A) Q = red
- (B) SA = blue
- (C) NSW = blue
- (D) V = green

<details><summary>Show answer</summary>

**Answer: (B)** — SA neighbours both WA and NT, leaving only blue. One legal value is the minimum, so MRV picks SA = blue.

</details>

**QII.11** `L2` What is the worst-case time complexity of AC-3 for c binary constraints and domain size d?

- (A) O(cd)
- (B) O(cd²)
- (C) O(cd³)
- (D) O(c²d)

<details><summary>Show answer</summary>

**Answer: (C)** — Each arc can be re-queued up to d times and each revision costs O(d²): O(cd³).

</details>

**QII.12** `L3` On the Romania map, greedy best-first search (straight-line distance) finds Arad→Sibiu→Fagaras→Bucharest. How much longer is it than the optimal A* route?

- (A) 0 km
- (B) 18 km
- (C) 32 km
- (D) 57 km

<details><summary>Show answer</summary>

**Answer: (C)** — Greedy: 140 + 99 + 211 = 450 km. A*: Arad–Sibiu–Rimnicu–Pitesti–Bucharest = 140 + 80 + 97 + 101 = 418 km. Difference 32 km.

</details>

**QII.13** `L3` In the genetic-algorithm encoding of 8-queens, fitness is the number of non-attacking pairs. What is the fitness of a solution?

- (A) 8
- (B) 16
- (C) 28
- (D) 56

<details><summary>Show answer</summary>

**Answer: (C)** — There are C(8,2) = 28 pairs of queens; in a solution none attack, so fitness = 28.

</details>

**QII.14** `L5` Which heuristic is admissible but NOT consistent? Edges S→A cost 1, A→G cost 1.

- (A) h(S)=2, h(A)=1, h(G)=0
- (B) h(S)=2, h(A)=0, h(G)=0
- (C) h(S)=3, h(A)=1, h(G)=0
- (D) h(S)=1, h(A)=1, h(G)=0

<details><summary>Show answer</summary>

**Answer: (B)** — True costs are 2 and 1, so h(S)=2, h(A)=0 never overestimate (admissible), but h(S)=2 > c(S,A) + h(A) = 1 violates consistency. Option C overestimates.

</details>

**QII.15** `L4` Why is random-restart hill climbing complete with probability approaching 1?

- (A) It never revisits states
- (B) Each restart has a non-zero chance p of success, so failure after k restarts is (1−p)ᵏ → 0
- (C) It accepts worse moves
- (D) It keeps a frontier of all neighbours

<details><summary>Show answer</summary>

**Answer: (B)** — Independent restarts each succeed with probability p; expected restarts are 1/p and the failure probability vanishes.

</details>

## Unit III: Knowledge Representation and Reasoning (CO204.3)

**QIII.01** `L3` Over symbols P, Q, R, how many models satisfy (P ∨ Q) ∧ ¬R?

- (A) 2
- (B) 3
- (C) 4
- (D) 6

<details><summary>Show answer</summary>

**Answer: (B)** — P ∨ Q is true in 3 of the 4 (P, Q) combinations and ¬R fixes R = false: 3 models.

</details>

**QIII.02** `L4` Which sentence is valid (a tautology)?

- (A) (P ⇒ Q) ⇒ (Q ⇒ P)
- (B) (P ∧ (P ⇒ Q)) ⇒ Q
- (C) P ∨ Q
- (D) (P ⇒ Q) ∧ P

<details><summary>Show answer</summary>

**Answer: (B)** — This is modus ponens as a sentence and is true in all four models; the others fail in at least one.

</details>

**QIII.03** `L3` What is the CNF of P ⇔ Q?

- (A) (P ∨ Q) ∧ (¬P ∨ ¬Q)
- (B) (¬P ∨ Q) ∧ (P ∨ ¬Q)
- (C) (¬P ∧ Q) ∨ (P ∧ ¬Q)
- (D) (P ∧ Q) ∨ (¬P ∧ ¬Q)

<details><summary>Show answer</summary>

**Answer: (B)** — P ⇔ Q ≡ (P ⇒ Q) ∧ (Q ⇒ P) ≡ (¬P ∨ Q) ∧ (¬Q ∨ P). Option D is equivalent but in DNF.

</details>

**QIII.04** `L3` What is the most general unifier of P(x, f(y), y) and P(g(z), f(a), z)?

- (A) {x/g(z), y/a}
- (B) {x/g(a), y/a, z/a}
- (C) {x/g(y), z/y}
- (D) No unifier exists

<details><summary>Show answer</summary>

**Answer: (B)** — x/g(z); f(y)=f(a) gives y/a; y=z gives z/a; substituting back gives x/g(a).

</details>

**QIII.05** `L4` Why does unifying Knows(John, x) with Knows(x, Elizabeth) fail, and what fixes it?

- (A) Occurs check; rename predicates
- (B) x cannot be both John and Elizabeth; standardise variables apart
- (C) Different arity; add arguments
- (D) Constants never unify; use Skolem functions

<details><summary>Show answer</summary>

**Answer: (B)** — The same variable x would need two values. Renaming one sentence's variable (x₁) gives {x₁/Elizabeth, x/John}.

</details>

**QIII.06** `L3` Which FOL sentence correctly says 'Every student who takes AI likes some professor'?

- (A) ∀x ∃y Student(x) ∧ Takes(x, AI) ∧ Professor(y) ∧ Likes(x, y)
- (B) ∀x [Student(x) ∧ Takes(x, AI) ⇒ ∃y (Professor(y) ∧ Likes(x, y))]
- (C) ∃y ∀x [Student(x) ⇒ Likes(x, y)]
- (D) ∀x ∃y [Student(x) ∧ Takes(x, AI) ⇒ Professor(y) ⇒ Likes(x, y)]

<details><summary>Show answer</summary>

**Answer: (B)** — ∀ pairs with ⇒ and ∃ pairs with ∧. Option A wrongly makes everyone an AI student; C makes one professor liked by all.

</details>

**QIII.07** `L3` Which is equivalent to ¬∀x (Student(x) ⇒ Smart(x))?

- (A) ∀x (Student(x) ∧ ¬Smart(x))
- (B) ∃x (Student(x) ∧ ¬Smart(x))
- (C) ∃x (¬Student(x) ⇒ Smart(x))
- (D) ¬∃x Student(x)

<details><summary>Show answer</summary>

**Answer: (B)** — ¬∀x φ ≡ ∃x ¬φ, and ¬(A ⇒ B) ≡ A ∧ ¬B.

</details>

**QIII.08** `L3` What does Skolemisation turn ∀x ∃y Loves(x, y) into?

- (A) Loves(x, C)
- (B) Loves(x, F(x))
- (C) Loves(F(y), y)
- (D) ∃y Loves(C, y)

<details><summary>Show answer</summary>

**Answer: (B)** — The existential y depends on the universal x, so it becomes a Skolem function F(x). A constant would wrongly mean everyone loves the same person.

</details>

**QIII.09** `L2` Forward chaining with Generalised Modus Ponens is sound and complete for which class of KBs?

- (A) Any FOL KB
- (B) First-order definite clauses
- (C) Propositional CNF
- (D) KBs with negation as failure

<details><summary>Show answer</summary>

**Answer: (B)** — For definite clauses (exactly one positive literal), forward chaining derives every entailed atomic fact.

</details>

**QIII.10** `L3` Resolve (A ∨ B ∨ ¬C) with (C ∨ D). What is the resolvent?

- (A) A ∨ B
- (B) A ∨ B ∨ D
- (C) A ∨ B ∨ C ∨ D
- (D) □

<details><summary>Show answer</summary>

**Answer: (B)** — Cancel the complementary pair ¬C / C and keep the remaining literals: A ∨ B ∨ D.

</details>

**QIII.11** `L4` KB = {P ⇒ Q, ¬Q}. Which statement does the KB entail?

- (A) P
- (B) ¬P
- (C) Q
- (D) Nothing beyond the KB

<details><summary>Show answer</summary>

**Answer: (B)** — Modus tollens: the only model with P ⇒ Q true and Q false has P false. By resolution, ¬P ∨ Q with ¬Q gives ¬P.

</details>

**QIII.12** `L2` Which sentence is satisfiable but not valid?

- (A) P ∨ ¬P
- (B) P ∧ ¬P
- (C) P ∨ Q
- (D) (P ⇒ P)

<details><summary>Show answer</summary>

**Answer: (C)** — P ∨ Q is true when either holds but false when both are false.

</details>

**QIII.13** `L4` A semantic network says Bird —can→ Fly, Penguin —is-a→ Bird, Penguin —can→ ¬Fly. How does a typical inheritance reasoner answer 'Can Tweety the penguin fly?'

- (A) Yes, from Bird
- (B) No, the most specific class overrides the default
- (C) Contradiction, no answer
- (D) Unknown, nets cannot represent this

<details><summary>Show answer</summary>

**Answer: (B)** — Default inheritance lets the more specific class (Penguin) override the inherited default (Bird). This is non-monotonic reasoning, which pure FOL cannot do.

</details>

**QIII.14** `L2` Which clause is a Horn clause?

- (A) A ∨ B ∨ ¬C
- (B) ¬A ∨ ¬B ∨ C
- (C) A ∨ B
- (D) A ∨ ¬B ∨ C

<details><summary>Show answer</summary>

**Answer: (B)** — A Horn clause has at most one positive literal; ¬A ∨ ¬B ∨ C is the rule A ∧ B ⇒ C.

</details>

**QIII.15** `L5` Why can Prolog-style backward chaining fail to terminate on ancestor(X, Y) :- ancestor(X, Z), parent(Z, Y)?

- (A) Unification is undecidable
- (B) Depth-first, left-to-right search loops on the left-recursive goal
- (C) Resolution is incomplete
- (D) The KB is not Horn

<details><summary>Show answer</summary>

**Answer: (B)** — The first subgoal calls ancestor again with no progress, an infinite descent. Reordering the body (parent first) or tabling fixes it.

</details>

## Unit IV: Planning and Reasoning under Uncertainty (CO204.4)

**QIV.01** `L3` Prevalence is 1%, sensitivity 90% and false-positive rate 5%. What is P(disease | positive)?

- (A) 0.90
- (B) 0.50
- (C) 0.154
- (D) 0.045

<details><summary>Show answer</summary>

**Answer: (C)** — 0.9 × 0.01 / (0.9 × 0.01 + 0.05 × 0.99) = 0.009 / 0.0585 ≈ 0.154.

</details>

**QIV.02** `L3` The same patient takes a second, independent test that is also positive. What is the updated posterior?

- (A) 0.154
- (B) 0.31
- (C) 0.77
- (D) 0.99

<details><summary>Show answer</summary>

**Answer: (C)** — Use 0.154 as the prior: 0.9 × 0.154 / (0.9 × 0.154 + 0.05 × 0.846) ≈ 0.1386 / 0.1809 ≈ 0.77.

</details>

**QIV.03** `L3` In the burglary network (P(B)=.001, P(E)=.002, P(a | ¬b, ¬e)=.001, P(j | a)=.9, P(m | a)=.7), what is P(j, m, a, ¬b, ¬e)?

- (A) 0.000628
- (B) 0.00063 × 10⁻³
- (C) 0.0063
- (D) 0.063

<details><summary>Show answer</summary>

**Answer: (A)** — 0.9 × 0.7 × 0.001 × 0.999 × 0.998 ≈ 0.000628.

</details>

**QIV.04** `L3` How many independent probabilities does the burglary network (B, E → A; A → J, M; all Boolean) need, compared with the full joint?

- (A) 10 vs 31
- (B) 10 vs 32
- (C) 5 vs 31
- (D) 16 vs 32

<details><summary>Show answer</summary>

**Answer: (A)** — B 1 + E 1 + A 4 + J 2 + M 2 = 10; the full joint over 5 Boolean variables needs 2⁵ − 1 = 31.

</details>

**QIV.05** `L4` Which independence does the burglary network structure imply?

- (A) Burglary and Earthquake are dependent
- (B) JohnCalls and MaryCalls are independent given Alarm
- (C) JohnCalls is independent of Burglary unconditionally
- (D) Alarm is independent of Earthquake

<details><summary>Show answer</summary>

**Answer: (B)** — J and M share only the parent A, so they are conditionally independent given A. B and E are independent a priori but dependent given A (explaining away).

</details>

**QIV.06** `L3` Apply Stack(A, B) [PRE Holding(A) ∧ Clear(B); ADD On(A,B), Clear(A), HandEmpty; DEL Holding(A), Clear(B)] to the state {Holding(A), Clear(B), OnTable(B)}. What is the result?

- (A) {On(A,B), Clear(A), HandEmpty, OnTable(B)}
- (B) {On(A,B), Clear(B), HandEmpty}
- (C) {Holding(A), On(A,B), OnTable(B)}
- (D) {On(A,B), Clear(A), Clear(B), OnTable(B)}

<details><summary>Show answer</summary>

**Answer: (A)** — Result = (s − DEL) ∪ ADD: remove Holding(A) and Clear(B), add On(A,B), Clear(A), HandEmpty; OnTable(B) persists.

</details>

**QIV.07** `L3` Regress the goal {On(A,B), OnTable(B)} through Stack(A, B). What is the new subgoal?

- (A) {OnTable(B)}
- (B) {Holding(A), Clear(B), OnTable(B)}
- (C) {On(A,B), Holding(A)}
- (D) {Clear(A), HandEmpty}

<details><summary>Show answer</summary>

**Answer: (B)** — g′ = (g − ADD(a)) ∪ PRE(a) = {OnTable(B)} ∪ {Holding(A), Clear(B)}.

</details>

**QIV.08** `L4` In partial-order planning, action C deletes p, which a causal link A —p→ B protects. Which fixes resolve the threat?

- (A) Promotion (C before A) or demotion (C after B)
- (B) Demotion (C before A) or promotion (C after B)
- (C) Delete C from the plan
- (D) Add p to the preconditions of C

<details><summary>Show answer</summary>

**Answer: (B)** — Demotion orders the threat before the link's producer (C ≺ A); promotion orders it after the consumer (B ≺ C).

</details>

**QIV.09** `L3` How many valid total orders (linearisations) does the partial-order plan Left-Sock ≺ Left-Shoe, Right-Sock ≺ Right-Shoe have?

- (A) 2
- (B) 4
- (C) 6
- (D) 24

<details><summary>Show answer</summary>

**Answer: (C)** — Interleave two ordered pairs: C(4,2) = 6 orders.

</details>

**QIV.10** `L3` μ_A(x) = 0.7 and μ_B(x) = 0.4. Under Zadeh operators, what are μ(A AND B), μ(A OR B), μ(NOT A) and μ(very A)?

- (A) 0.4, 0.7, 0.3, 0.49
- (B) 0.28, 0.82, 0.3, 0.84
- (C) 0.4, 0.7, 0.6, 0.49
- (D) 0.7, 0.4, 0.3, 0.70

<details><summary>Show answer</summary>

**Answer: (A)** — AND = min = 0.4, OR = max = 0.7, NOT = 1 − 0.7 = 0.3, very = μ² = 0.49.

</details>

**QIV.11** `L3` Warm is the triangular fuzzy set (a, b, c) = (10, 25, 40) °C. What is μ_Warm(18 °C)?

- (A) 0.32
- (B) 0.47
- (C) 0.53
- (D) 0.80

<details><summary>Show answer</summary>

**Answer: (C)** — On the rising edge: (18 − 10) / (25 − 10) = 8 / 15 ≈ 0.53.

</details>

**QIV.12** `L3` An aggregated fuzzy output has singleton spikes of height 0.5 at fan speed 20% and 1.0 at 80%. What is the centroid output?

- (A) 50%
- (B) 60%
- (C) 70%
- (D) 80%

<details><summary>Show answer</summary>

**Answer: (B)** — (0.5 × 20 + 1.0 × 80) / (0.5 + 1.0) = 90 / 1.5 = 60%.

</details>

**QIV.13** `L3` In a spam filter, P(spam) = 0.3, P(word | spam) = 0.6 and P(word | ham) = 0.05. What is P(spam | word)?

- (A) 0.60
- (B) 0.72
- (C) 0.84
- (D) 0.95

<details><summary>Show answer</summary>

**Answer: (C)** — 0.6 × 0.3 / (0.6 × 0.3 + 0.05 × 0.7) = 0.18 / 0.215 ≈ 0.84.

</details>

**QIV.14** `L4` What does the Sussman anomaly demonstrate?

- (A) STRIPS cannot represent blocks
- (B) Non-interleaved (linear) planning of subgoals can be incomplete
- (C) Backward search is slower than forward search
- (D) Partial-order planning is unsound

<details><summary>Show answer</summary>

**Answer: (B)** — Achieving On(A,B) then On(B,C) undoes the first goal; solving the problem requires interleaving the subgoals' actions.

</details>

**QIV.15** `L5` From the full joint table (cavity ∧ toothache = 0.12, toothache = 0.2), what is P(cavity | toothache), and what does it show?

- (A) 0.6; toothache is evidence for, but not proof of, a cavity
- (B) 0.12; joint equals conditional
- (C) 0.2; toothache is independent of cavity
- (D) 1.0; toothache implies cavity

<details><summary>Show answer</summary>

**Answer: (A)** — 0.12 / 0.2 = 0.6. Logic (Toothache ⇒ Cavity) fails; probability quantifies the degree of belief.

</details>

## Unit V: Learning, Expert Systems and Applications of AI (CO204.5)

**QV.01** `L3` A dataset has 9 positive and 5 negative examples. What is its entropy?

- (A) 0.500
- (B) 0.643
- (C) 0.940
- (D) 1.000

<details><summary>Show answer</summary>

**Answer: (C)** — −(9/14) log₂(9/14) − (5/14) log₂(5/14) ≈ 0.410 + 0.530 = 0.940.

</details>

**QV.02** `L3` Outlook splits Play Tennis into Sunny (2+, 3−), Overcast (4+, 0−) and Rain (3+, 2−). What is Gain(S, Outlook)?

- (A) 0.048
- (B) 0.151
- (C) 0.247
- (D) 0.940

<details><summary>Show answer</summary>

**Answer: (C)** — 0.940 − (5/14)(0.971) − (4/14)(0) − (5/14)(0.971) ≈ 0.247.

</details>

**QV.03** `L3` What is the Gini impurity of a node with 9 positive and 5 negative examples?

- (A) 0.230
- (B) 0.459
- (C) 0.541
- (D) 0.940

<details><summary>Show answer</summary>

**Answer: (B)** — 1 − (9/14)² − (5/14)² = 1 − 0.413 − 0.128 ≈ 0.459.

</details>

**QV.04** `L3` A perceptron has w = (w₀, w₁, w₂) = (−1, 0, 0) with bias input x₀ = 1. On x = (1, 1) with target y = 1 and η = 1, what are the weights after one update?

- (A) (−1, 0, 0)
- (B) (0, 1, 1)
- (C) (−2, −1, −1)
- (D) (1, 1, 1)

<details><summary>Show answer</summary>

**Answer: (B)** — w·x = −1 < 0, so ŷ = 0 and the error is +1. Update w ← w + (1)(1, 1, 1) = (0, 1, 1).

</details>

**QV.05** `L4` What is the smallest feed-forward network with threshold units that represents XOR?

- (A) One perceptron
- (B) One hidden layer with 2 units
- (C) One hidden layer with 4 units
- (D) Two hidden layers with 1 unit each

<details><summary>Show answer</summary>

**Answer: (B)** — XOR is not linearly separable. Two hidden units (e.g. OR and NAND) combined by an AND output unit compute XOR.

</details>

**QV.06** `L3` A classifier has TP = 40, FP = 10 and FN = 20. What are its precision, recall and F1?

- (A) 0.80, 0.67, 0.73
- (B) 0.67, 0.80, 0.73
- (C) 0.80, 0.80, 0.80
- (D) 0.57, 0.67, 0.62

<details><summary>Show answer</summary>

**Answer: (A)** — Precision 40/50 = 0.80; recall 40/60 ≈ 0.667; F1 = 2PR/(P+R) ≈ 0.727.

</details>

**QV.07** `L4` A decision tree scores 99% training accuracy and 70% test accuracy; a depth-3 tree scores 85% and 84%. What is the right reading?

- (A) The deep tree is better
- (B) The deep tree overfits; prefer the shallow tree or prune
- (C) Both underfit
- (D) The test set is wrong

<details><summary>Show answer</summary>

**Answer: (B)** — A large train–test gap signals high variance; the shallow tree generalises better.

</details>

**QV.08** `L3` Two independent rules support the same conclusion with CF₁ = 0.6 and CF₂ = 0.5. What is the combined CF (MYCIN)?

- (A) 0.30
- (B) 0.55
- (C) 0.80
- (D) 1.10

<details><summary>Show answer</summary>

**Answer: (C)** — CF = CF₁ + CF₂(1 − CF₁) = 0.6 + 0.5 × 0.4 = 0.80.

</details>

**QV.09** `L3` Rule: IF fever (CF 0.9) AND cough (CF 0.7) THEN flu with rule CF 0.8. What is CF(flu)?

- (A) 0.50
- (B) 0.56
- (C) 0.63
- (D) 0.72

<details><summary>Show answer</summary>

**Answer: (B)** — AND takes the minimum premise CF (0.7), multiplied by the rule CF: 0.7 × 0.8 = 0.56.

</details>

**QV.10** `L4` Which pairing of classic expert system and chaining strategy is correct?

- (A) MYCIN: forward; XCON: backward
- (B) MYCIN: backward; XCON: forward
- (C) Both backward
- (D) Both forward

<details><summary>Show answer</summary>

**Answer: (B)** — MYCIN diagnoses goal-first (backward); XCON configures systems data-first (forward).

</details>

**QV.11** `L5` In a dataset with 2% positives, a model predicts 'negative' for everyone. What is its accuracy, and what should you report instead?

- (A) 2%; report accuracy
- (B) 98%; report precision, recall, F1 and PR-AUC
- (C) 50%; report ROC-AUC only
- (D) 100%; nothing else needed

<details><summary>Show answer</summary>

**Answer: (B)** — Accuracy is 98% but recall is 0: the accuracy paradox. Imbalanced problems need class-sensitive metrics.

</details>

**QV.12** `L3` What are sigmoid(0), tanh(0) and ReLU(−2)?

- (A) 0.5, 0, 0
- (B) 0, 0, −2
- (C) 1, 1, 0
- (D) 0.5, 0.5, 2

<details><summary>Show answer</summary>

**Answer: (A)** — σ(0) = 1/(1 + e⁰) = 0.5; tanh(0) = 0; ReLU(−2) = max(0, −2) = 0.

</details>

**QV.13** `L5` A loan model never sees religion or caste but splits first on pin code, and approval rates differ sharply by community. What is this called?

- (A) Overfitting
- (B) Proxy discrimination
- (C) Label noise
- (D) Concept drift

<details><summary>Show answer</summary>

**Answer: (B)** — Pin code correlates with protected attributes, so the model discriminates through a proxy. Audit group metrics and remove or constrain proxies.

</details>

**QV.14** `L2` Which expert-system component answers the user's 'WHY are you asking this?' and 'HOW did you conclude that?'

- (A) Knowledge acquisition
- (B) Inference engine
- (C) Explanation facility
- (D) Working memory

<details><summary>Show answer</summary>

**Answer: (C)** — The explanation facility traces the rules fired (HOW) and the goal being pursued (WHY).

</details>

**QV.15** `L3` How many leaves does the ID3 tree learned from the 14-example Play Tennis data have?

- (A) 3
- (B) 4
- (C) 5
- (D) 7

<details><summary>Show answer</summary>

**Answer: (C)** — Outlook → Sunny: Humidity (High → No, Normal → Yes); Overcast → Yes; Rain: Wind (Strong → No, Weak → Yes). Five leaves.

</details>

