# Username Hunter

![Status](https://img.shields.io/badge/Status-Stable%20Release-brightgreen)

![Version](https://img.shields.io/badge/Version-v1.0-blue)

![Python](https://img.shields.io/badge/Python-3.x-yellow)

![License](https://img.shields.io/badge/License-MIT-green)

Username Hunter is a Python-based OSINT tool designed to check whether a username may be associated with different social media platforms.

The project was developed incrementally, with each version introducing new functionality while maintaining a structured and modular design. Version 1.0 provides a stable first release with HTTP request error handling, improved response interpretation, and formatted terminal output.

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
- Develop a foundation for future OSINT and automation projects.

---

# Current Version

**Version:** `v1.0`

Version 1.0 is the first stable release of Username Hunter. It implements the username enumeration workflow, handles HTTP request exceptions, and presents interpreted results using the Rich library.

### Current Features

- Username input through command-line arguments.
- Support for multiple social media platforms.
- Platform configuration using dictionaries.
- Automatic URL generation using username templates.
- HTTP `GET` requests using the `requests` library.
- Request timeout configuration.
- HTTP request exception handling.
- Structured storage of URLs, status codes, and request errors.
- Basic interpretation of HTTP responses.
- Formatted terminal output using Rich.
- Results displayed in a table.
- Color-coded status codes and result classifications.

### HTTP Response Interpretation

HTTP responses are interpreted as follows:

| Status Code | Result | Color |
|:-----------:|:------:|:-----:|
| Request error | Request Error | Red |
| `200` | Found | Green |
| `300–399` | Redirect | Yellow |
| `403` | Access Restricted | Yellow |
| `404` | Not Found | Red |
| Other status codes | Unknown | Yellow |

> **Note:** These classifications are based on HTTP responses and do not conclusively establish whether a username exists. Redirects, access restrictions, authentication requirements, anti-bot mechanisms, rate limiting, and platform-specific behavior may affect the results.

---

# Workflow

The application follows this workflow:

```text
Start
  |
  v
Parse Arguments
  |
  v
Receive Username and Social Media
  |
  v
Validate Selected Platforms
  |
  v
Build URLs
  |
  v
Send HTTP Requests
  |
  +---- Request Error
  |
  +---- HTTP Response
             |
             v
      Analyze Status Code
             |
             v
       Store Results
             |
             v
  Display Results Using Rich
             |
             v
            End
```

---

# Project Structure

The project follows a modular structure that separates the source code from the development documentation.

```text
Username_Hunter/
├── docs/
│   ├── flowchart/
│   └── pseudocode/
├── src/
│   ├── main.py
│   └── username_hunter.py
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

Methods include:

- `build_url()` — Builds the URLs corresponding to the selected social media platforms.
- `build_request()` — Performs HTTP requests and stores the resulting URLs, status codes, or request errors.
- `show_results()` — Interprets and displays the collected results using Rich.

### `docs/`

Contains the design and development documentation.

#### `flowchart/`

Contains the flowcharts used to represent the application's logic and workflow.

#### `pseudocode/`

Contains the pseudocode created before implementation and updated as the project evolves.

### `requirements.txt`

Contains the external Python dependencies required by the project.

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
| `requests` | HTTP requests and exception handling |
| `rich` | Formatted terminal output |
| Dictionaries | Platform configuration and result storage |
| Object-Oriented Programming | Application structure |
| Git | Version control |
| GitHub | Source code management and portfolio |

---

# Usage

The username is provided using `-u` or `--username`.

The username argument is **required**.

Social media platforms can be provided using `-s` or `--social`. This argument accepts one or more supported platforms.

### Single Social Media Platform

```bash
python3 src/main.py -u JohnDoe -s Github
```

### Multiple Social Media Platforms

```bash
python3 src/main.py -u JohnDoe -s Github Instagram Facebook TikTok OnlyFans YouTube LinkedIn X
```

### Example Output

The following output illustrates the result format. Actual status codes and classifications depend on the responses returned by the platforms.

```text
                         Username Hunter

┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Platform  ┃ Status ┃      Result       ┃ URL                              ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ github    │ 200    │ Found             │ https://github.com/JohnDoe       │
│ instagram │ 404    │ Not Found         │ https://www.instagram.com/JohnDoe│
│ tiktok    │ 403    │ Access Restricted │ https://www.tiktok.com/@JohnDoe  │
│ linkedin  │ ERROR  │ Request Error     │ https://www.linkedin.com/in/...  │
└───────────┴────────┴───────────────────┴──────────────────────────────────┘
```

The application evaluates the HTTP response status code returned by each requested URL. If a request fails, the error is stored and displayed separately from HTTP responses.

> **Important:** A `200` response does not guarantee that the username belongs to an actual profile, and a `403` response does not mean the username is unavailable. The tool provides an initial indication based on HTTP behavior, not definitive identity verification.

---

# Development Process

Username Hunter was developed incrementally.

Each version follows a structured development process in which functionality is planned, implemented, tested, and documented before moving to the next development stage.

The development workflow is:

```text
Planning
   |
   v
Flowchart
   |
   v
Pseudocode
   |
   v
Implementation
   |
   v
Testing
   |
   v
Documentation
   |
   v
Version Review
   |
   v
Next Version
```

### Planning

The functionality and objectives of each version are defined before implementation.

### Flowchart

The application's execution flow is represented visually to define the required logic and decision points.

### Pseudocode

The planned logic is defined through pseudocode before writing the Python implementation.

### Implementation

The planned functionality is implemented in Python.

### Testing

The application is executed with different inputs to verify that the implemented functionality behaves as expected.

### Documentation

The source code, pseudocode, and flowcharts are updated to reflect the implemented version.

### Version Review

Once the functionality has been implemented and tested, the version is reviewed before being considered complete.

---

# Version History

| Version | Description | Status |
|:-------:|---|:------:|
| `v0.1` | Initial username enumeration workflow | Completed |
| `v0.2` | Multiple social media platforms, URL generation, HTTP requests, and basic result interpretation | Completed |
| `v0.3` | Improved result presentation using Rich and HTTP status code color classification | Completed |
| `v1.0` | Stable first release with request error handling and improved HTTP response interpretation | Current |

The project uses Git for version control, allowing previous development stages to be tracked through commits and version tags.

---

# Roadmap

Potential future improvements include:

- Additional social media platforms.
- More detailed, platform-specific HTTP response analysis.
- Improved username detection techniques.
- Exporting results to structured formats such as JSON or CSV.
- Additional OSINT capabilities.
- Further automation and testing.

The roadmap may evolve as the project develops.

---

# Disclaimer

Username Hunter is developed for **educational purposes, cybersecurity research, and authorized OSINT activities**.

The tool is intended to query publicly accessible resources.

Users are responsible for ensuring that their use of the tool complies with applicable laws, regulations, and the terms of service of the platforms being queried.

This project must not be used for unauthorized access, harassment, privacy violations, or other malicious activities.

---

# License

This project is licensed under the **MIT License**.

See the `LICENSE` file in the repository for the complete license terms.