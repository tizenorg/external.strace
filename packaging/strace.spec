#sbs-git:slp/pkgs/s/strace strace 4.5.20 c85d16265104f1b4b4e0793e61d1f3bb4605f5a6
Name:       strace
Summary:    A system call tracer
Version: 4.5.20
Release:    1
Group:      utils
License:    BSD3c
URL:        http://sourceforge.net/projects/strace/
Source0:    strace-4.5.20.tar.gz

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

%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%files
%defattr(-,root,root,-)
%{_bindir}/strace
