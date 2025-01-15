
// 实现一个选中翻译的浏览器插件
chrome.contextMenus.create({
    type: "normal",
    title: "Quick translation",
    contexts: ["selection", "link"],
    onclick: function (info) {
        window.open(`https://fanyi.baidu.com/#en/zh/${info.selectionText}`)
    }
}, function() {

})