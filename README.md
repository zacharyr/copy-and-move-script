Copy-and-Move-Script
====================

<ul>
<li>The purpose of this script is to give users the ability to copy or move directories (including subdirectories) or files (including the skipping of subdirectories) to a single destination of their choice. The user is asked 4 simple questions (2 of them being source/destination) and the script works through everything else for them.</li>
<li>This script utilizes python's built in <a title="Distutils" href="http://docs.python.org/library/distutils.html">distutils</a> library to copy / move directories and files.</li>
</ul>

<h2>Making it Executable</h2>

<h3>For Linux users:</h3>

<ol>
<li>Type the following command in terminal: <code>$ chmod +x copy_move_script.py</code> (assuming you have python installed to run the script).</li>
</ol>

<h3>For Windows users:</h3>

<ol>
<li>Download and install <a title="Python" href="http://www.python.org/download/">Python</a>, <a title="PyInstaller" href="http://www.pyinstaller.org/">PyInstaller</a>, and <a title="PyWin32" href="http://sourceforge.net/projects/pywin32/files/">PyWin32</a> if you have not already installed it.</li>
<li>After you downloaded and installed the previous packages, run the following command in your python terminal: <code>python pyinstaller.py -F copy_move_script.py</code>. 
<li>Running the previous command will create a single file (-F option) executable which you can place on a computer that does or even does not have python installed. This is ideal for putting the script on a flash drive so you can move directories or files on the go, involving multiple computers.</li>
</ol>

<h2>Authors</h2>
<a title="Zach Rohde" href="http://zachrohde.com">Zach Rohde</a>