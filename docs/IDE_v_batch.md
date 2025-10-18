# Running Python code: An outline for clarification of some confusing options

Once you have a script that runs a model, how should you run it?
Here are the common approaches.

## IDE (integrated development environment) or script editor + console
In this common approach programmers work on a script and run some or all as it is written or edited.
IDEs, or "integrated development environments", are software programs that facilitate this by providing text editing functionality and a way to send script code to a Python interpreter (also called a REPL, for read-evalulate-print loop), which evaluates the code and returns results.
Examples of IDEs: Spyder, Visual Studio Code, PyCharm.
1. Interactive
    * User typically has a script open and sends lines, blocks, or whole file to a console running Python interactively
    * IDEs streamline this with all kinds of shortcuts and features and varying levels of complexity
    * Could be done without an IDE, for example copying lines from a script open in Notepad and pasting them in Command Prompt running Python
2. Batch
    * Run entire file in one step with keyboard shortcut or by clicking button
    * Useful for testing the whole model or script, but during development running only new or edited parts by line, block, or "cell" can be faster and is often more logical

## Console
Examples: Command Prompt, PowerShell, Terminal, Bash
1. Interactive
    * Launch Python interpreter and type code 
    * This interactive usage is also called working in a REPL
    * Fine for throw-away code, like small checks or experiments, but not for any code you should save
2. Batch
    * For running completed scripts
    * Enter e.g., `python3 somescript.py`
    * Common for established code and automated tasks (especially on Linux)
    * Probably not used much in this course but useful once a project is finished
