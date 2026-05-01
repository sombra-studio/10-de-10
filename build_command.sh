#!/bin/sh
uv run python -m nuitka \
      --include-data-dir=./assets=. \
      --include-data-dir=./locales=. \
      --include-package-data=pudu_ui \
      --product-name="10 de 10" \
      --product-version="1.0.0" \
      main.py
