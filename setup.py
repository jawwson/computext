from distutils.core import setup
setup(
  name = 'computype',         # How you named your package folder (MyLib)
  packages = ['computype'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This library allows you to do things like: make it look like the computer is typing, backspace text, make your program wait for you to press enter(for text games), and clear the screen.',   # Give a short description about your library
  author = 'Jason "Jawwson" Wang',                   # Type in your name
  author_email = 'jawwson@outlook.com',      # Type in your E-Mail
  url = 'https://github.com/jawwson',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['TYPING', 'CLEAR', 'BACKSPACE'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.7',      #Specify which python versions that you want to support
    'Programming Language :: Python :: 3.8',
  ],
)