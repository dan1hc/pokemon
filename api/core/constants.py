import os


class PackageConstants:

    # App
    AppName               = __module__.split('.')[0]
    AppNameClean          = ' '.join(AppName.split('_')).title()
    Authorization         = None
    Env                   = os.getenv('PROJECT_ENV', 'dev')
    Security              = None


    @classmethod
    def register(cls, obj):
        setattr(cls, obj.__name__, obj)
        return obj
