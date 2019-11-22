1. 安装mysql数据库
2. 安装anaconda
3. conda create -n py36 python=3.6
4. activate py36
5. pip install -r requirements.txt
6. 修改项目的python环境， 再修改项目中 news/settings.py 和 other/home_crawldata.py 文件里面的相关数据库配置文件
7. 删除项目中的home/migrations文件夹，  再使用cmd切换到项目根目录，执行 python manage.py makegrations home , 命令成功后执行 python manage.py migrate 命令执行完后数据库就创建成功了，
项目应该就能运行了，但是爬虫相关的数据库配置还需要修改一下
8. 替换pyspider 的数据库文件， 在爬虫里面引用了项目中的 other/home_crawldata.py 文件连接数据库，由于路径是写死的，会导致数据库无法访问，
因此需要把other/home_crawldata.py 的路径加入到python 的系统路径中。 具体方法是：先使用conda info -e 找到py36环境的安装路径，例如
(py36) ➜  site-packages conda info -e
base                     /home/chencai/anaconda3
py36                  *  /home/chencai/anaconda3/envs/py36
这里的py36环境的路径就是/home/chencai/anaconda3/envs/py36  ，
接下来在/home/chencai/anaconda3/envs/py36/lib/python3.6/site-packages 这个路径下面新建一个文件， 文件名my.pth ,内容是 other/home_crawldata.py 这个文件的绝对路径
重启爬虫程序，看下爬到的数据能不能写入数据库
9. 项目的关键词提取，摘要提取等功能目前是通过手动的方式运行的，运行方式是右键单击项目中的 other/news_annlysis.py 文件选择运行即可，运行完成后完成新闻的关键词提取和文本摘要等功能。
10 python manage.py runserver
11 访问 127.0.0.1:8000/index 就能访问项目主页了

