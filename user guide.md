Payload Generator CLI Tool -- 
common payloads for XSS, SQL Injection, command injection payload windows and linux , bypassing techniques, and
encoding.

✅ Step 1: Run Help Command To see all available options:

python tool.py --h
![Image Alt](https://github.com/Imtiaz-ktk/payload-generator-cli/blob/83625336cc867d01bcfdda30801fb650496a1da7/Capture.PNG)

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

  ![Image Alt](https://github.com/Imtiaz-ktk/payload-generator-cli/blob/8aba8bcc098a6ce449a479c45ee7d26102c443b6/Capture2.PNG)

🔹 Encode Payloads To encode any input:

python tool.py --encode Then enter one of these options:
![Image Alt](https://github.com/Imtiaz-ktk/payload-generator-cli/blob/8edf9b92abacaf32ebe338abb18ac5c102f80e14/Capture3.PNG)

--url + payload → URL encode

--base64 + payload → Base64 encode

--hex + payload → Hex encode

--unicode + payload → Unicode encode
![Image Alt](https://github.com/Imtiaz-ktk/payload-generator-cli/blob/0d89fcc99405c6e6f875da14ee9c90304410f199/Capture4.PNG)

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
