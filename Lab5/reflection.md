# Reflection — Static Code Analysis

## 1. What is static code analysis?

Static code analysis examines source code without executing it. Pylint checks code quality and potential logical problems, Flake8 checks formatting and PEP 8 compliance, and Bandit identifies common security risks.

## 2. What issues did you identify?

The original program contained unsafe use of `eval()`, a hardcoded portal token, a shell command constructed using a filename, a mutable default argument, a bare exception handler, and unused code. These problems affected security, reliability, and maintainability.

## 3. How did you fix the issues?

I replaced dynamic expression evaluation with direct GPA calculation, moved the token to an environment variable, removed shell execution, changed the mutable default argument to `None`, removed broad exception suppression, and used a context manager for file operations. I also replaced the PIN generator with Python's `secrets` module.

## 4. What did you learn from static analysis?

I learned that code can produce the expected output while still containing security vulnerabilities and maintainability problems. Running multiple tools provides complementary feedback, but their findings still require human review. Rerunning the tools after changes helps verify that the reported issues have been addressed.
