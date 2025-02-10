# Quorum Coding Challenge

## Question 1. Discuss your strategy and decisions implementing the application. Please, consider time complexity, effort cost, technologies used, and any other variable that you understand important in your development process.

The choice of **Django** and **Django REST Framework** ensures efficient time complexity management. Django's ORM abstracts away the complexities of SQL queries, which can be further optimized as needed. DRF's serializers handle data conversion efficiently, reducing development effort.

Django's built-in testing framework offers a comprehensive and integrated solution for writing and running tests.

For the database, **SQLite3** was chosen due to its lightweight and file-based characteristics. While not ideal for highly concurrent production environments, it is perfect for development and testing due to its simplicity and ease of setup.

The use of **drf-spectacular** simplifies API documentation by automating the documentation process, reducing manual effort and ensuring consistency.

On the UI, **Tailwind CSS** streamlines the styling process, enabling rapid prototyping and a consistent design without extensive custom CSS.

**Autopep8**, **Mypy**, and **Pylint** were used to enhance code quality by enforcing consistent formatting, catching type errors early, and identifying potential code issues

---

## Question 2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?

### On `quorum_app`:

1. **Modify the Models**
   - Add "Co-Sponsor" to the `Bill` model as a `ManyToManyField`.
   - Add "Bill Voted On Date" to the `Vote` model as a `DateTimeField`.

2. **Generate and Apply Migrations**
   
   ```bash
   python manage.py makemigrations quorum_app
   python manage.py migrate quorum_app
   ```

3. **Update the Serializers**
   - Modify the existing serializer to include the new fields.

### On `quorum_app_ui`:

1. **Update the Templates**
   - Adjust the templates to display the newly added fields appropriately.

---

## Question 3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?

### 1. Loading Data via `load_data.py` Script

The `load_data.py` script implements the Strategy Pattern, allowing different data-loading algorithms to be defined, encapsulated, and made interchangeable.

- The currently implemented algorithm is `StdLibCSVDataSource`, which utilizes the `csv` module from the Python Standard Library.
- `PandasCSVDataSource`, `PandasJSONDataSource`, and `PandasExcelDataSource` are placeholders for potential future implementations.

**Pros:**
- The script leverages Django models to load data into the database, ensuring that all constraints defined in the models and database tables are applied.
- Any data that fails to load is logged in the `load_data.log` file.

**Cons:**
- Implementing new strategy algorithms may require installing additional modules, adding more dependencies to the project.
- Requires running commands locally on the platform where the application is deployed.

### 2. Loading Data via API Endpoints

This approach utilizes Django REST Framework's `ModelViewSet` to provide CRUD (Create, Read, Update, Delete) operations for application models.

- The current implementation uses token-based authentication to restrict access to the endpoints under `/api/v1/model-view-set/`.

**Pros:**
- Can be accessed by external applications or scripts.
- Does not require running commands locally on the hosting platform.

**Cons:**
- The application or script calling the endpoints must implement error handling and logging.
- Currently, the application does not enforce HTTPS.

---

## Question 4. How long did you spend working on the assignment?

- **Reviewing requirements and planning the implementation:** 1 hour
- **Developing and writing the code:** 4 hours
- **Answering the questions:** 1.5 hours

