
# Oopsie

![Platform](https://img.shields.io/badge/Platform-Hack%20The%20Box-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)
![OS](https://img.shields.io/badge/OS-Linux-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## Machine Overview

| Property | Value |
|----------|-------|
| Platform | Hack The Box |
| Operating System | Linux |
| Difficulty | Easy |
| Category | Web Application / Linux |
| Status | Completed |

---

## Overview

Oopsie is an Easy-rated Hack The Box machine focused on web application security, broken access controls, file upload vulnerabilities, remote code execution, credential discovery, and Linux privilege escalation.

The assessment emphasizes manual enumeration, vulnerability validation, exploitation, and post-exploitation activities. The attack chain demonstrates how multiple vulnerabilities can be combined to obtain initial access and ultimately achieve root-level privileges.

---

## Assessment Objectives

- Identify exposed network services.
- Enumerate the web application and its functionality.
- Discover and validate access control vulnerabilities.
- Identify insecure direct object references (IDOR).
- Exploit an unrestricted file upload vulnerability to obtain remote code execution.
- Perform post-exploitation enumeration and credential discovery.
- Escalate privileges from `www-data` to `robert` and ultimately to `root`.
- Document the assessment findings and remediation recommendations.

---

## Skills Practiced

- Information Gathering
- Service Enumeration
- Web Enumeration
- Access Control Testing
- IDOR Identification
- File Upload Testing
- Remote Code Execution
- Credential Discovery
- Linux Privilege Escalation
- PATH Hijacking
- Post-Exploitation
- Technical Reporting

---

## Tools Used

- Nmap
- Curl
- Whatweb
- Gobuster
- Nikto
- Burp Suite


---

## Reports
## Reports

- 📄 [Executive Report](./reports/Oopsie_Executive_Report.pdf)
- 📄 [Technical Report](./reports/Oopsie_Technical_Report.pdf)

---

## Supporting Artifacts

## Supporting Artifacts

The supporting evidence collected during the assessment is available in the **artifacts** directory.

📁 [Browse Artifacts](./artifacts/)
---

## Repository Structure

```text
Oopsie/
├── README.md
├── reports/
│   ├── Executive_Report.pdf
│   └── Technical_Report.pdf
└── artifacts/
    ├── scans/
    ├── exploits/
    ├── evidence/
    └── credentials/
```

---

## Disclaimer

This assessment was performed exclusively in an authorized laboratory environment provided by Hack The Box for educational and professional development purposes.
