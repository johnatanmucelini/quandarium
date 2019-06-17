"""This package present several tools to processe KDD for QC data and
calculations.
In particular, this package focus on data extraction, feature
enginering, DM processes, and data plot."""

import pkgutil

__path__ = pkgutil.extend_path(__path__, __name__)
for importer, modname, ispkg in pkgutil.walk_packages(path=__path__, prefix=__name__+'.'):
      __import__(modname)
