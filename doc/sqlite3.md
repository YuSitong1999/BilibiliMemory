# SQLite3 数据库

## 数据表格式

### UP主信息表(upper)

| 英文名          | 含义        | 类型   | 备注          | 
|--------------|-----------|------|-------------|
| id           | UP主ID     | INT  | PRIMARY KEY |
| name         | 名字        | TEXT |             |
| introduction | 介绍        | TEXT |             |
| update_time  | 本地记录更新时间戳 | INT  |             |

### 投稿信息表(media)

| 英文名           | 含义        | 类型       | 备注                                      | 
|---------------|-----------|----------|-----------------------------------------|
| bv_id         | bv号       | CHAR(12) | PRIMARY KEY                             |
| up_id         | up主ID     | INT      | FOREIGN KEY(up_id) REFERENCES upper(id) |
| title         | 标题        | TEXT     |                                         |
| introduction  | 介绍        | TEXT     |                                         |
| duration      | 时长秒数      | INT      |                                         |
| create_time   | 创建时间戳     | INT      |                                         |
| favorite_time | 收藏时间戳     | INT      | 对于非收藏，同创建时间戳                            |
| update_time   | 数据最后更新时间戳 | INT      |                                         |
| is_local      | 已保存到本地    | BOOL     |                                         |
| is_delete     | 线上已删除     | BOOL     |                                         |

### 投稿所属目标表(media_aim)

| 英文名    | 含义    | 类型       | 备注                                         | 
|--------|-------|----------|--------------------------------------------|
| bv_id  | bv号   | CHAR(12) | FOREIGN KEY(bv_id) REFERENCES media(bv_id) |
| aim_id | up主ID | INT      | FOREIGN KEY(aim_id) REFERENCES aim(id)     |

PRIMARY KEY(bv_id, aim_id)

### 下载目标表(aim)

| 英文名         | 含义      | 类型   | 备注                        | 
|-------------|---------|------|---------------------------|
| id          | 目标序号    | INT  | PRIMARY KEY AUTOINCREMENT |
| type        | 目标类型    | INT  |                           |
| target_id   | 线上目标ID  | INT  |                           |
| name        | 目标名字    | TEXT |                           |
| update_time | 本地更新时间戳 | INT  |                           |

UNIQUE(typ, target_id)

### 目标限制表(aim_limiter)

| 英文名          | 含义     | 类型  | 备注                                     | 
|--------------|--------|-----|----------------------------------------|
| id           | 限制序号   | INT | PRIMARY KEY AUTOINCREMENT              |
| aim_id       | 下载目标序号 | INT | FOREIGN KEY(aim_id) REFERENCES aim(id) |
| after        | 开始时间戳  | INT | 可为空                                    |
| max_duration | 最大长度   | INT | 可为空                                    |
