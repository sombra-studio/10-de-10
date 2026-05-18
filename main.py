# --- Build Configuration ---
# nuitka-project: --standalone
# nuitka-project: --product-name="10 de 10"
# nuitka-project: --product-version=1.0.0

# --- Windows ---
# nuitka-project-if: {OS} == "Windows":
#    nuitka-project: --windows-icon-from-ico={MAIN_DIRECTORY}/assets/imgs/line-game-logo.png

# --- macOS ---
# nuitka-project-if: {OS} == "Darwin":
#    nuitka-project: --macos-create-app-bundle
#    nuitka-project: --macos-app-icon={MAIN_DIRECTORY}/assets/imgs/line-game-logo.png

# --- Files & Packages ---
# nuitka-project: --include-data-dir={MAIN_DIRECTORY}/assets=assets
# nuitka-project: --include-data-dir={MAIN_DIRECTORY}/locales=locales
# nuitka-project: --include-package-data=pudu_ui
# nuitka-project: --include-package=pyglet

# --- Exclusions ---
# nuitka-project: --nofollow-import-to=tkinter
# nuitka-project: --nofollow-import-to=_tkinter
# nuitka-project: --nofollow-import-to=unittest
# nuitka-project: --nofollow-import-to=pydoc


from app import GameApp


if __name__ == '__main__':
    app = GameApp()
    app.run()
