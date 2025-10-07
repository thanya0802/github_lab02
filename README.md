# LAB02-Github

This lab focuses on 5 modules, which includes creating a virtual environment, creating a GitHub repository, creating Python files, creating test files using pytest and unittest, and implementing GitHub Actions.




## Step 1: Creating a Virtual Environment

In software development, it's crucial to manage project dependencies and isolate your project's environment from the global Python environment. This isolation ensures that your project remains consistent, stable, and free from conflicts with other Python packages or projects. To achieve this, we create a virtual environment dedicated to our project. <br>
<br>
To create a virtual environment, follow these steps:

1. Open a Command Prompt or Terminal in the directory where you want to create your project.
2. Choose a name for your virtual environment (e.g "lab_01") and run the appropriate command:
    ```
    python -m venv lab_01
    ```
3. Activate the virtual environment
    ```
    lab01\Scripts\activate
    ```
After activation, you will see the virtual environment's name in your command prompt or terminal, indicating that you are working within the virtual environment.


## Step 2: Creating a GitHub Repository, Cloning and Folder Structure
Now that we have set up our virtual environment, the next step is to create a GitHub repository for our project and establish a structured folder layout. This organization helps maintain your project's code, data, and tests in an organized manner.

### Creating a GitHub Repository
- Open a web browser and go to GitHub.
- In the upper right corner, click the "+" button and select "New repository."
- Choose a name for your repository.
- Choose the visibility of your repository—either public (visible to everyone) or private (accessible only to selected collaborators)
- Check the "Initialize this repository with a README" box. This will create an initial README file that you can edit to provide project documentation.
- Click the "Create repository" button.

### Cloning the Repository
- Open a Command Prompt or Terminal.
- Navigate to the directory where you want to clone your GitHub repository. This should be the same directory where you created your virtual environment.
- Run the following command to clone your GitHub repository into the current directory:
    ```
    git clone <repository_url>
    ```
- Replace <repository_url> with the URL of your GitHub repository. You can find this URL on your GitHub repository's main page.
After running the command, the repository will be cloned, and you'll have a local copy of your GitHub project in your chosen directory.

### Establishing Folder Structure
- Once you have cloned yor repository, you can establish a structured folder layout within it. This layout helps organize your project into key directories for code, data, and tests. Create the following subfolders within your repository: <br>
- data: This folder is used for storing project data files or datasets. <br>
- src: This folder is where you'll store your project's source code files. <br>
- test: This folder is dedicated to unit tests and test scripts for your code. <br>
- Create a file named .gitignore. This is useful to exclude the virtual environment and other unnecessary files from version control.
- Add the virtual environment folder name inside your gitignore file so that its not tracked by Git.

### Adding and Pushing Your Project Code to GitHub
Now that we have our virtual environment set up, the GitHub repository created, and the folder structure organized, let's add our project's code and push it to GitHub. 

**Adding Your Project Code** <br>
- Navigate to your project directory using the Command Prompt or Terminal, where you have the virtual environment and folder structure set up.
- Create and write your Python code or other project files within the specified directories (src, data, etc.) according to your project requirements.
- Once your project files are ready, it's time to add them to Git's staging area. In your project directory, run the following command:
    ```
    git add .
    ```
- This command stages all the changes and new files in your project directory for the next commit.

**Committing Your Changes** <br>
- After staging your changes, commit them with a meaningful commit message that describes the changes you made. Replace <your_commit_message> with a descriptive message:
    ```
    git commit -m "<your_commit_message>"
    ```

**Pushing to GitHub** <br>
- To push your committed changes to your GitHub repository, use the following command:
    ```
    git push origin main
    ```
## Step 3: Creating string_processor.py in src Folder
- In this step, we create a Python script named string_processor.py within the src folder of your project. This script implements basic string operations such as:
- to_uppercase(text) converts input string to uppercase.
- to_lowercase(text) converts input string to lowercase.
- count_vowels(text) counts vowels (a,e,i,o,u) in the string.
- reverse_string(text) returns the reversed string.


