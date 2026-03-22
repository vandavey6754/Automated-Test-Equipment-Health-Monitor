import psutil

def get_system_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    metrics = {
        "cpu": cpu,
        "memory": memory,
        "disk": disk
    }

    return metrics