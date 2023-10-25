# deploy.py
from fabric import Connection, task

# Define the remote server's SSH connection details
remote_server = "username@your_remote_server_ip"

# Define the paths to your local and remote application directories
local_app_dir = "path/to/your/local/app"
remote_app_dir = "path/to/remote/app"

# Fabric task to deploy the application
@task
def deploy(c):
    # Connect to the remote server
    conn = Connection(remote_server)

    # Transfer the application code to the remote server
    conn.put(local=local_app_dir, remote=remote_app_dir, use_sudo=True)

    # Install dependencies and configure the server
    conn.sudo("apt-get update")
    conn.sudo("apt-get install -y python3-pip")
    conn.sudo("pip3 install -r {}/requirements.txt".format(remote_app_dir))

    # Start the web application server (adjust the command based on your app)
    conn.run("cd {} && python3 manage.py runserver".format(remote_app_dir))

    # Close the SSH connection
    conn.close()

