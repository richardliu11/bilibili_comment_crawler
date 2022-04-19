# bilibili_comment_crawler
B站视频下方评论数据抓取

## 文档说明
- \<BvToAv\>.py 由于评论API接口仅支持传入AV号，故需要先将视频链接中的BV号转换为AV号。
- <B站评论爬虫>.py 数据抓取程序
 

## AV2BV2OID 示例
- BV:	BV1pa411z7VB
- AV:	av210376916
- oid: 210376916

## 使用步骤
- 执行 \<BvToAv\>.py，输入Bv号，转为AV号
- 删除AV号中的av字符
- 输入评论API中
- 确定总评论数，根评论数
- 执行
- 输出为本地XLSX文件
