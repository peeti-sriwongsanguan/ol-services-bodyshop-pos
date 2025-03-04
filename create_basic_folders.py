import os

# Define the project structure
# project_name = "ol-services-bodyshop-pos"
project_structure = [
    "alembic/versions", "alembic/env.py", "alembic/alembic.ini",
    "api/routes/__init__.py", "api/routes/customers.py", "api/routes/vehicles.py", "api/routes/jobs.py",
    "api/routes/insurance.py", "api/routes/inventory.py", "api/routes/invoices.py", "api/routes/documents.py",
    "api/routes/photos.py", "api/routes/users.py", "api/routes/dashboard.py",
    "api/core/__init__.py", "api/core/config.py", "api/core/security.py", "api/core/auth.py", "api/core/i18n.py",
    "api/models/__init__.py", "api/models/base.py", "api/models/user.py", "api/models/customer.py",
    "api/models/vehicle.py",
    "api/models/job.py", "api/models/insurance.py", "api/models/inventory.py", "api/models/document.py",
    "api/models/invoice.py", "api/models/audit.py",
    "api/schemas/__init__.py", "api/schemas/user.py", "api/schemas/customer.py", "api/schemas/vehicle.py",
    "api/schemas/job.py", "api/schemas/insurance.py", "api/schemas/inventory.py", "api/schemas/document.py",
    "api/schemas/invoice.py",
    "api/services/__init__.py", "api/services/email.py", "api/services/document_storage.py",
    "api/services/image_processing.py",
    "api/services/pdf_generation.py", "api/services/reporting.py", "api/services/insurance_api.py",
    "api/middleware/__init__.py", "api/middleware/logging.py", "api/middleware/auth.py", "api/middleware/language.py",
    "api/utils/__init__.py", "api/utils/date_utils.py", "api/utils/string_utils.py", "api/utils/number_utils.py",
    "api/utils/validators.py",
    "api/__init__.py", "api/main.py", "api/database.py",
    "static/css/main.css", "static/css/rtl.css", "static/css/themes/light.css", "static/css/themes/dark.css",
    "static/css/vendor/bootstrap.min.css",
    "static/js/main.js", "static/js/i18n/en.js", "static/js/i18n/th.js", "static/js/modules/customers.js",
    "static/js/modules/vehicles.js", "static/js/modules/jobs.js", "static/js/modules/inventory.js",
    "static/js/modules/invoices.js", "static/js/modules/photos.js", "static/js/modules/dashboard.js",
    "static/js/vendor/jquery.min.js", "static/js/vendor/bootstrap.min.js", "static/js/vendor/chart.min.js",
    "static/img/logo.png", "static/img/icons/", "static/img/placeholders/",
    "static/fonts/thai/", "static/fonts/latin/",
    "static/templates/emails/en/welcome.html", "static/templates/emails/en/invoice.html",
    "static/templates/emails/th/welcome.html", "static/templates/emails/th/invoice.html",
    "static/templates/pdf/en/invoice.html", "static/templates/pdf/en/job_sheet.html",
    "static/templates/pdf/th/invoice.html", "static/templates/pdf/th/job_sheet.html",
    "mobile/assets/images/", "mobile/assets/fonts/", "mobile/assets/i18n/en.json", "mobile/assets/i18n/th.json",
    "mobile/lib/main.dart", "mobile/lib/models/", "mobile/lib/screens/", "mobile/lib/widgets/", "mobile/lib/services/",
    "mobile/lib/utils/",
    "mobile/pubspec.yml",
    "tests/api/test_customers.py", "tests/api/test_vehicles.py",
    "tests/models/", "tests/services/", "tests/conftest.py",
    "docs/api/", "docs/database/", "docs/deployment/", "docs/user/en/", "docs/user/th/",
    "scripts/db_init.py", "scripts/db_seed.py", "scripts/translations_export.py", "scripts/translations_import.py",
    "i18n/en.json", "i18n/th.json",
    "docker/Dockerfile", "docker/docker-compose.yml", "docker/nginx/nginx.conf",
    ".env.example", ".gitignore", "requirements.txt", "README.md", "setup.py"
]


def create_project_structure(base_path, structure):
    for path in structure:
        full_path = os.path.join(base_path, path)

        if path.endswith("/"):  # It's a directory
            os.makedirs(full_path, exist_ok=True)
        else:  # It's a file
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            if not os.path.exists(full_path):
                with open(full_path, "w") as f:
                    pass  # Create an empty file


if __name__ == "__main__":
    base_directory = os.getcwd()

    # Ensure base project directory exists
    os.makedirs(base_directory, exist_ok=True)

    # Create the project structure
    create_project_structure(base_directory, project_structure)

    print(f"Project structure for '{base_directory}' has been successfully created in {base_directory}!")
