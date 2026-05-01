uv run python -m nuitka \
      --include-data-dir=./assets=. \
      --include-data-dir=./locales=. \
      --include-package-data=pudu_ui \
      --product-name="10 de 10" \
      --product-version="1.0.0" \
      --onefile \
      --windows-icon-from-ico=./assets/imgs/line-game-logo.png \
      main.py
