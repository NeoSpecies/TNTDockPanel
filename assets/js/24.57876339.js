(window.webpackJsonp=window.webpackJsonp||[]).push([[24],{356:function(t,s,a){"use strict";a.r(s);var r=a(8),n=Object(r.a)({},(function(){var t=this,s=t.$createElement,a=t._self._c||s;return a("ContentSlotsDistributor",{attrs:{"slot-key":t.$parent.slotKey}},[a("h3",{attrs:{id:"配置管理"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#配置管理"}},[t._v("#")]),t._v(" 配置管理")]),t._v(" "),a("p",[a("code",[t._v("DockerConfigs")]),t._v(" 类提供了一系列方法来管理 Docker 配置，包括创建、列出、获取详情和删除配置。")]),t._v(" "),a("h4",{attrs:{id:"使用方式"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#使用方式"}},[t._v("#")]),t._v(" 使用方式")]),t._v(" "),a("p",[t._v("首先，请确保您有 Docker 守护程序正在运行，并且您有与 Docker 交互的必要权限。")]),t._v(" "),a("p",[t._v("实例化类：")]),t._v(" "),a("div",{staticClass:"language-python extra-class"},[a("pre",{pre:!0,attrs:{class:"language-python"}},[a("code",[a("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("from")]),t._v(" your_module_name "),a("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" DockerConfigs  "),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("# 将 your_module_name 替换为您模块的实际名称")]),t._v("\n\ndocker_configs "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" DockerConfigs"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n")])])]),a("h4",{attrs:{id:"创建配置"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#创建配置"}},[t._v("#")]),t._v(" 创建配置")]),t._v(" "),a("p",[t._v("创建一个新的配置项：")]),t._v(" "),a("div",{staticClass:"language-python extra-class"},[a("pre",{pre:!0,attrs:{class:"language-python"}},[a("code",[t._v("create_result "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" docker_configs"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("create_config"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("name"),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"myconfig"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" data"),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"config_data_here"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n")])])]),a("h5",{attrs:{id:"示例响应"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#示例响应"}},[t._v("#")]),t._v(" 示例响应：")]),t._v(" "),a("div",{staticClass:"language-json extra-class"},[a("pre",{pre:!0,attrs:{class:"language-json"}},[a("code",[a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n  "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v('"id"')]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"k3mno4567pqr89stuvwx"')]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n")])])]),a("h4",{attrs:{id:"列出配置"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#列出配置"}},[t._v("#")]),t._v(" 列出配置")]),t._v(" "),a("p",[t._v("列出所有配置项：")]),t._v(" "),a("div",{staticClass:"language-python extra-class"},[a("pre",{pre:!0,attrs:{class:"language-python"}},[a("code",[t._v("list_result "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" docker_configs"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("list_configs"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n")])])]),a("h5",{attrs:{id:"示例响应-2"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#示例响应-2"}},[t._v("#")]),t._v(" 示例响应：")]),t._v(" "),a("div",{staticClass:"language-json extra-class"},[a("pre",{pre:!0,attrs:{class:"language-json"}},[a("code",[a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n  "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v('"configs"')]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),a("span",{pre:!0,attrs:{class:"token property"}},[t._v('"id"')]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"abcd1234efgh5678ijkl"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v('"name"')]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"myconfig"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n  "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n")])])]),a("h4",{attrs:{id:"获取配置详情"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#获取配置详情"}},[t._v("#")]),t._v(" 获取配置详情")]),t._v(" "),a("p",[t._v("获取特定配置的详细信息：")]),t._v(" "),a("div",{staticClass:"language-python extra-class"},[a("pre",{pre:!0,attrs:{class:"language-python"}},[a("code",[t._v("get_result "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" docker_configs"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("get_config_details"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("config_id"),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"abcd1234efgh5678ijkl"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n")])])]),a("h5",{attrs:{id:"示例响应-3"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#示例响应-3"}},[t._v("#")]),t._v(" 示例响应：")]),t._v(" "),a("div",{staticClass:"language-json extra-class"},[a("pre",{pre:!0,attrs:{class:"language-json"}},[a("code",[a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n  "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v('"id"')]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"abcd1234efgh5678ijkl"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n  "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v('"name"')]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"myconfig"')]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n")])])]),a("h4",{attrs:{id:"删除配置"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#删除配置"}},[t._v("#")]),t._v(" 删除配置")]),t._v(" "),a("p",[t._v("通过 ID 删除配置：")]),t._v(" "),a("div",{staticClass:"language-python extra-class"},[a("pre",{pre:!0,attrs:{class:"language-python"}},[a("code",[t._v("remove_result "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" docker_configs"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("remove_config"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("config_id"),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"abcd1234efgh5678ijkl"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n")])])]),a("h5",{attrs:{id:"示例响应-4"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#示例响应-4"}},[t._v("#")]),t._v(" 示例响应：")]),t._v(" "),a("div",{staticClass:"language-json extra-class"},[a("pre",{pre:!0,attrs:{class:"language-json"}},[a("code",[a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n  "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v('"message"')]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"Config removed"')]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n")])])]),a("h4",{attrs:{id:"错误处理"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#错误处理"}},[t._v("#")]),t._v(" 错误处理")]),t._v(" "),a("p",[t._v("如果出现错误，响应将包括错误代码和消息，指示出了什么问题。例如，如果您尝试获取一个不存在的配置：")]),t._v(" "),a("div",{staticClass:"language-python extra-class"},[a("pre",{pre:!0,attrs:{class:"language-python"}},[a("code",[t._v("error_response "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" docker_configs"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("get_config_details"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("config_id"),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"nonexisting"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n")])])]),a("h5",{attrs:{id:"示例错误响应"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#示例错误响应"}},[t._v("#")]),t._v(" 示例错误响应：")]),t._v(" "),a("div",{staticClass:"language-json extra-class"},[a("pre",{pre:!0,attrs:{class:"language-json"}},[a("code",[a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n  "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v('"error"')]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v('"code"')]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("404")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v('"message"')]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"Config not found"')]),t._v("\n  "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n")])])])])}),[],!1,null,null,null);s.default=n.exports}}]);