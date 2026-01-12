def align(research_output: dict, consultant_output: dict) -> dict:
    """
    Compare outputs from ResearchAgent and ConsultantAgent
    to determine alignment or divergence.

    NOTE:
    This is a reference implementation.
    The alignment logic is intentionally simple.
    """

    aligned = research_output.get("topic") == consultant_output.get("topic")

    return {
        "research_agent_output": research_output,
        "consultant_agent_output": consultant_output,
        "aligned": aligned,
        "interpretation": (
            "Both agents are aligned on the topic"
            if aligned
            else "Agents show divergence in perspective"
        )
    }
