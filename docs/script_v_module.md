# Programming models in Python: An outline for clarification of some confusing options

How should you implement or program a model in Python?
Here are three options.

1. Script
    * Everything in a single `.py` file (a script)
    * Model may be written with or without functions
    * Simple and quick
    * Not very modular or reusable
2. Module
    * Model is defined using functions in a `.py` file (a module)
    * The model module must then be imported for use
    * Model could be used interactively or in a second `.py` file (a script)
    * Better organized, clearer, more modular than option 1
3. Package
    * Model is defined within multiple modules 
    * Good for organizing complicated models or projects
    * Not used in this course
