class ArchitectAgent:
    def __init__(self, chunk_threshold=1000):
        self.chunk_threshold = chunk_threshold

    def plan_refactoring(self, toon_output):
        """Analyzes TOON output and plans chunks for large files."""
        print("[Architect Agent] Planning refactoring strategy...")
        
        # Simple TOON parser for planning
        plans = []
        current_file = None
        
        for line in toon_output.split('\n'):
            line = line.strip()
            if line.startswith("file:"):
                current_file = line.split("file:")[1].strip()
            elif line.startswith("chunk: true") and current_file:
                plans.append({
                    "file": current_file,
                    "action": "chunking_required",
                    "strategy": "Sequential read (offset 0, limit 200) with 20-line overlap."
                })
            elif line.startswith("hotspots[") and current_file:
                 plans.append({
                    "file": current_file,
                    "action": "surgical_refactoring",
                    "strategy": "Apply references/refactoring_patterns.md directly to lines."
                })
                 
        return plans
