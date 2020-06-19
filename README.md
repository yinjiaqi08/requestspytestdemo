- 在命令行执行pytest，会运行当前文件夹及子文件夹中的测试用例
- 在命令行执行pytest  文件名，会运行该文件中的测试用例
- 点为成功，F为失败
- 参考博客地址：https://www.cnblogs.com/dangkai/p/10937762.html
- 接口自动化框架博客：https://www.jianshu.com/p/e31c54bf15ee



### yaml
- 安装：pip install pyyaml
- 参考地址：https://www.runoob.com/w3cnote/yaml-intro.html
```
languages:
  - Ruby
  - Perl
  - Python
websites:
  YAML: yaml.org
  Ruby: ruby-lang.org
  Python: python.org
  Perl: use.perl.org
```
转化为
```
{
  languages: [ 'Ruby', 'Perl', 'Python'],
  websites: {
    YAML: 'yaml.org',
    Ruby: 'ruby-lang.org',
    Python: 'python.org',
    Perl: 'use.perl.org'
  }
}
```