## Step 4: Creating tests using Pytest and Unittests
- In this step, we'll set up unit tests for the functions in our calculator.py script using two popular testing frameworks: [pytest](https://docs.pytest.org/en/7.4.x/) and [unittest](https://docs.python.org/3/library/unittest.html). Unit testing ensures that individual components of your code work as expected, helping you catch and fix bugs early in the development process.

**Using Pytest** <br>
- Installation (if not already installed):
- If you haven't already installed pytest, you can do so using pip:
    ```
    pip install pytest
    ```
### Writing Pytest Tests
- Pytest makes it easy to write tests for your Python code. Tests are written as regular Python functions, and test file names typically start with test_ or end with _test.py.
- To run your Pytest tests, you can use the pytest command followed by the name of the test file or directory containing your tests:
    ```
    pytest test_sample.py
    ```
- Pytest automatically discovers test functions based on naming conventions. It searches for functions starting with test_ or ending with _test, and it can discover tests in subdirectories as well. This makes it easy to organize your tests.
- Pytest supports parametrized tests, which allow you to run the same test function with multiple sets of inputs and expected outputs. This is particularly useful for testing functions with different input scenarios. Please refer the commented out code in the test_pytest.py file for your reference.
- Let's create a test file named test_pytest.py within the test folder. This file will contain a series of test functions, each aimed at verifying the behavior of specific functions within calculator.py.
- We've prepared four test functions (test_fun1, test_fun2, test_fun3, and test_fun4) to test the functions within calculator.py. Each test function uses the assert statement to validate the expected outcomes. Refer the file under test folder for your [reference](https://github.com/raminmohammadi/MLOps/blob/main/Github_Labs/Lab1/test/test_pytest.py).
- By running these pytest tests, you can verify that your calculator functions are working correctly.

### Writing Tests with UnitTest
- Unittest allows you to write tests as classes that inherit from the unittest.TestCase class. Test methods are identified by their names, which must start with "test_" to be recognized as test cases.
- To run Unittest tests, you typically execute your test script, which should include a call to unittest.main() at the end. Here's how you can run the tests:
    ```
    python test_sample.py
    ```
- Unittest relies on test discovery, which means it will find test methods based on naming conventions, similar to Pytest. Test methods must start with "test_" to be recognized as test cases.
- Unittest provides a variety of assertion methods, such as assertEqual, assertTrue, assertFalse, and others, to check conditions in your tests. You can choose the assertion method that best suits your testing needs.
- Let's create a test file named test_unittest.py within the test folder. This file will contain a series of test functions, each aimed at verifying the behavior of specific functions within calculator.py.
- We've prepared four test functions (test_fun1, test_fun2, test_fun3, and test_fun4) to test the functions within calculator.py. Each test function uses the self.assertEqual statement to validate the expected outcomes. Refer the file under test folder for your [reference](https://github.com/raminmohammadi/MLOps/blob/main/Github_Labs/Lab1/test/test_unittest.py).
- By running these unittest tests, you can verify that your calculator functions are working correctly.

## Step 5. Implementing GitHub Actions
- GitHub Actions is a powerful automation and CI/CD (Continuous Integration/Continuous Deployment) platform provided by GitHub. It enables you to automate various workflows and tasks directly within your GitHub repository. GitHub Actions can be used for a wide range of purposes, such as running tests, deploying applications, and automating release processes.

**How GitHub Actions Work:** <br>

- GitHub Actions work based on events, actions, and triggers:
- **Events:** These are specific activities that occur within your GitHub repository, such as code pushes, pull requests, or issue comments. GitHub Actions can respond to these events.
- **Actions:** Actions are individual tasks or steps that you define in a workflow file. These tasks can be anything from building your code to running tests or deploying your application.
- **Triggers:** Triggers are conditions that cause a workflow to run. They can be based on events (e.g., a new pull request) or scheduled to run at specific times.

**The Purpose of GitHub Actions:** <br>

- GitHub Actions serves several purposes:
- **Automation:** It automates repetitive tasks, reducing manual effort and ensuring consistency in your development process.
- **Continuous Integration (CI):** It allows you to set up CI pipelines to automatically build, test, and validate your code changes whenever new code is pushed to the repository.
- **Continuous Deployment (CD):** It enables automatic deployment of your application when changes are merged into a specific branch, ensuring a smooth and reliable release process.

