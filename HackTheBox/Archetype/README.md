

# Archetype

![Platform](https://img.shields.io/badge/Platform-Hack%20The%20Box-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)
![OS](https://img.shields.io/badge/OS-Windows-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## Machine Overview

| Property | Value |
|----------|-------|
| Platform | Hack The Box |
| Operating System | Windows |
| Difficulty | Easy |
| Category | SMB / MSSQL / Windows |
| Status | Completed |

---

## Overview

Archetype is an Easy-rated Hack The Box machine focused on SMB enumeration, exposed credentials, Microsoft SQL Server misconfigurations, remote command execution, credential discovery, and Windows post-exploitation.

The assessment emphasizes service enumeration, access validation, exploitation, and post-exploitation activities. The attack chain demonstrates how exposed credentials in a configuration file can lead to database access and operating system command execution. Further enumeration reveals credentials stored in PowerShell history, which can be reused to obtain administrative access through Windows Remote Management (WinRM).

---

## Assessment Objectives

- Identify exposed network services.
- Enumerate SMB shares and assess their accessibility.
- Discover credentials stored in configuration files.
- Enumerate Microsoft SQL Server and assess user privileges.
- Analyze the security implications of enabling `xp_cmdshell`.
- Obtain operating system command execution through SQL Server.
- Perform local Windows enumeration and credential discovery.
- Examine PowerShell history for sensitive information.
- Obtain administrative access through WinRM using discovered credentials.
- Document the assessment findings and remediation recommendations.

---

## Skills Practiced

- Information Gathering
- Network and Service Enumeration
- SMB Enumeration
- Share Permission Analysis
- Credential Discovery and Validation
- Microsoft SQL Server Enumeration
- Database Privilege Assessment
- OS Command Execution
- Windows Post-Exploitation
- Local Privilege Escalation Enumeration
- PowerShell History Analysis
- WinRM Remote Access
- Technical Reporting

---

## Tools Used

- Nmap
- Rpcclient
- Smbclient
- Impacket
- WinPEAS
- Evil-WinRM

---

## Reports

- 📄 [Executive Report](./reports/Archetype_Executive_Report.pdf)
- 📄 [Technical Report](./reports/Archetype_Technical_Report.pdf)

---

## Supporting Artifacts

The supporting evidence collected during the assessment is available in the **artifacts** directory.

📁 [Browse Artifacts](./artifacts/)

---

## Repository Structure

```text
Archetype/
├── README.md
├── reports/
│   ├── Archetype_Executive_Report.pdf
│   └── Archetype_Technical_Report.pdf
└── artifacts/
    ├── scans/
    ├── enumeration/
    ├── exploitation/
    └── evidence/