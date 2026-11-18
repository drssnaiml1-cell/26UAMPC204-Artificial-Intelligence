# 🔬 Research Ideas — 26UAMPC204 Artificial Intelligence

20 unit-aligned research directions. **Levels:** 🟢 UG Project · 🔵 M.Tech / Minor Thesis · 🔴 Ph.D. Direction.

📄 Full handbook: [AI_Research_Ideas.pdf](AI_Research_Ideas.pdf)

## Unit I: Introduction to AI and Intelligent Agents

<details><summary>🔵 <b>RI.1 Measuring rationality of LLM-based agents with PEAS-grounded benchmarks</b> <i>(M.Tech / Minor Thesis)</i></summary>

- **Gap:** LLM agents are evaluated on task success only; there is no standard way to check whether their behaviour is rational for a declared performance measure.
- **Method:** Define PEAS specifications for 10 tool-using tasks, log agent percept–action traces, score expected-utility regret against an oracle planner, and compare prompting strategies.
- **Data & tools:** Open-source LLMs, LangGraph / simple tool APIs, Python logging
- **Expected outcome:** A benchmark and a 'rationality score' for agentic AI systems.
- **Target venues:** IEEE Access; Expert Systems with Applications; AAMAS workshops

</details>

<details><summary>🟢 <b>RI.2 Environment-property classifier for automatic agent-architecture selection</b> <i>(UG Project)</i></summary>

- **Gap:** Students and engineers pick agent architectures by intuition; there is no tool that maps a problem description to environment properties.
- **Method:** Build a labelled set of 300 task descriptions, fine-tune a small text classifier for the seven properties, and recommend an architecture with rules.
- **Data & tools:** Hugging Face transformers, scikit-learn, Streamlit
- **Expected outcome:** A web tool that outputs PEAS, properties and a recommended agent type.
- **Target venues:** Student conferences; IEEE ICCCNT; Springer LNNS

</details>

<details><summary>🔵 <b>RI.3 Reward hacking in campus-scale smart agents</b> <i>(M.Tech / Minor Thesis)</i></summary>

- **Gap:** Poorly chosen performance measures make agents optimise the wrong thing (e.g. energy agents that cut comfort).
- **Method:** Simulate a smart-building agent with several reward definitions; quantify side effects; propose constrained or multi-objective reward design.
- **Data & tools:** Python simulation, Gymnasium, RL baselines
- **Expected outcome:** Design guidelines for safe performance measures in building automation.
- **Target venues:** Energy and Buildings; IEEE SmartGridComm

</details>

<details><summary>🔴 <b>RI.4 Human-vs-AI Turing-style evaluation for Indian-language chatbots</b> <i>(Ph.D. Direction)</i></summary>

- **Gap:** Turing-style evaluations are English-centric; Indian languages and code-mixed speech are under-studied.
- **Method:** Run controlled, blinded conversations in Marathi/Hindi/English mixes; analyse detection cues and failure modes; propose an evaluation protocol.
- **Data & tools:** Open LLMs, survey platform, statistical analysis (R / Python)
- **Expected outcome:** A multilingual evaluation protocol and dataset of judged conversations.
- **Target venues:** ACL / EMNLP workshops; Language Resources and Evaluation

</details>

## Unit II: Problem Solving by Search

<details><summary>🔴 <b>RII.1 Learned heuristics for A*: neural guidance with admissibility guarantees</b> <i>(Ph.D. Direction)</i></summary>

- **Gap:** Neural heuristics speed up search but can over-estimate, losing optimality.
- **Method:** Train a GNN to predict cost-to-go, then clip with an admissible bound or use bounded-suboptimal search (weighted A*, focal search) with proven error bounds.
- **Data & tools:** PyTorch Geometric, 8/15-puzzle and grid-map benchmarks
- **Expected outcome:** Faster search with guaranteed bounded sub-optimality.
- **Target venues:** AAAI; IJCAI; SoCS (Symposium on Combinatorial Search)

</details>

<details><summary>🔵 <b>RII.2 Exam and lab timetabling for Indian universities as a hybrid CSP + metaheuristic</b> <i>(M.Tech / Minor Thesis)</i></summary>

- **Gap:** Manual timetabling causes clashes and poor room use; generic solvers ignore local rules such as practical batches.
- **Method:** Model batches, rooms and faculty as a CSP; solve hard constraints with CP-SAT, optimise soft constraints with simulated annealing; compare with manual timetables.
- **Data & tools:** Google OR-Tools CP-SAT, Python, real (anonymised) department data
- **Expected outcome:** A deployable timetable generator with measurable clash and utilisation gains.
- **Target venues:** Journal of Scheduling; Computers & Operations Research

