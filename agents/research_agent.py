class ResearchAgent:
    """
    ResearchAgent is responsible for exploring a topic
    and producing factual or contextual insights.

    NOTE:
    This is a reference implementation.
    The logic is intentionally simple and extensible.
    """

    def run(self, topic: str) -> dict:
        """
        Execute research on a given topic.

        Args:
            topic (str): The subject to research

        Returns:
            dict: Structured research output
        """
        return {
            "agent": "ResearchAgent",
            "topic": topic,
            "method": "exploratory research",
            "output": f"Key background and facts about {topic}"
        }
