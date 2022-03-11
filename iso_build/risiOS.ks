%include fedora-live-workstation.ks

repo --name="risiOS" --baseurl=https://download.copr.fedorainfracloud.org/results/risi/risiOS/fedora-35-$basearch

%packages

# risiOS features/system stuff
adw-gtk-theme
anaconda-risi
gnome-backgrounds
plymouth-theme-risi-spinner
risi-settings
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
-gnome-classic-session
-gnome-extensions-app
-gnome-tour
-desktop-backgrounds-gnome
-f35-backgrounds-base
-fedora-release-workstation
-fedora-workstation-backgrounds
-rhythmbox

%end
