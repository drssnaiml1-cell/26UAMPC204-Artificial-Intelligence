# 📝 Assignments — 26UAMPC204 Artificial Intelligence

Five unit-wise assignments. **Part A:** think-out-of-the-box questions. **Part B:** open-ended coding problems with runnable starter code in [`notebooks/`](notebooks).

📄 Printable booklet: [AI_Assignments_Booklet.pdf](AI_Assignments_Booklet.pdf) · Rubric: originality 5 · reasoning 5 · implementation 6 · analysis 4 = **20 marks**

## Assignment 1: Agents in the Wild (Unit I · CO204.1 · due End of Week 3)

▶️ Starter notebook: [`Assignment_1_Starter.ipynb`](notebooks/Assignment_1_Starter.ipynb)

### Part A — Think out of the box

1. **[L5]** If a self-driving car is perfectly rational for its performance measure but still hits a pedestrian in a sudden event, is the car 'to blame'? Argue from the definition of rationality, then propose how the performance measure itself should change.
2. **[L6]** Invent a new agent type that does not fit any of the five classical architectures (reflex, model, goal, utility, learning). Describe its internal structure with a diagram and give a real problem where it beats all five.
3. **[L4]** Your phone's keyboard autocomplete is an agent. Write its PEAS, classify its environment along all seven properties, and identify which property makes it hardest to design.
4. **[L5]** Design a 'Reverse Turing Test' in which a machine must decide whether it is talking to a human or another AI. What questions would it ask, and why might this become important by 2030?

### Part B — Open-ended coding

1. **Open-ended: a smarter vacuum world** — Extend the vacuum world to an n×n grid where dirt re-appears randomly. Design the best agent you can and justify its performance measure. Compare at least three agent designs over 500 runs.
2. **Open-ended: formulate your own search problem** — Pick a real problem from your daily life (bus route to campus, cooking a meal, packing a bag). Formulate it with the five components and solve a small instance with BFS. Report the state-space size.
3. **Open-ended: performance-measure stress test** — Write two performance measures for the same agent that lead to visibly different behaviour. Show the difference with a plot and explain which you would ship.

## Assignment 2: Search Beyond the Textbook (Unit II · CO204.2 · due End of Week 6)

▶️ Starter notebook: [`Assignment_2_Starter.ipynb`](notebooks/Assignment_2_Starter.ipynb)

### Part A — Think out of the box

1. **[L5]** A* is optimal with an admissible heuristic. Give a real situation where you would deliberately use an inadmissible heuristic, and argue why the loss of optimality is acceptable.
2. **[L6]** Design a heuristic for finding the fastest route between two classrooms on your campus that accounts for stairs, lifts and crowds at bell time. Is it admissible? Prove or disprove it.
3. **[L4]** Why can a chess engine look 20 moves ahead but a cricket-captain AI cannot? Analyse the difference in branching factor, observability and stochasticity.
4. **[L6]** Invent a two-player game that is small enough to solve with Minimax but would be interesting for humans. Define its rules and predict who wins with perfect play.

### Part B — Open-ended coding

1. **Open-ended: heuristic design challenge** — Invent at least two new admissible heuristics for the 8-puzzle (beyond misplaced tiles and Manhattan distance) and compare nodes expanded on 50 random solvable puzzles.
2. **Open-ended: local search on a real optimisation problem** — Choose a real optimisation task (seating plan, delivery tour, playlist ordering) and solve it with hill climbing and simulated annealing. Report how often each reaches the best value you found.
3. **Open-ended: build and break a game AI** — Write a Minimax + alpha–beta agent for Connect-Three on a 4×4 board (or your own game). Then write an evaluation function for a depth-limited version and show a position where it blunders.

## Assignment 3: Logic Meets the Real World (Unit III · CO204.3 · due End of Week 9)

▶️ Starter notebook: [`Assignment_3_Starter.ipynb`](notebooks/Assignment_3_Starter.ipynb)

### Part A — Think out of the box

