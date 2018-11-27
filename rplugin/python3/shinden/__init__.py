import sys
import neovim
from .shinden import Shinden


sys.dont_write_bytecode = True


@neovim.plugin
class shinden(object):
    _cmd_pre = 'Shinden'

    def __init__(self, nvim):
        self._nvim = nvim
        self._shinden = Shinden(self._nvim)

    @neovim.command(_cmd_pre+'Begin', range='', nargs='*')
    def open_shinden(self, args, range):
        file_name = str(args[0])
        self._shinden.init_env(file_name)

    # @neovim.command(_cmd_pre+'Run', nargs='*')
    # def run_current_cmd(self, args):
    #     cmd = self._nvim.current.line
    #     self._shinden.run_cmd(cmd)

    @neovim.function(_cmd_pre + 'Run', sync=True)
    def run_current_cmd(self, args):
        cmd = self._shinden.get_cmd()
        self._shinden.run_cmd(cmd)
        return args



