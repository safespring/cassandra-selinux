%define _prefix   /

Name:		cassandra-selinux	
Version:	1.0.0
Release:	1%{?dist}
Summary:	SELinux Policy for cassandra

Group:		System Environment/Base
BuildArch:	noarch
License:	GPLv2
Requires:		policycoreutils, libselinux-utils
Requires(post):		selinux-policy-base >= %{selinux_policyver}, selinux-policy-targeted >= %{selinux_policyver}, policycoreutils, policycoreutils-python
Requires(postun):	policycoreutils
BuildRequires:		selinux-policy selinux-policy-devel
Source0: 		./cassandra.pp


%description
SELinux Policy module for use with cassandra


%prep

%build

%install
install -D %{S:0} %{buildroot}%{_prefix}/usr/share/selinux/packages/cassandra/cassandra.pp


%files
%dir %attr(0700, root, root) /usr/share/selinux/packages/cassandra/
%attr(0600, root, root) /usr/share/selinux/packages/cassandra/cassandra.pp

%post
	/usr/sbin/semodule -i /usr/share/selinux/packages/cassandra/cassandra.pp 
	restorecon -R /usr/sbin/cassandra /var/log/cassandra /var/run/cassandra /var/lib/cassandra /etc/cassandra

%postun
if [ $1 -eq 0 ]; then
	/usr/sbin/semodule -r cassandra
	restorecon -R /usr/sbin/cassandra /var/log/cassandra /var/run/cassandra /var/lib/cassandra /etc/cassandra
fi


%changelog

