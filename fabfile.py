from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['tukipenda@tukipenda.webfactional.com']
prompt("Enter key: ", "password") 

def production():
    """
Work on production environment
"""
    env.settings = 'production'
    env.app_folder="math_picalytics"
    env.static_folder=''
    
def push():
	run('cd /home/tukipenda/webapps/%s/Picalytics/; git pull origin master' % env.app_folder)

def restart():
	run('/home/tukipenda/webapps/%s/apache2/bin/restart' % env.app_folder)

def stop():
	run('/home/tukipenda/webapps/%s/apache2/bin/stop' % env.app_folder)

def move_static_files():
	with settings(warn_only=True):
		result=run('rm -r /home/tukipenda/webapps/%s/*' % env.static_folder)
	if result.failed and not confirm("Could not remove files.  Continue anyway?"):
		abort("Aborting at user request.")
	run('cp -r /home/tukipenda/webapps/%s/CBT-Toolkit/Media/. /home/tukipenda/webapps/%s' % (env.app_folder, env.static_folder))

def deploy():
	push()
#	move_static_files()
	restart()
