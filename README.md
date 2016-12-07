## Installation Instructions

NOTE: The WPDA automatic installer requires Ubuntu 16.04.1 LTS.

1. Install Git.

        sudo apt install -y git

2. Clone the WPDA Server repository.

    (WPDA expects to be installed in /var/www/wpda-server/ and will not work anywhere else.)

        sudo git clone https://github.com/DaJoNel/wpda.git /var/www/wpda-server/
        
3. Navigate to the project directory.

        cd /var/www/wpda-server/
        
3. Run the installation script.

    (You will be prompted for administrator credentials.)

        ./install.sh
