"""
Get dependencies without installing packages
"""
import requests
from pprint import pprint


def request_reqs(package: str, version: str = None) -> list[str]:
    """
    Request requirements in PyPI
    """
    ver = str(version) + "/" if version is not None else ""
    url = f"https://pypi.org/pypi/{package}/" + ver + "json"
    json = requests.get(url).json()
    deps = json["info"]["requires_dist"]
    return deps


if __name__ == "__main__":
    deps = request_reqs("pandas", "2.2.0")
    pprint(deps)
"""
['numpy<2,>=1.22.4; python_version < "3.11"',
 'numpy<2,>=1.23.2; python_version == "3.11"',
 'numpy<2,>=1.26.0; python_version >= "3.12"',
 'python-dateutil>=2.8.2',
 'pytz>=2020.1',
 'tzdata>=2022.7',
 'hypothesis>=6.46.1; extra == "test"',
 'pytest>=7.3.2; extra == "test"',
 'pytest-xdist>=2.2.0; extra == "test"',
 'bottleneck>=1.3.6; extra == "performance"',
 'numba>=0.56.4; extra == "performance"',
 'numexpr>=2.8.4; extra == "performance"',
 'scipy>=1.10.0; extra == "computation"',
 'xarray>=2022.12.0; extra == "computation"',
 'fsspec>=2022.11.0; extra == "fss"',
 's3fs>=2022.11.0; extra == "aws"',
 'gcsfs>=2022.11.0; extra == "gcp"',
 'pandas-gbq>=0.19.0; extra == "gcp"',
 'odfpy>=1.4.1; extra == "excel"',
 'openpyxl>=3.1.0; extra == "excel"',
 'python-calamine>=0.1.7; extra == "excel"',
 'pyxlsb>=1.0.10; extra == "excel"',
 'xlrd>=2.0.1; extra == "excel"',
 'xlsxwriter>=3.0.5; extra == "excel"',
 'pyarrow>=10.0.1; extra == "parquet"',
 'pyarrow>=10.0.1; extra == "feather"',
 'tables>=3.8.0; extra == "hdf5"',
 'pyreadstat>=1.2.0; extra == "spss"',
 'SQLAlchemy>=2.0.0; extra == "postgresql"',
 'psycopg2>=2.9.6; extra == "postgresql"',
 'adbc-driver-postgresql>=0.8.0; extra == "postgresql"',
 'SQLAlchemy>=2.0.0; extra == "mysql"',
 'pymysql>=1.0.2; extra == "mysql"',
 'SQLAlchemy>=2.0.0; extra == "sql-other"',
 'adbc-driver-postgresql>=0.8.0; extra == "sql-other"',
 'adbc-driver-sqlite>=0.8.0; extra == "sql-other"',
 'beautifulsoup4>=4.11.2; extra == "html"',
 'html5lib>=1.1; extra == "html"',
 'lxml>=4.9.2; extra == "html"',
 'lxml>=4.9.2; extra == "xml"',
 'matplotlib>=3.6.3; extra == "plot"',
 'jinja2>=3.1.2; extra == "output-formatting"',
 'tabulate>=0.9.0; extra == "output-formatting"',
 'PyQt5>=5.15.9; extra == "clipboard"',
 'qtpy>=2.3.0; extra == "clipboard"',
 'zstandard>=0.19.0; extra == "compression"',
 'dataframe-api-compat>=0.1.7; extra == "consortium-standard"',
 'adbc-driver-postgresql>=0.8.0; extra == "all"',
 'adbc-driver-sqlite>=0.8.0; extra == "all"',
 'beautifulsoup4>=4.11.2; extra == "all"',
 'bottleneck>=1.3.6; extra == "all"',
 'dataframe-api-compat>=0.1.7; extra == "all"',
 'fastparquet>=2022.12.0; extra == "all"',
 'fsspec>=2022.11.0; extra == "all"',
 'gcsfs>=2022.11.0; extra == "all"',
 'html5lib>=1.1; extra == "all"',
 'hypothesis>=6.46.1; extra == "all"',
 'jinja2>=3.1.2; extra == "all"',
 'lxml>=4.9.2; extra == "all"',
 'matplotlib>=3.6.3; extra == "all"',
 'numba>=0.56.4; extra == "all"',
 'numexpr>=2.8.4; extra == "all"',
 'odfpy>=1.4.1; extra == "all"',
 'openpyxl>=3.1.0; extra == "all"',
 'pandas-gbq>=0.19.0; extra == "all"',
 'psycopg2>=2.9.6; extra == "all"',
 'pyarrow>=10.0.1; extra == "all"',
 'pymysql>=1.0.2; extra == "all"',
 'PyQt5>=5.15.9; extra == "all"',
 'pyreadstat>=1.2.0; extra == "all"',
 'pytest>=7.3.2; extra == "all"',
 'pytest-xdist>=2.2.0; extra == "all"',
 'python-calamine>=0.1.7; extra == "all"',
 'pyxlsb>=1.0.10; extra == "all"',
 'qtpy>=2.3.0; extra == "all"',
 'scipy>=1.10.0; extra == "all"',
 's3fs>=2022.11.0; extra == "all"',
 'SQLAlchemy>=2.0.0; extra == "all"',
 'tables>=3.8.0; extra == "all"',
 'tabulate>=0.9.0; extra == "all"',
 'xarray>=2022.12.0; extra == "all"',
 'xlrd>=2.0.1; extra == "all"',
 'xlsxwriter>=3.0.5; extra == "all"',
 'zstandard>=0.19.0; extra == "all"']
"""