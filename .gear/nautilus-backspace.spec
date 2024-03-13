Name: nautilus-backspace
Version: 0.4.0
Release: alt1

Summary: extension for configuring the backtrack combination for Gnome nautilus
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/alt-gnome-team/nautilus-backspace

BuildArch: noarch

Source: %name-%version.tar

Requires: nautilus-python
Requires: libnautilus-gir

%description
The extension allows you to return to the previous directory in Nautilus by
pressing the backspace button or another keyboard shortcut assigned through
the configuration file.

%description -l ru_RU.UTF-8
Расширение позволяет возвращаться в предыдущую директорию в Nautilus по
нажатию кнопки backspace или иного сочетания клавиш, назначенного через
файл конфигурации.

%prep
%setup -v

%install
mkdir -p %buildroot%_datadir/nautilus-python/extensions/
cp Back.py %buildroot%_datadir/nautilus-python/extensions/
mkdir -p %buildroot%_sysconfdir/%name/
cp config %buildroot%_sysconfdir/%name/

%files
%_datadir/nautilus-python/extensions/Back.py
%config(noreplace) %_sysconfdir/%name/config

%changelog