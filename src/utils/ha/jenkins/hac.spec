Name: eos-hac
Version: %{version}
Release: %{_build_number}_%{dist}
Summary: HAC Tools
License: Seagate Proprietary
URL: http://gitlab.mero.colo.seagate.com/eos/py-utils/tree/master/src/utils/ha
Source0: eos-hac-%{version}.tar.gz
%define debug_package %{nil}

%description
HAC Tools

%prep
%setup -n ha
# Nothing to do here

%build

%install
mkdir -p ${RPM_BUILD_ROOT}/opt/seagate/eos/ha
cp -rp . ${RPM_BUILD_ROOT}/opt/seagate/eos/ha
exit 0

%post
ln -sf /opt/seagate/eos/ha/hac.py /usr/bin/hac
exit 0

%postun
rm -rf /usr/bin/hac
rm -rf /opt/seagate/eos/ha/
exit 0

%clean

%files
%defattr(-, root, root, -)
/opt/seagate/eos/ha/*

%changelog
* Mon Mar 16 2020 Ajay Paratmandali <ajay.paratmandali@seagate.com> - 1.0.0
- Initial spec file
