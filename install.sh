function setUpEnv {
    rm .env
    touch .env
    echo "--- Init ---"
    arch="$(uname -m)"
    echo "We detected the following architecture: $arch"
    #should be aarch64 or x86_64
    case $arch in
        #[aarch64]* ) echo 'HOST_ARCHITECTURE=aarch64' >> .env;;
        [aarch64]* ) echo 'HOST_ARCHITECTURE=x86_64' >> .env;;
        [x86_64]* ) echo 'HOST_ARCHITECTURE=x86_64' >> .env;;
        * ) echo "Architecture not yet supported"; exit;;
    esac
    source .env
}

# 1. Check if .env file exists
if [ -e .env ]; then
    echo "There is already an env file, do you want to continue with this one? (no will delete it and create a new one) [y/n]"
    read -p ":" fs
    case $fs in
        [Yy]* ) source .env;;
        [Nn]* ) setUpEnv;;
        * ) echo "Please answer full or soft."; exit;;
    esac
else 
    setUpEnv
fi

case $HOST_ARCHITECTURE in
    [aarch64]* ) docker build -f 'DockerBuilds/aarch64_pi/Dockerfile' -t fulltiktokbot:latest .;;
    [x86_64]* ) docker build -f 'DockerBuilds/x86_64/Dockerfile' -t fulltiktokbot:latest .;;
    * ) echo "Architecture not found"; exit;;
esac

#to change file and make it stealth
#perl -pi -e 's/cdc_adoQpoasnfa76pfcZLmcfl/lhf_ufoQjkhsnpa76pfcOPLcfl/g' /path/to/chromedriver 

echo "Run Docker Image"
docker-compose up -d
