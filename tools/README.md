# Reproduce contribution 001

Follow [AGENTS.md](../AGENTS.md). Use the repository-specific OrbStack container and persistent workspace.

```sh
docker --context orbstack exec security-executive-briefs-dev python tools/verify.py --output /workspaces/security-executive-briefs/work/check
```

AI and post-quantum repositories require their hash-locked optional runtime, described in contribution 001. Final verification runs use the same pinned Python image with the workspace mounted read-only and external networking disabled. Output goes to disposable `/tmp` and is transferred back to `evidence/`. No credentials or Docker socket are mounted.
