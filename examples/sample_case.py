from agents.research_agent import ResearchAgent
from agents.consultant_agent import ConsultantAgent
from agents.alignment_logic import align


def run_example():
    topic = "US–Venezuela relations"

    research_agent = ResearchAgent()
    consultant_agent = ConsultantAgent()

    research_output = research_agent.run(topic)
    consultant_output = consultant_agent.run(topic)

    alignment_result = align(research_output, consultant_output)

    print("=== Research Output ===")
    print(research_output)

    print("\n=== Consultant Output ===")
    print(consultant_output)

    print("\n=== Alignment Result ===")
    print(alignment_result)


if __name__ == "__main__":
    run_example()
