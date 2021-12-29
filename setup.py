import pathlib
import sysconfig

from setuptools import find_packages, setup
from setuptools.command.build_ext import build_ext

try:
    import nimporter

    kws = {"ext_modules": nimporter.build_nim_extensions()}

except Exception:
    kws = {}


class NoSuffixBuilder(build_ext):  # noqa
    # NO Suffix: module.linux-x86_64.cpython.3.8.5.so --> module.so
    def get_ext_filename(self, ext_name):  # noqa
        filename = super().get_ext_filename(ext_name)
        return (
            filename.replace(sysconfig.get_config_var("EXT_SUFFIX"), "")
            + pathlib.Path(filename).suffix
        )


setup(
    name="play",
    packages=find_packages("play"),
    package_dir={"": "play"},
    install_requires=["nimporter"],
    include_package_data=True,
    cmdclass={"build_ext": NoSuffixBuilder},
    **kws,
)