### Using Pytest and Unittest with GitHub Actions:
- Integrating Pytest and Unittest with GitHub Actions can significantly improve the quality and reliability of your codebase. Here's how:
- Pytest with GitHub Actions: You can create a GitHub Actions workflow (e.g., pytest_action.yml) that specifies the steps for running your Pytest tests. When events like code pushes or pull requests occur, GitHub Actions will automatically trigger the workflow, running your Pytest tests and reporting the results back to you. This helps you catch bugs and ensure that your code meets quality standards early in the development process.
- Unittest with GitHub Actions: Similarly, you can create a separate GitHub Actions workflow (e.g., unittest_action.yml) to run your Unittest tests. This ensures that both your Pytest and Unittest suites are executed automatically whenever code changes are made or pull requests are submitted. It provides a robust validation mechanism for your codebase.
- When collaborating in teams, the automated testing process ensures that all test cases pass successfully before allowing the merge of a pull request into the main branch.

### Creating GitHub Actions Workflow Files:
- To implement Pytest and Unittest with GitHub Actions, you'll create two workflow files under the .github/workflows directory in your repository: pytest_action.yml and unittest_action.yml. These workflow files define the specific actions and triggers for running your tests.

**pytest_action.yml** <br>
Please refer [this](https://github.com/raminmohammadi/MLOps/blob/main/Github_Labs/Lab1/workflows/pytest_action.yml) file for your reference
1. Workflow Name: The workflow is named "Testing with Pytest."
2. Event Trigger: It specifies the event that triggers the workflow. In this case, it triggers when code is pushed to the main branch.
3. Jobs: The workflow contains a single job named "build," which runs on the ubuntu-latest virtual machine environment.
4. Steps:
- Checkout code: This step checks out the code from the repository using actions/checkout@v2.
- Set up Python: It sets up the Python environment using actions/setup-python@v2 and specifies Python version 3.8.
- Install Dependencies: This step installs the project dependencies by running pip install -r requirements.txt.
- Run Tests and Generate XML Report: The core testing step runs Pytest with the --junitxml flag to generate an XML report named pytest-report.xml. The continue-on-error: false setting ensures that the workflow will be marked as failed if any test fails.
- Upload Test Results: In this step, the generated XML report is uploaded as an artifact using actions/upload-artifact@v2. The name of the artifact is "test-results," and the path to the report is specified as pytest-report.xml.
- Notify on Success and Failure: These two steps use conditional logic to notify based on the outcome of the tests.
- if: success() checks if the tests passed successfully and runs the "Tests passed successfully" message.
- if: failure() checks if the tests failed and runs the "Tests failed" message.

**unittest_action.yml** <br>
 Please refer [this](https://github.com/raminmohammadi/MLOps/blob/main/Github_Labs/Lab1/workflows/unittest_action.yml) file for your reference
1. Workflow Name: This GitHub Actions workflow is named "Python Unittests."
2. Event Trigger: The workflow is triggered by the "push" event, specifically when changes are pushed to the main branch.
3. Jobs: The workflow defines a single job named "build" that runs on the ubuntu-latest virtual machine environment.
4. Steps:
- Checkout code: This step uses the actions/checkout@v2 action to check out the code from the repository. It ensures that the workflow has access to the latest code.
- Set up Python: The "Set up Python" step uses the actions/setup-python@v2 action to configure the Python environment. It specifies that Python version 3.8 should be used.
- Install Dependencies: This step runs the command pip install -r requirements.txt to install the project's Python dependencies. It assumes that the project's dependencies are listed in the requirements.txt file.
- Run unittests: In this step, the unittest tests are executed using the command python -m unittest test.test_unittest. It runs the unittest test suite defined in the test.test_unittest module.
- Notify on success: This step uses conditional logic with if: success() to check if all the unittest tests passed successfully. If they did, it runs the message "Unit tests passed successfully."
- Notify on failure: Similarly, this step uses conditional logic with if: failure() to check if any of the unittest tests failed. If any test failed, it runs the message "Unit tests failed."


# LAB2 – MLOps (IE-7374)

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

## Step 3 — Creating `string_processor.py` in the src Folder

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


