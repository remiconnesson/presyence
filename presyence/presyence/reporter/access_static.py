from dataclasses import dataclass, field
import importlib.resources as resources
from typing import TextIO

@dataclass
class StaticFile:
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
    @property
    def route(self) -> str:
        """ URL route corresponding to that static file"""
        parent = "/".join(self.package_name.split('www')[-1].split('.'))
        return "/".join([parent, self.resource_name])

def get_website_static_files_from_folder(package_name):
    result = []
    folder_files = resources.contents(package_name)
    for file_name in folder_files:
        if resources.is_resource(package_name, file_name):
            if not file_name.startswith("__"):
                result.append(
                    WebsiteStaticFile(
                        package_name,
                        file_name
                    )
                )
    return result

def get_website_files() -> list[WebsiteStaticFile]:
    static_files = []
    for package_name in ["presyence.reporter.www", "presyence.reporter.www.assets"]:
        static_files += get_website_static_files_from_folder(package_name)
    return static_files
