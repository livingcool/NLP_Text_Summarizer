import setuptools

# Read the contents of the README.md file to use as the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# --- Project Metadata ---
__version__ = "0.0.0"

REPO_NAME = "NLP_Text_Summarizer"
AUTHOR_USER_NAME = "Ganesh K"
SRC_REPO = "textSummarizer" # This is the name of the main source directory/package
AUTHOR_EMAIL = "ganeshkhovalan2203@gmail.com"
# ------------------------

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP Text Summarizer app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"}, # Tells setup to look for packages inside the 'src' directory
    packages=setuptools.find_packages(where="src") # Automatically finds all packages in 'src'
)