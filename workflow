name: CI

on:
  push:
    branches:
      - main  # Adjust the branch name as needed

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8

    - name: Install dependencies
      run: pip install -r requirements.txt  # Adjust the command based on your requirements

    - name: Run tests
      run: |
        python run_tests.py  # Adjust the test command based on your test suite

    - name: Build game
      run: |
        python build_game.py  # Adjust the build command based on your build process

