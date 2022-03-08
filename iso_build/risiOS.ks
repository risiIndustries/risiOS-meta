%include fedora-live-workstation.ks

repo --name="risiOS" --baseurl=https://download.copr.fedorainfracloud.org/results/risi/risiOS/fedora-35-$basearch

%packages

file-roller
anaconda-risi
plymouth-theme-risi-spinner
geary
drawing
gnome-music
risi-tweaks
risios-release
risi-gnome-session
risios-logos
risios-repositories
risios-35-backgrounds
-abrt-desktop
-gnome-classic-session
-fedora-release-workstation
-fedora-workstation-backgrounds
-f35-backgrounds-*
-rhythmbox
-gnome-session-xsession
-gnome-session-wayland-session
-gnome-tour

%end

# Edit fedora-welcome to use risiOS name (code from Ultramarine, thanks)
sed -i 's/Fedora/risiOS/g' /usr/share/anaconda/gnome/fedora-welcome
cat << EOF >>/home/liveuser/Desktop/liveinst.desktop
visibleName=Install risiOS
EOF
