import argparse
from monitor import get_system_metrics
from thresholds import evaluate_metrics
from report import save_report
from logger import setup_logger

def main():
    parser = argparse.ArgumentParser(description="ATE Health Monitor")
    parser.add_argument(
        "--test-failure",
        action="store_true",
        help="Simulate a CPU failure for testing"
    )
    args = parser.parse_args()
    logger = setup_logger()

    logger.info("Starting ATE Health Monitor")

    metrics = get_system_metrics()

    if args.test_failure:
        metrics["cpu"] = 95
        logger.info("Test failure mode enabled: CPU set to 95%")

    # ----- FAKE FAILURE TEST -----

    logger.info(f"Collected metrics: {metrics}")

    results, overall_status, failed_metrics = evaluate_metrics(metrics)
    logger.info(f"Evaluation results: {results}")

    print("\n----- SYSTEM METRICS -----:")

    for metric, value in metrics.items():
        print(f"{metric.upper()}: {value}%")
        logger.info(f"{metric.upper()}: {value}%")

    print("\n----- HEALTH CHECK -----")

    for metric, result in results.items():
        print(f"{metric.upper()}: {result}")
        logger.info(f"{metric.upper()}: {result}")

    print(f"\nOVERALL STATUS: {overall_status}")
    logger.info(f"OVERALL STATUS: {overall_status}")

    if failed_metrics:
        print("\nFAILED METRICS:")
        for metric in failed_metrics:
            print(f"- {metric.upper()}")
            logger.info(f"FAILED METRIC: {metric.upper()}")

    save_report(metrics, results, overall_status)
    logger.info("Report saved successfully")
    logger.info("ATE health monitoring finished\n")

if __name__ == "__main__":
    main()
