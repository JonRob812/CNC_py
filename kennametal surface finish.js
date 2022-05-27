function calculateSurfaceFinish(corner_radius, b, c) {
  "inch" === c
    ? (corner_radius = 1e7 * (corner_radius - 0.5 * Math.sqrt(4 * corner_radius *corner_radius - 0.159154 * 0.159154 * b * b)))
    : ((corner_radius =
        1 / Math.pow((Math.sqrt((a / 25.4) * 21.6) / (b / 25.4)) * 0.001, 2)),
      (a /= 39.4));
  return calculatorCommon.roundNumber(a, 2);
}
function calculateIPR(a, b, c) {
  "inch" === c
    ? (a = (2 * Math.sqrt((b / 1e7) * (2 * a - b / 1e7))) / 0.159154)
    : ((a = 0.001 * Math.sqrt((a / 25.4) * 39.4 * b * 21.6)), (a *= 25.4));
  return calculatorCommon.roundNumber(a, 4);
}
function calculateCornerRadius(a, b, c) {
  "inch" === c
    ? (a =
        (0.159154 * b * 0.159154 * b + (a / 1e7) * 4 * (a / 1e7)) /
        ((a / 1e7) * 8))
    : ((a = 1 / Math.pow((Math.sqrt(21.6 * 39.4 * a) / (b / 25.4)) * 0.001, 2)),
      (a *= 25.4));
  return calculatorCommon.roundNumber(a, 4);
}
$(document).ready(function () {
  $("#radius-button").click(function (a) {
    a.preventDefault();
    a = $("#cornerRadiusInchesPerRev").val();
    var b = $("#cornerRadiusSurfaceFinish").val();
    a = calculateCornerRadius(b, a, $("#unitOfMeasure").val());
    $("#out-cornerRadius").html(a);
    $("#out-cornerRadius-group").fadeIn();
  });
  $("#inches-button").click(function (a) {
    a.preventDefault();
    a = $("#inchesPerRevCornerRadius").val();
    var b = $("#inchesPerRevSurfaceFinish").val();
    a = calculateIPR(a, b, $("#unitOfMeasure").val());
    $("#out-inchesPerRev").html(a);
    $("#out-inchesPerRev-group").fadeIn();
  });
  $("#finish-button").click(function (a) {
    a.preventDefault();
    a = $("#surfaceFinishInchesPerRev").val();
    var b = $("#surfaceFinishCornerRadius").val();
    a = calculateSurfaceFinish(b, a, $("#unitOfMeasure").val());
    $("#out-SurfaceFinish").html(a);
    $("#out-SurfaceFinish-group").fadeIn();
  });
});
