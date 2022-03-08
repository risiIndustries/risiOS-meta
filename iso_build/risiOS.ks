%include fedora-live-workstation.ks

repo --name="risiOS" --baseurl=https://download.copr.fedorainfracloud.org/results/risi/risiOS/fedora-35-$basearch

%packages
# risiOS features/system stuff
adw-gtk-theme
anaconda-risi
gnome-backgrounds
plymouth-theme-risi-spinner
risi-gnome-session
risi-script
risi-tweaks
risi-welcome
risios-release
risios-logos
risios-repositories
risios-35-backgrounds
webapp-manager

# Applications
drawing
file-roller
geary
gnome-music

# Removed
-abrt-desktop
-desktop-backgrounds-gnome
-gnome-classic-session
-gnome-session-xsession
-gnome-session-wayland-session
-gnome-tour
-f35-backgrounds-*
-fedora-release-workstation
-fedora-workstation-backgrounds
-rhythmbox

%end

# Edit fedora-welcome to use risiOS name (code from Ultramarine, thanks)
sed -i 's/Fedora/risiOS/g' /usr/share/anaconda/gnome/fedora-welcome
cat << EOF >>/home/liveuser/Desktop/liveinst.desktop
visibleName=Install risiOS
EOF
