# `linear-equation-solver-using-python`

CLI tool to solve linear equations AX = B using `NumPy` and matrix algebra with `Rich` -styled output.

---

## 🐙 How This Project Works

This program solves a system of linear equations AX = B using matrix algebra. If A is invertible, it computes X = A⁻¹ × B, otherwise it reports infinite or no solutions. Calculations use NumPy, and output is displayed via Rich.

## 🛠️ Tools And Tech Used

<p align="left">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" width="60">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-original.svg" width="60">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bash/bash-original.svg" width="60">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg" width="60">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original-wordmark.svg" width="60">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original.svg" width="60">
</p>

---

## 📊 Features

- Input coefficient matrix `A`, variable matrix `X`, and constant matrix `B`.
- Solve equations using : `X = A⁻¹ × B`

- Detect if the system has:
- A **unique solution**
- **Infinite solutions**
- **No solution**
- Pretty CLI outputs with **Rich** library (progress bars, styled messages).
- Automatic determinant and solution calculation using **NumPy**.

- Detect if the system has:
- `UNIQUE SOLUTION`
- `INFINITE SOLUTIONS`
- `NO SOLUTIONS`
- Pretty CLI outputs with `Rich` library (progress bars, styled messages).
- Automatic determinant and solution calculation using `NumPy`.

---

## 🛸 Project Requirements

- Python 3.8+
- NumPy (Python Library) [more about `NumPy`](https://numpy.org/)
- Rich (Python Library) [more about `rich`](https://rich.readthedocs.io/en/stable/index.html#)

---

## 🏗️ How to Run

### 1. Clone The Project Repository In Your Desired Location (example : here `Desktop`)

```bash
cd Desktop
git clone <repo_url>
```

### 2. Navigate To The Project Repository

```bash
cd linear-equation-solver
```

### 3. Create a virtual environment

```bash
python3 -m venv venv # create the virtual environment venv
```

### 4. Activate The Virtual Environment

```bash
source venv/bin/activate   # mac or linux
venv\Scripts\activate      # windows
```

### 5. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 6. Run The Project

```bash
python solver.py
```

---

## 🪪 LICENSE

## This Project is licensed under MIT license.

---

## Tests

```
1x + 1y + 1z = 6
0x + 2y + 5z = -4
2x + 5y - 1z = 27

x = 5
y = 3
z = -2
```

```
1x + 1y + 1z = 3
2x + 2y + 2z = 6
1x - 1y + 1z = 2

EITHER INFINITE SOLUTIONS OR NO SOLUTIONS
```
