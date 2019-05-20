// JavaScript Document
function  Zhu3d(data,lables,title){
$(function(){
			
	        
			var chart = new iChart.ColumnStacked3D({
					render : 'Zhu3d',
					data: data,
					labels:lables,
					title : {
						text:title,
						color:'#254d70'
					},
					footnote : '数据来源：系统数据库',
					width : 800,
					height : 600,
					column_width:70,
					background_color : '#ffffff',
					shadow : true,
					shadow_blur : 3,
					shadow_color : '#aaaaaa',
					shadow_offsetx : 1,
					shadow_offsety : 0, 
					sub_option:{
						label:{color:'#f9f9f9',fontsize:12,fontweight:600},
						border : {
							width : 2,
							color : '#ffffff'
						} 
					},
					label:{color:'#254d70',fontsize:12,fontweight:600},
					legend:{
						enable:true,
						background_color : null,
						line_height:25,
						color:'#254d70',
						fontsize:12,
						fontweight:600,
						border : {
							enable : false
						}
					},
					tip:{
						enable :true,
						listeners:{
							//tip:提示框对象、name:数据名称、value:数据值、text:当前文本、i:数据点的索引
							parseText:function(tip,name,value,text,i){
								return name+":"+value+ '个';
							}
						} 
					},
					text_space : 16,//坐标系下方的label距离坐标系的距离。
					zScale:0.5,
					xAngle : 50,
					bottom_scale:1.1, 
					coordinate:{
						width:'74%',
						height:'80%',
						board_deep:10,//背面厚度
						pedestal_height:10,//底座高度
						left_board:false,//取消左侧面板 
						shadow:true,//底座的阴影效果
						grid_color:'#6a6a80',//网格线
						wall_style:[{//坐标系的各个面样式
						color : '#6a6a80'
						},{
						color : '#b2b2d3'
						}, {
						color : '#a6a6cb'
						},{
						color : '#6a6a80'
						},{
						color : '#74749b'
						},{
						color : '#a6a6cb'
						}], 
						axis : {
							color : '#c0d0e0',
							width : 0
						}, 
						scale:[{
							 position:'left',	
							 scale_enable : false,
							 start_scale:0,
							 scale_space:20,
							 end_scale:120,
							 label:{color:'#254d70',fontsize:11,fontweight:600}
						}]
					}
			});

			//利用自定义组件构造左上侧单位
			chart.plugin(new iChart.Custom({
					drawFn:function(){
						//计算位置
						var coo = chart.getCoordinate(),
							x = coo.get('originx'),
							y = coo.get('originy');
						//在左上侧的位置，渲染一个单位的文字
						chart.target.textAlign('end')
						.textBaseline('bottom')
						.textFont('600 12px 微软雅黑')
						.fillText('单位(个)',x+10,y-20,false,'#254d70')
						
					}
			}));
			
			chart.draw();
		});
}

function Pie3d(title,data){
		$(function(){
			//var data = data;
			var num=0;
			for(var i=0;i<data.length;i++){
				num+=data[i]['value'];
			}
			var chart = new iChart.Pie3D({
				render : 'Pie3d',
				data: data,
				title : {
					text : title,
					height:40,
					fontsize : 30,
					color : '#282828'
				},
				footnote : {
					text : 'ichartjs.com',
					color : '#486c8f',
					fontsize : 12,
					padding : '0 38'
				},
				sub_option : {
					mini_label_threshold_angle : 40,//迷你label的阀值,单位:角度
					mini_label:{//迷你label配置项
						fontsize:20,
						fontweight:600,
						color : '#ffffff'
					},
					label : {
						background_color:null,
						sign:false,//设置禁用label的小图标
						padding:'0 4',
						border:{
							enable:false,
							color:'#666666'
						},
						fontsize:11,
						fontweight:600,
						color : '#4572a7'
					},
					border : {
						width : 2,
						color : '#ffffff'
					},
					listeners:{
						parseText:function(d, t){
							return ((d.get('value')/num)*100).toFixed(2)+"%/"+d.get('value');//自定义label文本
						}
					} 
				},
				legend:{
					enable:true,
					padding:0,
					offsetx:120,
					offsety:50,
					color:'#3e576f',
					fontsize:20,//文本大小
					sign_size:20,//小图标大小
					line_height:28,//设置行高
					sign_space:10,//小图标与文本间距
					border:false,
					align:'left',
					background_color : null//透明背景
				}, 
				shadow : true,
				shadow_blur : 6,
				shadow_color : '#aaaaaa',
				shadow_offsetx : 0,
				shadow_offsety : 0,
				background_color:'#f1f1f1',
				align:'right',//右对齐
				offsetx:-100,//设置向x轴负方向偏移位置60px
				offset_angle:-90,//逆时针偏移120度
				width : 800,
				height : 600,
				radius:150
			});
			//利用自定义组件构造右侧说明文本
			chart.plugin(new iChart.Custom({
					drawFn:function(){
						//在右侧的位置，渲染说明文字
						chart.target.textAlign('start')
						.textBaseline('top')
						.textFont('600 20px Verdana')
						.fillText('Market Fragmentation:\nTop Mobile\nOperating Systems',120,80,false,'#be5985',false,24)
						.textFont('600 12px Verdana')
						.fillText('Source:ComScore,2012',120,160,false,'#999999');
					}
			}));
			
			chart.draw();
		});
	}
	
