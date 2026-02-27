import subprocess
import json

class ScannerAgent:
    def __init__(self, target_dir="."):
        self.target_dir = target_dir

    def audit(self, format="toon"):
        """Executes scan.py and returns the debt map."""
        print(f"[Scanner Agent] Auditing {self.target_dir}...")
        cmd = ["python3", "scripts/scan.py", self.target_dir]
        if format == "toon":
            cmd.append("--toon")
        elif format == "json":
            cmd.append("--json")
            
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Scanner failed: {result.stderr}")
            return None
            
        return result.stdout