</details>

<details><summary>🟢 <b>RII.3 Energy-aware route planning for electric two-wheelers</b> <i>(UG Project)</i></summary>

- **Gap:** Shortest routes are not lowest-energy routes for EVs because of elevation and traffic.
- **Method:** Build a city road graph with elevation; define an energy cost; compare Dijkstra, A* and multi-objective search for time vs energy.
- **Data & tools:** OSMnx, SRTM elevation data, NetworkX
- **Expected outcome:** A route planner that reports energy saved vs time lost.
- **Target venues:** IEEE ITSC; Transportation Research Part D

</details>

<details><summary>🟢 <b>RII.4 Explainable game-playing agents for teaching</b> <i>(UG Project)</i></summary>

- **Gap:** Minimax/MCTS agents choose moves without explaining them, so students cannot learn from them.
- **Method:** Add move explanations from the search tree (principal variation, threats, pruned alternatives) and evaluate learning gains in a classroom study.
- **Data & tools:** Python, Pygame, small user study
- **Expected outcome:** An explainable Tic-Tac-Toe / Connect-Four tutor.
- **Target venues:** IEEE Transactions on Learning Technologies; IEEE Conference on Games

</details>

## Unit III: Knowledge Representation and Reasoning

<details><summary>🔵 <b>RIII.1 Knowledge-graph-grounded LLM assistant for university regulations</b> <i>(M.Tech / Minor Thesis)</i></summary>

- **Gap:** LLM chatbots hallucinate policy details such as fees, attendance and exam rules.
- **Method:** Build a KG from regulation documents, combine retrieval with symbolic rule checking, and measure hallucination against a curated question set.
- **Data & tools:** Neo4j / rdflib, open LLM, RAG pipeline
- **Expected outcome:** Lower hallucination rate with cited, rule-checked answers.
- **Target venues:** Knowledge-Based Systems; ISWC workshops

</details>

<details><summary>🔴 <b>RIII.2 Neuro-symbolic reasoning: learning rules from data and verifying them in logic</b> <i>(Ph.D. Direction)</i></summary>

- **Gap:** Neural models are accurate but not verifiable; logic is verifiable but hand-built.
- **Method:** Learn candidate rules with inductive logic programming or differentiable logic, verify consistency with a theorem prover, and test on relational benchmarks.
- **Data & tools:** PyTorch, Popper ILP / Scallop, SWI-Prolog
- **Expected outcome:** A pipeline that yields accurate and auditable rule sets.
- **Target venues:** NeurIPS / ICLR workshops; Artificial Intelligence (Elsevier)

</details>

<details><summary>🟢 <b>RIII.3 Agricultural ontology for Maharashtra crops and diseases</b> <i>(UG Project)</i></summary>

- **Gap:** Advisory apps lack a shared vocabulary linking crops, symptoms, diseases and treatments in local languages.
- **Method:** Design an OWL ontology with Marathi labels, populate from extension literature, and answer farmer queries with SPARQL.
- **Data & tools:** Protégé, OWL, rdflib, SPARQL
- **Expected outcome:** A reusable, multilingual agricultural ontology.
- **Target venues:** Computers and Electronics in Agriculture; Semantic Web journal

</details>

<details><summary>🔵 <b>RIII.4 Automated legal-rule compliance checking with first-order logic</b> <i>(M.Tech / Minor Thesis)</i></summary>

- **Gap:** Compliance checks (e.g. data-protection rules) are manual and error-prone.
- **Method:** Encode selected DPDP Act 2023 obligations in FOL / rules, map system logs to facts, and use forward chaining to flag violations with explanations.
- **Data & tools:** Python rule engine or Prolog, synthetic audit logs
- **Expected outcome:** An explainable compliance checker prototype.
- **Target venues:** Artificial Intelligence and Law; JURIX

</details>

## Unit IV: Planning and Reasoning under Uncertainty

<details><summary>🔵 <b>RIV.1 Bayesian network for early sepsis or dengue risk in primary-care settings</b> <i>(M.Tech / Minor Thesis)</i></summary>

- **Gap:** Rural clinics lack lab tests; risk tools built on complete data do not transfer.
- **Method:** Elicit structure with clinicians, learn CPTs from public data, handle missing evidence natively, and compare with logistic regression on calibration.
- **Data & tools:** pgmpy, public clinical datasets (with permission), calibration metrics
- **Expected outcome:** A calibrated, explainable risk tool that works with missing tests.
- **Target venues:** Journal of Biomedical Informatics; AIME conference

