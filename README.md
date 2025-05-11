# SSH-Log-Analyzer
A Flask-based web application designed for Blue Teams to analyze SSH logs and detect brute-force login attempts. The tool identifies suspicious IP addresses, evaluates threat levels, enriches logs with geolocation data, and allows exporting threat reports as CSV files.

🎯 Key Features
✅ Parses SSH logs and identifies "Failed password" attempts

🌍 Fetches the geolocation (country) of suspicious IPs using IP-API

📊 Classifies threats as Low, Medium, or High based on frequency

🕵️ Shows timestamps of first and last failed login attempts

📥 Allows exporting results as a CSV threat report

**⚙️ Planned support for more log types, including:**

🔥 Firewall logs (e.g., UFW, iptables)
🧱 Web server logs (e.g., Apache, NGINX)
🎯 IDS/IPS alert logs (e.g., Snort, Suricata)

![image](https://github.com/user-attachments/assets/7389f35f-b250-49c6-bede-8b7b73cdf5ba)

![image](https://github.com/user-attachments/assets/349263c2-9c29-4385-8e2d-a7ab14589ca2)

**🚀 Getting Started:** To run this tool locally: 
📥 Installation 
bash
git clone https://github.com/akmal-cyb/SSH-Log-Analyzer.git 
You can run and debug the project easily in PyCharm by opening the project folder and running app.py.



