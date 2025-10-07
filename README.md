
# LAB2 – MLOps

This lab focuses on five core MLOps concepts: creating a virtual environment, managing GitHub repositories, writing modular Python code, testing with Pytest and Unittest, and automating testing using GitHub Actions.

---

## Step 1 — Creating a Virtual Environment

In software development, virtual environments isolate dependencies for each project, ensuring consistency and preventing conflicts between global and project-specific packages.

**To create and activate a virtual environment:**

- Use the command to create:  
  `python -m venv lab_01`
- Activate it:  
  - **macOS/Linux:** `source lab_01/bin/activate`  
  - **Windows:** `lab_01\Scripts\activate`

Once activated, the environment name will appear in your terminal, confirming that you are working inside an isolated environment.

---

## Step 2 — Creating a GitHub Repository and Project Structure

A well-organized structure ensures that code, data, and tests remain clean and maintainable throughout the project.

**Folder structure:**
- `data`: stores datasets or reference files  
- `src`: contains the source code  
- `test`: includes all unit testing scripts  
- `.github/workflows`: holds the automation workflows for testing  
- `requirements.txt`: lists required dependencies  
- `.gitignore`: defines files and folders to be excluded from version control  
- `README.md`: serves as documentation for the project  

**To add and push code to GitHub:**
1. Stage all files using `git add .`
2. Commit changes using `git commit -m "Initial commit"`
3. Push updates using `git push origin main`

---

## Step 3 — Creating string_processor.py in the src Folder

The string processor module includes fundamental string manipulation functions such as:
- Converting strings to uppercase  
- Converting strings to lowercase  
- Counting vowels  
- Reversing strings  

This module demonstrates Python’s basic operations and forms the foundation for testing and automation in later steps.

---

## Step 4 — Creating Tests Using Pytest and Unittest

Testing ensures that each function behaves as expected, improving software quality and reliability.

### **Pytest**
- Pytest allows writing lightweight test functions that automatically discover and validate results.  
- It supports assertions and parametrized testing, enabling multiple test cases with different inputs.

### **Unittest**
- Unittest organizes tests using a class-based structure derived from Python’s standard library.  
- Each test method checks specific functionality using assertion methods like `assertEqual`, `assertTrue`, or `assertFalse`.  
- Running the tests verifies the correctness of the implemented string functions.

---

## Step 5 — Implementing GitHub Actions

GitHub Actions automates testing and validation every time code is pushed to the repository.  
This ensures that the main branch remains stable and that new changes don’t break existing functionality.

### **How GitHub Actions Work**
- **Events:** Actions are triggered when specific activities occur, such as pushing new code or creating a pull request.  
- **Jobs:** Each workflow runs in an isolated environment (like Ubuntu) to perform tasks.  
- **Steps:** These define specific actions such as checking out the code, setting up Python, installing dependencies, and running tests.

### **Purpose**
- **Automation:** Removes the need for manual test execution.  
- **Continuous Integration:** Automatically validates new commits.  
- **Continuous Deployment:** Ensures code is ready for deployment once all tests pass.

---

## Step 6 — Pytest and Unittest Workflows

Two workflows are configured under the `.github/workflows` directory.

### **Pytest Workflow**
- Runs whenever new code is pushed to the main branch.  
- Checks out code, sets up Python 3.8, installs dependencies, runs Pytest, and uploads test reports.  
- Displays messages indicating whether all tests passed or failed.

### **Unittest Workflow**
- Also triggered by pushes to the main branch.  
- Runs Unittest cases defined in the `test_unittest.py` file.  
- Displays notifications for successful or failed test execution.

Both workflows ensure automated quality checks through continuous integration.

---

## Step 7 — Verifying CI/CD Automation

After pushing changes to GitHub:

1. Open the **Actions** tab in your repository.  
2. Observe the two workflows:  
   - **Testing with Pytest**  
   - **Python Unittests**  
3. A green checkmark indicates successful runs, confirming that the automation is functioning correctly.


