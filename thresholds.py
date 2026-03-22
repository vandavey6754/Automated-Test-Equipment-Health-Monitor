def evaluate_metrics(metrics):

    thresholds = {
        "cpu": 90,
        "memory": 85,
        "disk": 90
    }

    results = {}
    failed_metrics = []

    for metric in metrics:
        value = metrics[metric]
        limit = thresholds[metric]

        if value > limit:
            results[metric] = "FAIL"
            failed_metrics.append(metric)
        else:
            results[metric] = "PASS"

    if failed_metrics:
        #(is not empty)
        overall_status = "FAIL"
    else:
        overall_status = "PASS"

    return results, overall_status, failed_metrics