from cx_Freeze import setup, Executable

setup(
    name= "labyrinth",
    version = "0.1",
    description = "n'affiche qu'une petite phrase...",
    executables = [Executable("main.py")]
)