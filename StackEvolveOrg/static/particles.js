window.onload=function(){
    function DrawSpiral(mod) {
        var c = document.getElementById("canvas1");
        var cxt = c.getContext("2d");
        var centerX = 150;
        var centerY = 150;
        cxt.save();
        cxt.clearRect(0, 0, c.width, c.height);
        cxt.beginPath();
        cxt.moveTo(centerX, centerY);
        var STEPS_PER_ROTATION = 60;
        var increment = 2 * Math.PI / STEPS_PER_ROTATION;
        var theta = increment;
        while (theta < 40 * Math.PI) {
            var newX = centerX + theta * Math.cos(theta - mod);
            var newY = centerY + theta * Math.sin(theta - mod);
            cxt.lineTo(newX, newY);
            theta = theta + increment;
        }
        cxt.stroke();
        cxt.restore();
    }
    var counter = 0;
    setInterval(function () {
        DrawSpiral(counter);
        counter += 0.075;
    }, 10);
}
