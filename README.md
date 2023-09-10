# Clarify

Command Line application to help make your Python code better by adding comments and docstrings! Powered by Google's PaLM. (Currently Mac/Linux only)

## Setup
### Clone the repository
Clone the repository to your computer by running the following command in your terminal:

```sh
git clone https://github.com/NicholasLe04/Clarify.git
```

### Create the Bash alias
1. cd into the the `Clarify` folder
2. Add an alias to your terminals config file like:
```sh
# for linux
./clarify.sh completion >> ~/.bashrc

# for mac
./clarify.sh completion >> ~/.zshrc
```
3. After doing the above, making a new terminal and typing `clarify` should work.

## How to Use
1. Run ```clarify``` followed by the path to the Python file you wish to clarify (relative to the current directory)

Example:
```sh
clarify ./helloworld.py
```
