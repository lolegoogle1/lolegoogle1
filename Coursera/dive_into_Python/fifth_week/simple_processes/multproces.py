# Creating process, <multiprocessing> module

from multiprocessing import Process


def func(name):
    print("hello", name)


p = Process(target=func, args=("Oleh",))  # Passing the func and args for execution in child process
p.start()  # os.fork()
p.join()  # os.wait()

"""
        def start(self):
            '''
                Start child process
            '''
            
            self._check_closed()
            assert self._popen is None, 'cannot start a process twice'
            assert self._parent_pid == os.getpid(), \
                   'can only start a process object created by current process'
            assert not _current_process._config.get('daemon'), \
                   'daemonic processes are not allowed to have children'
            _cleanup()
            self._popen = self._Popen(self)
            self._sentinel = self._popen.sentinel
            
            # Avoid a refcycle if the target function holds an indirect
            # reference to the process object (see bpo-30775)
            
            del self._target, self._args, self._kwargs
            _children.add(self)
            
        def join(self, timeout=None):
            '''
                Wait until child process terminates
            '''
            
            self._check_closed()
            assert self._parent_pid == os.getpid(), 'can only join a child process'
            assert self._popen is not None, 'can only join a started process'
            res = self._popen.wait(timeout)
            if res is not None:
                _children.discard(self)
"""