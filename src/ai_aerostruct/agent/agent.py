class EngineeringAgent:
    """Minimal placeholder for the future LLM-powered agent.

    The agent should:
    1. Parse user requirements.
    2. Produce DesignSpec.
    3. Call registered skills.
    4. Explain computed results.
    """

    def __init__(self, registry):
        self.registry = registry

    def run_skill(self, name: str, data: dict):
        skill = self.registry.get(name)
        return skill.run(data)
