import re


class Shinden(object):

    def __init__(self, nvim):
        self._nvim = nvim
        self._window_list = {}
        self._buffer_list = {}

    #
    # call first in order to assign widows.
    #
    def assign_window_num(self, term, script):
        # TODO
        # assign window to term or script automatically
        #   assign term-window, script-window
        # currently, assigin using args.

        wins = self._nvim.windows
        self._windows['term'] = wins[term]
        self._windows['script'] = wins[script]

        # only when no term, one buffer
        #   ->create term window
        # otherwise
        #   ->create tab, term
        #   if buf=b, cp buf to new tab

        # get buffers dict
        # {buf_num : buf_obj}
        _bufs = self._nvim.buffers
        if (len(_bufs) == 1 and
                not re.match('^term:.*', list(_bufs.values())[0])):
            self._nvim.command('vsp|term')
        else:
            pass

    #
    # main routin, put cmd to terminal and run.
    #
    def run_cmd(self, cmd):
        self._nvim.current.window = self._windows['term']
        self._nvim.feedkeys('i' + cmd + '\n')
        self._nvim.current.window = self._windows['script']