</details>

<details><summary>🔴 <b>RIV.2 LLM-generated PDDL: can language models write correct planning domains?</b> <i>(Ph.D. Direction)</i></summary>

- **Gap:** LLMs plan poorly on their own but may help by writing formal models that classical planners solve.
- **Method:** Prompt LLMs to produce PDDL from text, validate with VAL, repair with feedback loops, and measure plan validity across IPC domains.
- **Data & tools:** PDDL, Fast Downward, VAL, open LLMs
- **Expected outcome:** Evidence on when LLM-written models are reliable, with a repair method.
- **Target venues:** ICAPS; AAAI; Journal of Artificial Intelligence Research

</details>

<details><summary>🟢 <b>RIV.3 Fuzzy irrigation controller with IoT sensors</b> <i>(UG Project)</i></summary>

- **Gap:** Fixed irrigation schedules waste water; farmers need simple, robust controllers.
- **Method:** Design a Mamdani controller using soil moisture, temperature and crop stage; deploy on a microcontroller; compare water use with timer control.
- **Data & tools:** scikit-fuzzy, ESP32 / Arduino, moisture sensors
- **Expected outcome:** Measured water savings in a pilot plot.
- **Target venues:** Smart Agricultural Technology; IEEE Sensors Journal

</details>

<details><summary>🔵 <b>RIV.4 Uncertainty-aware fraud detection for UPI transactions</b> <i>(M.Tech / Minor Thesis)</i></summary>

- **Gap:** Fraud scores are over-confident and drift as fraud patterns change.
- **Method:** Combine a probabilistic model with conformal prediction to give calibrated risk sets; simulate drift and study alert quality.
- **Data & tools:** Synthetic transaction generator, scikit-learn, MAPIE (conformal)
- **Expected outcome:** Calibrated, drift-robust fraud alerts with guaranteed coverage.
- **Target venues:** Expert Systems with Applications; IEEE Transactions on Dependable and Secure Computing

</details>

## Unit V: Learning, Expert Systems and Applications of AI

<details><summary>🔵 <b>RV.1 Explainable crop-disease diagnosis: CNN plus rule-based expert system</b> <i>(M.Tech / Minor Thesis)</i></summary>

- **Gap:** Image classifiers detect diseases but give no actionable, trustworthy advice.
- **Method:** Use a CNN for symptom detection and an expert system for diagnosis and treatment with certainty factors; evaluate with agronomists.
- **Data & tools:** PlantVillage dataset, PyTorch, rule engine
- **Expected outcome:** A hybrid system with higher farmer trust and clear explanations.
- **Target venues:** Computers and Electronics in Agriculture; Expert Systems with Applications

</details>

<details><summary>🟢 <b>RV.2 Fairness audit of student-performance prediction models</b> <i>(UG Project)</i></summary>

- **Gap:** Early-warning models may flag students unfairly by gender, region or school board.
- **Method:** Train decision trees and other models on anonymised data, measure group fairness, apply mitigation and report trade-offs in a model card.
- **Data & tools:** scikit-learn, Fairlearn, SHAP
- **Expected outcome:** A fairness audit report and mitigation guidelines for universities.
- **Target venues:** IEEE Transactions on Education; Educational Data Mining conference

</details>

<details><summary>🔵 <b>RV.3 Low-resource intent detection for Marathi admission chatbots</b> <i>(M.Tech / Minor Thesis)</i></summary>

- **Gap:** Few labelled examples exist for Marathi or code-mixed queries.
- **Method:** Compare keyword rules, TF-IDF models and multilingual sentence embeddings with few-shot learning; add confidence-based fallback to humans.
- **Data & tools:** IndicBERT / LaBSE, scikit-learn, Rasa
- **Expected outcome:** A data-efficient chatbot pipeline for Indian languages.
- **Target venues:** ACM TALLIP; ICON (Indian NLP conference)

</details>

<details><summary>🔴 <b>RV.4 Interpretable-by-design models for clinical decision support</b> <i>(Ph.D. Direction)</i></summary>

- **Gap:** Post-hoc explanations can be unfaithful; clinicians need models that are interpretable by construction.
- **Method:** Study optimal sparse decision trees and rule lists vs black-box models plus SHAP on clinical tasks; run clinician user studies on trust and accuracy.
- **Data & tools:** GOSDT / imodels, SHAP, clinical datasets
- **Expected outcome:** Evidence on when interpretable models match black-box accuracy, with clinician-validated explanations.
- **Target venues:** Nature Machine Intelligence; JAMIA; Artificial Intelligence in Medicine

</details>

