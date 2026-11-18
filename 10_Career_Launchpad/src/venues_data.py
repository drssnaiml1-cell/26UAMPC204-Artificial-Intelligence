"""Hackathons, conferences and journals mapped to 26UAMPC204, plus the end-of-course skill outcome.
Hackathon windows were checked against 2025–26 editions (Nov 2026); always confirm on the official site.
CORE ranks are from the CORE conference portal (portal.core.edu.au); re-check before citing.
"""

HACKATHONS = [
# (name, organiser, level, typical window, who, ai_fit, units, url)
("Smart India Hackathon (SIH) — Software Edition", "Ministry of Education Innovation Cell & AICTE", "National",
 "Internal rounds Aug–Sep; Grand Finale in December (SIH 2025 finale: 8–9 Dec 2025)",
 "Teams of 6 from AICTE institutions", "Government problem statements; many need AI/ML, NLP, vision and optimisation",
 "I–V", "https://sih.gov.in"),
("Microsoft Imagine Cup", "Microsoft", "Global",
 "Registration from about September; submissions in early January; world final at Microsoft Build (2026 final: 2 June 2026)",
 "Student founders (Microsoft has announced it will open to startups from 2027)", "AI startups built on Microsoft AI and Azure",
 "V", "https://imaginecup.microsoft.com"),
("Google Solution Challenge (Build with AI)", "Google for Developers / GDG on Campus", "Global / India",
 "Kick-offs at GDG on Campus chapters around March–April",
 "University students in teams", "Solutions for the UN Sustainable Development Goals with Gemini, Firebase and Google Cloud",
 "I, V", "https://gdg.community.dev"),
("Amazon ML Challenge", "Amazon India (on Unstop)", "National",
 "Registration around August–September; 72-hour online round; finale in October (2025 finale: 17 Oct 2025)",
 "Engineering students in India, teams of 3–4", "Real Amazon datasets; top teams get pre-placement interviews for Applied Scientist intern roles",
 "IV, V", "https://unstop.com"),
("Flipkart GRiD", "Flipkart", "National",
 "Registration mid-June to early July; national finals at Flipkart HQ, Bengaluru (GRiD 8.0 in 2026 added three tracks)",
 "B.Tech / M.Tech / M.S. / dual-degree students; PhD students from 8.0", "Engineering and data challenges with SDE / intern offers for finalists",
 "II, V", "https://unstop.com"),
("Kaggle Competitions", "Kaggle (Google)", "Global, year-round",
 "Always open; featured, research, playground and community competitions",
 "Anyone, solo or teams", "Supervised learning, NLP, vision, time series, reinforcement learning",
 "II, IV, V", "https://www.kaggle.com/competitions"),
("NASA International Space Apps Challenge", "NASA and partner space agencies", "Global",
 "Annual, usually a weekend in early October, with local events in India",
 "Anyone, teams of up to 6", "Earth and space data, AI for climate, disaster and mapping problems",
 "II, IV, V", "https://www.spaceappschallenge.org"),
("Major League Hacking (MLH) season", "MLH and member hackathons", "Global, year-round",
 "Weekend hackathons all year, many online; Indian college fests join the MLH season",
 "Students", "Open themes; AI and agent tracks are common", "I–V", "https://mlh.io/seasons"),
]

CONFERENCES = [
# (acronym, full name, core, units, focus, student_tip)
("NeurIPS", "Conference on Neural Information Processing Systems", "A*", "V", "Machine learning and deep learning", "Workshops and the Datasets & Benchmarks track suit first papers"),
("ICML", "International Conference on Machine Learning", "A*", "IV, V", "Machine learning theory and practice", "Workshops accept short papers"),
("ICLR", "International Conference on Learning Representations", "A*", "V", "Representation and deep learning", "Open reviews on OpenReview are good reading"),
("AAAI", "AAAI Conference on Artificial Intelligence", "A*", "I–V", "All of AI, including search, planning and knowledge", "Student abstract and undergraduate consortium tracks"),
("IJCAI", "International Joint Conference on Artificial Intelligence", "A*", "I–V", "All of AI", "Doctoral consortium; demo track"),
("AAMAS", "Autonomous Agents and Multiagent Systems", "A*", "I, II", "Agents, multi-agent systems, game theory", "Extended abstracts for early work"),
("ICAPS", "International Conference on Automated Planning and Scheduling", "A*", "II, IV", "Planning, scheduling, PDDL", "Workshops and planning competitions (IPC)"),
("KR", "Principles of Knowledge Representation and Reasoning", "A*", "III", "Logic, ontologies, reasoning", "Good fit for logic-based projects"),
("ACL / EMNLP", "Association for Computational Linguistics / Empirical Methods in NLP", "A*", "V", "Natural language processing", "Student research workshop at ACL"),
("CVPR / ICCV", "Computer Vision and Pattern Recognition / International Conference on Computer Vision", "A*", "V", "Computer vision", "Workshops on applied vision"),
("KDD", "ACM SIGKDD Conference on Knowledge Discovery and Data Mining", "A*", "IV, V", "Data mining, applied data science", "Applied data science track"),
("UAI", "Conference on Uncertainty in Artificial Intelligence", "A", "IV", "Probabilistic reasoning, Bayesian networks", "Ideal for Unit IV research"),
("AISTATS", "Artificial Intelligence and Statistics", "A", "IV, V", "Statistical machine learning", "Strong for probabilistic methods"),
("ECAI", "European Conference on Artificial Intelligence", "A", "I–V", "All of AI", "Accessible broad venue"),
("CODS-COMAD", "ACM India Joint International Conference on Data Science & Management of Data", "—", "IV, V", "Data science (India)", "Young researchers' symposium; good first venue in India"),
("ICON", "International Conference on Natural Language Processing (India)", "—", "V", "NLP for Indian languages", "Fits Marathi / Hindi NLP projects"),
("ICVGIP", "Indian Conference on Computer Vision, Graphics and Image Processing", "—", "V", "Vision and graphics (India)", "Strong Indian vision community"),
]

