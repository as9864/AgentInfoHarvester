import yaml
import os

def load_config(path="config\config.yaml") -> dict:
    #기준을 현재 파일 위치로 보정
    base_dir = os.path.dirname(os.path.abspath(__file__))

    config_path = os.path.join(base_dir, "..", path)


    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
