# pygame-codon
The pygame port for codon.
### Basics
- install codon:
    - https://docs.exaloop.io/codon
- add codon to path:
    - export PATH=....
- add python for codon to path
    - for importing python modules we need to `export CODON_PYTHON=python_path.so` as mentioned in the website.
### Build/Compile
    - for run/compiling dont use 
      - `codon run -release simple.py`
    - instead use
      - `codon build -release -exe simple.py`
because the normal `codon run causes - llvm error` on some devices.
### Run
    `./simple`
