# gitPublic

.git �����ص��ļ�Ŀ¼�����ǹ�������
stage(index)�����ݴ���,git �Զ������ĵ�һ����֧master,�Լ�ָ��master��һ��ָ�����HEAD

git �����ܽ�

���ز�����
git config user.name"xx"�����û���xx
git config user.email"xx"�����û���email��xx
git init �����ֿ�  ls -ah ��ʾ����
git add xx.x ����ļ����ֿ��ݴ���
git rm xx.x ɾ���ļ�
git commit -m "xxxx"  �ύ�ֿ��˵��
git status ���յ�ǰ�ֿ��״̬������ʹ�ã�
git diff xx.x	�鿴��ǰxx�ļ�����ʷ�Ĳ�֮ͬ��
git log �汾��ʷ��Ϣ��ֻ�ǵ�ǰ����ʷ��Ϣ��--pretty=oneline  ������ʾ�汾��Ϣ
git log --pretty=oneline --abbrev-commit	���в鿴��ʷ�汾����д�汾��Ϣ
git reset --hard HEAD^ ������һ���汾�����ϸ�^^,��100����~100
git reset --hard 1234567 ����ָ��SHA1ֵ�汾
git reflog ��¼ÿ�ε�����
git checkout --xx.x xx�ļ����ص��汾����ݴ�����״̬������commit �� add ״̬
git reset HEAD file ���ݴ��������ݳ����������ع�������HEAD˵�������µİ汾
git rm xx.x ɾ���汾���е��ļ���Ȼ��git commit -m "xxxx"
git checkout --xx.x ��ɾ�İ汾���е��ļ��滻��������
����Զ�̿�Ĳ���
ssh-keygen -t rsa -C "youremail@example.com"  ����ssh��Կ���ֹ�Կ����Կ�������github��
git remote add my_site git@github.com:gushende/gitPublic.git �ύ���ؿ�my_site ��Զ�̿�gitPblic
git push -u my_site master ���ͱ��ؿ��master ��Զ��
git push my_site master ���ͱ���master��֧�������޸ĵ�Զ�̿�
git push my_site dev ���ͷ�֧dev��Զ��
git checkout -b dev origin/dev���ش���Զ�̵�origin�ķ�֧dev
git pull ��������
git branch --set-upstream dev origin/devָ�����ط�֧��Զ�̷�֧origin/dev������
Զ�ֿ̲��¡����
git clone git@github.com:guishende/gitLocal.git ����Զ�̿�󣬿�¡������
git remote �鿴Զ�̿�
��֧����
git checkout -b dev ������֧dev���л�,�൱��git branch dev;git checkout dev
git branch �鿴��ǰ��֧
git checkout master �л���master��֧
git merge dev ��dev�ķ�֧�ϲ���master��
git branch -d dev ɾ����֧dev
git log --graph --pretty=oneline --abbrev-commit  ��֧�ϲ�ʱ��ͻ���Լ�������ȫ�ɣ������ͻ�����ύ
git merge --no-ff -m "merge with no-ff" dev  ����fastforward -m �ύ����Ϣ����������ʷ�ϲ�
git stash �洢��ǰ�Ĺ����������ɶ��
git stash list �鿴������ֳ�
git stash apply stash@{0} �ָ��ֳ�0��ɾ����git stash drop ɾ���ֳ�
git stash pop �ָ��ֳ���ɾ��stash����
git branch -D dev ǰ��ɾ����֧dev
��ǩ
git tag v1.0	���ǩv1.0
git tag �鿴���еı�ǩ
git tag v0.9 1234567 ��1234567�汾���ǩv0.9
git tag -a v0.1 -m "version 0.1 released" 1234567 ��1234567���ǩ��˵������
git tag -s v0.2 -m "signed version 0.2 released" fec145a	-s ����˽Կǩ���Ĵ��ǩ
git show v0.9	�鿴�汾��ǩv0.9
git tag -d v0.1 ɾ����ǩ
git push origin <tagname> �ƴӱ�ǩ��Զ��
git push origin --tags һ�������ͱ�����δ���͵ı�ǩ��Զ��
git push origin :refs/tags/v0.9 �ȱ���ɾ����ǩ�󣬴�����ɾ��Զ�̱�ǩ
����
git config --global color.ui true	�������ʾ����Ŀ
.gitignore ����һ�����ļ��������Բ����ύ���ļ�
git add -f App.class ǿ���ύ�ļ�App.class
��д
git config --global alias.st status	��st����status,����
git config --global alias.co checkout
git config --global alias.ci commit
git config --global alias.br branch
git config --global alias.unstage 'reset HEAD'����
git config --global alias.last 'log -1'	����ύ����Ϣ
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
�
sudo apt-get install git
sudo adduser git
/home/git/.ssh/authorized_keys	��Կд������ļ���
sudo git init --bare sample.git	Ŀ¼�´���
sudo chown -R git:git sample.gitȨ���޸�
git:x:1001:1001:,,,:/home/git:/usr/bin/git-shell��¼Ȩ���޸ģ�û����/etc/passwd
git clone git@server:/srv/sample.git��¡�����أ�ע��·��
ssh git@192.168.31.185	ssh��¼����

����˵���ĵ���
���ĵ��Ǳ��ش���֮���ϴ���github�ϵġ�
��һ�������ĵ������ֱ��زֿ�����Զ�̵Ĳֿ�������ͬ��
��ʱ�����ɣ��Ժ���취������
����my_site remote:gitPublic

