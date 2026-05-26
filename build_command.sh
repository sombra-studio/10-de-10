#!/bin/sh
pyinstaller --windowed --noconfirm \
    --add-data="assets:assets" \
    --add-data="locales:locales" \
    --collect-data=pudu_ui \
    --icon=./assets/imgs/line-game-logo.png \
    --name="10 de 10" \
    --onefile \
    main.py
