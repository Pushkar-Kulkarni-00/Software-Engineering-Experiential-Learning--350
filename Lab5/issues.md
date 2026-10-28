# Static Code Analysis — Issues Found

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe use of `eval()` | Security — High | 37 | Evaluates a user-supplied expression, potentially allowing arbitrary code execution. | Replace expression evaluation with a predefined, validated GPA calculation. |
| Hardcoded portal token | Security — High | 52 | A secret is embedded in source code and printed to the terminal. | Read the token from an environment variable and never print its value. |
| Unsafe shell command | Security — Medium | 47–49 | `os.system()` executes a shell command containing a filename. | Remove the shell command and use Python file operations. |
| Mutable default argument | Bug / Maintainability | 15 | `grade_list=[]` creates a shared mutable default across calls. | Use `None` as the default and initialize a new list when needed. |
| Bare exception handler | Reliability | 25–27 | `except:` suppresses all exceptions, hiding errors and invalid student IDs. | Validate inputs and catch specific exceptions where necessary. |
| Unused `grace_marks` | Code quality | 31 | The variable is assigned but never used, so the apparent grace-mark policy has no effect. | Implement the intended policy or remove the variable. |
| Weak hash for security-sensitive use | Security | 42 | MD5 is unsuitable for security-sensitive hashing. | Use a modern cryptographic hash if a secure digest is required; otherwise document the hash's non-security purpose. |
| Resource handling | Reliability | 47–49 | The file is opened and closed manually, so exceptions may prevent proper closure. | Use a `with open(...)` context manager. |

**Note:** Line numbers refer to the supplied version and may change after edits. Confirm the findings against the actual reports before final submission.