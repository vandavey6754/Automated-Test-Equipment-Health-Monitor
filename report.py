import json
import os
from datetime import datetime

def save_report(metrics, results, overall_status):

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M%S")

    report_data = {
        "timestamp": timestamp,
        "metrics": metrics,
        "results": results,
        "overall_status": overall_status
    }

    #create reports directory if it does not exist
    os.makedirs("reports", exist_ok = True)

    filename = f"reports/health_report_{timestamp}.json"

    with open(filename, "w") as file:
        json.dump(report_data, file, indent = 4)

    print(f"\nReport saved to {filename}")
