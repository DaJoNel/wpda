## Installation Instructions

NOTE: The WPDA automatic installer requires Ubuntu 16.04.1 LTS.

1. Install Git.  
    `sudo apt install -y git`

2. Clone the WPDA Server repository.  
    *(WPDA expects to be installed in /var/www/wpda-server/ and will not work anywhere else.)*  
    `sudo git clone https://github.com/DaJoNel/wpda.git /var/www/wpda-server/`

3. Navigate to the project directory.  
    `cd /var/www/wpda-server/`

4. Run the installation script.  
    *(You will be prompted for administrator credentials.)*  
    `./install.sh`

5. Build the WPDA Client application.  
    `cd /var/www/wpda-client/`  
    `ember build -o /var/www/wpda-server/static/ember/`  
    *Or, if using Watchman to watch the directory for changes and automatically build.*  
    `ember build --watch -o /var/www/wpda-server/static/ember/`

## Usage Instructions

1. Using the server virtual machine, determine its IP address.  
    `ifconfig`

2. Navigate to that IP address in a web browser of your choice on the host machine.  
    *Or, if using a GUI version of Ubuntu for the server, navigate to* `localhost` *on the virtual machine.*
