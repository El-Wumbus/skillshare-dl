# Skillshare downloader

Install/Build Dependencies: *`pip`*  
Dependencies: *`python3`, `python-slugify`, `requests`*

## Setup
--------
1. Clone the git repo and enter the directory.

```bash
git clone https://github.com/el-wumbus/skillshare-dl
cd ./skillshare-dl/src
```

2. Go to [Skillshare.com](https://skillshare.com)

3. After logging in, enter the javascript console using F12 and picking the console tab.

4. Type `document.cookie` and copy the output.

> If the output is wrapped in quotes, omit them.

5. run `load-cookies.sh`, or `load-cookies.ps1` for windows users. The script will ask for the cookies interactively; just run it and paste the cookies into the prompt and click enter.

6. install dependencies with pip,

```bash
pip install -r ./requirements.txt
```

## Usage
-----
```bash
python3 ./skillshare-dl.py -u <url> #for URL
python3 ./skillshare-dl.py -i <course ID> # for ID
```

The output of the folowing will be in a `./data/` directory

### Adding to path/making it a command

*The Following is only for users of unix-like operating systems.

Directory: **skillshare-dl/src**

```bash
sudo mkdir /opt/skillshare-dl
mkdir ./data
mkdir $HOME/skillshare-out
cp ./* /opt/skillshare-dl
ln -s /opt/sillshare-dl/skillshare-dl.py /usr/bin/skillshare-dl
ln -s $(pwd)/data/ $HOME/skillshare-dl
```

> The above method of "installing" this tool ins't a great one. If you'd like to improve it you can do so and make a pull request. I'd do it myself but i don't care enough to.
