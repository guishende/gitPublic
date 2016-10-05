# gitPublic

.git 是隐藏的文件目录，不是工作区。
stage(index)叫做暂存区,git 自动创建的第一个分支master,以及指向master的一个指针叫做HEAD

git 命令总结

本地操作库
git config user.name"xx"配置用户名xx
git config user.email"xx"配置用户的email是xx
git init 创建仓库  ls -ah 显示出来
git add xx.x 添加文件到仓库暂存区
git rm xx.x 删除文件
git commit -m "xxxx"  提交仓库的说明
git status 掌握当前仓库的状态（经常使用）
git diff xx.x	查看当前xx文件与历史的不同之处
git log 版本历史信息（只是当前的历史信息）--pretty=oneline  单行显示版本信息
git log --pretty=oneline --abbrev-commit	单行查看历史版本，缩写版本信息
git reset --hard HEAD^ 返回上一个版本，上上个^^,上100个，~100
git reset --hard 1234567 返回指定SHA1值版本
git reflog 记录每次的命令
git checkout --xx.x xx文件返回到版本库或暂存区的状态，就是commit 或 add 状态
git reset HEAD file 吧暂存区的数据撤销掉，返回工作区。HEAD说明是最新的版本
git rm xx.x 删除版本库中的文件。然后git commit -m "xxxx"
git checkout --xx.x 误删的版本库中的文件替换到工作区
链接远程库的操作
ssh-keygen -t rsa -C "youremail@example.com"  生成ssh密钥，分公钥和密钥，添加在github中
git remote add my_site git@github.com:gushende/gitPublic.git 提交本地库my_site 到远程库gitPblic
git push -u my_site master 推送本地库的master 到远程
git push my_site master 推送本地master分支的最新修改到远程库
git push my_site dev 推送分支dev到远程
git checkout -b dev origin/dev本地创建远程的origin的分支dev
git pull 下载下来
git branch --set-upstream dev origin/dev指定本地分支与远程分支origin/dev的链接
远程仓库克隆下来
git clone git@github.com:guishende/gitLocal.git 创建远程库后，克隆到本地
git remote 查看远程库
分支管理
git checkout -b dev 创建分支dev并切换,相当于git branch dev;git checkout dev
git branch 查看当前分支
git checkout master 切换到master分支
git merge dev 把dev的分支合并到master上
git branch -d dev 删除分支dev
git log --graph --pretty=oneline --abbrev-commit  分支合并时冲突会自己内容中全由，解决冲突后再提交
git merge --no-ff -m "merge with no-ff" dev  禁用fastforward -m 提交的信息，看不出历史合并
git stash 存储当前的工作场景，可多次
git stash list 查看保存的现场
git stash apply stash@{0} 恢复现场0不删除，git stash drop 删除现场
git stash pop 恢复现场并删除stash内容
git branch -D dev 前行删除分支dev
标签
git tag v1.0	打标签v1.0
git tag 查看所有的标签
git tag v0.9 1234567 给1234567版本大标签v0.9
git tag -a v0.1 -m "version 0.1 released" 1234567 给1234567打标签和说明文字
git tag -s v0.2 -m "signed version 0.2 released" fec145a	-s 给用私钥签名的打标签
git show v0.9	查看版本标签v0.9
git tag -d v0.1 删除标签
git push origin <tagname> 推从标签到远程
git push origin --tags 一次性推送本地尚未推送的标签到远程
git push origin :refs/tags/v0.9 先本地删除标签后，此命令删除远程标签
其他
git config --global color.ui true	让命令窗显示更醒目
.gitignore 创建一个此文件，来忽略不想提交的文件
git add -f App.class 强制提交文件App.class
缩写
git config --global alias.st status	用st代替status,如下
git config --global alias.co checkout
git config --global alias.ci commit
git config --global alias.br branch
git config --global alias.unstage 'reset HEAD'撤销
git config --global alias.last 'log -1'	最后提交的信息
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
搭建
sudo apt-get install git
sudo adduser git
/home/git/.ssh/authorized_keys	公钥写进这个文件中
sudo git init --bare sample.git	目录下创建
sudo chown -R git:git sample.git权限修改
git:x:1001:1001:,,,:/home/git:/usr/bin/git-shell登录权限修改（没做）/etc/passwd
git clone git@server:/srv/sample.git克隆到本地，注意路径
ssh git@192.168.31.185	ssh登录测试

这是说明文档：
本文档是本地创建之后，上传到github上的。
第一次做的文档，出现本地仓库名和远程的仓库名不相同。
暂时这样吧，以后想办法改正。
本地my_site remote:gitPublic