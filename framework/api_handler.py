import requests
import yaml

class AviAPI:
    def __init__(self, config_path="config.yaml"):
        # Load configuration from YAML file
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)

        # --- User-defined configuration ---
        self.base_url = "https://avi-mock-api-production.up.railway.app"
        self.username = "Test"
        self.password = "password"
        self.target_vs_name = config["api"]["target_vs_name"]

        # --- Authentication details ---
        self.token = None
        self.headers = {}

    # =====================================================
    # 1️⃣  LOGIN
    # =====================================================
    def login(self):
        """Authenticate user and store token."""
        print(" Logging in to Mock Avi API...")
        r = requests.post(f"{self.base_url}/login", auth=(self.username, self.password))
        if r.status_code == 200:
            self.token = r.json().get("token")
            self.headers = {"Authorization": f"Bearer {self.token}"}
            print(" Login successful")
        else:
            raise Exception(f" Login failed: {r.text}")

    # =====================================================
    # 2️⃣  GET ALL VIRTUAL SERVICES
    # =====================================================
    def get_virtual_services(self):
        """Fetch all Virtual Services."""
        print("📡 Fetching Virtual Services...")
        r = requests.get(f"{self.base_url}/api/virtualservice", headers=self.headers)
        if r.status_code == 200:
            return r.json()
        raise Exception(f" Failed to fetch Virtual Services: {r.text}")

    # =====================================================
    # 3️⃣  FIND A VS BY NAME (robust version)
    # =====================================================
    def get_vs_by_name(self, name):
        """Find a specific Virtual Service by name."""
        data = self.get_virtual_services()

        # --- Case 1: API returns a list of VS objects
        if isinstance(data, list):
            for vs in data:
                if isinstance(vs, dict) and vs.get("name") == name:
                    return vs

        # --- Case 2: API returns a dictionary with nested data
        elif isinstance(data, dict):
            # Directly a single VS
            if data.get("name") == name:
                return data
            # Nested list inside dictionary
            for key, value in data.items():
                if isinstance(value, list):
                    for vs in value:
                        if isinstance(vs, dict) and vs.get("name") == name:
                            return vs

        # --- No match found
        print(f"  Virtual Service '{name}' not found.")
        return None

    # =====================================================
    # 4️⃣  ENABLE / DISABLE VIRTUAL SERVICE
    # =====================================================
    def toggle_vs(self, uuid, enable=False):
        """Enable or disable a Virtual Service."""
        print(f"  Updating VS (UUID: {uuid}) → enabled={enable}")
        payload = {"enabled": enable}
        r = requests.put(
            f"{self.base_url}/api/virtualservice/{uuid}",
            headers=self.headers,
            json=payload
        )
        if r.status_code == 200:
            print(f" VS toggled successfully → enabled={enable}")
            return r.json()
        else:
            raise Exception(f" Failed to toggle VS: {r.text}")

    # =====================================================
    # 5️⃣  FETCH BY UUID
    # =====================================================
    def get_vs_by_uuid(self, uuid):
        """Fetch a single VS by UUID."""
        print(f" Fetching VS details by UUID: {uuid}")
        r = requests.get(f"{self.base_url}/api/virtualservice/{uuid}", headers=self.headers)
        if r.status_code == 200:
            return r.json()
        raise Exception(f" Failed to get VS by UUID: {r.text}")
