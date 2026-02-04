from pathlib import Path

base_dir = Path("alx-backend-python/messaging_app")

files = [
    "kurbeScript",
    "deployment.yaml",
    "kubctl-0x01",
    "ingress.yaml",
    "commands.txt",
    "blue_deployment.yaml",
    "green_deployment.yaml",
    "kubeservice.yaml",
    "kubctl-0x02",
    "kubctl-0x03",
]

# Create directory
base_dir.mkdir(parents=True, exist_ok=True)

# Create files
for file in files:
    file_path = base_dir / file
    file_path.touch(exist_ok=True)

print("✅ Kubernetes project structure created successfully.")
