from agents.planner import PlannerAgent
from agents.literature import LiteratureAgent
from agents.methodology import MethodologyAgent
from agents.results import ResultsAgent
from agents.discussion import DiscussionAgent
from agents.editor import EditorAgent

def generate_manuscript(topic):
    planner = PlannerAgent()
    literature = LiteratureAgent()
    methodology = MethodologyAgent()
    results = ResultsAgent()
    discussion = DiscussionAgent()
    editor = EditorAgent()

    plan = planner.run(topic)
    lit = literature.run(plan)
    method = methodology.run(plan)
    res = results.run(method)
    disc = discussion.run(res)

    #combined = f"""
    combined = f"""
    PAPER TYPE: CONCEPTUAL FRAMEWORK PAPER.
    NO EMPIRICAL RESULTS ARE CLAIMED.
    ALL EVALUATION IS THEORETICAL AND QUALITATIVE.
     
    {plan}

    {lit}

    {method}

    {res}

    {disc}
    """

    #final_paper = editor.run(combined)
    print("=== COMBINED INPUT TO EDITOR ===")
    print(combined[:1500])

    final_paper = editor.run(combined, temperature=0.1)


    with open("output/manuscript.txt", "w", encoding="utf-8") as f:
        f.write(final_paper)

    print("Manuscript generated successfully.")

if __name__ == "__main__":
    generate_manuscript(
        "AI agent architectures for automating scientific manuscript generation"
    )
