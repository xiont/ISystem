
//������С
function linephoto(dataset) {
    var width = 550;
    var height = 250;
//��bodyԪ�������һ������
    var svg = d3.select("#linephoto")
            .append("svg")
            .attr("width", width)
            .attr("height", height);
//�����ܱߵĿհײ���
    var padding = {left: 60, right: 40, top: 30, bottom: 30};

//����һ������
    var dataset =dataset;
//x�ı�����
    var xScale = d3.scale.ordinal()
            .domain(d3.range(dataset.length))
            .rangeRoundBands([0, width - padding.left - padding.right])
//y��ı�����
    var yScale = d3.scale.linear()
            .domain([0, d3.max(dataset)])
            .range([height - padding.top - padding.bottom, 0]);
//����x��
    var xAxis = d3.svg.axis()
            .scale(xScale)
            .orient("bottom");
//����y ��
    var yAxis = d3.svg.axis()
            .scale(yScale)
            .orient("left");
//����֮��Ŀհ׸�

    var rectPadding = 4;
//��Ӿ���Ԫ��
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

//�������Ԫ��
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

//���x��
    svg.append("g")
            .attr("class", "axis")
            .attr("transform", "translate(" + padding.left + "," + (height - padding.bottom) + ")")
            .call(xAxis);

//���y��
    svg.append("g")
            .attr("class", "axis")
            .attr("transform", "translate(" + padding.left + "," + padding.top + ")")
            .call(yAxis);
}


//������С
function linephoto2(dataset) {
    var width = 550;
    var height = 250;
//��bodyԪ�������һ������
    var svg = d3.select("#linephoto2")
            .append("svg")
            .attr("width", width)
            .attr("height", height);
//�����ܱߵĿհײ���
    var padding = {left: 60, right: 40, top: 30, bottom: 30};

//����һ������
    var dataset =dataset;
//x�ı�����
    var xScale = d3.scale.ordinal()
            .domain(d3.range(dataset.length))
            .rangeRoundBands([0, width - padding.left - padding.right])
//y��ı�����
    var yScale = d3.scale.linear()
            .domain([0, d3.max(dataset)])
            .range([height - padding.top - padding.bottom, 0]);
//����x��
    var xAxis = d3.svg.axis()
            .scale(xScale)
            .orient("bottom");
//����y ��
    var yAxis = d3.svg.axis()
            .scale(yScale)
            .orient("left");
//����֮��Ŀհ׸�

    var rectPadding = 4;
//��Ӿ���Ԫ��
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

//�������Ԫ��
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

//���x��
    svg.append("g")
            .attr("class", "axis")
            .attr("transform", "translate(" + padding.left + "," + (height - padding.bottom) + ")")
            .call(xAxis);

//���y��
    svg.append("g")
            .attr("class", "axis")
            .attr("transform", "translate(" + padding.left + "," + padding.top + ")")
            .call(yAxis);
}