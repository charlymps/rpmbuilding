Name:		waf-fle
Version:	0.6.4
Release:	1%{?dist}
Summary:	Web Application Firewall: Fast Log and Event Console

License:	GPL v2
URL:		http://waf-fle.org
Source0:	http://waf-fle.org/downloads/waf-fle_0.6.4.tar.gz
Requires:	httpd php php-pdo php-mysql php-pecl-apc php-pecl-geoip GeoIP

%description
WAF-FLE is a OpenSource ModSecurity Console, allows modsecurity admin to store, view and search events sent by sensors using a graphical dashboard to drill-down and find quickly the most relevant events. It is designed to be fast and flexible, while keeping a powerful and easy to use filter, with almost all fields clickable to use on filter.

%prep
%setup -q -n waf-fle_0.6.4

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/waf-fle
cp -R extra dashboard controller $RPM_BUILD_ROOT/usr/local/waf-fle/
install -m 644 *.php config.php.example $RPM_BUILD_ROOT/usr/local/waf-fle/
install -D -m 644 extra/waf-fle.conf $RPM_BUILD_ROOT/etc/httpd/conf.d/waf-fle.conf
install -D -m 600 config.php.example $RPM_BUILD_ROOT/etc/waf-fle/config.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/waf-fle/config.php.example
/usr/local/waf-fle/footer.php
/usr/local/waf-fle/session.php
/usr/local/waf-fle/functions.php
/usr/local/waf-fle/header.php
/usr/local/waf-fle/extra
/usr/local/waf-fle/filterprocessing.php
/usr/local/waf-fle/filtershow.php
/usr/local/waf-fle/dashboard
/usr/local/waf-fle/controller
/usr/local/waf-fle/filter.php
%config /etc/httpd/conf.d/waf-fle.conf
%config /etc/waf-fle/config.php
%doc ChangeLog README README.md LICENSE

%post
ln -s /etc/waf-fle/config.php /usr/local/waf-fle/config.php
cp /usr/share/GeoIP/GeoIPASNum.dat /usr/share/GeoIP/GeoIPISP.dat

%changelog
* Tue Dec 1 2015 Carlos Pintado
- Example build
