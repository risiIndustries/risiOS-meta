%include fedora-live-workstation.ks

repo --name="risiOS" --baseurl=https://download.copr.fedorainfracloud.org/results/risi/risiOS/fedora-36-$basearch --cost=1 --priority=50
repo --name="OnlyOffice" --baseurl=http://download.onlyoffice.com/repo/centos/main/noarch/

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
risi-zsh-plugins
risios-release
risios-logos
risios-repositories
risios-36-backgrounds
risios-bookmarks
webapp-manager
mozilla-risiSearx
risios-meta
chromium

# Applications
drawing
file-roller
onlyoffice-desktopeditors

# Removed
-abrt-desktop
-desktop-backgrounds-gnome
-gnome-classic-session
-gnome-tour
-fedora-release-workstation
-fedora-workstation-backgrounds
-rhythmbox
-mediawriter
-gnome-boxes
-fedora-bookmarks
-cheese
-libreoffice*
-unoconv
-firefox


%end

%post
# Edit fedora-welcome to use risiOS name (code from Ultramarine, thanks)
sed -i 's/Fedora/risiOS/g' /usr/share/anaconda/gnome/fedora-welcome
cat << EOF >>/home/liveuser/Desktop/liveinst.desktop
visibleName=Install risiOS
EOF

# Prevent risiWelcome from popping up on Live Media
printf "[io.risi.Welcome]\nstartup-show = false" >> /usr/share/glib-2.0/schemas/00_risi.gschema.override
%end
