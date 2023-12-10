## Release flow

1. push any code changes
2. run `git tag -a v1.0.1 -m "tag description"` with an appropriate incremented version (e.g. `v1.0.1` -> `v1.0.2`) following major versioning. A `latest` tag will be added for you by GitHub.
3. push the tag `git push origin v1.0.1` which triggers an automated builds