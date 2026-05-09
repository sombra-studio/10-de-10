# Compilation mode, support OS-specific options
# nuitka-project: --mode=standalone

# Set variables dynamically and use them later, e.g., for Windows metadata
# nuitka-project-if: {OS} == "Windows":
#    nuitka-project-set: MY_VERSION = __import__("line-game").__version__
#    nuitka-project: --file-version={MY_VERSION}
#    nuitka-project: --windows-icon-from-ico={MAIN_DIRECTORY}/assets/imgs/line-game-logo.png

# nuitka-project-if: {OS} == "Darwin":
#    nuitka-project: --macos-app-icon={MAIN_DIRECTORY}/assets/imgs/line-game-logo.png
#    nuitka-project: --include-frameworks=AppKit,CoreVideo,CoreFoundation,OpenGL,QuartzCore

# nuitka-project: --product-name="10 de 10"
# nuitka-project: --include-data-dir={MAIN_DIRECTORY}/assets=.
# nuitka-project: --include-data-dir={MAIN_DIRECTORY}/locales=.
# nuitka-project: --include-package-data=pudu_ui

# Don't depend on tkinter
# nuitka-project: --nofollow-import-to=tkinter
# nuitka-project: --nofollow-import-to=_tkinter

# Other dependencies we don't want
# nuitka-project: --nofollow-import-to=unittest
# nuitka-project: --nofollow-import-to=pydoc

from app import GameApp


if __name__ == '__main__':
    app = GameApp()
    app.run()
