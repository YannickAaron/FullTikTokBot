#download from github an update files if necessary
#maybe ask for full update (creates new image as well) or only files update (soft update)
function fullUpdate {
    echo "Full Update"
}
function softupdate {
    echo "Soft Update"
}

echo "Do you wish to performe a full or soft update? [f/s]"
read -p ":" fs
case $fs in
    [Ff]* ) fullUpdate;;
    [Ss]* ) softupdate;;
    * ) echo "Please answer full or soft."; exit;;
esac