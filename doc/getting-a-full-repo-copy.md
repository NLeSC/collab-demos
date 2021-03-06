
# Getting a full, local copy of this repo

## Windows 7 and later

Let's say you're on Windows and want to get a local copy of this repository. There is a ``Download ZIP`` button on the [main](../../../) website, but that does curently not give you all the files in the repository (it skips the larger files, which are stored in [git-lfs](https://git-lfs.github.com/)). Fortunately, there is a relatively simple solution:

1. Download and install GitHub Desktop from [http://desktop.github.com/](http://desktop.github.com/)
3. Start the application by clicking the icon on your desktop
4. Login with your GitHub credentials
5. In the upper left corner of the application, click the '+' sign button
6. At the top of the dialog, there are 3 options, ``Add``, ``Create``, and ``Clone``. Select ``Clone``
7. You now see the repositories of which you are a member
8. Select ``collab-demos`` and click on the tick mark at the bottom
9. Wait for the download to finish
10. Use your file explorer to navigate to the local copy of your repository, it should include all files, including local copies of large (video) files.



## Linux (Ubuntu)

```
# make sure you have git
sudo apt-get install git

# get a full copy
git clone https://github.com/NLeSC/collab-demos.git

```
