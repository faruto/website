from fabric.api import *
import fabric.contrib.project as project
import os
import os.path as osp
import shutil
import sys
import SimpleHTTPServer
import SocketServer
import sass

from pelicanconf import OUTPUT_PATH

# Globals
REMOVE_EXTENSIONS = ['.pyc', '~']

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = OUTPUT_PATH  # from the pelicanconf.py
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'


def scss():
    """ """
    ifile = 'content/static/custom.scss'
    ofile = 'content/static/custom.css'
    style = 'compressed'
    result = sass.compile(filename=ifile, output_style=style)

    with open(ofile, 'w') as f:
        f.write(result)


def clean():
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(env.deploy_path)


def build():
    local('pelican -s pelicanconf.py')


def rebuild():
    clean()
    scss()
    build()
#    regenerate()


def regenerate():
    local('pelican -r -s pelicanconf.py')


def serve():
    os.chdir(env.deploy_path)

    PORT = 8888

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT),
                                   SimpleHTTPServer.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()


def reserve():
    rebuild()
    serve()


def preview():
    local('pelican -s publishconf.py')


def cf_upload():
    rebuild()
    local('cd {deploy_path} && '
          'swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
          '-U {cloudfiles_username} '
          '-K {cloudfiles_api_key} '
          'upload -c {cloudfiles_container} .'.format(**env))


@hosts(production)
def publish():
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts='-c',
    )

if __name__ == '__main__':
    reserve()
