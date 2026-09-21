#!/usr/bin/env python3
from __future__ import annotations

import re
from html import escape
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPO_ROOT / "README.md"

CATEGORY_GROUPS = [
    {
        "id": "use-cases",
        "title": "🎯 USE CASES",
        "description": "Applications where Jev makes, scores, gates, or controls a concrete decision.",
        "sections": [
            (
                "By decision pattern",
                [
                    "classification-routing.md",
                    "verification-guardrails.md",
                    "scoring-ranking.md",
                    "agent-action-control.md",
                    "data-labeling-curation.md",
                ],
            ),
            (
                "By application domain",
                [
                    "games-robotics-simulation.md",
                    "finance-trading.md",
                    "legal-compliance.md",
                    "content-filtering-moderation.md",
                    "scientific-workflows.md",
                ],
            ),
        ],
    },
    {
        "id": "sdks-integrations",
        "title": "🧰 SDKs & INTEGRATIONS",
        "description": "Clients, gateways, runtimes, framework adapters, and developer tools for integrating Jev.",
        "sections": [
            (None, ["sdks-integrations-infrastructure.md"]),
        ],
    },
    {
        "id": "research-evaluation",
        "title": "🧪 RESEARCH & EVALUATION",
        "description": "Evaluators, comparative benchmarks, calibration studies, open reproductions, and Jev-style model research.",
        "sections": [
            (None, ["evaluation-benchmarks.md", "calibration-model-research.md"]),
        ],
    },
    {
        "id": "guides-community",
        "title": "📚 GUIDES & COMMUNITY",
        "description": "Tutorials, explainers, technical analyses, case reports, directories, and public discussion.",
        "sections": [
            (None, ["guides-analysis-community.md"]),
        ],
    },
]

ALL_FILES = [
    filename
    for group in CATEGORY_GROUPS
    for _, filenames in group["sections"]
    for filename in filenames
]


class Category:
    def __init__(
        self,
        filename: str,
        title: str,
        description: str,
        count: int,
        lines: list[str],
    ) -> None:
        self.filename = filename
        self.title = title
        self.description = description
        self.count = count
        self.lines = lines

    @property
    def path(self) -> str:
        return f"categories/{self.filename}"


def parse_category(filename: str) -> Category:
    path = REPO_ROOT / "categories" / filename
    lines = path.read_text().splitlines()

    try:
        title = next(line[2:].strip() for line in lines if line.startswith("# "))
    except StopIteration as exc:
        raise ValueError(f"missing title in {path}") from exc

    try:
        entries_index = lines.index("## Entries")
    except ValueError as exc:
        raise ValueError(f"missing '## Entries' section in {path}") from exc

    description = next(
        (
            line.strip()
            for line in lines[1:entries_index]
            if line.strip()
            and not line.startswith("#")
            and not line.startswith("```")
            and not line.startswith("- [")
        ),
        "",
    )

    raw_entry_lines = lines[entries_index + 1 :]
    while raw_entry_lines and not raw_entry_lines[0].strip():
        raw_entry_lines.pop(0)
    while raw_entry_lines and not raw_entry_lines[-1].strip():
        raw_entry_lines.pop()

    count = sum(1 for line in raw_entry_lines if line.startswith("- ["))

    rendered: list[str] = []
    previous_blank = False
    for line in raw_entry_lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("<!--"):
            if rendered and not previous_blank:
                rendered.append("")
                previous_blank = True
            continue
        if line.startswith("### ") or line.startswith("- ["):
            rendered.append(line)
            previous_blank = False

    while rendered and not rendered[-1].strip():
        rendered.pop()

    if count == 0:
        rendered = ["_No direct Jev examples added yet._"]

    return Category(
        filename=filename,
        title=title,
        description=description,
        count=count,
        lines=rendered,
    )


ENTRY_RE = re.compile(
    r"^- \[([^\]]+)\]\((https?://[^)]+)\)\s*[—-]\s*(.+)$"
)


def github_repo(url: str) -> str | None:
    match = re.fullmatch(r"https://github\.com/([^/]+)/([^/#?]+)/?", url)
    if not match:
        return None
    return f"{match.group(1)}/{match.group(2)}"


def entry_teaser(description: str, max_words: int = 14) -> str:
    domain, separator, detail = description.partition(":")
    if not separator:
        words = description.split()
        return description if len(words) <= max_words else " ".join(words[:max_words]) + "…"

    detail_words = detail.strip().split()
    if len(detail_words) > max_words:
        detail = " ".join(detail_words[:max_words]).rstrip(",;:.—-") + "…"
    else:
        detail = detail.strip()
    return f"{domain.strip()} — {detail}"


def entry_details(line: str) -> list[str]:
    match = ENTRY_RE.match(line)
    if not match:
        return [line]

    name, url, description = match.groups()
    repo = github_repo(url)
    badge = (
        f' <img src="https://badgen.net/github/stars/{repo}" height="14" alt="GitHub stars"/>'
        if repo
        else ""
    )
    link_label = "View Repository" if repo else "View Source"

    return [
        "<details>",
        f'  <summary><b>{escape(name)}</b>{badge} - <i>{escape(entry_teaser(description))}</i></summary>',
        "  <blockquote>",
        f"    {description}",
        "    <br><br>",
        f'    <a href="{url}">🔗 <b>{link_label}</b></a>',
        "  </blockquote>",
        "</details>",
        "",
    ]


