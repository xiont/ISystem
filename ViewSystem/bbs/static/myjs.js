
//画布大小
function linephoto(dataset) {
    var width = 550;
    var height = 250;
//在body元素中添加一个画布
    var svg = d3.select("#linephoto")
            .append("svg")
            .attr("width", width)
            .attr("height", height);
//画布周边的空白部分
    var padding = {left: 60, right: 40, top: 30, bottom: 30};

//定义一个数组
    var dataset =dataset;
//x的比例尺
    var xScale = d3.scale.ordinal()
            .domain(d3.range(dataset.length))
            .rangeRoundBands([0, width - padding.left - padding.right])
//y轴的比例尺
    var yScale = d3.scale.linear()
            .domain([0, d3.max(dataset)])
            .range([height - padding.top - padding.bottom, 0]);
//定义x轴
    var xAxis = d3.svg.axis()
            .scale(xScale)
            .orient("bottom");
//定义y 轴
    var yAxis = d3.svg.axis()
            .scale(yScale)
            .orient("left");
//矩形之间的空白格

    var rectPadding = 4;
//添加矩形元素
    var rects = svg.selectAll(".MyRect")
            .data(dataset)
            .enter()
            .append("rect")
            .attr("class", "MyRect")
            .attr("transform", "translate(" + padding.left + "," + padding.top + ")")
            .attr("x", function (d, i) {
                return xScale(i) + rectPadding / 2;
            })
            .attr("y", function (d) {
                return yScale(d);
            })
            .attr("width", xScale.rangeBand() - rectPadding)
            .attr("height", function (d) {
                return height - padding.top - padding.bottom - yScale(d);
            });

//添加文字元素
    var texts = svg.selectAll(".MyText")
            .data(dataset)
            .enter()
            .append("text")
            .attr("class", "MyText")
            .attr("transform", "translate(" + padding.left + "," + padding.top + ")")
            .attr("x", function (d, i) {
                return xScale(i) + rectPadding / 2;
            })
            .attr("y", function (d) {
                return yScale(d);
            })
            .attr("dx", function () {
                return (xScale.rangeBand() - rectPadding) / 2;
            })
            .attr("dy", function (d) {
                return 20;
            })
            .text(function (d) {
                return d;
            });

//添加x轴
    svg.append("g")
            .attr("class", "axis")
            .attr("transform", "translate(" + padding.left + "," + (height - padding.bottom) + ")")
            .call(xAxis);

//添加y轴
    svg.append("g")
            .attr("class", "axis")
            .attr("transform", "translate(" + padding.left + "," + padding.top + ")")
            .call(yAxis);
}


//画布大小
function linephoto2(dataset) {
    var width = 550;
    var height = 250;
//在body元素中添加一个画布
    var svg = d3.select("#linephoto2")
            .append("svg")
            .attr("width", width)
            .attr("height", height);
//画布周边的空白部分
    var padding = {left: 60, right: 40, top: 30, bottom: 30};

//定义一个数组
    var dataset =dataset;
//x的比例尺
    var xScale = d3.scale.ordinal()
            .domain(d3.range(dataset.length))
            .rangeRoundBands([0, width - padding.left - padding.right])
//y轴的比例尺
    var yScale = d3.scale.linear()
            .domain([0, d3.max(dataset)])
            .range([height - padding.top - padding.bottom, 0]);
//定义x轴
    var xAxis = d3.svg.axis()
            .scale(xScale)
            .orient("bottom");
//定义y 轴
    var yAxis = d3.svg.axis()
            .scale(yScale)
            .orient("left");
//矩形之间的空白格

    var rectPadding = 4;
//添加矩形元素
    var rects = svg.selectAll(".MyRect")
            .data(dataset)
            .enter()
            .append("rect")
            .attr("class", "MyRect")
            .attr("transform", "translate(" + padding.left + "," + padding.top + ")")
            .attr("x", function (d, i) {
                return xScale(i) + rectPadding / 2;
            })
            .attr("y", function (d) {
                return yScale(d);
            })
            .attr("width", xScale.rangeBand() - rectPadding)
            .attr("height", function (d) {
                return height - padding.top - padding.bottom - yScale(d);
            });

//添加文字元素
    var texts = svg.selectAll(".MyText")
            .data(dataset)
            .enter()
            .append("text")
            .attr("class", "MyText")
            .attr("transform", "translate(" + padding.left + "," + padding.top + ")")
            .attr("x", function (d, i) {
                return xScale(i) + rectPadding / 2;
            })
            .attr("y", function (d) {
                return yScale(d);
            })
            .attr("dx", function () {
                return (xScale.rangeBand() - rectPadding) / 2;
            })
            .attr("dy", function (d) {
                return 20;
            })
            .text(function (d) {
                return d;
            });

//添加x轴
    svg.append("g")
            .attr("class", "axis")
            .attr("transform", "translate(" + padding.left + "," + (height - padding.bottom) + ")")
            .call(xAxis);

//添加y轴
    svg.append("g")
            .attr("class", "axis")
            .attr("transform", "translate(" + padding.left + "," + padding.top + ")")
            .call(yAxis);
}