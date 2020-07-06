from setuptools import setup

setup(
    name='playit',
    packages = ['playit'],
    version="0.01",
    license='MIT', 
    description = 'It play music on console in various mode.',
    author = 'Saurabh Gujjar',
    author_email = 'saurabhpanwar127@gmail.com',
    url = 'https://github.com/SaurabhGujjar/playit.git', 
    download_url = 'https://github.com/SaurabhGujjar/playit/archive/v_0.01.tar.gz',
    keywords = ['music player', 'cli', 'command line interface'],

    py_modules=['playit'],
    install_requires=['Click', 'pyfiglet', 'pygame', 'mutagen', 'tqdm', 'times', ],
    entry_points=''' 
    [console_scripts]
    playit = playit.cli:main
    ''',

    classifiers=[
    'Development Status :: 3 - Alpha',    
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',  
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ]

)