function Bar1(data,lables,title){
	$(function(){
				//创建数据
				var data = [
				        	{
				        		name : 'A产品',
				        		value:[2680,2200,1014,2590,2800,3200,2184,3456,2693,2064,2414,2044],
				        		color:'#01acb6',
				        		line_width:2
				        	}
				       ];
				//创建x轴标签文本   
			    var labels = ["一月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月"];
			       
				var chart = new iChart.Area2D({
						render : 'Bar1',
						data: data,
						title:{
							text:'A产品2011年度订单数据分析',
							color:'#eff4f8',
							background_color:'#1c4156',
							height:40,
							border:{
								enable:true,
								width:[0,0,4,0],//只显示下边框
								color:'#173a4e'
							}
						},
						subtitle:{
							text:'单位:万件',//利用副标题设置单位信息
							fontsize:14,
							color:'#eff4f8',
							textAlign:'left',
							padding:'0 40',
							height:20
						},
						footnote:{
							text:'数据来源:企业ERP数据中心',
							color:'#708794',
							padding:'0 20',
							background_color:'#102c3c',
							height:30,
							border:{
								enable:true,
								width:[3,0,0,0],//只显示上边框
								color:'#0f2b3a'
							}
						},
						padding:'5 1',//设置padding,以便title能占满x轴
						sub_option:{
							label:false,
							hollow_inside:false,//设置一个点的亮色在外环的效果
							point_size:10
						},
						tip:{
							enable:true,
							listeners:{
								 //tip:提示框对象、name:数据名称、value:数据值、text:当前文本、i:数据点的索引
								parseText:function(tip,name,value,text,i){
									return labels[i]+"订单数:<span style='color:red'>"+value+"</span>万件";
								}
							}
						},
						width : 800,
						height : 600,
						background_color:'#0c222f',
						gradient:true,
						shadow:true,
						shadow_blur:2,
						shadow_color:'#4e8bae',
						shadow_offsetx:0,
						shadow_offsety:0,
						gradient_mode:'LinearGradientDownUp',//设置一个从下到上的渐变背景
						border:{
							radius:5
						},
						coordinate:{
							width : 600,
							height : 240,
							grid_color:'#506e7d',
							background_color:null,//设置坐标系为透明背景
							scale:[{
								 position:'left',	
								 label:{
									 color:'#eff4f8',
									 fontsize:14,
									 fontweight:600
								 },
								 start_scale:0,
								 end_scale:4000,
								 scale_space:500
							},{
								 position:'bottom',	
								 label:{
									 color:'#506673',
									 fontweight:600
								 },
								 labels:labels
							}]
						}
					});
				
				chart.draw();
			});
	}
	
function Zhuhen1(data,title){
	var data = data;
					$(function(){
						new iChart.Bar2D({
								render : 'Zhuhen1',
								data: data,
								title : title,
								footnote : '数据来源于系统数据库',
								width : 800,
								height : 600,
								coordinate:{
									width:640,
									height:280,
									scale:[{
										 position:'bottom',	
										 start_scale:0,
										 end_scale:25,
										 scale_space:5,
										 listeners:{
											parseText:function(t,x,y){
												return {text:t+""}
											}
										 }
									}]
								},
								rectangle:{
									listeners:{
										drawText:function(r,t){
											return t+"";
										}
									}
								}
						}).draw();
					});
			}

