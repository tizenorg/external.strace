#sbs-git:slp/pkgs/s/strace strace 4.5.20 c85d16265104f1b4b4e0793e61d1f3bb4605f5a6
Name:       strace
Summary:    A system call tracer
Version: 4.5.20
Release:    3
Group:      utils
License:    BSD3c
URL:        http://sourceforge.net/projects/strace/
Source0:    strace-4.5.20.tar.gz
Source1001:     %{name}.manifest

%description
A system call tracer
 strace is a system call tracer, i.e. a debugging tool which prints out
 a trace of all the system calls made by a another process/program.
 The program to be traced need not be recompiled for this, so you can
 use it on binaries for which you don't have source.
 .
 System calls and signals are events that happen at the user/kernel
 interface. A close examination of this boundary is very useful for bug
 isolation, sanity checking and attempting to capture race conditions..

%prep
%setup -q -n %{name}-%{version}


%build
cp %{SOURCE1001} .
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/license
for keyword in LICENSE COPYING COPYRIGHT;
do
	for file in `find %{_builddir} -name $keyword`;
	do
		cat $file >> $RPM_BUILD_ROOT%{_datadir}/license/%{name};
		echo "";
	done;
done

# license
mkdir -p %{buildroot}/usr/share/license
cp COPYRIGHT %{buildroot}/usr/share/license/%{name}

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_datadir}/license/%{name}
%{_bindir}/strace
/usr/share/license/%{name}
