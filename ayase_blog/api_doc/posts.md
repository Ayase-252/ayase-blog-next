# 文章相关API

## 单篇文章

API格式： `/post/:postId`

参数：
- `:postId`： 文章ID 

### GET

#### 响应

若`postId`所指的文章在数据库中：

响应状态码：200 OK

响应JSON：

```JSON
{
    "title": String,
    "postId": Integer,
    "content": String
}
```

若`postId`所指的文章不在数据库中：

响应状态码：404 NOT FOUND

响应JSON: 无

## 文章集合

API格式:`/posts?from=number&max_pages=number`

Query参数：
 - `from` 从哪一篇文章开始获取，用`postId`标识，若忽略，默认从最新的文章开始。（可选）
 - `max_pages` 最多获取文章数。若数据库中文章不足，会返回所有剩余文章。

### GET

#### 响应

响应状态码：200 OK

响应JSON：

```JSON
{
    "num_pages": number, // 响应中的文章数
    "pages": [{
        "title": string,
        "postId": number,
        "content": string
    }]
}
```

注意：会以`postId`倒序的方式发送。
