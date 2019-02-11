from data.axioms.config import paths

class ConfigReader:
    def read(self, config, ftype):
        reader = get_reader(ftype)
        return reader(config)

def get_reader(ftype):
    if ftype == 'golem':
        return _read_from_golem
    elif ftype == 'proc':
        return _read_from_proc
    else:
        raise ValueError(ftype)

def _read_from_golem(config):
  """
  validate inputs
  check for a valid golem type file in the golem type database (lol. it's a directory for the MVP)
  throw an error for existance of validation operational violations
  ctags --options=C:\Users\sturmy\.vscode\extensions\ms-python.python-2018.12.1\resources\ctagOptions --languages=Python --exclude=**/site-packages/** -o d:\Projects\golem-factory\.vscode\tags .
Install Universal Ctags Win32 to enable support for Workspace Symbols
Download the CTags binary from the Universal CTags site.
Option 1: Extract ctags.exe from the downloaded zip to any folder within your PATH so that Visual Studio Code can run it.
Option 2: Extract to any folder and add the path to this folder to the command setting.
Option 3: Extract to any folder and define that path in the python.workspaceSymbols.ctagsPath setting of your user settings file (settings.json).
  """
    config_fname = f'{paths['golem']}{config}.golem'
    golem_type_config = load(open(config_fname))
    settings = golem_type_config.extend({
        'desired_base_dests': num_dests,
        'paired': is_pair, #should be capable of handling through config as well at some point
        # 'core_config': core_config
        #'core_type_fname': config.core_type_fname. CORE_TYPE or CORE_TYPE_FNAME SHOULD BE INCLUDED IN GOLEM_TYPE config already
    })
    return settings


def _read_from_proc(config):
    config_fname = f'{paths['golem']}{config}.golem'
    proc_type_config = load(open(config_fname))
    settings = golem_type_config.extend({
        'desired_base_dests': num_dests,
        'paired': is_pair, #should be capable of handling through config as well at some point
        # 'core_config': core_config
        #'core_type_fname': config.core_type_fname. CORE_TYPE or CORE_TYPE_FNAME SHOULD BE INCLUDED IN GOLEM_TYPE config already
    })
    return settings