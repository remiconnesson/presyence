from dataclasses import dataclass, field
import importlib.resources as resources
from typing import TextIO


@dataclass
class StaticFile:
    """This is meant to represent a static file in this python package.

    Actually it can represents any kind of resource in the package, but right now it's purposed is to be subclassed.
    """

    package_name: str
    resource_name: str
    content: str | bytes = field(init=False)

    def __post_init__(self):
        try:
            self.content = resources.read_text(self.package_name, self.resource_name)
        except UnicodeDecodeError:
            self.content = resources.read_binary(self.package_name, self.resource_name)


@dataclass
class WebsiteStaticFile(StaticFile):
    """Represents a static file used by the Vue.JS SPA. It has a route property allowing to match a URL to that file.

    Currently static files used by the website must be stored in the `www` sub-package (directory) for it to work.
    """

    @property
    def route(self) -> str:
        """URL route corresponding to that static file"""
        parent = "/".join(self.package_name.split("www")[-1].split("."))
        return "/".join([parent, self.resource_name])


def get_website_static_files_from_folder(package_name) -> list[WebsiteStaticFile]:
    """Look for resources accessible from `package_name`

    Python can only load resources in a package if those are at the root of this package.
    For example, in the following structure:
    ```
    mypackage/__init__.py
    mypackage/firstresource.py
    mypackage/subdirectory/__init__.py
    mypackage/subdirectory/secondresource.py
    ```
    One can use `resources.read_test("mypackage", "firstresource.py")` but not `resources.read_test("mypackage/subdirectory", "firstresource.py")`.

    """
    result = []
    folder_files = resources.contents(package_name)
    for file_name in folder_files:
        if resources.is_resource(package_name, file_name):
            if not file_name.startswith("__"):  # ignore files like `__init__.py`
                result.append(WebsiteStaticFile(package_name, file_name))
    return result


def get_website_files(
    packages_containing_static_assets=[
        "presyence.reporter.www",
        "presyence.reporter.www.assets",
    ]
) -> list[WebsiteStaticFile]:
    """This loads resources from all folders containing static assets for the Vue.JS SPA."""
    static_files = []
    for package_name in packages_containing_static_assets:
        static_files += get_website_static_files_from_folder(package_name)
    return static_files
