<template>
  <div id="content">
    <div id="map-container"></div>
  </div>
</template>

<script>
export default {
  mounted() {
    var esmapID = "test666";
    var container = document.getElementById("map-container");
    // console.log(window.esmap)
    var map = new esmap.ESMap({
      container: container, //渲染dom
      mapDataSrc: "./data", //地图数据位置
      mapThemeSrc: "./data/theme", //主题数据位置
      visibleFloors: "all", //更多初始化参数配置请参考https://www.esmap.cn/escopemap/content/cn/develope/map-config.html
      token: "escope"
    });
    //打开地图数据
    map.openMapById(esmapID);
    map.showCompass = false; //显示指南针

    // 1.声明楼层控件配置参数
    var ctlOpt = new esmap.ESControlOptions({
      position: esmap.ESControlPositon.RIGHT_TOP,
      imgURL: "image/wedgets/"
    });

    // 2.在地图加载完成事件中新建楼层控制控件对象
    map.on("loadComplete", function() {
      //创建楼层控件
      floorControl = new esmap.ESScrollFloorsControl(map, ctlOpt);

      //单层多层切换按钮
      var toolControl = new esmap.ESToolControl(map);

      //或者折叠式按钮的楼层控件
      //floorControl = new esmap.ESButtonFloorsControl(map, ctlOpt);
    });
  }
};
</script>

<style>
#content {
  display: flex;
  justify-content: center;
}
#map-container {
  height: 800px;
  width: 80%;
}
</style>