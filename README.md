# haruka99
vup白神遥的《白氏乘法表》网页展示版，可用github pages访问（其实就是我的github pages习作）

访问链接：https://dan-kuroto.github.io/haruka99/

## 开发

### 新增音声
DD的能力是有极限的，而且我最近要忙着找实习，所以音频有缺省，并且我肯定漏了很多豹豹背错乘法表的记录，这方面就要麻烦大家帮我了……

会编程的请务必直接 PR！<del>（没错我就是这么懒）</del>

不会编程的给我BV号和出现时间就行，我有空会更新的。（B站视频评论区、B站私信、issue都行吧）

### 注意
github pages所用的路径与在本地测试的时候的路径是不一样的，要在前面加上项目名称！这也是为什么我编写了 `app.py` 。

`app.py` 这个文件与本项目期望实现的功能无关，只是因为github pages中的路径与项目内的路径不同(要在前面加上项目名称)，导致本地测试不方便，所以我用 `flask` 写了个轻量级的测试工具而已。

使用方法就是先 `pip install flask` 安装完成之后 `flask run` 即可，然后访问 `http://localhost:5000/haruka99` 即可。

### 二次开发
本项目基于MIT协议开源，如果你也想为自己D的不擅长乘法表的V制作类似的东西，可以在协议范围内随意使用源码，但你仍应当注意以下几点：
1. 各种文件替换干净，所有代码、包括这个 `README.md` 里的 vup 名称等信息也要全部修改为对应的 vup。否则混起来的话会很尴尬的。
2. github pages的访问路径是 `https://{你的GitHub用户名}.github.io/{存储库名称}/` ，为了方便记忆，在创建存储库的时候取一个和对应 vup 有关的名字。
