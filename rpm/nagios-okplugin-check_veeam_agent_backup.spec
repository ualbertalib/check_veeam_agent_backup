%define debug_package %{nil}

Summary:	A Nagios plugin to check if veeam linux agent is backing up
Name:		check_veeam_agent_backup
Version:	1.0.3
Release:	0%{?dist}
License:	GPLv3+
Group:		Applications/System
URL:		https://github.com/ualbertalib/check_veeam_agent_backup/issues
Source0:	https://github.com/ualbertalib/check_veeam_agent_backup
Requires:	veeam
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Packager:	Neil MacGregor <neilmacgregor@ualberta.ca>



%description
A Nagios plugin to check if veeam linux agent is doing successful backups


%prep
%setup -q

%build


%install
rm -rf %{buildroot}
install -D -p -m 0755 check_veeam_agent_backup.sh %{buildroot}%{_libdir}/nagios/plugins/check_veeam_agent_backup.sh

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md LICENSE
%{_libdir}/nagios/plugins/*

%post
restorecon -v %{_libdir}/nagios/plugins/check_veeam_agent_backup.sh
usermod -a -G veeam nagios

%changelog
* Tue Nov 22 2022  Neil MacGregor <neilmacgregor@ualberta.ca> 1.0.3-0
- Removed the files we do not require, and cleaned up this .spec file
* Wed Oct 10 2017  Samúel Jón Gunnarsson <samuel@ok.is> 1.0.2-1
- Removed sudo command dependency, using veeam group instead. Updated README.
* Wed Oct 10 2017  Samúel Jón Gunnarsson <samuel@ok.is> 1.0.1-1
- Added nrpe.d configuration item for the command
* Wed Sep 27 2017  Samúel Jón Gunnarsson <samuel@ok.is> 1.0.0-1
- Initial packaging
