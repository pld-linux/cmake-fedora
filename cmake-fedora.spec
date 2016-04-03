# NOTE: -modules subpackage is equivalent of cmake-fedora-%{version}-modules-only.tar.gz
Summary:	CMake modules and scripts that simplify and automate the release process for software package
Summary(pl.UTF-8):	Moduły CMake'a i skrypty ułatwiające i automatyzujące proces wydawania oprogramowania
Name:		cmake-fedora
Version:	2.6.0
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	https://fedorahosted.org/releases/c/m/cmake-fedora/%{name}-%{version}-Source.tar.gz
# Source0-md5:	4f487ed5e97d46e20d6356d5cc7a7fa5
URL:		https://fedorahosted.org/cmake-fedora/
BuildRequires:	cmake >= 2.6.2
Requires:	%{name}-modules = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cmake-fedora consists of CMake modules and scripts that simplify and
automate the release process for software package, especially for
Fedora and EPEL.

%description -l pl.UTF-8
Ten pakiet składa się z modułów CMake'a oraz skryptów upraszczających
i automatyzujących proces wydawania pakietów oprogramowania, w
szczególności dla dystrybucji Fedora i EPEL.

%package modules
Summary:	CMake modules that simplify and automate the release process for software package
Summary(pl.UTF-8):	Moduły CMake'a ułatwiające i automatyzujące proces wydawania oprogramowania
Group:		Development/Tools
Requires:	cmake >= 2.6.2

%description modules
cmake-fedora consists of CMake modules that simplify and automate the
release process for software package, especially for Fedora and EPEL.

%description modules -l pl.UTF-8
Ten pakiet składa się z modułów CMake'a upraszczających i
automatyzujących proces wydawania pakietów oprogramowania, w
szczególności dla dystrybucji Fedora i EPEL.

%prep
%setup -q -n %{name}-%{version}-Source

%build
%cmake \
	-DCMAKE_FEDORA_ENABLE_FEDORA_BUILD=0
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/cmake-fedora

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cmake-fedora.conf
%attr(755,root,root) %{_bindir}/cmake-fedora-fedpkg
%attr(755,root,root) %{_bindir}/cmake-fedora-koji
%attr(755,root,root) %{_bindir}/cmake-fedora-newprj
%attr(755,root,root) %{_bindir}/cmake-fedora-pkgdb
%attr(755,root,root) %{_bindir}/cmake-fedora-zanata
%attr(755,root,root) %{_bindir}/koji-build-scratch
%{_datadir}/cmake/Templates/fedora

%files modules
%defattr(644,root,root,755)
%{_datadir}/cmake/Modules/CmakeFedoraScript.cmake
%{_datadir}/cmake/Modules/DateTimeFormat.cmake
%{_datadir}/cmake/Modules/ManageAPIDoc.cmake
%{_datadir}/cmake/Modules/ManageArchive.cmake
%{_datadir}/cmake/Modules/ManageChangeLogScript.cmake
%{_datadir}/cmake/Modules/ManageDependency.cmake
%{_datadir}/cmake/Modules/ManageEnvironment.cmake
%{_datadir}/cmake/Modules/ManageEnvironmentCommon.cmake
%{_datadir}/cmake/Modules/ManageFile.cmake
%{_datadir}/cmake/Modules/ManageGConf.cmake
%{_datadir}/cmake/Modules/ManageGettextScript.cmake
%{_datadir}/cmake/Modules/ManageGitScript.cmake
%{_datadir}/cmake/Modules/ManageMessage.cmake
%{_datadir}/cmake/Modules/ManageRPM.cmake
%{_datadir}/cmake/Modules/ManageRPMScript.cmake
%{_datadir}/cmake/Modules/ManageRelease.cmake
%{_datadir}/cmake/Modules/ManageReleaseFedora.cmake
%{_datadir}/cmake/Modules/ManageSourceVersionControl.cmake
%{_datadir}/cmake/Modules/ManageString.cmake
%{_datadir}/cmake/Modules/ManageTarget.cmake
%{_datadir}/cmake/Modules/ManageTranslation.cmake
%{_datadir}/cmake/Modules/ManageUninstall.cmake
%{_datadir}/cmake/Modules/ManageUpload.cmake
%{_datadir}/cmake/Modules/ManageVariable.cmake
%{_datadir}/cmake/Modules/ManageVersion.cmake
%{_datadir}/cmake/Modules/ManageZanata.cmake
%{_datadir}/cmake/Modules/ManageZanataDefinition.cmake
%{_datadir}/cmake/Modules/ManageZanataScript.cmake
%{_datadir}/cmake/Modules/ManageZanataSuggest.cmake
%{_datadir}/cmake/Modules/cmake_uninstall.cmake.in
