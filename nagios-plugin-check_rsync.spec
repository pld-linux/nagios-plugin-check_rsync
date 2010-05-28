%define		plugin	check_rsync
%include	/usr/lib/rpm/macros.perl
Summary:	Nagios rsync plugin
Name:		nagios-plugin-%{plugin}
Version:	1.02
Release:	1
License:	GPL
Group:		Networking
Source0:	check_rsync.pl
Source1:	check_rsync.cfg
URL:		http://exchange.nagios.org/directory/Plugins/Network-Protocols/Rsync/check_rsync/details
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	nagios-common
Requires:	nagios-plugins-libs
Requires:	rsync
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%define		_noautoreq	perl(utils)

%description
Checks rsync servers availability, as well as (optionally) individual
modules availability. It also supports authentication on modules.

%prep
%setup -qcT
cp -p %{SOURCE0} %{plugin}
%{__sed} -i -e 's,/usr/local/nagios/libexec,%{plugindir},' %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin} $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
