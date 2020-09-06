touch install.sh
curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh > install.sh
chmod 777 install.sh
./install.sh
brew install wget
wget http://tug.org/cgi-bin/mactex-download/MacTeX.pkg
installer -pkg MacTeX.pkg -target CurrentUserHomeDirectory
