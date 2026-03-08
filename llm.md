# Context for Future LLMs

## User Goal
The user (Yashas, see: www.yashas-dev.com) aims to achieve **mastery of Python** to a degree where they can compete with LLMs in code generation and understanding.

## Project Structure & Status
- **`style-guide.md`**: Mandatory standards for all code (LLM & Human readable).
- **`Beginner/tasks.md`**: 40 granular tasks for the Beginner tier.
- **`Roadmap/`**: Tiered roadmaps from Beginner to God.
- **`Projects/projects.md`**: 100 domain-specific projects.
- **Current Status**: Beginner tasks mostly done. Skipped Section 7 (PEP 8 & Code Style) for now. Moved to Projects.
- **Completed Projects**: Cloud Project 1 (S3 File Uploader), Cloud Project 2 (EC2 Instance Lister), Cloud Project 3 (IAM User Auditor).
- **Active Task**: Cloud Project 4 (Cloud Storage Space Checker).
- **Completed Beginner Tasks**: All of Section 1, 2, and 6 (6.1–6.10). Section 7 skipped.
- **Next After Project**: Resume Section 7 (PEP 8 & Code Style) or continue with Cloud Project 3.

## Operational Instructions
1. **Strict Style Enforcement:** Any code that does not strictly follow `style-guide.md` is considered **incorrect**. You MUST flag style violations as errors.
2. **Brevity:** Keep responses **under 5 lines** unless the user asks for code/deep dive.
2. **Workflow (User-Led):** 
   - LLM provides a `.py` template containing ONLY I/O, Syntax, Examples (in docstrings), and `# TODO` comments.
   - LLM MUST NOT provide any code stubs (no `def`, `if __name__ == "__main__":`, etc.).
   - User writes the actual code from scratch.
   - LLM reviews code against `style-guide.md` only when asked.
3. **Zero Code Stubs:** Templates must be pure documentation and TODOs. Never provide skeleton functions or logic unless the user is stuck.
4. **Style Adherence:** All templates and code reviews MUST follow `style-guide.md`.

## Next Steps
1. Complete all 40 tasks in `Beginner/tasks.md`.
2. Move to Beginner Projects in `Projects/projects.md` (Domain: TBD).
3. Update `start.md` after completing each tier.