function Zhexian1(value,lables,title){
	$(function(){
			//var flow=[];
			//for(var i=0;i<25;i++){
			//	flow.push(Math.floor(Math.random()*(10+((i%16)*5)))+10);
			//}
			
			var data = [
			         	{
			         		name : 'PV',
			         		value:value,
			         		color:'#ec4646',
			         		line_width:2
			         	}
			         ];
	        
			var labels = ['今天','昨天','前两天','前三天','前四天','前五天','前六天'];
			
			var chart = new iChart.LineBasic2D({
				render : 'Zhexian1',
				data: data,
				align:'center',
				title : {
					text:title,
					font : '微软雅黑',
					fontsize:24,
					color:'#b4b4b4'
				},
				subtitle : {
					text:'',
					font : '微软雅黑',
					color:'#b4b4b4'
				},
				footnote : {
					text:'ichartjs.com',
					font : '微软雅黑',
					fontsize:11,
					fontweight:600,
					padding:'0 28',
					color:'#b4b4b4'
				},
				width : 800,
				height : 600,
				shadow:true,
				shadow_color : '#202020',
				shadow_blur : 8,
				shadow_offsetx : 0,
				shadow_offsety : 0,
				background_color:'#2e2e2e',
				animation : true,//开启过渡动画
				animation_duration:600,//600ms完成动画
				tip:{
					enable:true,
					shadow:true,
					listeners:{
						 //tip:提示框对象、name:数据名称、value:数据值、text:当前文本、i:数据点的索引
						parseText:function(tip,name,value,text,i){
							 return "<span style='color:#005268;font-size:12px;'>"+labels[i]+"漏洞数量约:<br/>"+ "</span><span style='color:#005268;font-size:20px;'>"+value+"个</span>";
						}
					}
				},
				crosshair:{
					enable:true,
					line_color:'#ec4646'
				},
				sub_option : {
					smooth : true,
					label:false,
					hollow:false,
					hollow_inside:false,
					point_size:8
				},
				coordinate:{
					width:640,
					height:260,
					striped_factor : 0.18,
					grid_color:'#4e4e4e',
					axis:{
						color:'#252525',
						width:[0,0,4,4]
					},
					scale:[{
						 position:'left',	
						 start_scale:0,
						 end_scale:100,
						 scale_space:10,
						 scale_size:2,
						 scale_enable : false,
						 label : {color:'#9d987a',font : '微软雅黑',fontsize:11,fontweight:600},
						 scale_color:'#9f9f9f'
					},{
						 position:'bottom',	
						 label : {color:'#9d987a',font : '微软雅黑',fontsize:11,fontweight:600},
						 scale_enable : false,
						 labels:labels
					}]
				}
			});
			//利用自定义组件构造左侧说明文本
			chart.plugin(new iChart.Custom({
					drawFn:function(){
						//计算位置
						var coo = chart.getCoordinate(),
							x = coo.get('originx'),
							y = coo.get('originy'),
							w = coo.width,
							h = coo.height;
						//在左上侧的位置，渲染一个单位的文字
						chart.target.textAlign('start')
						.textBaseline('bottom')
						.textFont('600 11px 微软雅黑')
						.fillText('数量(个)',x-40,y-12,false,'#9d987a')
						.textBaseline('top')
						.fillText('(时间)',x+w+12,y+h+10,false,'#9d987a');
						
					}
			}));
		//开始画图
		chart.draw();
	});
	}

function Zhexian2(value,lables,title){
	$(function(){
			//var flow=[];
			//for(var i=0;i<25;i++){
			//	flow.push(Math.floor(Math.random()*(10+((i%16)*5)))+10);
			//}

			var data = [
			         	{
			         		name : 'PV',
			         		value:value,
			         		color:'#ec4646',
			         		line_width:2
			         	}
			         ];

			var labels = ['今天','昨天','前两天','前三天','前四天','前五天','前六天'];

			var chart = new iChart.LineBasic2D({
				render : 'Zhexian2',
				data: data,
				align:'center',
				title : {
					text:title,
					font : '微软雅黑',
					fontsize:24,
					color:'#b4b4b4'
				},
				subtitle : {
					text:'',
					font : '微软雅黑',
					color:'#b4b4b4'
				},
				footnote : {
					text:'ichartjs.com',
					font : '微软雅黑',
					fontsize:11,
					fontweight:600,
					padding:'0 28',
					color:'#b4b4b4'
				},
				width : 800,
				height : 600,
				shadow:true,
				shadow_color : '#202020',
				shadow_blur : 8,
				shadow_offsetx : 0,
				shadow_offsety : 0,
				background_color:'#2e2e2e',
				animation : true,//开启过渡动画
				animation_duration:600,//600ms完成动画
				tip:{
					enable:true,
					shadow:true,
					listeners:{
						 //tip:提示框对象、name:数据名称、value:数据值、text:当前文本、i:数据点的索引
						parseText:function(tip,name,value,text,i){
							 return "<span style='color:#005268;font-size:12px;'>"+labels[i]+"安全事件数量约:<br/>"+ "</span><span style='color:#005268;font-size:20px;'>"+value+"个</span>";
						}
					}
				},
				crosshair:{
					enable:true,
					line_color:'#ec4646'
				},
				sub_option : {
					smooth : true,
					label:false,
					hollow:false,
					hollow_inside:false,
					point_size:8
				},
				coordinate:{
					width:640,
					height:260,
					striped_factor : 0.18,
					grid_color:'#4e4e4e',
					axis:{
						color:'#252525',
						width:[0,0,4,4]
					},
					scale:[{
						 position:'left',
						 start_scale:0,
						 end_scale:100,
						 scale_space:10,
						 scale_size:2,
						 scale_enable : false,
						 label : {color:'#9d987a',font : '微软雅黑',fontsize:11,fontweight:600},
						 scale_color:'#9f9f9f'
					},{
						 position:'bottom',
						 label : {color:'#9d987a',font : '微软雅黑',fontsize:11,fontweight:600},
						 scale_enable : false,
						 labels:labels
					}]
				}
			});
			//利用自定义组件构造左侧说明文本
			chart.plugin(new iChart.Custom({
					drawFn:function(){
						//计算位置
						var coo = chart.getCoordinate(),
							x = coo.get('originx'),
							y = coo.get('originy'),
							w = coo.width,
							h = coo.height;
						//在左上侧的位置，渲染一个单位的文字
						chart.target.textAlign('start')
						.textBaseline('bottom')
						.textFont('600 11px 微软雅黑')
						.fillText('数量(个)',x-40,y-12,false,'#9d987a')
						.textBaseline('top')
						.fillText('(时间)',x+w+12,y+h+10,false,'#9d987a');

					}
			}));
		//开始画图
		chart.draw();
	});
	}

