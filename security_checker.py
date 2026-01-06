import requests

url = input("Enter website URL (https://example.com): ")

try:
    response = requests.get(url, timeout=5)

    print("\n[+] Status Code:", response.status_code)

    print("\n[+] Security Headers Check:")
    headers = response.headers

    security_headers = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Strict-Transport-Security"
    ]

    for header in security_headers:
        if header in headers:
            print(f"[✔] {header}: Present")
        else:
            print(f"[✘] {header}: Missing")

    if url.startswith("https://"):
        print("\n[✔] HTTPS is enabled")
    else:
        print("\n[✘] HTTPS is not enabled")

except Exception as e:
    print("Error:", e)
