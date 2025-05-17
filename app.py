import json
from models import Project, Stage
import pandas as pd

def create_sample_project():
    return Project(
        name="AI Rollout",
        start_month=1,
        end_month=6,
        stages=[
            Stage("Planning", 1, 2, {"PM": 1, "BA": 1}),
            Stage("Development", 3, 5, {"Developer": 3, "Tester": 1}),
            Stage("Deployment", 6, 6, {"DevOps": 2})
        ]
    )

def generate_resource_matrix(projects: list[Project]) -> pd.DataFrame:
    all_roles = set()
    max_month = 0
    for p in projects:
        max_month = max(max_month, p.end_month)
        for s in p.stages:
            all_roles.update(s.resource_needs.keys())

    data = {role: [0] * max_month for role in all_roles}

    for project in projects:
        for stage in project.stages:
            for month in range(stage.start_month, stage.end_month + 1):
                for role, count in stage.resource_needs.items():
                    data[role][month - 1] += count

    df = pd.DataFrame(data)
    df.index = [f"Month {i+1}" for i in range(max_month)]
    return df

def main():
    print("Generating resource model...\n")
    project = create_sample_project()
    df = generate_resource_matrix([project])
    print(df)

    save_csv = input("\nExport to CSV? (y/n): ").lower()
    if save_csv == 'y':
        df.to_csv("resource_model_output.csv")
        print("Saved as resource_model_output.csv")

if __name__ == "__main__":
    main()
