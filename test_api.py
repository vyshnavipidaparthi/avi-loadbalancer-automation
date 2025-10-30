import requests

base_url = "https://avi-mock-api-production.up.railway.app"

# --- 1️⃣ Login to get token ---
login = requests.post(f"{base_url}/login", auth=("Test", "password"))
print("Login Response:", login.status_code, login.text)

if login.status_code != 200:
    print("❌ Login failed! Please check credentials.")
    exit()

# --- 2️⃣ Extract token and headers ---
token = login.json().get("token")
headers = {"Authorization": f"Bearer {token}"}
print("✅ Login successful. Token acquired.\n")

# --- 3️⃣ Fetch all Virtual Services ---
vs_list = requests.get(f"{base_url}/api/virtualservice", headers=headers)
if vs_list.status_code != 200:
    print("❌ Failed to fetch virtual services.")
    exit()

vs_data = vs_list.json()
print("Fetched Virtual Services:", len(vs_data))

# --- 4️⃣ Find the target Virtual Service ---
target_vs_name = "backend-vs-t1r_1000-1"
target_vs = None
for vs in vs_data:
    if vs["name"] == target_vs_name:
        target_vs = vs
        break

if not target_vs:
    print(f"❌ Virtual Service '{target_vs_name}' not found.")
    exit()

uuid = target_vs["uuid"]
print(f"🎯 Found Target Virtual Service: {target_vs_name}")
print(f"UUID: {uuid}")
print(f"Enabled Status (Before): {target_vs['enabled']}\n")

# --- 5️⃣ Disable the Virtual Service (PUT request) ---
payload = {"enabled": False}
put_resp = requests.put(f"{base_url}/api/virtualservice/{uuid}", headers=headers, json=payload)
print("PUT Response:", put_resp.status_code, put_resp.text)

if put_resp.status_code != 200:
    print("❌ PUT request failed.")
    exit()

# --- 6️⃣ Verify the change (GET request again) ---
verify_resp = requests.get(f"{base_url}/api/virtualservice/{uuid}", headers=headers)
if verify_resp.status_code == 200:
    updated_vs = verify_resp.json()
    print("\n✅ Post-Validation:")
    print(f"Enabled Status (After): {updated_vs['enabled']}")
else:
    print("❌ Post-validation failed.")
