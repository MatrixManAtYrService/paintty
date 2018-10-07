from setuptools import setup
setup(name='paintty',
      version='0.1.0.dev1',
      description='capture cli interactions so they can be painted on',
      url='https://github.com/MatrixManAtYrService/paintty',
      author='Matt Rixman',
      packages=['paintty'],
      python_requires= '>=3',
      install_requires=['python-daemon', 'sh'],
      entry_points={'console_scripts' : [

          # source the output of this command to configure zsh to communicate with the paintty daemon
          #  usage: source <(sp-zsh)
          #  - creates the sp zsh function (sp for "semantic paint")
          #  - configures zsh to notice 'sp <command>' and rewrite history with just '<command>'
          #  - calls sp-start
          #  - redirect terminal output (via script) to the paintty daemon if the '-l, --live' flag was passed
          'sp-zsh = paintty.zsh:setup',

          # The `sp` zsh function is used like:
          #    sp <the command>
          #
          # it does the following:
          #  - generates a uuid for the new canvas and sends it to paintty daemon along with the command and context
          #  - allows the daemon to block the current process (in case a loaded palette wants to analyze the before-state)
          #  - redirect terminal output (via script) to the paintty daemon (if this isn't alredy happening)
          #  - run the command with 'strace', redirecting the trace to the paintty daemon
          #  - again allows the daemon to block the curren process (in case a loaded palette wants to analyze the after-state)
          #  - kills terminal redirection if it started it

          # undoes 'sp-zsh', used mostly for testing
          'unsp-zsh = paintty.zsh:unsetup',

          # starts the paintty daemon if it isn't already running
          'sp-start = paintty.daemon:ensure_started',

          # stops the paintty daemon if it isn't already stopped
          'sp-stop = paintty.daemon:ensure_stopped',

          ]}
      )

