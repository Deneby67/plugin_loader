import inspect
import pkgutil

import sys

import plugins


class Main(object):
    def __init__(self):
        mpath = plugins.__path__
        if mpath:
            for importer, package_name, _ in pkgutil.iter_modules(mpath):
                full_package_name = '%s.%s' % (mpath, package_name)
                if full_package_name not in sys.modules:
                    modul = importer.find_module(package_name
                                                 ).load_module(full_package_name)
                    for _, cls in inspect.getmembers(modul, inspect.isclass):
                        cls = cls()
                        cls.__dict__['parent'] = self
                        for _, method in inspect.getmembers(cls, inspect.ismethod):
                            if hasattr(method, 'route_name'):
                                setattr(self, method.route_name, method)

    def run(self):
        print self.api('test')


m = Main()
m.run()
