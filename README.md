# 浏览器插件开发

[官方文档](https://developer.chrome.com/docs/extensions/get-started?hl=zh-cn)

## 配置文件
manifes.json
```
{
    "manifest_version": 2,
    "name": "Quick translation",
    "description": "通过选中一个单子或者一个句子，或者一段话，快速跳转到百度翻译页面",
    "version": "1.0.0",
    "icons": {
        "16": "images/daibanshixiang-16.png",
        "32": "images/daibanshixiang-32.png",
        "48": "images/daibanshixiang-48.png"
    },
    "background": {
        "scripts": ["background.js"]
    },
    "permissions": [
        "contextMenus"
    ]
}

``` 