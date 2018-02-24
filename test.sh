# INSTRUCTIONS:
 
# Enter the terminal (Ctrl-Alt-F2, username is "chronos" and password is either blank or "password" for ArnoldTheBat's builds) and run:
#
# curl -L https://goo.gl/BBV79Q | sudo bash
#
# to install. You'll likely have to re-enter the password "password".
# Attempts to grab the latest Flash version straight from Adobe's website.
# Should be a bit more bullet-proof than some of the other flash installer scripts.

# NOTE: If you can't enter the terminal, follow step 5 from: https://gist.github.com/balupton/9908197
 
set -e
mount -o remount,rw /
conf=/etc/chrome_dev.conf
flashdir=$HOME/flash
flashlib=$flashdir/libpepflashplayer.so
mkdir -p $flashdir
[ `arch` = x86_64 ] && arch=x86_64 || arch=i386
latest=`curl -sL www.adobe.com/software/flash/about | awk '/Linux/{x=1}/Chrome \(embedded\) - PPAPI/{if(x){getline;print}}' | grep -o '[0-9.]*'`
 
append_or_update() {
  grep -q -- "$1" $conf && sed -i "s@\s*$1=.*@$1=$2@" $conf || echo "$1=$2" >> $conf
}
 
echo "Downloading and extracting Flash $latest for architecture $arch..."
curl -sL "https://fpdownload.adobe.com/pub/flashplayer/pdc/$latest/flash_player_ppapi_linux.$arch.tar.gz" | tar xzf - -C $flashdir
chmod +x $flashlib
 
echo "Editing $conf..."
cp $conf $flashdir/backup.conf
append_or_update --ppapi-flash-path $flashlib
append_or_update --ppapi-flash-version "$latest".
echo "Restarting UI..."
restart ui