function Zhuxin2d(title,data){
		//定义数据
		var data = data;
		 $(function(){
			var chart = new iChart.Column2D({
				render : 'Zhuxin2d',//渲染的Dom目标,canvasDiv为Dom的ID
				data: data,//绑定数据
				title : title,//设置标题
				width : 800,//设置宽度，默认单位为px
				height : 600,//设置高度，默认单位为px
				shadow:true,//激活阴影
				shadow_color:'#c7c7c7',//设置阴影颜色
				coordinate:{//配置自定义坐标轴
					scale:[{//配置自定义值轴
						 position:'left',//配置左值轴
						 start_scale:0,//设置开始刻度为0
						 end_scale:1600,//设置结束刻度为26
						 scale_space:100,//设置刻度间距
						 listeners:{//配置事件
							parseText:function(t,x,y){//设置解析值轴文本
								return {text:t}
							}
						}
					}]
				}
			});
			//调用绘图方法开始绘图
			chart.draw();
		});
}

function Huanxin(data,title){
	var data = data;
	$(function(){
			var chart = new iChart.Donut2D({
				render : 'Huanxin',
				center:{
					text:title,
					shadow:true,
					shadow_offsetx:0,
					shadow_offsety:2,
					shadow_blur:2,
					shadow_color:'#b7b7b7',
					color:'#6f6f6f'
				},
				data: data,
				offsetx:-60,
				shadow:true,
				background_color:'#f4f4f4',
				separate_angle:10,//分离角度
				tip:{
					enable:true,
					showType:'fixed'
				},
				legend : {
					enable : true,
					shadow:true,
					background_color:null,
					border:false,
					legend_space:30,//图例间距
					line_height:34,//设置行高
					sign_space:10,//小图标与文本间距
					sign_size:30,//小图标大小
					color:'#6f6f6f',
					fontsize:30//文本大小
				},
				sub_option:{
					label:false,
					color_factor : 0.3
				},
				showpercent:true,
				decimalsnum:2,
				width : 800,
				height : 600,
				radius:140
			});

			/**
			 *利用自定义组件构造左侧说明文本。
			 */
			chart.plugin(new iChart.Custom({
					drawFn:function(){
						/**
						 *计算位置
						 */
						var y = chart.get('originy');
						/**
						 *在左侧的位置，设置竖排模式渲染文字。
						 */
						chart.target.textAlign('center')
						.textBaseline('middle')
						.textFont('600 24px 微软雅黑')
						.fillText('漏洞发布平台数量统计',100,y,false,'#6d869f', 'tb',26,false,0,'middle');

					}
			}));

			chart.draw();
		});
}

function Tiao(data,title){	$(function(){
				var numbers=[];
				for(var i=0;i<data.length;i++){
					numbers.push(data[i]["value"]);
				}
				var maxNum=Math.max.apply(null, numbers);
				new iChart.Bar2D({
					render : 'Tiao',
					background_color : '#EEEEEE',
					data: data,
					title : title,
					subtitle : '',
					footnote : '数据来源：平台漏洞库',
					width : 800,
					height : 600,
					coordinate:{
						width:640,
						height:360,
						scale:[{
							 position:'bottom',
							 start_scale:0,
							 end_scale:maxNum,
							 scale_space:maxNum/10
						}]
					},
					sub_option:{
						border:{
							enable : false
						},
						label:{color:'#333333'}
					},
					shadow:true,
					shadow_color:'#8d8d8d',
					shadow_blur:1,
					shadow_offsety:1,
					shadow_offsetx:1,
					legend:{enable:false}
				}).draw();
			});}