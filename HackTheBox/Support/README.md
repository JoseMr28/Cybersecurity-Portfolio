# Support

![Platform](https://img.shields.io/badge/Platform-HTB-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)
![OS](https://img.shields.io/badge/OS-Windows-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## Machine Overview

| Property | Value |
|---|---|
| Platform | Hack The Box |
| Machine | Support |
| Operating System | Windows |
| Difficulty | Easy |
| Category | Active Directory / Windows |
| Status | Completed |

## Overview

Support is a Windows-based Hack The Box machine focused on Active Directory enumeration and privilege escalation.

The assessment involved identifying exposed services, analyzing a .NET application to recover embedded credentials, and using the recovered information to enumerate Active Directory.

Initial access was obtained through Windows Remote Management (WinRM). Further enumeration revealed excessive Active Directory permissions that enabled a Resource-Based Constrained Delegation (RBCD) attack path, ultimately leading to administrative access to the Domain Controller.

## Objectives

- Identify exposed services and potential attack surfaces.
- Enumerate SMB shares and Active Directory services.
- Perform static analysis of a .NET application.
- Identify and recover exposed credentials.
- Authenticate to LDAP and enumerate domain information.
- Obtain initial access through WinRM.
- Identify excessive Active Directory permissions.
- Configure and exploit Resource-Based Constrained Delegation (RBCD).
- Obtain administrative access to the Domain Controller.
- Document the attack path and security findings.

## Skills Practiced

- Information Gathering
- Service Enumeration
- SMB Enumeration
- DNS Enumeration
- LDAP Enumeration
- Kerberos Enumeration
- Active Directory Enumeration
- Static Analysis
- .NET Application Analysis
- Credential Recovery
- Windows Remote Management (WinRM)
- BloodHound Analysis
- Active Directory ACL Abuse
- Resource-Based Constrained Delegation (RBCD)
- Kerberos Ticket Manipulation
- Windows Post-Exploitation
- Privilege Escalation
- Technical Reporting

## Tools Used

- Nmap
- SMBClient
- RPCClient
- LDAPSearch
- LDAPWhoami
- Nslookup
- Strings
- Monodis
- Grep
- Od
- Awk
- jq
- Impacket
- Netcat
- BloodHound CE
- BloodHound CE Python
- Evil-WinRM

## Reports

### Executive Report

A high-level overview of the assessment, including the identified security weaknesses, their impact, and remediation recommendations.

[View Executive Report](./reports/Support_Executive_Report.pdf)

### Technical Report

A detailed walkthrough of the assessment, covering reconnaissance, enumeration, vulnerability analysis, exploitation, post-exploitation, privilege escalation, and evidence collection.

[View Technical Report](./reports/Support_Technical_Report.pdf)

## Supporting Artifacts

The `artifacts/` directory contains supporting files collected or generated during the assessment, organized by category:

- `scans/` – Network and service scan results.
- `enumeration/` – Enumeration output and supporting data.
- `exploits/` – Exploitation-related artifacts.
- `evidence/` – Screenshots and evidence supporting the findings.

## Repository Structure

```text
Support/
├── README.md
├── reports/
│   ├── Support_Executive_Report.pdf
│   └── Support_Technical_Report.pdf
└── artifacts/
    ├── scans/
    ├── enumeration/
    ├── exploits/
    └── evidence/