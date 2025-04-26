function timer(totaltime,deadline) {
    var time = totaltime * 1000;
    var dayDuration = time / deadline;
    var actualDay = deadline;
    var timer = setInterval(ciunttime, dayDuration);
    function countTime() {
        --actualDay;
        $('.deadline-days .day').text(actualDay);
        if (actualDay == 0){
            clearInterval(timer);
            $('.deadline-days .day').text(dealine);
        }
    }
}