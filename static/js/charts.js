function dict_listdict(dict)
{
    keys = Object.keys(dict)
   values = Object.values(dict)
   data = []
   for(var i=0;i<keys.length;i++)
   {
        t ={'name':keys[i],'value':values[i]}
        data.push(t)
   }
   return data
}
function list_listdict(names,values)
{
    data=[]
    for(var i=0;i<names.length;i++){
        data.push({'name':names[i],'value':values[i]})
    }
    return data
}

function piechartload(id,title,names,values)
{

    data = list_listdict(names,values)

    var myChart = echarts.init(document.getElementById(id));

     option = {
            title : {
                text: title,
                x:'center'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            legend: {
                orient: 'vertical',
                left: 'left',
                data: names,
                textStyle:{fontSize:15},
            },
            series : [
                {
                    name:'数量',
                    type: 'pie',
                    radius : '55%',
                    center: ['50%', '60%'],
                    data:data,
                    itemStyle: {
                        emphasis: {
                            shadowBlur: 10,
                            shadowOffsetX: 0,
                            shadowColor: 'rgba(0, 0, 0, 0.5)'
                        },
                        normal: {
                             label:{
                                    textStyle:{fontSize:15},
                                    show: true,
                                    formatter: '{b}: {c}({d}%)'
                              }
                         },

                    },
                }
            ]
        };

    myChart.setOption(option);

}



function linechartload(id,title,names,values)
{
   var myChart = echarts.init(document.getElementById(id));
   option = {
    title: {
        text: title,

    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:[]
    },
    toolbox: {
        show: true,
        feature: {
            dataZoom: {
                yAxisIndex: 'none'
            },
            dataView: {readOnly: false},
            magicType: {type: ['line', 'bar']},
            restore: {},
            saveAsImage: {}
        }
    },
    xAxis:  {
        type: 'category',
        boundaryGap: false,
        data: names
    },
    yAxis: {
        type: 'value',
        axisLabel: {
            formatter: '{value} '
        }
    },
    series: [
        {

            type:'line',
            data:values,
            markPoint: {
                data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'}
                ]
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ]
            },
            itemStyle:{
            normal: {
                             label:{
                                    textStyle:{fontSize:10},
                                    show: true,
                                    formatter: '{c}'
                              }
                         },
             },
        }

    ]
    };
    myChart.setOption(option);


}


function mutilinechartload(id,title,mutillinedata)
{

   mutillinedata={
    types:['中国农产品网|农业','中国农产品网|非农业','新浪|农业','新浪|非农业','慧农网|农业','慧农网|非农业','中国农业新闻网|农业','中国农业新闻网|非农业','农村网|农业','农村网|非农业'],
    names:['2019-01','2019-02','2019-03'],
    values:[
    [103,140,130],
    [25,13,23],
    [420,258,352],
     [250,106,130],
    [124,205,240],
    [30,48,60],
    [503,603,307],
    [53,42,49],
    [63,58,74],
    [14,12,16],
    ]
   }
   var myChart = echarts.init(document.getElementById(id));
   option = {
    title: {
        text: title,

    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:mutillinedata['types']
    },
    toolbox: {
        show: true,
        feature: {

            magicType: {type: ['bar']},

        }
    },
    xAxis:  {
        type: 'category',

        data: mutillinedata['names']
    },
    yAxis: {
        type: 'value',
        axisLabel: {
            formatter: '{value} '
        }
    },
    series: [

    ]
    };

    data = []
    for(var i=0;i<mutillinedata['types'].length;i++)
    {

         values_1 = mutillinedata['values'][i]

         name = mutillinedata['types'][i]
         data.push({type:'bar',data:values_1,name:name,stack:name.split('|')[0]})

    }
    option.series = data




    myChart.setOption(option);


}




