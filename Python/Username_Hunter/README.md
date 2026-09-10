# Username Hunter

![Status](https://img.shields.io/badge/Status-In%20Development-orange)

![Version](https://img.shields.io/badge/Version-v0.3-blue)

![Python](https://img.shields.io/badge/Python-3.x-yellow)

![License](https://img.shields.io/badge/License-MIT-green)

Username Hunter is a Python-based OSINT tool designed to check whether a username is associated with different social media platforms.

The project is being developed incrementally, with each version introducing new functionality while maintaining a structured and modular design.

---

# Project Objectives

The main objectives of Username Hunter are:

- Automate username enumeration across social media platforms.
- Practice Python programming applied to cybersecurity and OSINT.
- Develop modular and maintainable security tooling.
- Practice Object-Oriented Programming.
- Work with HTTP requests and response status codes.
- Apply structured software development practices.
- Document the development process through pseudocode and flowcharts.
- Gradually introduce additional OSINT and automation capabilities.

---

# Current Version

**Version:** `v0.3`

The current version implements the basic username enumeration workflow with structured terminal output using the Rich library.

### Current Features

- Username input through command-line arguments.
- Support for multiple social media platforms.
- Platform configuration using nested dictionaries.
- Automatic URL generation using username templates.
- HTTP `GET` requests using the `requests` library.
- Storage of URLs and HTTP status codes in a dictionary.
- Basic interpretation of HTTP responses.
- Structured terminal output using Rich.
- Formatted results displayed in a table.
- HTTP status code color classification.

HTTP status codes are currently interpreted as:

| Status Code | Result | Color |
|:-----------:|:------:|:-----:|
| `200` | Found | 🟢 Green |
| `300–399` | Not Found | 🟡 Yellow |
| `400+` | Not Found | 🔴 Red |

> **Note:** The current detection method is based primarily on HTTP response status codes. Some platforms may use redirects, anti-bot mechanisms, authentication requirements, rate limiting, or other response behaviors that can affect the accuracy of username detection.

---

# Workflow

The current version follows this workflow:

```text
Start
  │
  ▼
Parse Arguments
  │
  ▼
Username
  │
  ▼
Select Social Media
  │
  ▼
Build URL
  │
  ▼
Build Request
  │
  ▼
Analyze Response
  │
  ▼
Show Results
  │
  ▼
End
```

---

# Project Structure

The project follows a modular structure that separates the source code from the development documentation.

```text
Username_Hunter/

│
├── docs/
│   ├── flowchart/
│   └── pseudocode/
│
├── src/
│   ├── main.py
│   └── username_hunter.py
│
├── requirements.txt
└── README.md
```

### `src/`

Contains the Python source code.

#### `main.py`

Responsible for:

- Command-line argument parsing using `argparse`.
- Receiving the username and selected social media platforms.
- Creating the `UsernameHunter` object.
- Calling the methods that make up the application workflow.

#### `username_hunter.py`

Contains the `UsernameHunter` class and the main functionality of the application.

Current methods include:

- `build_url()` — Builds the URLs corresponding to the selected social media platforms.
- `build_request()` — Performs HTTP requests and stores the resulting URLs and status codes.
- `show_results()` — Displays and interprets the collected results using Rich.

### `docs/`

Contains the design and development documentation.

#### `flowchart/`

Contains the flowcharts used to represent the application's logic and workflow.

#### `pseudocode/`

Contains the pseudocode created before implementation and updated as the project evolves.

### `requirements.txt`

Contains the external Python dependencies required by the project.

The current version uses:

```text
requests
rich
```

Python standard library modules such as `argparse` do not need to be included in this file.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/JoseMr28/Cybersecurity-Portfolio.git
```

Navigate to the Username Hunter directory:

```bash
cd Cybersecurity-Portfolio/Python/Username_Hunter
```

Create the Conda environment:

```bash
conda create -n username_hunter python=3.13
```

Activate the environment:

```bash
conda activate username_hunter
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

The tool is now ready to use.

---

# Technologies

| Technology | Purpose |
|---|---|
| Python 3.x | Main programming language |
| `argparse` | Command-line argument parsing |
| `requests` | HTTP requests |
| `rich` | Formatted output |
| Dictionaries | Platform configuration and result storage |
| Object-Oriented Programming | Application structure |
| Git | Version control |
| GitHub | Source code management and portfolio |

---

# Usage

The username is provided using `-u` or `--username`.

The username argument is **required**.

Social media platforms can be provided using `-s` or `--social`.

The `--social` argument accepts one or more supported platforms.

### Single Social Media

```bash
python3 src/main.py -u JohnDoe -s Github
```

### Multiple Social Media Platforms

```bash
python3 src/main.py -u JohnDoe -s Github Instagram
```

### Example Output

```text
                                Username Hunter

┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Platform  ┃ Status ┃  Result   ┃ URL                                    ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│  github   │  200   │   Found   │ https://github.com/JohnDoe              │
│ instagram │  200   │   Found   │ https://www.instagram.com/JohnDoe      │
│ onlyfans  │  403   │ Not Found │ https://www.onlyfans.com/JohnDoe        │
│  tiktok   │  403   │ Not Found │ https://www.tiktok.com/@JohnDoe        │
└───────────┴────────┴───────────┴────────────────────────────────────────┘
```

The application currently evaluates the HTTP response status code returned by each requested URL.

A `200` response is interpreted as `Found`.

Responses in the `300–399` range are interpreted as `Not Found` and displayed in yellow.

Responses with a status code of `400` or higher are interpreted as `Not Found` and displayed in red.

> **Note:** This interpretation is part of the current development version and may be improved in future versions to account for platform-specific response behavior.

---

# Development Process

Username Hunter is developed incrementally.

Each version follows a structured development process in which the functionality is planned, implemented, tested and documented before moving to the next development stage.

The current development workflow is:

```text
Planning
   ↓
Flowchart
   ↓
Pseudocode
   ↓
Implementation
   ↓
Testing
   ↓
Documentation
   ↓
Version Review
   ↓
Next Version
```

### Planning

The functionality and objectives of the next version are defined before implementation.

### Flowchart

The application's execution flow is represented visually to define the required logic and decision points.

### Pseudocode

The planned logic is defined through pseudocode before writing the Python implementation.

### Implementation

The planned functionality is implemented in Python.

### Testing

The application is executed with different inputs to verify that the implemented functionality behaves as expected.

### Documentation

The source code, pseudocode and flowcharts are updated to reflect the implemented version.

### Version Review

Once the functionality has been implemented and tested, the version is reviewed before moving to the next development stage.

---

# Version History

| Version | Description | Status |
|:-------:|---|:------:|
| `v0.1` | Initial username enumeration workflow | ✅ Completed |
| `v0.2` | Multiple social media platforms, URL generation, HTTP requests and basic result interpretation | ✅ Completed |
| `v0.3` | Improved result presentation using Rich and HTTP status code color classification | 🚧 Current |
| `v1.0` | Stable release | 🔲 Planned |

The project uses Git for version control, allowing previous development stages to be tracked through commits and version tags.

The source code remains in the main project structure while Git preserves the history of previous versions.

---

# Roadmap

Future versions may introduce:

- Improved HTTP error handling.
- Additional social media platforms.
- More detailed HTTP response analysis.
- Improved username detection techniques.
- Structured result handling.
- Additional OSINT capabilities.
- Further automation.

The roadmap may evolve as the project develops.

---

# Disclaimer

Username Hunter is developed for **educational purposes, cybersecurity research and authorized OSINT activities**.

The tool is intended to query publicly accessible resources.

Users are responsible for ensuring that their use of the tool complies with the applicable laws, regulations and terms of service of the platforms being queried.

This project must not be used for unauthorized access, harassment, privacy violations or other malicious activities.

---

# License

This project is licensed under the **MIT License**.

See the `LICENSE` file in the repository for the complete license terms.