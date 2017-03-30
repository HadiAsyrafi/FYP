Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> ls

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    ls
NameError: name 'ls' is not defined
>>> f = open('/home/hadi/users.txt')

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    f = open('/home/hadi/users.txt')
IOError: [Errno 2] No such file or directory: '/home/hadi/users.txt'
>>> f = open('/home/hadi/users')
>>> f
<open file '/home/hadi/users', mode 'r' at 0x7f7cdf95f8a0>
>>> users = f.readlines()
>>> users
['Jacob\tjacob@gmail.com\n', 'Hannah\tbanana@gmail.com\n']
>>> f
<open file '/home/hadi/users', mode 'r' at 0x7f7cdf95f8a0>
>>> f.close()
>>> type(f)
<type 'file'>
>>> type(users)
<type 'list'>
>>> f = open('/home/hadi/users')
>>> users = f.readline()
>>> type(users)
<type 'str'>
>>> users
'Jacob\tjacob@gmail.com\n'
>>> user2 = f.readline()
>>> user2
'Hannah\tbanana@gmail.com\n'
>>> user3 = f.readline()
>>> user3
''
>>> import os
>>> os.getcwd()
'/home/hadi'
>>> os.listdir()

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    os.listdir()
TypeError: listdir() takes exactly 1 argument (0 given)
>>> os.listdir()

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    os.listdir()
TypeError: listdir() takes exactly 1 argument (0 given)
>>> directory = os.getcwd()
>>> os.listdir(directory)
['.Xauthority', '.gconf', 'Public', '.ICEauthority', '.bash_logout', 'Downloads', '.xsession-errors.old', '.idlerc', '.bash_history', 'Pictures', '.cache', 'Templates', 'Desktop', 'users', 'examples.desktop', '.gnupg', 'Videos', '.compiz', '.xsession-errors', '.profile', 'Documents', 'Music', '.sudo_as_admin_successful', '.config', '.local', '.mozilla', '.bashrc']
>>> os.listdir('.')
['.Xauthority', '.gconf', 'Public', '.ICEauthority', '.bash_logout', 'Downloads', '.xsession-errors.old', '.idlerc', '.bash_history', 'Pictures', '.cache', 'Templates', 'Desktop', 'users', 'examples.desktop', '.gnupg', 'Videos', '.compiz', '.xsession-errors', '.profile', 'Documents', 'Music', '.sudo_as_admin_successful', '.config', '.local', '.mozilla', '.bashrc']
>>> os.listdir(".")
['.Xauthority', '.gconf', 'Public', '.ICEauthority', '.bash_logout', 'Downloads', '.xsession-errors.old', '.idlerc', '.bash_history', 'Pictures', '.cache', 'Templates', 'Desktop', 'users', 'examples.desktop', '.gnupg', 'Videos', '.compiz', '.xsession-errors', '.profile', 'Documents', 'Music', '.sudo_as_admin_successful', '.config', '.local', '.mozilla', '.bashrc']
>>> dirs = os.walk('.')
>>> dirs.next()
('.', ['.gconf', 'Public', 'Downloads', '.idlerc', 'Pictures', '.cache', 'Templates', 'Desktop', '.gnupg', 'Videos', '.compiz', 'Documents', 'Music', '.config', '.local', '.mozilla'], ['.Xauthority', '.ICEauthority', '.bash_logout', '.xsession-errors.old', '.bash_history', 'users', 'examples.desktop', '.xsession-errors', '.profile', '.sudo_as_admin_successful', '.bashrc'])
>>> dirs.next()
('./.gconf', [], [])
>>> dirs.next()
('./Public', [], [])
>>> dirs.next()
('./Downloads', [], ['Fedora-Workstation-Live-x86_64-25-1.3.iso.part', 'debian-8.7.1-amd64-netinst.iso'])
>>> dirs.next()
('./.idlerc', [], ['recent-files.lst'])
>>> dirs.next()
('./Pictures', [], [])
>>> dirs.next()
('./.cache', ['thumbnails', 'upstart', 'compizconfig-1', 'gstreamer-1.0', 'gnome-software', 'evolution', 'update-manager-core', 'logrotate', 'fontconfig', 'ibus', 'mozilla', 'wallpaper'], ['zeitgeist-vacuum.stamp', 'event-sound-cache.tdb.5d1d5981cf354ab79d1fbf42e6cd2351.x86_64-pc-linux-gnu'])
>>> dirs.next()
('./.cache/thumbnails', ['large'], [])
>>> dirs.next()
('./.cache/thumbnails/large', [], ['60c41bee9f7f5f1901a5c2efab479721.png', 'c82d216c0f4102512f2dc5e5dc07ecbb.png', 'bc1500b5f613e3e1f9092a1057307f2c.png', '6a582001e34c5c91d3c2ad500c71b1a3.png'])
>>> dirs.next()
('./.cache/upstart', [], ['dbus.log', 'ssh-agent.log.2.gz', 'indicator-application.log.1.gz', 'unity7.log.2.gz', 'upstart-event-bridge.log.2.gz', 'indicator-sound.log', 'indicator-sound.log.2.gz', 'gpg-agent.log.1.gz', 'upstart-event-bridge.log.1.gz', 'gpg-agent.log.2.gz', 'hud.log', 'gnome-keyring-ssh.log.2.gz', 'gnome-keyring-ssh.log.1.gz', 'unity-settings-daemon.log.1.gz', 'unity7.log', 'indicator-keyboard.log.1.gz', 'unity-settings-daemon.log.2.gz', 'window-stack-bridge.log.2.gz', 'unity-panel-service.log.1.gz', 'indicator-sound.log.1.gz', 'indicator-session.log.1.gz', 'at-spi2-registryd.log.1.gz', 'dbus.log.1.gz', 'gnome-keyring.log.2.gz', 'unity7.log.1.gz', 'indicator-printers.log.1.gz', 'ssh-agent.log.1.gz', 'window-stack-bridge.log.1.gz', 'update-notifier-release.log.1.gz', 'hud.log.1.gz', 'gnome-keyring.log.1.gz', 'dbus.log.2.gz', 'unity-panel-service.log.2.gz'])
>>> dirs.next()
('./.cache/compizconfig-1', [], ['session.pb', 'unitymtgrabhandles.pb', 'expo.pb', 'animation.pb', 'composite.pb', 'workarounds.pb', 'imgpng.pb', 'opengl.pb', 'move.pb', 'commands.pb', 'vpswitch.pb', 'fade.pb', 'gnomecompat.pb', 'decor.pb', 'mousepoll.pb', 'wall.pb', 'scale.pb', 'regex.pb', 'compiztoolbox.pb', 'place.pb', 'unityshell.pb', 'matecompat.pb', 'resize.pb', 'core.pb', 'grid.pb', 'ezoom.pb', 'snap.pb', 'staticswitcher.pb', 'switcher.pb', 'copytex.pb'])
>>> dirs.next()
('./.cache/gstreamer-1.0', [], ['registry.x86_64.bin'])
>>> dirs.next()
('./.cache/gnome-software', ['3.20'], [])
>>> dirs.next()
('./.cache/gnome-software/3.20', ['firmware'], [])
>>> dirs.next()
('./.cache/gnome-software/3.20/firmware', [], ['firmware.xml.gz', 'firmware.xml.gz.asc'])
>>> dirs.next()
('./.cache/evolution', ['sources', 'calendar', 'memos', 'mail', 'addressbook', 'tasks'], [])
>>> dirs.next()
('./.cache/evolution/sources', ['trash'], [])
>>> dirs.next()
('./.cache/evolution/sources/trash', [], [])
>>> dirs.next()
('./.cache/evolution/calendar', ['trash'], [])
>>> dirs.next()
('./.cache/evolution/calendar/trash', [], [])
>>> dirs.next()
('./.cache/evolution/memos', ['trash'], [])
>>> dirs.next()
('./.cache/evolution/memos/trash', [], [])
>>> dirs.next()
('./.cache/evolution/mail', ['trash'], [])
>>> dirs.next()
('./.cache/evolution/mail/trash', [], [])
>>> dirs.next()
('./.cache/evolution/addressbook', ['trash'], [])
>>> dirs.next()
('./.cache/evolution/addressbook/trash', [], [])
v
>>> dirs.next()
('./.cache/evolution/tasks', ['trash'], [])
>>> dirs.next()
('./.cache/evolution/tasks/trash', [], [])
>>> dirs.next()
('./.cache/update-manager-core', [], ['meta-release-lts'])
>>> dirs.next()
('./.cache/logrotate', [], ['status'])
>>> dirs.next()
('./.cache/fontconfig', [], ['4794a0821666d79190d59a36cb4f44b5-le64.cache-6', 'CACHEDIR.TAG'])
>>> os.listdir('.')
['.Xauthority', '.gconf', 'Public', '.ICEauthority', '.bash_logout', 'Downloads', '.xsession-errors.old', '.idlerc', '.bash_history', 'Pictures', '.cache', 'Templates', 'Desktop', 'users', 'examples.desktop', '.gnupg', 'Videos', '.compiz', '.xsession-errors', '.profile', 'Documents', 'Music', '.sudo_as_admin_successful', '.config', '.local', '.mozilla', '.bashrc']
>>> os.stat('users')
posix.stat_result(st_mode=33204, st_ino=525491, st_dev=2055, st_nlink=1, st_uid=1000, st_gid=1000, st_size=46, st_atime=1489106374, st_mtime=1489106287, st_ctime=1489106297)
>>> stats = os.stat('users')
>>> stats.st_size()

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    stats.st_size()
TypeError: 'int' object is not callable
>>> stats = os.stat('users')
>>> stats
posix.stat_result(st_mode=33204, st_ino=525491, st_dev=2055, st_nlink=1, st_uid=1000, st_gid=1000, st_size=46, st_atime=1489106374, st_mtime=1489106287, st_ctime=1489106297)
>>> stats.st_mode()

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    stats.st_mode()
TypeError: 'int' object is not callable
>>> stats.st_size
46
>>> stats.st_size/1000.00
0.046
>>> stats.st_time

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    stats.st_time
AttributeError: 'posix.stat_result' object has no attribute 'st_time'
>>> stats.st_atime
1489106374.5624313
>>> from datetime import datetime
>>> datetime.fromtimestamp(stats.st_atime)
datetime.datetime(2017, 3, 10, 8, 39, 34, 562431)
>>> print datetime.fromtimestamp(stats.st_atime)
2017-03-10 08:39:34.562431
>>> 