function mutilinechartload1(id,title)
{

   arr = [
    [45,45,50,80,110,85,80,60,80,90,80,60,40,40],
    [22,25,30,65,75,96,120,135,100,85,50,45,20,15],
    ]
    total = []
    for(var i=0;i<arr[0].length;i++)
    {
       total.push(arr[0][i]+arr[1][i])
    }

   mutillinedata={
    types:['正面','负面','总量'],
    names:['2019-01-20','2019-01-21','2019-01-22','2019-01-23','2019-01-24','2019-01-25','2019-01-26','2019-01-27','2019-01-28','2019-01-29','2019-01-30','2019-01-31',
    '2019-02-01','2019-02-02',
    ],

    values:[
    [45,45,50,80,110,85,80,60,80,90,80,60,40,40],
    [22,25,30,65,75,96,120,135,100,85,50,45,20,15],
    total
    ]
   }
   var myChart = echarts.init(document.getElementById(id));
   option = {
    title: {
        text: title,

    },
    tooltip: {
        trigger: 'axis'
    },
     toolbox: {
        show: true,
        feature: {

            magicType: {type: ['bar','line']},

        }
    },
    legend: {
        data:mutillinedata['types']
    },

    xAxis:  {
        type: 'category',
        data: mutillinedata['names']
    },
    yAxis: {
        type: 'value',
        axisLabel: {
            formatter: '{value} '
        }
    },
    series: [
         {type:'bar',data:mutillinedata['values'][0],name:'正面',barGap: 0,
         label: {
                normal: {
                    show: true,
                    position: 'top'
                }
            },

         },
         {type:'bar',data:mutillinedata['values'][1],name:'负面',barGap: 0,
         label: {
                normal: {
                    show: true,
                    position: 'top'
                }
            },
         },
         {type:'bar',data:mutillinedata['values'][2],name:'总量',barGap: 0,
         label: {
                normal: {
                    show: true,
                    position: 'top'
                }
            },
         }
    ]
    };


    myChart.setOption(option);


}



function barchartload(id,title,names,values)
{

   var myChart = echarts.init(document.getElementById(id));
   option = {
        tooltip : {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow',
                label: {
                    show: true
                }
            }
        },
        toolbox: {
            show : true,
            feature : {
                mark : {show: true},
                dataView : {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar']},
                restore : {show: true},
                saveAsImage : {show: true}
            }
        },
        calculable : true,
        legend: {

        },
        grid: {
            top: '12%',
            left: '1%',
            right: '10%',
            containLabel: true
        },
        xAxis: [
            {
                type : 'category',
                data : names
            }
        ],
        yAxis: [
            {

            }
        ],
        dataZoom: [
            {
                show: true,
                start: 0,
                end: 50
            },
            {
                type: 'inside',
                start: 94,
                end: 100
            },
            {
                show: true,
                yAxisIndex: 0,
                filterMode: 'empty',
                width: 30,
                height: '80%',
                showDataShadow: false,
                left: '93%'
            }
        ],
        series : [

            {
                name: '热度',
                type: 'bar',
                data: values
            }
        ]
    };

    myChart.setOption(option);



}

function wordcloudload(id,title,names,values)
{

     data = list_listdict(names,values)
     var chart = echarts.init(document.getElementById(id));

            var option = {
                tooltip: {},
                series: [ {
                    type: 'wordCloud',
                    gridSize: 5,
                    sizeRange: [20, 50],
                    rotationRange: [-90, 90],
                    shape: 'pentagon',
                    width: 600,
                    height: 500,
                    drawOutOfBound: true,
                    textStyle: {
                        normal: {
                            color: function () {
                                return 'rgb(' + [
                                    Math.round(Math.random() * 160),
                                    Math.round(Math.random() * 160),
                                    Math.round(Math.random() * 160)
                                ].join(',') + ')';
                            }
                        },
                        emphasis: {
                            shadowBlur: 10,
                            shadowColor: '#333'
                        }
                    },
                    data: data,
                } ]
            };

            chart.setOption(option);
}