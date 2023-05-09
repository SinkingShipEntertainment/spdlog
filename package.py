name = 'spdlog'

version = '1.9.2'

authors = [
    'Gabi Melman',
]

description = '''Fast header-only C++ log'''

with scope('config') as c:
    # Determine location to release: internal (int) vs external (ext)
    # NOTE: Modify this variable to reflect the current package situation
    release_as = 'ext'

    # The 'c' variable here is actually rezconfig.py
    # 'release_packages_path' is a variable defined inside rezconfig.py

    import os
    if release_as == 'int':
        c.release_packages_path = os.environ['SSE_REZ_REPO_RELEASE_INT']
    elif release_as == 'ext':
        c.release_packages_path = os.environ['SSE_REZ_REPO_RELEASE_EXT']

requires = [
]

private_build_requires = [
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-centos-7'],
]

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    env.REZ_SPDLOG_ROOT = '{root}'
    env.LD_LIBRARY_PATH.append("{root}/lib64")

uuid = 'repository.spdlog'

