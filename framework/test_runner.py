import threading
from framework.api_handler import AviAPI
from framework.mocks import mock_ssh, mock_rdp
import yaml

def run_test(test_id):
    print(f"\n Running Test {test_id}")
    api = AviAPI()
    api.login()
    mock_ssh()
    mock_rdp()

    # Step 1: Pre-Fetcher
    vs = api.get_vs_by_name(api.target_vs_name)
    if not vs:
        print(" Target Virtual Service not found!")
        return
    uuid = vs["uuid"]
    print(f"Found VS: {vs['name']} (UUID: {uuid})")

    # Step 2: Pre-Validation
    print(f"Pre-Validation: enabled={vs['enabled']}")
    if not vs["enabled"]:
        print(" Already disabled. Skipping toggle.")
        return

    # Step 3: Task/Trigger
    api.toggle_vs(uuid, enable=False)

    # Step 4: Post-Validation
    vs_after = api.get_vs_by_uuid(uuid)
    print(f"Post-Validation: enabled={vs_after['enabled']}")
    if not vs_after["enabled"]:
        print(" Virtual Service successfully disabled!")
    else:
        print(" Disable verification failed.")

def parallel_run(num_threads=2):
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=run_test, args=(i+1,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
