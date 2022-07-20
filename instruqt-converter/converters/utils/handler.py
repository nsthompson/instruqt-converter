import re
import yaml
from yaml import CSafeDumper as SafeDumper
from yaml import CSafeLoader as SafeLoader
from frontmatter.default_handlers import BaseHandler
from frontmatter.util import u


def str_presenter(dumper, data):
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar(
            'tag:yaml.org,2002:str',
            data,
            style="|"
          )
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


# Extension of frontmatter YAMLHandler to add support for yaml.add_representer
class YAMLHandler(BaseHandler):
    """
    Load and export YAML metadata. By default, this handler uses YAML's
    "safe" mode, though it's possible to override that.
    """

    FM_BOUNDARY = re.compile(r"^-{3,}\s*$", re.MULTILINE)
    START_DELIMITER = END_DELIMITER = "---"

    def load(self, fm, **kwargs):
        """
        Parse YAML front matter. This uses yaml.SafeLoader by default.
        """
        kwargs.setdefault("Loader", SafeLoader)
        return yaml.load(fm, **kwargs)

    def export(self, metadata, **kwargs):
        """
        Export metadata as YAML. This uses yaml.SafeDumper by default.
        """
        kwargs.setdefault("Dumper", SafeDumper)
        kwargs.setdefault("default_flow_style", False)
        kwargs.setdefault("allow_unicode", True)

        yaml.add_representer(str, str_presenter, Dumper=SafeDumper)
        metadata = yaml.dump(metadata, **kwargs).strip()
        return u(metadata)  # ensure unicode