def category_details(category: Category) -> list[str]:
    lines = [
        "<details>",
        f"<summary><b>{category.title}</b></summary>",
        "<br>",
        "",
        category.description,
        "",
    ]

    for line in category.lines:
        if not line.strip():
            continue
        if line.startswith("- ["):
            lines.extend(entry_details(line))
        else:
            lines.extend([line, ""])

    while lines and not lines[-1].strip():
        lines.pop()
    lines.extend(["", "</details>", ""])
    return lines


def group_details(group: dict[str, object], categories: dict[str, Category]) -> list[str]:
    lines = [
        f'<div id="{group["id"]}"></div>',
        "",
        "<details open>",
        f'<summary><strong>{group["title"]}</strong></summary>',
        "<br>",
        "",
        str(group["description"]),
        "",
    ]

    for section_title, filenames in group["sections"]:
        if section_title:
            lines.extend([f"### {section_title}", ""])
        for filename in filenames:
            category = categories[filename]
            if category.count == 0:
                continue
            lines.extend(category_details(category))

    lines.extend(["</details>", "", "<br>", ""])
    return lines


def check_duplicates(categories: dict[str, Category]) -> list[tuple[str, list[str]]]:
    """Find entries whose primary source URL appears in more than one category."""
    url_map: dict[str, list[str]] = {}
    for category in categories.values():
        for line in category.lines:
            if not line.startswith("- ["):
                continue
            m = re.search(r"\((https?://[^)\s]+)\)", line)
            if m:
                key = m.group(1).lower().rstrip("/")
                url_map.setdefault(key, []).append(category.filename)
    return [(url, files) for url, files in url_map.items() if len(files) > 1]


def build_readme() -> str:
    categories = {filename: parse_category(filename) for filename in ALL_FILES}

    duplicates = check_duplicates(categories)
    if duplicates:
        print("⚠️  WARNING: duplicate sources detected:")
        for url, files in duplicates:
            print(f"    {url} appears in {', '.join(files)}")
        print()

    out: list[str] = [
        "<!-- Generated by scripts/build-readme.py. Edit category files, then rebuild README. -->",
        "<!-- HEADER -->",
        '<div align="center">',
        "",
        "<h1>Awesome Jev</h1>",
        "",
        "<p>",
        '<a href="https://github.com/sindresorhus/awesome"><img src="https://awesome.re/badge.svg" height="28" alt="Awesome" /></a>',
        "&nbsp;&nbsp;",
        '<a href="https://github.com/yibie/awesome-jev"><img src="https://img.shields.io/badge/upstream-yibie%2Fawesome--jev-555?logo=github" height="28" alt="Upstream yibie/awesome-jev" /></a>',
        "</p>",
        "",
        '<h3>A curated list of projects, integrations, research, and resources built around <a href="https://typesafe.ai/">Jev</a>.</h3>',
        "<p>Jev turns unstructured state plus a <strong>typed question</strong> into a <strong>typed decision</strong> with confidence.</p>",
        "",
        "[**USE CASES**](#use-cases) • [**SDKs & INTEGRATIONS**](#sdks-integrations) • [**RESEARCH & EVALUATION**](#research-evaluation) • [**GUIDES & COMMUNITY**](#guides-community)",
        "",
        "<hr>",
        "</div>",
        "",
        "Browse by **what Jev does** first. Use cases are grouped by reusable decision pattern and application domain; integration tooling, research, and learning resources are kept separate.",
        "",
        "> [!WARNING]",
        "> **Inclusion is not endorsement.** Entries are checked for public, concrete Jev usage — not code quality, security, maturity, reproducibility, or licensing. See [CONTRIBUTING.md](CONTRIBUTING.md) for the curation rules.",
        "",
    ]

    for group in CATEGORY_GROUPS:
        out.extend(group_details(group, categories))

    out.extend(
        [
            '<div id="curation"></div>',
            "",
            "<details>",
            "<summary><strong>🔎 CURATION</strong></summary>",
            "<br>",
            "",
            "An entry should be public, citable, and show Jev (or a documented Jev-style derivative) making a concrete typed decision.",
            "",
            "- Prefer a real request carrying typed questions and a parsed answer coming back.",
            "- Keep each entry to one sentence: scenario + typed decision + useful outcome.",
            "- Treat reported accuracy, latency, cost, and volume as source claims unless independently reproduced.",
            "- Treat bulk, same-scaffold releases as leads rather than evidence of maturity.",
            "",
            "Before adopting a project, check whether it actually calls Jev, has a runnable example or demo, supports any numbers it reports, and has a license that permits your use.",
            "",
            "</details>",
            "",
            "<br>",
            "",
            '<div align="center">',
            "<h3>🤝 Contributing</h3>",
            "Found a useful Jev project or resource?<br>",
            '<a href="CONTRIBUTING.md"><b>Submit a pull request</b></a> or open an issue if an existing entry is wrong.',
            "<br><br>",
            '<sub>README generated from the category files · Released under the <a href="LICENSE">MIT License</a>.</sub>',
            "</div>",
            "",
        ]
    )

    return "\n".join(out)


def main() -> None:
    README_PATH.write_text(build_readme())


if __name__ == "__main__":
    main()
