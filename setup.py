from os import path as os_path

from setuptools import setup, find_packages

from easy_clash_tool import __version__

this_directory = os_path.abspath(os_path.dirname(__file__))


# 读取文件内容
def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


if __name__ == '__main__':
    setup(
        name='easy_clash_tool',  # 包名
        # python_requires='>=2.7',  # python环境
        version=__version__,  # 包的版本
        description="easy_clash_tool是一个clash的python库,可以很便捷的自动切换可用节点",  # 包简介，显示在PyPI上
        long_description=read_file('README.md'),  # 读取的Readme文档内容
        long_description_content_type="text/markdown",  # 指定包文档格式为markdown
        author="hanxinkong",  # 作者相关信息
        author_email='xinkonghan@gmail.com',
        url='https://easy-clash-tool.xink.top/',
        packages=find_packages(),
        install_requires=read_requirements('requirements.txt'),  # 指定需要安装的依赖
        license="MIT",
        keywords=['easy', 'clash', 'tool'],
        classifiers=[
            # 发展时期,常见的如下
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 5 - Production/Stable',

            'Environment :: Console',

            # 开发的目标用户
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',

            'Operating System :: OS Independent',

            # 属于什么类型
            'Topic :: System :: Monitoring',
            'Topic :: System :: Networking',
            'Topic :: System :: Networking :: Firewalls',
            'Topic :: System :: Networking :: Monitoring',

            # 许可证信息
            'License :: OSI Approved :: MIT License',

            # 目标 Python 版本
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10'
            'Programming Language :: Python :: 3.11'
        ]
    )
