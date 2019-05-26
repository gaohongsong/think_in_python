# -*- coding: utf-8 -*-

import sys
import six
from importlib import import_module


def import_string(dotted_path):
    """Import a dotted module path and
    return attribute/class by the last name in path"""

    try:
        module_path, class_name = dotted_path.rsplit('.', 1)
    except ValueError:
        msg = "%s is not a module path" % dotted_path
        six.reraise(ImportError, ImportError(msg), sys.exc_info()[2])

    module = import_module(module_path)

    try:
        return getattr(module, class_name)
    except:
        msg = "%s does not have attribute: %s" % (module_path, class_name)
        six.reraise(ImportError, ImportError(msg), sys.exc_info()[2])
