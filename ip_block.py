import requests
import socket
import subprocess
from urllib.parse import urlparse

def block_site(domain):
    # URL 형식일 경우 호스트만 추출
    parsed = urlparse(domain)
    print(parsed)
    host = parsed.netloc if parsed.netloc else parsed.path

    print(f"[+] {host} 에 연결 중...")

    # 실제 접속 시 사용된 IP 탐지
    try:
        response = requests.get(f"https://{host}", timeout=5)
        # 요청이 실제로 연결된 IP (소켓에서 추출)
        ip = socket.gethostbyname(host)
        print(f"[+] 실제 연결된 IP: {ip}")
    except Exception as e:
        print(f"[-] 접속 실패: {e}")
        return

    # netsh 명령어로 IP 차단 (관리자 권한 필요)
    rule_name = f"Block_{host}"
    cmd = [
        "netsh", "advfirewall", "firewall", "add", "rule",
        f"name={rule_name}",
        "dir=out","dir=in", "action=block", f"remoteip={ip}"
    ]

    try:
        subprocess.run(cmd, check=True, shell=True)
        print(f"[✅] {host} ({ip}) 차단 완료!")
    except subprocess.CalledProcessError as e:
        print(f"[-] netsh 실행 실패: {e}")

if __name__ == "__main__":
    target = input("차단할 사이트 주소를 입력하세요 (예: example.com 또는 https://example.com): ")
    block_site(target)
