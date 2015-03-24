from cx_Freeze import setup, Executable

setup(
    name = "security",
    version = "0.1",
    description = "Security",
    executables = [Executable("logs.py")]
)