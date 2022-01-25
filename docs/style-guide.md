# Project Style Guide

## Requirements

- [Visual Studio Code]
- [Node.js] >= v14.x

## Overview

The workflow is the following:

- VS Code shows style issues after saving Python files.
  - Issues are reported by `flake8` because `black` does not provide this
    service. However, this feature is of limited use because `black` fixes most
    style issues upon saving files.
- VS Code automatically fixes style issues when saving files.
  - Manually lint all files with `npm run lint`.
  - Manually fix all style issues with `npm run lint:fix`.
- The style of staged files is validated upon creating a new commit.
- The style of files pushed to GitHub is validated using a GitHub workflow.

## Examples

Sucessful validation of the style when creating a commit:

```console
$ git commit -S -m 'Fix issue and commit again'

> lint-staged
> lint-staged

✔ Preparing lint-staged...
✔ Running tasks for staged files...
✔ Applying modifications from tasks...
✔ Cleaning up temporary files...
[add-style-guide-and-tools 2861202] Fix issue and commit again
 2 files changed, 31 insertions(+), 5 deletions(-)
```

Failed validation of the style when creating a commit:

```console
$ git commit -S -m 'Test automated linter before commit'

> lint-staged
> lint-staged

✔ Preparing lint-staged...
⚠ Running tasks for staged files...
  ❯ package.json — 1 file
    ❯ server/**/*.py — 1 file
      ✖ npm run lint [FAILED]
↓ Skipped because of errors from tasks. [SKIPPED]
✔ Reverting to original state because of errors...
✔ Cleaning up temporary files...

✖ npm run lint:
would reformat /home/tschaffter/dev2/sage-bionetworks/rocc/rocc-service/server/openapi_server/__main__.py
would reformat openapi_server/__main__.py
Oh no! 💥 💔 💥
2 files would be reformatted, 31 files would be left unchanged.

> lint
> cd server && black --check openapi_server/ --exclude 'openapi_server/(models|test)' "/home/tschaffter/dev2/sage-bionetworks/rocc/rocc-service/server/openapi_server/__main__.py"

husky - pre-commit hook exited with code 1 (error)
```

## Setup

- VS Code invites you to install the recommended extensions required to validate
  and fix style issues.
- Install `flake8`, `black` and other development Python packages.

      pip install -r server/dev-requirements.txt

## Why using `npm` in a Python project

- Standardize scripts across projects developed with different programming
  languages/frameworks.
    - Examples: `npm test`, `npm run lint`, `npm run release`.
- Development tools such as [OpenAPI Generator] (server and client projects) and
  [release-it] are available via `npm`.

## Markdown

- Lines must not be longer than 80 characters. To rewrap text, place your cursor
  in a paragraph or highlight multiple paragraph and press `ALT+Q` provided by
  the VS Code extension `stkb.rewrap`.

<!-- Links -->

[husky]: https://www.npmjs.com/package/husky
[stage-lint]: https://www.npmjs.com/package/lint-staged
[Visual Studio Code]: https://code.visualstudio.com/
[Node.js]: https://nodejs.org/en/
[OpenAPI Generator]: https://www.npmjs.com/package/@openapitools/openapi-generator-cli
[release-it]: https://www.npmjs.com/package/release-it