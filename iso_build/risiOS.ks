%include fedora-live-workstation.ks

repo --name="risiOS" --baseurl=https://download.copr.fedorainfracloud.org/results/risi/risiOS/fedora-37-$basearch --cost=1 --priority=50
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
risios-backgrounds-37
risios-bookmarks
webapp-manager
risios-meta
rtheme-lib
rtheme-d
rtheme-plugin-gtk3
rtheme-plugin-gtk4

# Applications
drawing
file-roller
chromium
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
-gnome-extensions-app
-systemd-networkd

%end

%post
# Edit fedora-welcome to use risiOS name (code from Ultramarine, thanks)
sed -i 's/Fedora/risiOS/g' /usr/share/anaconda/gnome/fedora-welcome
cat << EOF >>/home/liveuser/Desktop/liveinst.desktop
visibleName=Install risiOS
EOF

# Prevent risiWelcome from popping up on Live Media
printf "[io.risi.Welcome]\nstartup-show = false" >> /usr/share/glib-2.0/schemas/00_risi.gschema.override

# Edit favorite apps on ISO

cat >> /etc/rc.d/init.d/livesys << EOF
rm /usr/share/glib-2.0/schemas/org.gnome.shell.gschema.override

cat >> /usr/share/glib-2.0/schemas/org.gnome.shell.gschema.override << FOE
[org.gnome.shell]
favorite-apps=['chromium-browser.desktop', 'chromium-freeworld.desktop', 'org.gnome.Nautilus.desktop','org.gnome.Calendar.desktop', 'org.gnome.Photos.desktop', 'org.gnome.Totem.desktop', 'anaconda.desktop']
FOE

glib-compile-schemas /usr/share/glib-2.0/schemas
EOF

%end
