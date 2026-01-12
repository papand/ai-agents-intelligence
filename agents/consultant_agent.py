class ConsultantAgent:
    """
    ConsultantAgent is responsible for analyzing a topic
    and providing recommendations or opinions based on the analysis.

    NOTE:
    This is a reference implementation.
    The logic is intentionally simple and extensible.
    """

    def run(self, topic: str) -> dict:
        """
        Execute consulting analysis on a given topic.

        Args:
            topic (str): The subject to analyze

        Returns:
            dict: Structured consulting output
        """
        return {
            "agent": "ConsultantAgent",
            "topic": topic,
            "method": "advisory analysis",
            "output": f"Strategic considerations and recommendations for {topic}"
        }
