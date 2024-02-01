### GitHub Actions Cheat Sheet

#### Basics:

- **Workflow File:** Stored in `.github/workflows/` directory of your repository as YAML files.
- **Trigger Events:** Defined using `on` keyword.
  ```yaml
  on:
    push:
      branches:
        - main
    pull_request:
      branches:
        - main
  ```

#### Jobs:

- **Jobs:** Defined under the `jobs` keyword.
- **Runner:** Specifies the environment for the job.
  ```yaml
  jobs:
    build:
      runs-on: ubuntu-latest
  ```

#### Steps:

- **Steps:** Defined under the `steps` keyword within a job.
- **Name:** Describes the purpose of each step.
- **Run:** Specifies the command or action to be executed.
  ```yaml
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - name: Set up Python 
        uses: actions/setup-python@v3

        - name: Install Dependencies
        run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt
            
        - name: Run Tests
        run: |
            python manage.py test
  ```

#### Actions:

- **Reuse Code:** Use existing GitHub Actions using the `uses` keyword.
  ```yaml
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - name: Checkout Repository
          uses: actions/checkout@v2
  ```

#### Environments:

- **Environment Variables:** Define environment variables using the `env` keyword.
  ```yaml
  env:
    MY_VARIABLE: "value"
  ```

#### Secrets:

- **Secrets:** Store sensitive information securely.
  ```yaml
  env:
    API_KEY: ${{ secrets.API_KEY }}
  ```

#### Conditional Execution:

- **If Statement:** Execute a step based on a condition.
  ```yaml
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - name: Run on Push to Main
          if: github.event_name == 'push' && github.ref == 'refs/heads/main'
          run: echo "This step runs only on push to main branch."
  ```

#### Notifications:

- **Notifications:** Receive notifications on workflow status.
  ```yaml
  on:
    push:
      email:
        recipients:
          - user@example.com
  ```