JOURNALS = [
# (name, publisher, units, focus, tier_note)
("Artificial Intelligence (AIJ)", "Elsevier", "I–V", "Foundational AI: search, logic, planning, learning", "Flagship AI journal"),
("Journal of Artificial Intelligence Research (JAIR)", "AI Access Foundation (open access)", "I–V", "All of AI", "Flagship, open access"),
("Journal of Machine Learning Research (JMLR)", "JMLR (open access)", "V", "Machine learning", "Flagship, open access"),
("Transactions on Machine Learning Research (TMLR)", "OpenReview (open access)", "V", "Machine learning", "Rolling reviews"),
("IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)", "IEEE", "V", "Vision and learning", "Top-tier IEEE Transactions"),
("IEEE Transactions on Neural Networks and Learning Systems (TNNLS)", "IEEE", "V", "Neural networks and learning", "IEEE Transactions"),
("IEEE Transactions on Artificial Intelligence (TAI)", "IEEE", "I–V", "Broad AI", "IEEE Transactions"),
("IEEE Transactions on Fuzzy Systems", "IEEE", "IV", "Fuzzy logic and systems", "Leading fuzzy-systems journal"),
("Knowledge-Based Systems", "Elsevier", "III, V", "Knowledge representation, intelligent systems", "Q1 applied AI"),
("Expert Systems with Applications", "Elsevier", "III, V", "Expert systems and applied AI", "Q1 applied AI"),
("Engineering Applications of Artificial Intelligence", "Elsevier", "II, IV, V", "AI in engineering", "Q1 applied AI"),
("Neural Networks", "Elsevier", "V", "Neural computation", "Q1"),
("Pattern Recognition", "Elsevier", "V", "Pattern recognition and vision", "Q1"),
("International Journal of Approximate Reasoning", "Elsevier", "IV", "Uncertainty, Bayesian networks, fuzzy reasoning", "Specialist venue for Unit IV"),
("Nature Machine Intelligence", "Springer Nature", "V", "High-impact AI across disciplines", "Highly selective"),
("IEEE Access", "IEEE (open access)", "I–V", "Multidisciplinary engineering incl. AI", "Fast open-access venue for student work"),
]

# ---------------------------------------------------------------- end-of-course skill outcome
SKILL_BARS = [  # (skill, target level 0-100 by end of course, evidence)
("Problem formulation (PEAS & state spaces)", 90, "Exp 1, Assignment 1"),
("Search & optimisation algorithms", 92, "Exp 2–5, interview coding set"),
("Game AI & constraint solving", 85, "Exp 4–5, Assignment 2"),
("Logic, knowledge graphs & inference", 85, "Exp 6–7, Assignment 3"),
("Probabilistic reasoning & planning", 85, "Exp 8, Assignment 4"),
("Machine learning & interpretation", 88, "Exp 9, Assignment 5"),
("Expert systems & chatbots", 88, "Exp 10 mini-project"),
("Responsible AI & ethics", 80, "Assignment 5, model card"),
]

END_PRODUCTS = [  # what every student walks out with
("GitHub portfolio", "10 working lab notebooks + 5 assignment repositories with READMEs"),
("Mini-project", "Rule-based expert system or chatbot with explanation facility (Exp 10)"),
("Algorithm library", "Own implementations of BFS, DFS, UCS, A*, Minimax, CSP, unification, Bayes, ID3"),
("Model card", "A documented, fairness-checked classifier (Assignment 5)"),
("Hackathon-ready team pitch", "A problem formulation and prototype plan for SIH / Kaggle / Solution Challenge"),
("Research starter", "One research idea with gap statement and baseline (08_Research_Ideas)"),
("Interview readiness", "75 practised questions and 10 solved coding problems"),
]

CAN_DO = [
"Turn an open-ended problem into a precise AI specification (PEAS, states, actions, costs, goals).",
"Choose and implement the right search, optimisation or game-playing algorithm and analyse its complexity.",
"Encode domain knowledge as logic, rules or a knowledge graph and explain every inference.",
"Reason with probabilities, build a Bayesian network and plan under uncertainty.",
"Train, evaluate and interpret a learning model, and audit it for fairness and safety.",
"Build and demo an expert system or chatbot end to end, with documentation on GitHub.",
"Pitch an AI solution at a hackathon and turn an idea into a research proposal.",
]
