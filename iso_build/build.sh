VERSION=36
DATE=$(date +"%Y%m%d")

rm -rf fedora-kickstarts
rm anaconda.log
rm risiOS-Live-$VERSION-$DATE.iso

git clone https://pagure.io/fedora-kickstarts.git --branch=f$VERSION
cp risiOS.ks fedora-kickstarts/risiOS.ks
cd fedora-kickstarts
ksflatten -v, --config risiOS.ks -o ./risiOS-$VERSION-live-flat.ks --version f35

mock --init fedora-$VERSION-x86_64
mock --root fedora-$VERSION-x86_64 --install lorax-lmc-novirt nano sed
mock --root fedora-$VERSION-x86_64 --copyin risiOS-$VERSION-live-flat.ks /
mock --root fedora-$VERSION-x86_64 --enable-network --isolation=simple --chroot "/sbin/livemedia-creator --ks /risiOS-$VERSION-live-flat.ks --logfile /var/tmp/lmc-logs/livemedia-out.log --no-virt --resultdir /var/tmp/lmc --project risiOS-Live --make-iso --volid risiOS-Live-$VERSION-$DATE.n.0 --iso-only --iso-name risiOS-Live-$VERSION-$DATE.iso --releasever $VERSION --macboot"
mock --root fedora-$VERSION-x86_64 --copyout /var/tmp/lmc/risiOS-Live-$VERSION-$DATE.iso ..
mock --root fedora-$VERSION-x86_64 --copyout /var/tmp/lmc-logs/anaconda/anaconda.log ..

mock --root fedora-$VERSION-x86_64 --clean
cd ..
# rm -rf fedora-kickstarts
