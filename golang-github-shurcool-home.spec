# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/home
%global commit          80b7ffcb30f96505d4bc10546d8cd3008bba0fd4

%global common_description %{expand:
Custom HTTP framework for Go.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Custom HTTP framework for Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/shurcooL/httperror)
BuildRequires: golang(github.com/shurcooL/users)
BuildRequires: golang(github.com/shurcooL/htmlg)
BuildRequires: golang(github.com/shurcooL/octicon)
BuildRequires: golang(golang.org/x/net/html)
BuildRequires: golang(golang.org/x/net/html/atom)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup

# We're only interested in httputil and component
find ./* -maxdepth 0 -not -name "httputil" -and -not -name "component" -and -not -name "README.md" -exec rm -rf "{}" \;


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%doc README.md


%changelog
* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20181026git80b7ffc
- Bump to commit 80b7ffcb30f96505d4bc10546d8cd3008bba0fd4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitfbbd8f2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180421gitfbbd8f2
- First package for Fedora

