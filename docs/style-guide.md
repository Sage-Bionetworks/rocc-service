# Project Style Guide

## Requirements

- [Visual Studio Code]
-

## Overview

The workflow is the following:

- VS Code shows immediately style issues when editing Python files.
<!-- - VS Code automatically fix style issues when saving files.
- The style of staged files is validated upon creating a new commit.
- The style of files pushed to GitHub is validated using a GitHub workflow. -->

## Setup

- VS Code invites you to install the recommended extensions, which include
  `dbaeumer.vscode-eslint`. This extension is used in the VS Code workspace
  settings file `settings.json` available in this repository.
- Install `flake8` and other development Python packages.

      pip install -r server/dev-requirements.txt

## Markdown

- Lines must not be longer than 80 characters. To rewrap text, place your cursor
  in a paragraph or highlight multiple paragraph and press `ALT+Q` provided by
  the VS Code extension `stkb.rewrap`.

## References

-

<!-- Links -->

[google typescript style guide]: https://google.github.io/styleguide/tsguide.html
[eslint]: https://www.npmjs.com/package/eslint
[husky]: https://www.npmjs.com/package/husky
[stage-lint]: https://www.npmjs.com/package/lint-staged
[prettier]: https://www.npmjs.com/package/prettier
[Visual Studio Code]: https://code.visualstudio.com/
[Node.js]: https://nodejs.org/en/