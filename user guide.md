Payload Generator CLI Tool -- 
common payloads for XSS, SQL Injection, command injection payload windows and linux , bypassing techniques, and
encoding.

✅ Step 1: Run Help Command To see all available options:

python tool.py --h

🔹 XSS Payloads Command Description
--xss --reflected        Reflected XSS payloads
--xss --stored           Stored XSS payloads 
--xss --dom              DOM-based XSS payloads

🔹 SQL Injection Payloads Command Description 
--sqli --error           Error-based SQLi payloads 
--sqli --union           Union-based SQLi payloads
--sqli --boolean         Boolean-based SQLi payloads 
--sqli --time            Time-based SQLi payloads

🔹 Command Injection Payloads 
▪ Linux and Windows payload variants (e.g., ;ls, && whoami, | net user) 
  For windows 
  --windows
  For Linux 
  --linux

🔹 Encode Payloads To encode any input:

python tool.py --encode Then enter one of these options:

--url + payload → URL encode

--base64 + payload → Base64 encode

--hex + payload → Hex encode

--unicode + payload → Unicode encode

🔹 Bypassing Techniques Command Description --bypassingTechniques Show
all bypass types 
--b --svg                   SVG-based XSS payloads
--b --srcdoc                Iframe srcdoc payloads 
 --b --eventHandler         onload, onerror bypasses
--b --nullByte              Null byte payloads 
--b --comments              SQLi using comment
--b --caseVariation         SQLi using mixed-case keywords 
--b --specialCharacters     SQLi using special characters

📌 Examples 
python tool.py --xss --reflected 
python tool.py --sqli --union
python tool.py --b --svg 
python tool.py --encode

⚠️ Disclaimer Use this tool only on systems you own or have explicit
permission to test. Unauthorized use is illegal.
