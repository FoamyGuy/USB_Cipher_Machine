# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: Copyright 2025 Sam Blenny

.PHONY: help bundle sync tty clean mount umount

# Name of top level folder in project bundle zip file should match repo name
PROJECT_DIR = $(shell basename `git rev-parse --show-toplevel`)

help:
	@echo "build project bundle:         make bundle"

# This is for use by .github/workflows/buildbundle.yml GitHub Actions workflow
# To use this on Debian, you might need to apt install curl and zip.
bundle:
	@mkdir -p build
	python3 bundle_builder.py