1. **[L4]** Translate the Sanjivani attendance rule (minimum attendance required to sit the exam, with medical exceptions) into first-order logic. Which parts resist precise logical encoding, and why?
2. **[L5]** LLMs often answer logic puzzles wrongly. Is a resolution theorem prover 'smarter' than an LLM? Argue both sides with a concrete example.
3. **[L6]** Design a knowledge graph of your own life (people, places, courses, skills). What new facts can you infer with three rules? What privacy risks would publishing it create?
4. **[L5]** A semantic network says 'penguins are birds' and 'birds fly'. Propose a principled way to handle exceptions without rewriting every rule, and evaluate its weaknesses.

### Part B — Open-ended coding

1. **Open-ended: your own expert knowledge base** — Encode at least 15 facts and 8 rules about a domain you know well (cricket rules, a recipe, a game). Answer five non-trivial queries with forward chaining and print the derivation trace.
2. **Open-ended: resolution vs model checking** — Implement CNF conversion for propositional sentences and compare the speed of resolution and truth-table model checking as the number of symbols grows from 4 to 16.
3. **Open-ended: mini ontology with SPARQL** — Build a small ontology (≥ 20 triples) for the AI&DS department and answer four questions with SPARQL queries.

## Assignment 4: Reasoning When Nothing Is Certain (Unit IV · CO204.4 · due End of Week 12)

▶️ Starter notebook: [`Assignment_4_Starter.ipynb`](notebooks/Assignment_4_Starter.ipynb)

### Part A — Think out of the box

1. **[L5]** A COVID-style rapid test is advertised as '95% accurate'. Explain to your family, without formulas, why a positive result might still be more likely wrong than right. When does it become reliable?
2. **[L6]** Design a STRIPS model for 'getting ready for college in the morning'. Where does the classical-planning assumption fail in real life, and how would you repair the plan on the fly?
3. **[L4]** Is 'tall' better modelled by probability or fuzzy logic? Construct a situation where using the wrong one leads to a bad decision.
4. **[L5]** Bayesian networks need a causal structure. What goes wrong if an expert draws an arrow in the wrong direction? Propose a test to detect it from data.

### Part B — Open-ended coding

1. **Open-ended: build a Bayesian network for a decision you care about** — Choose a diagnosis or decision (laptop won't boot, will it rain at college, should I take the bus). Build a network with ≥ 5 nodes, justify every CPT, and answer three queries with enumeration.
2. **Open-ended: fuzzy controller you can feel** — Design a fuzzy controller for something physical (fan speed, phone brightness, shower temperature). Plot membership functions and the control surface, then argue whether a simple formula would do better.
3. **Open-ended: planning with surprises** — Implement a forward STRIPS planner for a delivery robot. Then make one action randomly fail and add execution monitoring with re-planning. Measure how often goals are still reached.

## Assignment 5: Learning Machines and Responsible AI (Unit V · CO204.5 · due End of Week 15)

▶️ Starter notebook: [`Assignment_5_Starter.ipynb`](notebooks/Assignment_5_Starter.ipynb)

### Part A — Think out of the box

1. **[L5]** A decision tree for loan approval uses 'pin code' as its top split. Is the model biased even if it never sees religion or caste? Explain proxy discrimination and propose a test.
2. **[L6]** Design an expert system that could replace your college's help-desk for one week. Which questions must still go to a human, and how would the system know?
3. **[L4]** Why did expert systems decline in the 1990s while machine learning rose? Would a 2030 'expert system' built on LLMs suffer the same problems?
4. **[L5]** Should AI-generated assignments be banned, allowed or required? Take a position, then write the strongest argument against it.

### Part B — Open-ended coding

1. **Open-ended: interpretable model vs black box** — Train a decision tree and one other model on a public dataset. Compare accuracy, extract the tree's rules, and decide whether the accuracy gain of the other model is worth the loss of interpretability.
2. **Open-ended: perceptron to multilayer network** — Implement a perceptron and a 2-layer network from scratch with NumPy. Show the perceptron failing on XOR and the network succeeding; visualise both decision boundaries.
3. **Open-ended: fairness audit** — Using a dataset with a sensitive attribute (or a synthetic one you generate), train a classifier, measure accuracy and selection rate per group, and test one mitigation technique.

